from pathlib import Path
from typing import Optional, List

from phidata.infra.docker.args import DockerArgs
from phidata.infra.docker.enums import DockerManagerStatus
from phidata.infra.docker.exceptions import DockerArgsException
from phidata.infra.docker.resource.types import DockerResourceType
from phidata.infra.docker.worker import DockerWorker
from phidata.utils.cli_console import print_error
from phidata.utils.log import logger


class DockerManager:
    def __init__(self, docker_args: DockerArgs):
        if docker_args is None or not isinstance(docker_args, DockerArgs):
            raise DockerArgsException("Invalid DockerArgs")
        if docker_args.workspace_root_path is None or not isinstance(
            docker_args.workspace_root_path, Path
        ):
            raise DockerArgsException("workspace_root_path invalid")
        if docker_args.workspace_config_file_path is None or not isinstance(
            docker_args.workspace_config_file_path, Path
        ):
            raise DockerArgsException("workspace_config_file_path invalid")

        self.docker_args: DockerArgs = docker_args
        self.docker_worker: DockerWorker = DockerWorker(self.docker_args)
        self.docker_status: DockerManagerStatus = DockerManagerStatus.PRE_INIT
        logger.debug("**-+-** DockerManager created")

    def get_status(self, refresh: bool = False) -> DockerManagerStatus:
        # logger.debug("Getting DockerManagerStatus")
        if refresh:
            self.docker_status = DockerManagerStatus.PRE_INIT
            logger.debug(f"DockerManagerStatus: {self.docker_status.value}")

        if self.docker_status == DockerManagerStatus.PRE_INIT:
            if (
                self.docker_worker is not None
                and self.docker_worker.is_client_initialized()
            ):
                self.docker_status = DockerManagerStatus.WORKER_READY
            else:
                print_error("DockerWorker not ready")

        if self.docker_status.can_create_resources():
            if (
                self.docker_worker is not None
                and self.docker_worker.are_resources_initialized()
            ):
                self.docker_status = DockerManagerStatus.RESOURCES_INIT

        logger.debug(f"DockerManagerStatus: {self.docker_status.value}")
        return self.docker_status

    def get_resources(
        self,
        name_filter: Optional[str] = None,
        type_filter: Optional[str] = None,
    ) -> Optional[List[DockerResourceType]]:

        status = self.get_status()
        if not status.can_get_resources():
            logger.debug("Cannot get resources")
            return None
        if self.docker_worker is None:
            logger.debug("No worker available")
            return None

        return self.docker_worker.get_resources(name_filter, type_filter)

    def create_resources_dry_run(
        self, name_filter: Optional[str] = None, type_filter: Optional[str] = None
    ) -> None:

        status = self.get_status()
        if not status.can_create_resources():
            logger.debug("Cannot create resources")
            return
        if self.docker_worker is None:
            logger.debug("No worker available")
            return

        # logger.debug("Creating resources dry run")
        self.docker_worker.create_resources_dry_run(
            name_filter=name_filter, type_filter=type_filter
        )

    def create_resources(
        self, name_filter: Optional[str] = None, type_filter: Optional[str] = None
    ) -> bool:

        status = self.get_status()
        if not status.can_create_resources():
            logger.debug("Cannot create resources")
            return False
        if self.docker_worker is None:
            logger.debug("No worker available")
            return False

        return self.docker_worker.create_resources(
            name_filter=name_filter, type_filter=type_filter
        )

    def validate_resources_are_created(
        self, name_filter: Optional[str] = None, type_filter: Optional[str] = None
    ) -> bool:

        logger.debug("Validating resources are created...")
        return True

    def delete_resources_dry_run(
        self, name_filter: Optional[str] = None, type_filter: Optional[str] = None
    ) -> None:

        status = self.get_status()
        if not status.can_delete_resources():
            logger.debug("Cannot delete resources")
            return
        if self.docker_worker is None:
            logger.debug("No worker available")
            return

        # logger.debug("Deleting resources dry run")
        self.docker_worker.delete_resources_dry_run(
            name_filter=name_filter, type_filter=type_filter
        )

    def delete_resources(
        self, name_filter: Optional[str] = None, type_filter: Optional[str] = None
    ) -> bool:

        status = self.get_status()
        if not status.can_delete_resources():
            logger.debug("Cannot delete resources")
            return False
        if self.docker_worker is None:
            logger.debug("No worker available")
            return False

        return self.docker_worker.delete_resources(name_filter=name_filter)

    def validate_resources_are_deleted(
        self, name_filter: Optional[str] = None, type_filter: Optional[str] = None
    ) -> bool:

        logger.debug("Validating resources are deleted...")
        return True

    ######################################################
    ## Patch Resources
    ######################################################

    def patch_resources_dry_run(
        self, name_filter: Optional[str] = None, type_filter: Optional[str] = None
    ) -> None:

        status = self.get_status()
        if not status.can_create_resources():
            logger.debug("Cannot patch resources")
            return
        if self.docker_worker is None:
            logger.debug("No worker available")
            return

        # logger.debug("Deleting resources dry run")
        self.docker_worker.patch_resources_dry_run(
            name_filter=name_filter, type_filter=type_filter
        )

    def patch_resources(
        self, name_filter: Optional[str] = None, type_filter: Optional[str] = None
    ) -> bool:

        status = self.get_status()
        if not status.can_create_resources():
            logger.debug("Cannot patch resources")
            return False
        if self.docker_worker is None:
            logger.debug("No worker available")
            return False

        return self.docker_worker.patch_resources(name_filter=name_filter)

    def validate_resources_are_patched(
        self, name_filter: Optional[str] = None, type_filter: Optional[str] = None
    ) -> bool:

        logger.debug("Validating resources are patched...")
        return True
