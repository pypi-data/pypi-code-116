from django_filters.filters import BooleanFilter, NumberFilter, MultipleChoiceFilter
import graphene

from nautobot.core.graphql import BigInteger
from nautobot.utilities.filters import MultiValueBigNumberFilter, MultiValueNumberFilter


def str_to_var_name(verbose_name):
    """Convert a string to a variable compatible name.
    Examples:
        IP Addresses > ip_addresses
    """
    return verbose_name.lower().replace(" ", "_").replace("-", "_")


def get_filtering_args_from_filterset(filterset_class):
    """Generate a list of filter arguments from a filterset.

    The FilterSet class will be instantiated before extracting the list of arguments to
    account for dynamic filters, inserted when the class is instantiated. (required for Custom Fields filters).

    Filter fields that are inheriting from BooleanFilter and NumberFilter will be converted
    to their appropriate type, everything else will be of type String.
    if the filter field is a subclass of MultipleChoiceFilter, the argument will be converted as a list

    Args:
        filterset_class(FilterSet): FilterSet class used to extract the argument

    Returns:
        dict(graphene.Argument): Filter Arguments organized in a dictionary
    """

    args = {}
    instance = filterset_class()

    for filter_name, filter_field in instance.filters.items():
        # For general safety, but especially for the case of custom fields
        # (https://github.com/nautobot/nautobot/issues/464)
        filter_name = str_to_var_name(filter_name)

        field_type = graphene.String
        filter_field_class = type(filter_field)

        if issubclass(filter_field_class, MultiValueBigNumberFilter):
            field_type = graphene.List(BigInteger)
        elif issubclass(filter_field_class, MultiValueNumberFilter):
            field_type = graphene.List(graphene.Int)
        else:
            if issubclass(filter_field_class, BooleanFilter):
                field_type = graphene.Boolean
            elif issubclass(filter_field_class, NumberFilter):
                field_type = graphene.Int
            else:
                field_type = graphene.String

            if issubclass(filter_field_class, MultipleChoiceFilter):
                field_type = graphene.List(field_type)

        args[filter_name] = graphene.Argument(
            field_type,
            description=filter_field.label,
            required=False,
        )

    # Hack to swap `type` fields to `_type` since they will conflict with
    # `graphene.types.fields.Field.type` in Graphene 2.x.
    # TODO(jathan): Once we upgrade to Graphene 3.x we can remove this, but we
    # will still need to do an API migration to deprecate it. This argument was
    # validated to be safe to keep even in Graphene 3.
    if "type" in args:
        args["_type"] = args.pop("type")

    return args


def construct_resolver(model_name, resolver_type):
    """Constructs a resolve_[cable_peer|connected_endpoint]_<endpoint> function for a given model type.

    Args:
        model_name (str): Name of the model to construct a resolver function for (e.g. CircuitTermination).
        resolver_type (str): One of ['connected_endpoint', 'cable_peer']
    """
    if resolver_type == "cable_peer":

        def resolve(self, args):
            peer = self.get_cable_peer()
            if type(peer).__name__ == model_name:
                return peer
            return None

        return resolve

    if resolver_type == "connected_endpoint":

        def resolve(self, args):
            peer = self.connected_endpoint
            if type(peer).__name__ == model_name:
                return peer
            return None

        return resolve
