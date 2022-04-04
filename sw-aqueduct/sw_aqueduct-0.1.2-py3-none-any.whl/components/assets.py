# Copyright: (c) 2022, Swimlane <info@swimlane.com>
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from ..base import Base
from ..models import Asset


class Assets(Base):

    """Used to sync assets from a source instance to a destination instance of Swimlane
    """

    def __set_dest_assets(self):
        if not hasattr(self, 'dest_assets'):
            dest_assets = self.destination_instance.get_assets()
            if dest_assets:
                self.dest_assets = [x.name for x in dest_assets]
            else: self.dest_assets = None

    def sync_asset(self, asset: Asset):
        """This method will create (add) a single asset from a source instance to a destination instance.

        Currently we are only adding assets and NOT updating them but this functionality may expand in the future.

        Args:
            asset (dict): A single Swimlane asset dictionary from the Swimlane API
        """
        if not self._is_in_include_exclude_lists(asset.name, 'assets'):
            self.__logger.info(f"Processing asset '{asset.name}'.")
            self.__set_dest_assets()
            if asset.name not in self.dest_assets:
                self.__logger.info(f"Asset '{asset.name}' was not found on destination.")
                self.destination_instance.add_asset(asset)
                self.__logger.info(f"Asset '{asset.name}' was successfully added to destination.")
            else:
                self.__logger.info(f"Asset '{asset.name}' already exists on destination. Skipping")

    def sync(self):
        """This method is used to sync (create) all assets from a source instance to a destination instance
        """
        self.__logger.info(f"Attempting to sync assets from '{self.source_host}' to '{self.dest_host}'")
        self.__set_dest_assets()
        for asset in self.source_instance.get_assets():
            self.sync_asset(asset=asset)
