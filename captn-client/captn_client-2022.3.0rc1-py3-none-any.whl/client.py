# AUTOGENERATED! DO NOT EDIT! File to edit: notebooks/Client.ipynb (unless otherwise specified).

__all__ = ["Client", "DataBlob", "DataSource"]

# Cell

from .components.client import Client as _Client

Client = _Client

from airt.client import DataBlob as _DataBlob

DataBlob = _DataBlob

from airt.client import DataSource as _DataSource

DataSource = _DataSource

for cls in [Client, DataBlob, DataSource]:
    cls.__module__ = "captn.client"
