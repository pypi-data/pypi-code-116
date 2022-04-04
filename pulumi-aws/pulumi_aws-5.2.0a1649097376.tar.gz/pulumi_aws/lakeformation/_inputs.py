# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'DataLakeSettingsCreateDatabaseDefaultPermissionArgs',
    'DataLakeSettingsCreateTableDefaultPermissionArgs',
    'PermissionsDataLocationArgs',
    'PermissionsDatabaseArgs',
    'PermissionsTableArgs',
    'PermissionsTableWithColumnsArgs',
    'GetPermissionsDataLocationArgs',
    'GetPermissionsDatabaseArgs',
    'GetPermissionsTableArgs',
    'GetPermissionsTableWithColumnsArgs',
]

@pulumi.input_type
class DataLakeSettingsCreateDatabaseDefaultPermissionArgs:
    def __init__(__self__, *,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 principal: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[Sequence[pulumi.Input[str]]] permissions: List of permissions that are granted to the principal. Valid values may include `ALL`, `SELECT`, `ALTER`, `DROP`, `DELETE`, `INSERT`, and `DESCRIBE`. For more details, see [Lake Formation Permissions Reference](https://docs.aws.amazon.com/lake-formation/latest/dg/lf-permissions-reference.html).
        :param pulumi.Input[str] principal: Principal who is granted permissions. To enforce metadata and underlying data access control only by IAM on new databases and tables set `principal` to `IAM_ALLOWED_PRINCIPALS` and `permissions` to `["ALL"]`.
        """
        if permissions is not None:
            pulumi.set(__self__, "permissions", permissions)
        if principal is not None:
            pulumi.set(__self__, "principal", principal)

    @property
    @pulumi.getter
    def permissions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of permissions that are granted to the principal. Valid values may include `ALL`, `SELECT`, `ALTER`, `DROP`, `DELETE`, `INSERT`, and `DESCRIBE`. For more details, see [Lake Formation Permissions Reference](https://docs.aws.amazon.com/lake-formation/latest/dg/lf-permissions-reference.html).
        """
        return pulumi.get(self, "permissions")

    @permissions.setter
    def permissions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "permissions", value)

    @property
    @pulumi.getter
    def principal(self) -> Optional[pulumi.Input[str]]:
        """
        Principal who is granted permissions. To enforce metadata and underlying data access control only by IAM on new databases and tables set `principal` to `IAM_ALLOWED_PRINCIPALS` and `permissions` to `["ALL"]`.
        """
        return pulumi.get(self, "principal")

    @principal.setter
    def principal(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "principal", value)


@pulumi.input_type
class DataLakeSettingsCreateTableDefaultPermissionArgs:
    def __init__(__self__, *,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 principal: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[Sequence[pulumi.Input[str]]] permissions: List of permissions that are granted to the principal. Valid values may include `ALL`, `SELECT`, `ALTER`, `DROP`, `DELETE`, `INSERT`, and `DESCRIBE`. For more details, see [Lake Formation Permissions Reference](https://docs.aws.amazon.com/lake-formation/latest/dg/lf-permissions-reference.html).
        :param pulumi.Input[str] principal: Principal who is granted permissions. To enforce metadata and underlying data access control only by IAM on new databases and tables set `principal` to `IAM_ALLOWED_PRINCIPALS` and `permissions` to `["ALL"]`.
        """
        if permissions is not None:
            pulumi.set(__self__, "permissions", permissions)
        if principal is not None:
            pulumi.set(__self__, "principal", principal)

    @property
    @pulumi.getter
    def permissions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of permissions that are granted to the principal. Valid values may include `ALL`, `SELECT`, `ALTER`, `DROP`, `DELETE`, `INSERT`, and `DESCRIBE`. For more details, see [Lake Formation Permissions Reference](https://docs.aws.amazon.com/lake-formation/latest/dg/lf-permissions-reference.html).
        """
        return pulumi.get(self, "permissions")

    @permissions.setter
    def permissions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "permissions", value)

    @property
    @pulumi.getter
    def principal(self) -> Optional[pulumi.Input[str]]:
        """
        Principal who is granted permissions. To enforce metadata and underlying data access control only by IAM on new databases and tables set `principal` to `IAM_ALLOWED_PRINCIPALS` and `permissions` to `["ALL"]`.
        """
        return pulumi.get(self, "principal")

    @principal.setter
    def principal(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "principal", value)


@pulumi.input_type
class PermissionsDataLocationArgs:
    def __init__(__self__, *,
                 arn: pulumi.Input[str],
                 catalog_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) that uniquely identifies the data location resource.
        :param pulumi.Input[str] catalog_id: Identifier for the Data Catalog. By default, it is the account ID of the caller.
        """
        pulumi.set(__self__, "arn", arn)
        if catalog_id is not None:
            pulumi.set(__self__, "catalog_id", catalog_id)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Input[str]:
        """
        Amazon Resource Name (ARN) that uniquely identifies the data location resource.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier for the Data Catalog. By default, it is the account ID of the caller.
        """
        return pulumi.get(self, "catalog_id")

    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "catalog_id", value)


@pulumi.input_type
class PermissionsDatabaseArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 catalog_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] name: Name of the table resource.
        :param pulumi.Input[str] catalog_id: Identifier for the Data Catalog. By default, it is the account ID of the caller.
        """
        pulumi.set(__self__, "name", name)
        if catalog_id is not None:
            pulumi.set(__self__, "catalog_id", catalog_id)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Name of the table resource.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier for the Data Catalog. By default, it is the account ID of the caller.
        """
        return pulumi.get(self, "catalog_id")

    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "catalog_id", value)


@pulumi.input_type
class PermissionsTableArgs:
    def __init__(__self__, *,
                 database_name: pulumi.Input[str],
                 catalog_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 wildcard: Optional[pulumi.Input[bool]] = None):
        """
        :param pulumi.Input[str] database_name: Name of the database for the table with columns resource. Unique to the Data Catalog.
        :param pulumi.Input[str] catalog_id: Identifier for the Data Catalog. By default, it is the account ID of the caller.
        :param pulumi.Input[str] name: Name of the table resource.
        """
        pulumi.set(__self__, "database_name", database_name)
        if catalog_id is not None:
            pulumi.set(__self__, "catalog_id", catalog_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if wildcard is not None:
            pulumi.set(__self__, "wildcard", wildcard)

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[str]:
        """
        Name of the database for the table with columns resource. Unique to the Data Catalog.
        """
        return pulumi.get(self, "database_name")

    @database_name.setter
    def database_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "database_name", value)

    @property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier for the Data Catalog. By default, it is the account ID of the caller.
        """
        return pulumi.get(self, "catalog_id")

    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "catalog_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the table resource.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def wildcard(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "wildcard")

    @wildcard.setter
    def wildcard(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "wildcard", value)


@pulumi.input_type
class PermissionsTableWithColumnsArgs:
    def __init__(__self__, *,
                 database_name: pulumi.Input[str],
                 name: pulumi.Input[str],
                 catalog_id: Optional[pulumi.Input[str]] = None,
                 column_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 excluded_column_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 wildcard: Optional[pulumi.Input[bool]] = None):
        """
        :param pulumi.Input[str] database_name: Name of the database for the table with columns resource. Unique to the Data Catalog.
        :param pulumi.Input[str] name: Name of the table resource.
        :param pulumi.Input[str] catalog_id: Identifier for the Data Catalog. By default, it is the account ID of the caller.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] column_names: Set of column names for the table.
        """
        pulumi.set(__self__, "database_name", database_name)
        pulumi.set(__self__, "name", name)
        if catalog_id is not None:
            pulumi.set(__self__, "catalog_id", catalog_id)
        if column_names is not None:
            pulumi.set(__self__, "column_names", column_names)
        if excluded_column_names is not None:
            pulumi.set(__self__, "excluded_column_names", excluded_column_names)
        if wildcard is not None:
            pulumi.set(__self__, "wildcard", wildcard)

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[str]:
        """
        Name of the database for the table with columns resource. Unique to the Data Catalog.
        """
        return pulumi.get(self, "database_name")

    @database_name.setter
    def database_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "database_name", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Name of the table resource.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier for the Data Catalog. By default, it is the account ID of the caller.
        """
        return pulumi.get(self, "catalog_id")

    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "catalog_id", value)

    @property
    @pulumi.getter(name="columnNames")
    def column_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Set of column names for the table.
        """
        return pulumi.get(self, "column_names")

    @column_names.setter
    def column_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "column_names", value)

    @property
    @pulumi.getter(name="excludedColumnNames")
    def excluded_column_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "excluded_column_names")

    @excluded_column_names.setter
    def excluded_column_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "excluded_column_names", value)

    @property
    @pulumi.getter
    def wildcard(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "wildcard")

    @wildcard.setter
    def wildcard(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "wildcard", value)


@pulumi.input_type
class GetPermissionsDataLocationArgs:
    def __init__(__self__, *,
                 arn: str,
                 catalog_id: str):
        """
        :param str arn: Amazon Resource Name (ARN) that uniquely identifies the data location resource.
        :param str catalog_id: Identifier for the Data Catalog. By default, it is the account ID of the caller.
        """
        pulumi.set(__self__, "arn", arn)
        pulumi.set(__self__, "catalog_id", catalog_id)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        Amazon Resource Name (ARN) that uniquely identifies the data location resource.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: str):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> str:
        """
        Identifier for the Data Catalog. By default, it is the account ID of the caller.
        """
        return pulumi.get(self, "catalog_id")

    @catalog_id.setter
    def catalog_id(self, value: str):
        pulumi.set(self, "catalog_id", value)


@pulumi.input_type
class GetPermissionsDatabaseArgs:
    def __init__(__self__, *,
                 catalog_id: str,
                 name: str):
        """
        :param str catalog_id: Identifier for the Data Catalog. By default, it is the account ID of the caller.
        :param str name: Name of the table resource.
        """
        pulumi.set(__self__, "catalog_id", catalog_id)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> str:
        """
        Identifier for the Data Catalog. By default, it is the account ID of the caller.
        """
        return pulumi.get(self, "catalog_id")

    @catalog_id.setter
    def catalog_id(self, value: str):
        pulumi.set(self, "catalog_id", value)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the table resource.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: str):
        pulumi.set(self, "name", value)


@pulumi.input_type
class GetPermissionsTableArgs:
    def __init__(__self__, *,
                 catalog_id: str,
                 database_name: str,
                 name: str,
                 wildcard: Optional[bool] = None):
        """
        :param str catalog_id: Identifier for the Data Catalog. By default, it is the account ID of the caller.
        :param str database_name: Name of the database for the table with columns resource. Unique to the Data Catalog.
        :param str name: Name of the table resource.
        :param bool wildcard: Whether to use a wildcard representing every table under a database. At least one of `name` or `wildcard` is required. Defaults to `false`.
        """
        pulumi.set(__self__, "catalog_id", catalog_id)
        pulumi.set(__self__, "database_name", database_name)
        pulumi.set(__self__, "name", name)
        if wildcard is not None:
            pulumi.set(__self__, "wildcard", wildcard)

    @property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> str:
        """
        Identifier for the Data Catalog. By default, it is the account ID of the caller.
        """
        return pulumi.get(self, "catalog_id")

    @catalog_id.setter
    def catalog_id(self, value: str):
        pulumi.set(self, "catalog_id", value)

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> str:
        """
        Name of the database for the table with columns resource. Unique to the Data Catalog.
        """
        return pulumi.get(self, "database_name")

    @database_name.setter
    def database_name(self, value: str):
        pulumi.set(self, "database_name", value)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the table resource.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: str):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def wildcard(self) -> Optional[bool]:
        """
        Whether to use a wildcard representing every table under a database. At least one of `name` or `wildcard` is required. Defaults to `false`.
        """
        return pulumi.get(self, "wildcard")

    @wildcard.setter
    def wildcard(self, value: Optional[bool]):
        pulumi.set(self, "wildcard", value)


@pulumi.input_type
class GetPermissionsTableWithColumnsArgs:
    def __init__(__self__, *,
                 catalog_id: str,
                 database_name: str,
                 name: str,
                 column_names: Optional[Sequence[str]] = None,
                 excluded_column_names: Optional[Sequence[str]] = None,
                 wildcard: Optional[bool] = None):
        """
        :param str catalog_id: Identifier for the Data Catalog. By default, it is the account ID of the caller.
        :param str database_name: Name of the database for the table with columns resource. Unique to the Data Catalog.
        :param str name: Name of the table resource.
        :param Sequence[str] column_names: Set of column names for the table. At least one of `column_names` or `excluded_column_names` is required.
        :param Sequence[str] excluded_column_names: Set of column names for the table to exclude. At least one of `column_names` or `excluded_column_names` is required.
        :param bool wildcard: Whether to use a wildcard representing every table under a database. At least one of `name` or `wildcard` is required. Defaults to `false`.
        """
        pulumi.set(__self__, "catalog_id", catalog_id)
        pulumi.set(__self__, "database_name", database_name)
        pulumi.set(__self__, "name", name)
        if column_names is not None:
            pulumi.set(__self__, "column_names", column_names)
        if excluded_column_names is not None:
            pulumi.set(__self__, "excluded_column_names", excluded_column_names)
        if wildcard is not None:
            pulumi.set(__self__, "wildcard", wildcard)

    @property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> str:
        """
        Identifier for the Data Catalog. By default, it is the account ID of the caller.
        """
        return pulumi.get(self, "catalog_id")

    @catalog_id.setter
    def catalog_id(self, value: str):
        pulumi.set(self, "catalog_id", value)

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> str:
        """
        Name of the database for the table with columns resource. Unique to the Data Catalog.
        """
        return pulumi.get(self, "database_name")

    @database_name.setter
    def database_name(self, value: str):
        pulumi.set(self, "database_name", value)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the table resource.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: str):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="columnNames")
    def column_names(self) -> Optional[Sequence[str]]:
        """
        Set of column names for the table. At least one of `column_names` or `excluded_column_names` is required.
        """
        return pulumi.get(self, "column_names")

    @column_names.setter
    def column_names(self, value: Optional[Sequence[str]]):
        pulumi.set(self, "column_names", value)

    @property
    @pulumi.getter(name="excludedColumnNames")
    def excluded_column_names(self) -> Optional[Sequence[str]]:
        """
        Set of column names for the table to exclude. At least one of `column_names` or `excluded_column_names` is required.
        """
        return pulumi.get(self, "excluded_column_names")

    @excluded_column_names.setter
    def excluded_column_names(self, value: Optional[Sequence[str]]):
        pulumi.set(self, "excluded_column_names", value)

    @property
    @pulumi.getter
    def wildcard(self) -> Optional[bool]:
        """
        Whether to use a wildcard representing every table under a database. At least one of `name` or `wildcard` is required. Defaults to `false`.
        """
        return pulumi.get(self, "wildcard")

    @wildcard.setter
    def wildcard(self, value: Optional[bool]):
        pulumi.set(self, "wildcard", value)


