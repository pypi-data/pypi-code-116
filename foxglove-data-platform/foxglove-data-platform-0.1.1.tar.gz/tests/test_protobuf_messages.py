from datetime import datetime
from unittest.mock import MagicMock, patch

import pytest

from foxglove_data_platform.client import Client

from .generate import generate_protobuf_data


def test_download_without_decoder():
    with patch(
        "foxglove_data_platform.client.decoder_for_schema",
        MagicMock(side_effect=Exception("Not found!")),
    ):
        client = Client("test")
        client.download_data = MagicMock(return_value=generate_protobuf_data())
        with pytest.raises(Exception):
            client.get_messages(
                device_id="test_id", start=datetime.now(), end=datetime.now()
            )


def test_download_with_decoder():
    client = Client("test")
    client.download_data = MagicMock(return_value=generate_protobuf_data())
    messages = client.get_messages(
        device_id="test_id", start=datetime.now(), end=datetime.now()
    )
    assert len(messages) == 10
