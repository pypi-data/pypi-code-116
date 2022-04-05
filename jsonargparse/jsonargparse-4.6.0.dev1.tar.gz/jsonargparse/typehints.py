"""Action to support type hints."""

import copy
import inspect
import os
import re
import warnings
from argparse import Action
from collections import abc, defaultdict
from contextlib import contextmanager
from contextvars import ContextVar
from copy import deepcopy
from enum import Enum
from functools import partial
from types import FunctionType
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    Mapping,
    MutableMapping,
    MutableSequence,
    MutableSet,
    Sequence,
    Set,
    Tuple,
    Type,
    TypeVar,
    Union,
)

from .actions import _find_action, _find_parent_action, _is_action_value_list
from .loaders_dumpers import get_loader_exceptions, load_value
from .namespace import is_empty_namespace, Namespace
from .typing import is_final_class, registered_types
from .optionals import (
    argcomplete_warn_redraw_prompt,
    files_completer,
)
from .util import (
    change_to_path_dir,
    get_import_path,
    import_object,
    object_path_serializer,
    ParserError,
    Path,
    NoneType,
    indent_text,
    _issubclass,
    _parse_value_or_config,
    warning,
    lenient_check,
)


__all__ = ['lazy_instance']


Literal = getattr(__import__('typing'), 'Literal', False)


root_types = {
    str,
    int,
    float,
    bool,
    Any,
    Literal,
    Type, type,
    Union,
    List, list, Iterable, Sequence, MutableSequence, abc.Iterable, abc.Sequence, abc.MutableSequence,
    Tuple, tuple,
    Set, set, frozenset, MutableSet, abc.MutableSet,
    Dict, dict, Mapping, MutableMapping, abc.Mapping, abc.MutableMapping,
    Callable, abc.Callable,
}

leaf_types = {
    str,
    int,
    float,
    bool,
    NoneType,
}

not_subclass_types: Set = set(k for k in registered_types.keys() if not isinstance(k, tuple))
not_subclass_types = not_subclass_types.union(leaf_types).union(root_types)

tuple_set_origin_types = {Tuple, tuple, Set, set, frozenset, MutableSet, abc.Set, abc.MutableSet}
sequence_origin_types = {List, list, Iterable, Sequence, MutableSequence, abc.Iterable, abc.Sequence,
                         abc.MutableSequence}
mapping_origin_types = {Dict, dict, Mapping, MutableMapping, abc.Mapping, abc.MutableMapping}
callable_origin_types = {Callable, abc.Callable}


subclass_arg_parser: ContextVar = ContextVar('subclass_arg_parser')
sub_defaults: ContextVar = ContextVar('sub_defaults', default=False)


class ActionTypeHint(Action):
    """Action to parse a type hint."""

    def __init__(
        self,
        typehint: Type = None,
        enable_path: bool = False,
        **kwargs
    ):
        """Initializer for ActionTypeHint instance.

        Args:
            typehint: The type hint to use for parsing.
            enable_path: Whether to try to load parsed value from path.

        Raises:
            ValueError: If a parameter is invalid.
        """
        if typehint is not None:
            if not self.is_supported_typehint(typehint, full=True):
                raise ValueError(f'Unsupported type hint {typehint}.')
            self._typehint = typehint
            self._enable_path = False if is_optional(typehint, Path) else enable_path
        elif '_typehint' not in kwargs:
            raise ValueError('Expected typehint keyword argument.')
        else:
            self._typehint = kwargs.pop('_typehint')
            self._enable_path = kwargs.pop('_enable_path')
            if 'metavar' not in kwargs:
                kwargs['metavar'] = typehint_metavar(self._typehint)
            super().__init__(**kwargs)
            self.normalize_default()


    def normalize_default(self):
        default = self.default
        if isinstance(default, LazyInitBaseClass):
            self.default = default.lazy_get_init_data()
        elif is_enum_type(self._typehint) and isinstance(default, Enum):
            self.default = default.name
        elif is_callable_type(self._typehint) and callable(default) and not inspect.isclass(default):
            self.default = get_import_path(default)


    @staticmethod
    def is_supported_typehint(typehint, full=False):
        """Whether the given type hint is supported."""
        supported = \
            typehint in root_types or \
            getattr(typehint, '__origin__', None) in root_types or \
            typehint in registered_types or \
            _issubclass(typehint, Enum) or \
            ActionTypeHint.is_class_typehint(typehint)
        if full and supported:
            typehint_origin = getattr(typehint, '__origin__', typehint)
            if typehint_origin in root_types and typehint_origin != Literal:
                for typehint in getattr(typehint, '__args__', []):
                    if typehint == Ellipsis or (typehint_origin == type and isinstance(typehint, TypeVar)):
                        continue
                    if not (typehint in leaf_types or ActionTypeHint.is_supported_typehint(typehint, full=True)):
                        return False
        return supported


    @staticmethod
    def is_class_typehint(typehint, only_subclasses=False, all_subtypes=True):
        typehint = typehint_from_action(typehint)
        if typehint is None:
            return False
        typehint_origin = getattr(typehint, '__origin__', None)
        if typehint_origin == Union:
            subtypes = [a for a in typehint.__args__ if a != NoneType]
            test = all if all_subtypes else any
            return test(ActionTypeHint.is_class_typehint(s, only_subclasses) for s in subtypes)
        if only_subclasses and is_final_class(typehint):
            return False
        return inspect.isclass(typehint) and \
            typehint not in not_subclass_types and \
            typehint_origin is None and \
            not _issubclass(typehint, (Path, Enum))


    @staticmethod
    def is_subclass_typehint(typehint, all_subtypes=True):
        return ActionTypeHint.is_class_typehint(typehint, only_subclasses=True, all_subtypes=all_subtypes)


    @staticmethod
    def is_mapping_typehint(typehint):
        typehint_origin = getattr(typehint, '__origin__', typehint)
        if typehint in mapping_origin_types or typehint_origin in mapping_origin_types or is_optional(typehint, tuple(mapping_origin_types)):
            return True
        return False


    def is_init_arg_mapping_typehint(self, key, cfg):
        result = False
        class_path = cfg.get(f'{self.dest}.class_path')
        if isinstance(class_path, str) and key.startswith(f'{self.dest}.init_args.') and self.is_subclass_typehint(self):
            sub_add_kwargs = dict(self.sub_add_kwargs)
            sub_add_kwargs.pop('linked_targets', None)
            parser = ActionTypeHint.get_class_parser(class_path, sub_add_kwargs=sub_add_kwargs)
            key = re.sub(f'^{self.dest}.init_args.', '', key)
            typehint = getattr(_find_action(parser, key), '_typehint', None)
            result = self.is_mapping_typehint(typehint)
        return result


    @staticmethod
    def parse_subclass_arg(arg_string):
        parser = subclass_arg_parser.get()
        action = None
        if arg_string.startswith('--'):
            arg_base, explicit_arg = (arg_string, None)
            if '=' in arg_string:
                arg_base, explicit_arg = arg_string.split('=', 1)
            if '.' in arg_base and arg_base not in parser._option_string_actions:
                action = _find_parent_action(parser, arg_base[2:])

        if ActionTypeHint.is_subclass_typehint(action, all_subtypes=False):
            return action, arg_base, explicit_arg
        elif parser._subcommands_action and arg_string in parser._subcommands_action._name_parser_map:
            subparser = parser._subcommands_action._name_parser_map[arg_string]
            subclass_arg_parser.set(subparser)


    @staticmethod
    @contextmanager
    def subclass_arg_context(parser):
        subclass_arg_parser.set(parser)
        yield


    @staticmethod
    @contextmanager
    def sub_defaults_context():
        t = sub_defaults.set(True)
        try:
            yield
        finally:
            sub_defaults.reset(t)


    @staticmethod
    def add_sub_defaults(parser, cfg):
        with ActionTypeHint.sub_defaults_context():
            parser._apply_actions(cfg)


    def serialize(self, value, dump_kwargs=None):
        sub_add_kwargs = getattr(self, 'sub_add_kwargs', {})
        with dump_kwargs_context(dump_kwargs):
            if _is_action_value_list(self):
                return [adapt_typehints(v, self._typehint, serialize=True, sub_add_kwargs=sub_add_kwargs) for v in value]
            return adapt_typehints(value, self._typehint, serialize=True, sub_add_kwargs=sub_add_kwargs)


    def __call__(self, *args, **kwargs):
        """Parses an argument validating against the corresponding type hint.

        Raises:
            TypeError: If the argument is not valid.
        """
        if len(args) == 0:
            kwargs['_typehint'] = self._typehint
            kwargs['_enable_path'] = self._enable_path
            if 'nargs' in kwargs and kwargs['nargs'] == 0:
                raise ValueError('ActionTypeHint does not allow nargs=0.')
            return ActionTypeHint(**kwargs)
        if self.nargs == '?' and args[2] is None:
            val = None
        else:
            parser, cfg, val, opt_str = args
            if isinstance(opt_str, str) and opt_str.startswith(f'--{self.dest}.'):
                sub_opt = opt_str[len(f'--{self.dest}.'):]
                if sub_opt != 'class_path':
                    cfg_dest = deepcopy(cfg.get(self.dest, Namespace()))
                    if self.dest not in cfg:
                        try:
                            default = parser.get_default(self.dest)
                            cfg_dest['class_path'] = default['class_path']
                        except (KeyError, TypeError):
                            pass
                    if 'class_path' not in cfg_dest:
                        raise ParserError(f'Found {opt_str} but not yet known to which class_path this corresponds.')
                    if not sub_opt.startswith('init_args.'):
                        sub_opt = 'init_args.' + sub_opt
                    cfg_dest[sub_opt] = val
                    val = cfg_dest
            val = self._check_type(val, cfg=cfg)
        args[1].update(val, self.dest)


    def _check_type(self, value, cfg=None):
        islist = _is_action_value_list(self)
        if not islist:
            value = [value]
        for num, val in enumerate(value):
            try:
                orig_val = val
                try:
                    val, config_path = _parse_value_or_config(val, enable_path=self._enable_path)
                except get_loader_exceptions():
                    config_path = None
                path_meta = val.pop('__path__', None) if isinstance(val, dict) else None
                sub_add_kwargs = getattr(self, 'sub_add_kwargs', {})
                prev_val = cfg.get(self.dest) if cfg else None
                try:
                    with change_to_path_dir(config_path):
                        val = adapt_typehints(val, self._typehint, prev_val=prev_val, sub_add_kwargs=sub_add_kwargs)
                except ValueError as ex:
                    val_is_int_float_or_none = isinstance(val, (int, float)) or val is None
                    if lenient_check.get():
                        value[num] = orig_val if val_is_int_float_or_none else val
                        continue
                    if val_is_int_float_or_none and config_path is None:
                        val = adapt_typehints(orig_val, self._typehint, prev_val=prev_val, sub_add_kwargs=sub_add_kwargs)
                    else:
                        if self._enable_path and config_path is None and isinstance(orig_val, str):
                            msg = f'\n- Expected a config path but "{orig_val}" either not accessible or invalid.\n- '
                            raise type(ex)(msg+str(ex)) from ex
                        raise ex
                if path_meta is not None:
                    val['__path__'] = path_meta
                if isinstance(val, (Namespace, dict)) and config_path is not None:
                    val['__path__'] = config_path
                value[num] = val
            except (TypeError, ValueError) as ex:
                elem = '' if not islist else f' element {num+1}'
                raise TypeError(f'Parser key "{self.dest}"{elem}: {ex}') from ex
        return value if islist else value[0]


    def instantiate_classes(self, value):
        islist = _is_action_value_list(self)
        if not islist:
            value = [value]
        sub_add_kwargs = getattr(self, 'sub_add_kwargs', {})
        for num, val in enumerate(value):
            value[num] = adapt_typehints(val, self._typehint, instantiate_classes=True, sub_add_kwargs=sub_add_kwargs)
        return value if islist else value[0]


    @staticmethod
    def get_class_parser(val_class, sub_add_kwargs=None):
        from .core import ArgumentParser
        if isinstance(val_class, str):
            val_class = import_object(val_class)
        parser = ArgumentParser(error_handler=None)
        parser.add_class_arguments(val_class, **(sub_add_kwargs or {}))
        return parser


    def extra_help(self):
        extra = ''
        if self.is_subclass_typehint(self, all_subtypes=False):
            class_paths = get_all_subclass_paths(self._typehint)
            if class_paths:
                extra = ', known class paths: '+', '.join(class_paths)
        return extra


    def completer(self, prefix, **kwargs):
        """Used by argcomplete, validates value and shows expected type."""
        if self._typehint == bool:
            return ['true', 'false']
        elif is_optional(self._typehint, bool):
            return ['true', 'false', 'null']
        elif _issubclass(self._typehint, Enum):
            enum = self._typehint
            return list(enum.__members__.keys())
        elif is_optional(self._typehint, Enum):
            enum = self._typehint.__args__[0]
            return list(enum.__members__.keys())+['null']
        elif is_optional(self._typehint, Path):
            return ['null'] + sorted(files_completer(prefix, **kwargs))
        elif chr(int(os.environ['COMP_TYPE'])) == '?':
            try:
                if prefix.strip() == '':
                    raise ValueError()
                self._check_type(prefix)
                msg = 'value already valid, '
            except (TypeError, ValueError) + get_loader_exceptions():
                msg = 'value not yet valid, '
            msg += 'expected type '+type_to_str(self._typehint)
            return argcomplete_warn_redraw_prompt(prefix, msg)


def adapt_typehints(val, typehint, serialize=False, instantiate_classes=False, prev_val=None, sub_add_kwargs=None):

    adapt_kwargs = {
        'serialize': serialize,
        'instantiate_classes': instantiate_classes,
        'prev_val': prev_val,
        'sub_add_kwargs': sub_add_kwargs or {},
    }
    subtypehints = getattr(typehint, '__args__', None)
    typehint_origin = getattr(typehint, '__origin__', typehint)

    # Any
    if typehint == Any:
        type_val = type(val)
        if type_val in registered_types or _issubclass(type_val, Enum):
            val = adapt_typehints(val, type_val, **adapt_kwargs)
        elif isinstance(val, str):
            try:
                val, _ = _parse_value_or_config(val, enable_path=False)
            except get_loader_exceptions():
                pass

    # Literal
    elif typehint_origin == Literal:
        if val not in subtypehints:
            raise ValueError(f'Expected a {typehint} but got "{val}"')

    # Basic types
    elif typehint in leaf_types:
        if not isinstance(val, typehint):
            if typehint is float and isinstance(val, int):
                val = float(val)
            else:
                raise ValueError(f'Expected a {typehint} but got "{val}"')

    # Registered types
    elif typehint in registered_types:
        registered_type = registered_types[typehint]
        if serialize:
            if registered_type.is_value_of_type(val):
                val = registered_type.serializer(val)
            else:
                registered_type.deserializer(val)
        elif not serialize and not registered_type.is_value_of_type(val):
            val = registered_type.deserializer(val)

    # Enum
    elif _issubclass(typehint, Enum):
        if serialize:
            if isinstance(val, typehint):
                val = val.name
            else:
                if val not in typehint.__members__:
                    raise ValueError(f'Value "{val}" is not a valid member name for the enum "{typehint}"')
        elif not serialize and not isinstance(val, typehint):
            val = typehint[val]

    # Type
    elif typehint in {Type, type} or typehint_origin in {Type, type}:
        if serialize:
            val = object_path_serializer(val)
        elif not serialize and not isinstance(val, type):
            path = val
            val = import_object(val)
            if (typehint in {Type, type} and not isinstance(val, type)) or \
               (typehint not in {Type, type} and not _issubclass(val, subtypehints[0])):
                raise ValueError(f'Value "{path}" is not a {typehint}.')

    # Union
    elif typehint_origin == Union:
        vals = []
        for subtypehint in subtypehints:
            try:
                vals.append(adapt_typehints(val, subtypehint, **adapt_kwargs))
                break
            except Exception as ex:
                vals.append(ex)
        if all(isinstance(v, Exception) for v in vals):
            e = indent_text('\n- '.join(str(v) for v in ['']+vals))
            raise ValueError(f'Value "{val}" does not validate against any of the types in {typehint}:{e}')
        val = [v for v in vals if not isinstance(v, Exception)][0]

    # Tuple or Set
    elif typehint_origin in tuple_set_origin_types:
        if not isinstance(val, (list, tuple, set)):
            raise ValueError(f'Expected a {typehint_origin} but got "{val}"')
        val = list(val)
        if subtypehints is not None:
            is_tuple = typehint_origin in {Tuple, tuple}
            is_ellipsis = is_ellipsis_tuple(typehint)
            if is_tuple and not is_ellipsis and len(val) != len(subtypehints):
                raise ValueError(f'Expected a tuple with {len(subtypehints)} elements but got "{val}"')
            for n, v in enumerate(val):
                subtypehint = subtypehints[0 if is_ellipsis else n]
                val[n] = adapt_typehints(v, subtypehint, **adapt_kwargs)
            if is_tuple and len(val) == 0:
                raise ValueError('Expected a non-empty tuple')
        if not serialize:
            val = tuple(val) if typehint_origin in {Tuple, tuple} else set(val)

    # List, Iterable or Sequence
    elif typehint_origin in sequence_origin_types:
        if not isinstance(val, list):
            raise ValueError(f'Expected a List but got "{val}"')
        if subtypehints is not None:
            for n, v in enumerate(val):
                val[n] = adapt_typehints(v, subtypehints[0], **adapt_kwargs)

    # Dict, Mapping
    elif typehint_origin in mapping_origin_types:
        if not isinstance(val, dict):
            raise ValueError(f'Expected a Dict but got "{val}"')
        if subtypehints is not None:
            if subtypehints[0] == int:
                cast = str if serialize else int
                val = {cast(k): v for k, v in val.items()}
            for k, v in val.items():
                if "linked_targets" in adapt_kwargs["sub_add_kwargs"]:
                    kwargs = copy.deepcopy(adapt_kwargs)
                    sub_add_kwargs = kwargs["sub_add_kwargs"]
                    sub_add_kwargs["linked_targets"] = {t[len(k + "."):] for t in sub_add_kwargs["linked_targets"]
                                                        if t.startswith(k + ".")}
                    sub_add_kwargs["linked_targets"] = {t[len("init_args."):] if t.startswith("init_args.") else t
                                                        for t in sub_add_kwargs["linked_targets"]}
                else:
                    kwargs = adapt_kwargs
                val[k] = adapt_typehints(v, subtypehints[1], **kwargs)

    # Callable
    elif typehint_origin in callable_origin_types or typehint in callable_origin_types:
        if serialize:
            if is_class_object(val):
                class_path = val['class_path']
                init_args = val.get('init_args', Namespace())
                val['init_args'] = adapt_class_type(class_path, init_args, True, False, sub_add_kwargs)
            else:
                val = object_path_serializer(val)
        else:
            try:
                if isinstance(val, str):
                    val_obj = import_object(val)
                    if inspect.isclass(val_obj):
                        val = {'class_path': val}
                    elif callable(val_obj):
                        val = val_obj
                    else:
                        raise ImportError(f'Unexpected import object {val_obj}')
                if isinstance(val, (dict, Namespace)):
                    if not is_class_object(val):
                        raise ImportError(f'Dict must include a class_path and optionally init_args, but got {val}')
                    val = Namespace(val)
                    val_class = import_object(val.class_path)
                    if not (inspect.isclass(val_class) and callable_instances(val_class)):
                        raise ImportError(f'"{val.class_path}" is not a callable class.')
                    val['class_path'] = get_import_path(val_class)
                    init_args = val.get('init_args', Namespace())
                    adapted = adapt_class_type(val_class, init_args, False, instantiate_classes, sub_add_kwargs)
                    if instantiate_classes and sub_add_kwargs.get('instantiate', True):
                        val = adapted
                    elif adapted is not None and not is_empty_namespace(adapted):
                        val['init_args'] = adapted
            except (ImportError, AttributeError, ParserError) as ex:
                raise ValueError(f'Type {typehint} expects a function or a callable class: {ex}')

    # Final class
    elif is_final_class(typehint):
        if isinstance(val, dict):
            val = Namespace(val)
        if not isinstance(val, Namespace):
            raise ValueError(f'Expected a Dict/Namespace but got "{val}"')
        val = adapt_class_type(typehint, val, serialize, instantiate_classes, sub_add_kwargs)

    # Subclass
    elif not hasattr(typehint, '__origin__') and inspect.isclass(typehint):
        if isinstance(val, typehint):
            if serialize:
                val = serialize_class_instance(val)
            return val
        if serialize and isinstance(val, str):
            return val
        if not (isinstance(val, str) or is_class_object(val)):
            raise ValueError(f'Type {typehint} expects an str or a Dict/Namespace with a class_path entry but got "{val}"')
        try:
            if isinstance(val, str):
                val = Namespace(class_path=val)
            elif isinstance(val, dict):
                val = Namespace(val)
            val_class = import_object(resolve_class_path_by_name(typehint, val['class_path']))
            if not _issubclass(val_class, typehint):
                raise ValueError(f'"{val["class_path"]}" is not a subclass of {typehint}')
            val['class_path'] = class_path = get_import_path(val_class)
            if isinstance(prev_val, Namespace) and 'class_path' in prev_val and 'init_args' not in val:
                prev_class_path = prev_val['class_path']
                prev_init_args = prev_val.get('init_args')
                if prev_class_path != class_path and not (prev_init_args is None or is_empty_namespace(prev_init_args)):
                    warnings.warn(
                        f'Changing class_path to {class_path} implies discarding init_args {prev_init_args.as_dict()} '
                        f'defined for class_path {prev_class_path}.'
                    )
            init_args = val.get('init_args', Namespace())
            adapted = adapt_class_type(val_class, init_args, serialize, instantiate_classes, sub_add_kwargs)
            if instantiate_classes and sub_add_kwargs.get('instantiate', True):
                val = adapted
            elif adapted is not None and not is_empty_namespace(adapted):
                val['init_args'] = adapted
        except (ImportError, AttributeError, AssertionError, ParserError) as ex:
            class_path = val if isinstance(val, str) else val['class_path']
            e = indent_text(f'\n- {ex}')
            raise ValueError(f'Problem with given class_path "{class_path}":{e}') from ex

    return val


def is_class_object(val):
    is_class = isinstance(val, (dict, Namespace)) and 'class_path' in val
    if is_class:
        keys = getattr(val, '__dict__', val).keys()
        is_class = len(set(keys)-{'class_path', 'init_args', '__path__'}) == 0
    return is_class


def get_all_subclass_paths(cls: Type) -> List[str]:
    subclass_list = []

    def is_local(cl):
        return '.<locals>.' in getattr(cl, '__qualname__', '.<locals>.')

    def is_private(class_path):
        return '._' in class_path

    def add_subclasses(cl):
        class_path = get_import_path(cl)
        if not (inspect.isabstract(cl) or is_local(cl) or is_private(class_path)):
            subclass_list.append(class_path)
        for subclass in cl.__subclasses__() if hasattr(cl, '__subclasses__') else []:
            add_subclasses(subclass)

    if getattr(cls, '__origin__', None) == Union:
        for arg in cls.__args__:
            if ActionTypeHint.is_subclass_typehint(arg):
                add_subclasses(arg)
    else:
        add_subclasses(cls)

    return subclass_list


def resolve_class_path_by_name(cls: Type, name: str) -> str:
    class_path = name
    if '.' not in class_path:
        subclass_dict = defaultdict(list)
        for subclass in get_all_subclass_paths(cls):
            subclass_name = subclass.rsplit('.', 1)[1]
            subclass_dict[subclass_name].append(subclass)
        if name in subclass_dict:
            name_subclasses = subclass_dict[name]
            class_path = name_subclasses[-1]
            if len(name_subclasses) > 1:
                class_paths = ', '.join(name_subclasses)
                warnings.warn(
                    f'Resolved "{name}" to "{class_path}". Found {len(class_paths)} subclasses of {cls} '
                    f'with that name: {class_paths}. Give the full class path to avoid ambiguity.'
                )
    return class_path


dump_kwargs: ContextVar = ContextVar('dump_kwargs', default={})


@contextmanager
def dump_kwargs_context(kwargs):
    dump_kwargs.set(kwargs if kwargs else {})
    yield


def adapt_class_type(val_class, init_args, serialize, instantiate_classes, sub_add_kwargs):
    if isinstance(init_args, dict):
        init_args = Namespace(init_args)
    parser = ActionTypeHint.get_class_parser(val_class, sub_add_kwargs)

    # No need to re-create the linked arg but just "inform" the corresponding parser actions that it exists upstream.
    for target in sub_add_kwargs.get('linked_targets', []):
        split_index = target.find(".")
        if split_index != -1:
            split = ".init_args." if target[split_index:].startswith(".init_args.") else "."

            parent_key, key = target.split(split, maxsplit=1)

            action = next(a for a in parser._actions if a.dest == parent_key)

            sub_add_kwargs = getattr(action, 'sub_add_kwargs')
            sub_add_kwargs.setdefault('linked_targets', set())
            sub_add_kwargs['linked_targets'].add(key)

            break

    if instantiate_classes:
        init_args = parser.instantiate_classes(init_args)
        if not sub_add_kwargs.get('instantiate', True):
            return init_args
        return val_class(**init_args)
    if serialize:
        init_args = None if is_empty_namespace(init_args) else load_value(parser.dump(init_args, **dump_kwargs.get()))
    else:
        init_args = parser.parse_object(init_args, defaults=sub_defaults.get())
    return init_args


def is_ellipsis_tuple(typehint):
    return typehint.__origin__ in {Tuple, tuple} and len(typehint.__args__) > 1 and typehint.__args__[1] == Ellipsis


def is_optional(annotation, ref_type):
    """Checks whether a type annotation is an optional for one type class."""
    return getattr(annotation, '__origin__', None) == Union and \
        len(annotation.__args__) == 2 and \
        any(NoneType == a for a in annotation.__args__) and \
        any(_issubclass(a, ref_type) for a in annotation.__args__)


def is_enum_type(annotation):
    return _issubclass(annotation, Enum) or \
        (getattr(annotation, '__origin__', None) == Union and
         any(_issubclass(a, Enum) for a in annotation.__args__))


def is_callable_type(annotation):
    def is_callable(a):
        return getattr(a, '__origin__', a) in callable_origin_types or a in callable_origin_types
    return is_callable(annotation) or \
        (getattr(annotation, '__origin__', None) == Union and
         any(is_callable(a) for a in annotation.__args__))


def typehint_from_action(action_or_typehint):
    if isinstance(action_or_typehint, Action):
        action_or_typehint = getattr(action_or_typehint, '_typehint', None)
    return action_or_typehint


def type_to_str(obj):
    if _issubclass(obj, (bool, int, float, str, Enum)):
        return obj.__name__
    elif obj is not None:
        return re.sub(r'[a-z_.]+\.', '', str(obj)).replace('NoneType', 'null')


def typehint_metavar(typehint):
    """Generates a metavar for some types."""
    metavar = None
    if typehint == bool:
        metavar = '{true,false}'
    elif is_optional(typehint, bool):
        metavar = '{true,false,null}'
    elif _issubclass(typehint, Enum):
        enum = typehint
        metavar = '{'+','.join(list(enum.__members__.keys()))+'}'
    elif is_optional(typehint, Enum):
        enum = typehint.__args__[0]
        metavar = '{'+','.join(list(enum.__members__.keys())+['null'])+'}'
    return metavar


def serialize_class_instance(val):
    type_val = type(val)
    val = str(val)
    warning(f"""
        Not possible to serialize an instance of {type_val}. It will be
        represented as the string {val}. If this was set as a default, consider
        using lazy_instance.
    """)
    return val


def callable_instances(cls: Type):
    # https://stackoverflow.com/a/71568161/2732151
    return isinstance(getattr(cls, '__call__', None), FunctionType)


def check_lazy_kwargs(class_type: Type, lazy_kwargs: dict):
    if lazy_kwargs:
        from .core import ArgumentParser
        parser = ArgumentParser(error_handler=None)
        parser.add_class_arguments(class_type)
        try:
            parser.parse_object(lazy_kwargs)
        except ParserError as ex:
            raise ValueError(str(ex)) from ex


class LazyInitBaseClass:

    def __init__(self, class_type: Type, lazy_kwargs: dict):
        check_lazy_kwargs(class_type, lazy_kwargs)
        self._lazy_class_type = class_type
        self._lazy_class_path = get_import_path(class_type)
        self._lazy_kwargs = lazy_kwargs
        self._lazy_methods = {}
        seen_methods: Dict = {}
        for name, _ in inspect.getmembers(class_type, predicate=inspect.isfunction):
            method = getattr(self, name)
            if not inspect.ismethod(method) or \
               name in {'__init__', '_lazy_init', '_lazy_init_then_call_method', 'lazy_get_init_data'}:
                continue
            assert name not in self.__dict__
            self._lazy_methods[name] = method
            if method in seen_methods:
                self.__dict__[name] = seen_methods[method]
            else:
                self.__dict__[name] = partial(self._lazy_init_then_call_method, name)
                seen_methods[method] = self.__dict__[name]

    def _lazy_init(self):
        for name in self._lazy_methods.keys():
            del self.__dict__[name]
        super().__init__(**self._lazy_kwargs)

    def _lazy_init_then_call_method(self, method_name, *args, **kwargs):
        self._lazy_init()
        return getattr(self, method_name)(*args, **kwargs)

    def lazy_get_init_data(self):
        init_args = Namespace(self._lazy_kwargs)
        if is_final_class(self._lazy_class_type):
            return init_args
        init = Namespace(class_path=self._lazy_class_path)
        if len(self._lazy_kwargs) > 0:
            init['init_args'] = init_args
        return init


ClassType = TypeVar('ClassType')


def lazy_instance(class_type: Type[ClassType], **kwargs) -> ClassType:
    """Instantiates a lazy instance of the given type.

    By lazy it is meant that the __init__ is delayed unit the first time that a
    method of the instance is called. It also provides a `lazy_get_init_data` method
    useful for serializing.

    Args:
        class_type: The class to instantiate.
        **kwargs: Any keyword arguments to use for instantiation.
    """
    lazy_init_class = type(
        'LazyInstance_'+class_type.__name__,
        (LazyInitBaseClass, class_type),
        {'__doc__': f'Class for lazy instances of {class_type}'},
    )
    return lazy_init_class(class_type, kwargs)
