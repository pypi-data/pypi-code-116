from __future__ import annotations

import weakref
from typing import AnyStr, Generic

from coredis.exceptions import FunctionError
from coredis.typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    Iterable,
    KeyT,
    Literal,
    Optional,
    StringT,
    ValueT,
)
from coredis.utils import EncodingInsensitiveDict, nativestr

if TYPE_CHECKING:
    import coredis.client


class Library(Generic[AnyStr]):
    def __init__(
        self,
        client: coredis.client.AbstractRedis,
        name: StringT,
        code: Optional[StringT] = None,
        *,
        engine: Literal["LUA"] = "LUA",
    ):
        """
        Abstraction over a library of redis functions

        Example::

            library_code = "redis.register_function('myfunc', function(k, a) return a[1] end)"
            lib = await Library(client, "mylib", library_code)
            assert "1" == await lib["myfunc"]([], [1])
        """
        self._client: weakref.ReferenceType[coredis.client.AbstractRedis] = weakref.ref(
            client
        )
        self._name = nativestr(name)
        self._engine = engine
        self._code = code
        self._functions: EncodingInsensitiveDict = EncodingInsensitiveDict()

    @property
    def client(self) -> coredis.client.AbstractRedis:
        c = self._client()
        assert c
        return c

    @property
    def functions(self) -> Dict[str, Function]:
        """
        mapping of function names to :class:`~coredis.commands.function.Function`
        instances that can be directly called.
        """
        return self._functions

    async def update(self, new_code: StringT) -> bool:
        """
        Update the code of a library with :paramref:`new_code`
        """
        if await self.client.function_load(
            self._engine, self._name, new_code, replace=True
        ):
            await self.__initialize()
            return True
        return False

    def __getitem__(self, function: str) -> Optional[Function]:
        return self._functions.get(function)

    async def __initialize(self):
        self._functions.clear()
        if self._code:
            await self.client.function_load(self._engine, self._name, self._code)
        library = (await self.client.function_list(self._name)).get(self._name)

        if not library:
            raise FunctionError(f"No library found for {self._name}")

        for name, function in library["functions"].items():
            self._functions[name] = Function(self.client, self._name, name)

    def __await__(self):
        async def closure():
            await self.__initialize()
            return self

        return closure().__await__()


class Function:
    def __init__(
        self, client: coredis.client.AbstractRedis, library: StringT, name: StringT
    ):
        """
        Wrapper to call a redis function that has already been loaded


        Example::

            func = await Function(client, "mylib", "myfunc")
            response = await func(keys=["a"], args=[1])
        """
        self._client: weakref.ReferenceType[coredis.client.AbstractRedis] = weakref.ref(
            client
        )
        self._library = Library(client, library)
        self._name = name

    @property
    def client(self) -> coredis.client.AbstractRedis:
        c = self._client()
        assert c
        return c

    def __await__(self):
        async def closure():
            await self._library

        return closure().__await__()

    async def __call__(
        self,
        *,
        keys: Optional[Iterable[KeyT]] = None,
        args: Optional[Iterable[ValueT]] = None,
    ) -> Any:
        """
        Wrapper to call :meth:`~coredis.Redis.fcall`

        :param args:
        :param keys:
        """
        return await self.client.fcall(self._name, keys or [], args or [])
