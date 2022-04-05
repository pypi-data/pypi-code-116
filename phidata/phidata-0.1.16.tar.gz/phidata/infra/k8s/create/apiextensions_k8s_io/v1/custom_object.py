from typing import Any, Dict, Optional

from pydantic import BaseModel

from phidata.infra.k8s.enums.api_version import ApiVersion
from phidata.infra.k8s.enums.kind import Kind
from phidata.infra.k8s.create.apiextensions_k8s_io.v1.custom_resource_definition import (
    CreateCustomResourceDefinition,
)
from phidata.infra.k8s.resource.apiextensions_k8s_io.v1.custom_object import (
    CustomObject,
)
from phidata.infra.k8s.create.common.labels import create_component_labels_dict
from phidata.infra.k8s.resource.meta.v1.object_meta import ObjectMeta
from phidata.utils.cli_console import print_error
from phidata.utils.log import logger


class CreateCustomObject(BaseModel):
    name: str
    app_name: str
    crd: CreateCustomResourceDefinition
    version: Optional[str] = None
    spec: Optional[Dict[str, Any]] = None
    namespace: Optional[str] = None
    service_account_name: Optional[str] = None
    labels: Optional[Dict[str, str]] = None

    def create(self) -> Optional[CustomObject]:
        """Creates a CustomObject resource."""
        # logger.debug(f"Creating CustomObject Resource: {group_name}")

        custom_object_name = self.name
        custom_object_labels = create_component_labels_dict(
            component_name=custom_object_name,
            app_name=self.app_name,
            labels=self.labels,
        )

        api_group_str: str = self.crd.group

        api_version_str: Optional[str] = None
        if self.version is not None and isinstance(self.version, str):
            api_version_str = self.version
        elif len(self.crd.versions) >= 1:
            api_version_str = self.crd.versions[0].name
        # api_version is required
        if api_version_str is None:
            print_error(f"CustomObject ApiVersion invalid: {api_version_str}")
            return None

        plural: Optional[str] = self.crd.names.plural
        # plural is required
        if plural is None:
            print_error(f"CustomResourceDefinition plural invalid: {plural}")
            return None

        # validate api_group_str and api_version_str
        api_group_version_str = "{}/{}".format(api_group_str, api_version_str)
        api_version_enum = None
        try:
            api_version_enum = ApiVersion.from_str(api_group_version_str)
        except NotImplementedError as e:
            print_error(f"{api_group_version_str} is not a supported API version")
            print_error("Please add to phidata.infra.k8s.enums.api_version.ApiVersion")
            return None

        kind_str: str = self.crd.names.kind
        kind_enum = None
        try:
            kind_enum = Kind.from_str(kind_str)
        except NotImplementedError as e:
            print_error(f"{kind_str} is not a supported Kind")
            print_error("Please add to phidata.infra.k8s.enums.kind.Kind")
            return None

        custom_object = CustomObject(
            api_version=api_version_enum,
            kind=kind_enum,
            metadata=ObjectMeta(
                name=custom_object_name,
                namespace=self.namespace,
                labels=custom_object_labels,
            ),
            group=api_group_str,
            version=api_version_str,
            plural=plural,
            spec=self.spec,
        )

        # logger.debug(
        #     f"CustomObject {custom_object_name}:\n{custom_object.json(exclude_defaults=True, indent=2)}"
        # )
        return custom_object
