from typing import Optional
from typing_extensions import Literal

import docker

from phidata.infra.base.api_client import InfraApiClient
from phidata.infra.docker.exceptions import DockerApiClientException
from phidata.utils.cli_console import print_error
from phidata.utils.log import logger


class DockerApiClient(InfraApiClient):
    """
    This class is a wrapper around the docker client to use with a DockerWorker
    Currently only supports local docker but can be modified to support a swarm cluster as well
    """

    def __init__(self, cluster_type: Literal["local", "swarm"] = "local"):

        super().__init__()
        # logger.debug(f"Creating DockerApiClient")
        # Cluster configuration
        self.cluster_type: Literal["local", "swarm"] = cluster_type

        # docker API client
        self._api_client: Optional[docker.DockerClient] = None
        logger.debug(f"**-+-** DockerApiClient created")

    def is_initialized(self) -> bool:
        if self.api_client is not None:
            return True
        return False

    def create_api_client(self) -> docker.DockerClient:
        """Create a docker.DockerApiClient"""

        logger.debug("Creating docker.DockerApiClient")
        api_client = None
        try:
            if self.cluster_type == "local":
                api_client = docker.from_env()
            else:
                raise DockerApiClientException(f"{self.cluster_type} not supported")
        except Exception as e:
            print_error("Could not create docker.DockerApiClient")
            print_error(e)
            exit(0)
        return api_client

    @property
    def api_client(self) -> docker.DockerClient:
        if self._api_client is None:
            self._api_client = self.create_api_client()
        return self._api_client
