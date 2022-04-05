from collections import defaultdict
from typing import Union

import tqdm
from superannotate.logger import get_default_logger


class Reporter:
    def __init__(
        self,
        log_info: bool = True,
        log_warning: bool = True,
        disable_progress_bar: bool = False,
        log_debug: bool = True,
    ):
        self.logger = get_default_logger()
        self._log_info = log_info
        self._log_warning = log_warning
        self._log_debug = log_debug
        self._disable_progress_bar = disable_progress_bar
        self.info_messages = []
        self.warning_messages = []
        self.debug_messages = []
        self.custom_messages = defaultdict(set)
        self.progress_bar = None

    def disable_warnings(self):
        self._log_warning = False

    def disable_info(self):
        self._log_info = False

    def enable_warnings(self):
        self._log_warning = True

    def enable_info(self):
        self._log_info = True

    def log_info(self, value: str):
        if self._log_info:
            self.logger.info(value)
        self.info_messages.append(value)

    def log_warning(self, value: str):
        if self._log_warning:
            self.logger.warning(value)
        self.warning_messages.append(value)

    def log_debug(self, value: str):
        if self._log_debug:
            self.logger.debug(value)
        self.debug_messages.append(value)

    def start_progress(
        self,
        iterations: Union[int, range],
        description: str = "Processing",
        disable=False,
    ):
        self.progress_bar = self.get_progress_bar(iterations, description, disable)

    @staticmethod
    def get_progress_bar(
        iterations: Union[int, range], description: str = "Processing", disable=False
    ):
        if isinstance(iterations, range):
            return tqdm.tqdm(iterations, desc=description, disable=disable)
        else:
            return tqdm.tqdm(total=iterations, desc=description, disable=disable)

    def finish_progress(self):
        self.progress_bar.close()

    def update_progress(self, value: int = 1):
        if self.progress_bar:
            self.progress_bar.update(value)

    def generate_report(self) -> str:
        report = ""
        if self.info_messages:
            report += "\n".join(self.info_messages)
        if self.warning_messages:
            report += "\n".join(self.warning_messages)
        return report

    def store_message(self, key: str, value: str):
        self.custom_messages[key].add(value)

    @property
    def messages(self):
        for key, values in self.custom_messages.items():
            yield f"{key} [{', '.join(values)}]"


class Progress:
    def __init__(self, iterations: Union[int, range], description: str = "Processing"):
        self._iterations = iterations
        self._description = description
        self._progress_bar = None

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        if self._progress_bar:
            self._progress_bar.close()

    def update(self, value=1):
        if not self._progress_bar:
            self._progress_bar = Reporter.get_progress_bar(
                self._iterations, self._description
            )
        self._progress_bar.update(value)
