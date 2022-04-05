import os
import shutil
from tarfile import TarFile
from typing import Callable, List, Optional, IO
from zipfile import ZipFile

import sfu_torch_lib.io as io


IsMemberType = Callable[[str], bool]


class FileFetcher:
    members: List[str]

    def __init__(self, path: str, is_member: IsMemberType) -> None:
        self.path = path
        self.is_member = is_member

    def __len__(self) -> int:
        return len(self.members)

    def __getitem__(self, index: int) -> str:
        return self.members[index]

    def open_member(self, key: str) -> IO:
        raise NotImplementedError()


class ZipFileFetcher(FileFetcher):
    def __init__(
            self, path: str,
            is_member: IsMemberType,
            ephemeral_path: Optional[str] = os.environ.get('DATA_EPHEMERAL_PATH'),
    ) -> None:

        super().__init__(path, is_member)

        self.ephemeral_path = ephemeral_path

        self.members = self.get_members(path, is_member)
        self.container: Optional[ZipFile] = None

    @staticmethod
    def get_members(path: str, is_member: Callable[[str], bool]) -> List[str]:
        return [name for name in ZipFile(path).namelist() if is_member(name)]

    def open_member(self, key: str) -> IO:
        if self.container is None:
            self.container = ZipFile(self.path)

        if self.ephemeral_path is not None:
            prefix = io.generate_path(prefix=self.ephemeral_path)
            path = os.path.join(prefix, key)

            if not io.exists(path):
                os.makedirs(os.path.dirname(path), exist_ok=True)
                self.container.extract(key, prefix)

            file_object = io.open(path)

        else:
            file_object = self.container.open(key)

        return file_object


class TarFileFetcher(FileFetcher):
    def __init__(
            self, path: str,
            is_member: IsMemberType,
            ephemeral_path: Optional[str] = os.environ.get('DATA_EPHEMERAL_PATH'),
    ) -> None:

        super().__init__(path, is_member)

        self.ephemeral_path = ephemeral_path

        self.members = self.get_members(path, is_member)
        self.container: Optional[TarFile] = None

    @staticmethod
    def get_members(path: str, is_member: Callable[[str], bool]) -> List[str]:
        return [name for name in TarFile(path).getnames() if is_member(name)]

    def open_member(self, key: str) -> IO:
        if self.container is None:
            self.container = TarFile(self.path)

        if self.ephemeral_path is not None:
            prefix = io.generate_path(prefix=self.ephemeral_path)
            path = os.path.join(prefix, key)

            if not io.exists(path):
                os.makedirs(os.path.dirname(path), exist_ok=True)
                self.container.extract(key, prefix)

            file_object = io.open(path)

        else:
            file_object_or_none = self.container.extractfile(key)

            if file_object_or_none is None:
                raise IOError(f'Member {key} is not a file.')

            file_object = file_object_or_none

        return file_object


class FileSystemFileFetcher(FileFetcher):
    def __init__(
            self,
            path: str,
            is_member: IsMemberType,
            ephemeral_path: Optional[str] = os.environ.get('DATA_EPHEMERAL_PATH'),
    ) -> None:

        super().__init__(path, is_member)

        self.ephemeral_path = ephemeral_path

        self.members = self.get_members(path, is_member)

    @staticmethod
    def get_members(path: str, is_member: Callable[[str], bool]) -> List[str]:
        return [
            name
            for name
            in (os.path.relpath(key, path) for key in io.get_files(path))
            if is_member(name)
        ]

    def open_member(self, key: str) -> IO:
        path_original = io.generate_path(key, self.path)

        if self.ephemeral_path is not None:
            prefix = io.generate_path(prefix=self.ephemeral_path)
            path_ephemeral = os.path.join(prefix, key)

            if not io.exists(path_ephemeral):
                os.makedirs(os.path.dirname(path_ephemeral), exist_ok=True)
                shutil.copy(path_original, path_ephemeral)

            file_object = io.open(path_ephemeral)

        else:
            file_object = io.open(path_original)

        return file_object


def get_file_fetcher(path: str, is_member: IsMemberType = lambda _: True) -> FileFetcher:
    if path.endswith('.zip'):
        return ZipFileFetcher(path, is_member)
    elif path.endswith('.tar'):
        return TarFileFetcher(path, is_member)
    else:
        return FileSystemFileFetcher(path, is_member)
