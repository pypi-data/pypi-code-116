# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: anki/collection.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from anki import generic_pb2 as anki_dot_generic__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x61nki/collection.proto\x12\x0f\x61nki.collection\x1a\x12\x61nki/generic.proto\"t\n\x15OpenCollectionRequest\x12\x17\n\x0f\x63ollection_path\x18\x01 \x01(\t\x12\x19\n\x11media_folder_path\x18\x02 \x01(\t\x12\x15\n\rmedia_db_path\x18\x03 \x01(\t\x12\x10\n\x08log_path\x18\x04 \x01(\t\"7\n\x16\x43loseCollectionRequest\x12\x1d\n\x15\x64owngrade_to_schema11\x18\x01 \x01(\x08\")\n\x15\x43heckDatabaseResponse\x12\x10\n\x08problems\x18\x01 \x03(\t\"\xe1\x01\n\tOpChanges\x12\x0c\n\x04\x63\x61rd\x18\x01 \x01(\x08\x12\x0c\n\x04note\x18\x02 \x01(\x08\x12\x0c\n\x04\x64\x65\x63k\x18\x03 \x01(\x08\x12\x0b\n\x03tag\x18\x04 \x01(\x08\x12\x10\n\x08notetype\x18\x05 \x01(\x08\x12\x0e\n\x06\x63onfig\x18\x06 \x01(\x08\x12\x13\n\x0b\x64\x65\x63k_config\x18\x0b \x01(\x08\x12\r\n\x05mtime\x18\x0c \x01(\x08\x12\x15\n\rbrowser_table\x18\x07 \x01(\x08\x12\x17\n\x0f\x62rowser_sidebar\x18\x08 \x01(\x08\x12\x11\n\tnote_text\x18\t \x01(\x08\x12\x14\n\x0cstudy_queues\x18\n \x01(\x08\"P\n\x12OpChangesWithCount\x12\r\n\x05\x63ount\x18\x01 \x01(\r\x12+\n\x07\x63hanges\x18\x02 \x01(\x0b\x32\x1a.anki.collection.OpChanges\"J\n\x0fOpChangesWithId\x12\n\n\x02id\x18\x01 \x01(\x03\x12+\n\x07\x63hanges\x18\x02 \x01(\x0b\x32\x1a.anki.collection.OpChanges\";\n\nUndoStatus\x12\x0c\n\x04undo\x18\x01 \x01(\t\x12\x0c\n\x04redo\x18\x02 \x01(\t\x12\x11\n\tlast_step\x18\x03 \x01(\r\"\xb5\x01\n\x12OpChangesAfterUndo\x12+\n\x07\x63hanges\x18\x01 \x01(\x0b\x32\x1a.anki.collection.OpChanges\x12\x11\n\toperation\x18\x02 \x01(\t\x12\x1d\n\x15reverted_to_timestamp\x18\x03 \x01(\x03\x12/\n\nnew_status\x18\x04 \x01(\x0b\x32\x1b.anki.collection.UndoStatus\x12\x0f\n\x07\x63ounter\x18\x05 \x01(\r\"\xe4\x04\n\x08Progress\x12#\n\x04none\x18\x01 \x01(\x0b\x32\x13.anki.generic.EmptyH\x00\x12\x39\n\nmedia_sync\x18\x02 \x01(\x0b\x32#.anki.collection.Progress.MediaSyncH\x00\x12\x15\n\x0bmedia_check\x18\x03 \x01(\tH\x00\x12\x37\n\tfull_sync\x18\x04 \x01(\x0b\x32\".anki.collection.Progress.FullSyncH\x00\x12;\n\x0bnormal_sync\x18\x05 \x01(\x0b\x32$.anki.collection.Progress.NormalSyncH\x00\x12\x41\n\x0e\x64\x61tabase_check\x18\x06 \x01(\x0b\x32\'.anki.collection.Progress.DatabaseCheckH\x00\x12\x13\n\timporting\x18\x07 \x01(\tH\x00\x12\x13\n\texporting\x18\x08 \x01(\rH\x00\x1a<\n\tMediaSync\x12\x0f\n\x07\x63hecked\x18\x01 \x01(\t\x12\r\n\x05\x61\x64\x64\x65\x64\x18\x02 \x01(\t\x12\x0f\n\x07removed\x18\x03 \x01(\t\x1a.\n\x08\x46ullSync\x12\x13\n\x0btransferred\x18\x01 \x01(\r\x12\r\n\x05total\x18\x02 \x01(\r\x1a;\n\nNormalSync\x12\r\n\x05stage\x18\x01 \x01(\t\x12\r\n\x05\x61\x64\x64\x65\x64\x18\x02 \x01(\t\x12\x0f\n\x07removed\x18\x03 \x01(\t\x1aJ\n\rDatabaseCheck\x12\r\n\x05stage\x18\x01 \x01(\t\x12\x13\n\x0bstage_total\x18\x02 \x01(\r\x12\x15\n\rstage_current\x18\x03 \x01(\rB\x07\n\x05value\"X\n\x13\x43reateBackupRequest\x12\x15\n\rbackup_folder\x18\x01 \x01(\t\x12\r\n\x05\x66orce\x18\x02 \x01(\x08\x12\x1b\n\x13wait_for_completion\x18\x03 \x01(\x08\x32\xda\x06\n\x11\x43ollectionService\x12M\n\x0eOpenCollection\x12&.anki.collection.OpenCollectionRequest\x1a\x13.anki.generic.Empty\x12O\n\x0f\x43loseCollection\x12\'.anki.collection.CloseCollectionRequest\x1a\x13.anki.generic.Empty\x12L\n\rCheckDatabase\x12\x13.anki.generic.Empty\x1a&.anki.collection.CheckDatabaseResponse\x12\x41\n\rGetUndoStatus\x12\x13.anki.generic.Empty\x1a\x1b.anki.collection.UndoStatus\x12@\n\x04Undo\x12\x13.anki.generic.Empty\x1a#.anki.collection.OpChangesAfterUndo\x12@\n\x04Redo\x12\x13.anki.generic.Empty\x1a#.anki.collection.OpChangesAfterUndo\x12@\n\x12\x41\x64\x64\x43ustomUndoEntry\x12\x14.anki.generic.String\x1a\x14.anki.generic.UInt32\x12\x44\n\x10MergeUndoEntries\x12\x14.anki.generic.UInt32\x1a\x1a.anki.collection.OpChanges\x12@\n\x0eLatestProgress\x12\x13.anki.generic.Empty\x1a\x19.anki.collection.Progress\x12\x39\n\rSetWantsAbort\x12\x13.anki.generic.Empty\x1a\x13.anki.generic.Empty\x12H\n\x0c\x43reateBackup\x12$.anki.collection.CreateBackupRequest\x1a\x12.anki.generic.Bool\x12\x41\n\x15\x41waitBackupCompletion\x12\x13.anki.generic.Empty\x1a\x13.anki.generic.Emptyb\x06proto3')



_OPENCOLLECTIONREQUEST = DESCRIPTOR.message_types_by_name['OpenCollectionRequest']
_CLOSECOLLECTIONREQUEST = DESCRIPTOR.message_types_by_name['CloseCollectionRequest']
_CHECKDATABASERESPONSE = DESCRIPTOR.message_types_by_name['CheckDatabaseResponse']
_OPCHANGES = DESCRIPTOR.message_types_by_name['OpChanges']
_OPCHANGESWITHCOUNT = DESCRIPTOR.message_types_by_name['OpChangesWithCount']
_OPCHANGESWITHID = DESCRIPTOR.message_types_by_name['OpChangesWithId']
_UNDOSTATUS = DESCRIPTOR.message_types_by_name['UndoStatus']
_OPCHANGESAFTERUNDO = DESCRIPTOR.message_types_by_name['OpChangesAfterUndo']
_PROGRESS = DESCRIPTOR.message_types_by_name['Progress']
_PROGRESS_MEDIASYNC = _PROGRESS.nested_types_by_name['MediaSync']
_PROGRESS_FULLSYNC = _PROGRESS.nested_types_by_name['FullSync']
_PROGRESS_NORMALSYNC = _PROGRESS.nested_types_by_name['NormalSync']
_PROGRESS_DATABASECHECK = _PROGRESS.nested_types_by_name['DatabaseCheck']
_CREATEBACKUPREQUEST = DESCRIPTOR.message_types_by_name['CreateBackupRequest']
OpenCollectionRequest = _reflection.GeneratedProtocolMessageType('OpenCollectionRequest', (_message.Message,), {
  'DESCRIPTOR' : _OPENCOLLECTIONREQUEST,
  '__module__' : 'anki.collection_pb2'
  # @@protoc_insertion_point(class_scope:anki.collection.OpenCollectionRequest)
  })
_sym_db.RegisterMessage(OpenCollectionRequest)

CloseCollectionRequest = _reflection.GeneratedProtocolMessageType('CloseCollectionRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLOSECOLLECTIONREQUEST,
  '__module__' : 'anki.collection_pb2'
  # @@protoc_insertion_point(class_scope:anki.collection.CloseCollectionRequest)
  })
_sym_db.RegisterMessage(CloseCollectionRequest)

CheckDatabaseResponse = _reflection.GeneratedProtocolMessageType('CheckDatabaseResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHECKDATABASERESPONSE,
  '__module__' : 'anki.collection_pb2'
  # @@protoc_insertion_point(class_scope:anki.collection.CheckDatabaseResponse)
  })
_sym_db.RegisterMessage(CheckDatabaseResponse)

OpChanges = _reflection.GeneratedProtocolMessageType('OpChanges', (_message.Message,), {
  'DESCRIPTOR' : _OPCHANGES,
  '__module__' : 'anki.collection_pb2'
  # @@protoc_insertion_point(class_scope:anki.collection.OpChanges)
  })
_sym_db.RegisterMessage(OpChanges)

OpChangesWithCount = _reflection.GeneratedProtocolMessageType('OpChangesWithCount', (_message.Message,), {
  'DESCRIPTOR' : _OPCHANGESWITHCOUNT,
  '__module__' : 'anki.collection_pb2'
  # @@protoc_insertion_point(class_scope:anki.collection.OpChangesWithCount)
  })
_sym_db.RegisterMessage(OpChangesWithCount)

OpChangesWithId = _reflection.GeneratedProtocolMessageType('OpChangesWithId', (_message.Message,), {
  'DESCRIPTOR' : _OPCHANGESWITHID,
  '__module__' : 'anki.collection_pb2'
  # @@protoc_insertion_point(class_scope:anki.collection.OpChangesWithId)
  })
_sym_db.RegisterMessage(OpChangesWithId)

UndoStatus = _reflection.GeneratedProtocolMessageType('UndoStatus', (_message.Message,), {
  'DESCRIPTOR' : _UNDOSTATUS,
  '__module__' : 'anki.collection_pb2'
  # @@protoc_insertion_point(class_scope:anki.collection.UndoStatus)
  })
_sym_db.RegisterMessage(UndoStatus)

OpChangesAfterUndo = _reflection.GeneratedProtocolMessageType('OpChangesAfterUndo', (_message.Message,), {
  'DESCRIPTOR' : _OPCHANGESAFTERUNDO,
  '__module__' : 'anki.collection_pb2'
  # @@protoc_insertion_point(class_scope:anki.collection.OpChangesAfterUndo)
  })
_sym_db.RegisterMessage(OpChangesAfterUndo)

Progress = _reflection.GeneratedProtocolMessageType('Progress', (_message.Message,), {

  'MediaSync' : _reflection.GeneratedProtocolMessageType('MediaSync', (_message.Message,), {
    'DESCRIPTOR' : _PROGRESS_MEDIASYNC,
    '__module__' : 'anki.collection_pb2'
    # @@protoc_insertion_point(class_scope:anki.collection.Progress.MediaSync)
    })
  ,

  'FullSync' : _reflection.GeneratedProtocolMessageType('FullSync', (_message.Message,), {
    'DESCRIPTOR' : _PROGRESS_FULLSYNC,
    '__module__' : 'anki.collection_pb2'
    # @@protoc_insertion_point(class_scope:anki.collection.Progress.FullSync)
    })
  ,

  'NormalSync' : _reflection.GeneratedProtocolMessageType('NormalSync', (_message.Message,), {
    'DESCRIPTOR' : _PROGRESS_NORMALSYNC,
    '__module__' : 'anki.collection_pb2'
    # @@protoc_insertion_point(class_scope:anki.collection.Progress.NormalSync)
    })
  ,

  'DatabaseCheck' : _reflection.GeneratedProtocolMessageType('DatabaseCheck', (_message.Message,), {
    'DESCRIPTOR' : _PROGRESS_DATABASECHECK,
    '__module__' : 'anki.collection_pb2'
    # @@protoc_insertion_point(class_scope:anki.collection.Progress.DatabaseCheck)
    })
  ,
  'DESCRIPTOR' : _PROGRESS,
  '__module__' : 'anki.collection_pb2'
  # @@protoc_insertion_point(class_scope:anki.collection.Progress)
  })
_sym_db.RegisterMessage(Progress)
_sym_db.RegisterMessage(Progress.MediaSync)
_sym_db.RegisterMessage(Progress.FullSync)
_sym_db.RegisterMessage(Progress.NormalSync)
_sym_db.RegisterMessage(Progress.DatabaseCheck)

CreateBackupRequest = _reflection.GeneratedProtocolMessageType('CreateBackupRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEBACKUPREQUEST,
  '__module__' : 'anki.collection_pb2'
  # @@protoc_insertion_point(class_scope:anki.collection.CreateBackupRequest)
  })
_sym_db.RegisterMessage(CreateBackupRequest)

_COLLECTIONSERVICE = DESCRIPTOR.services_by_name['CollectionService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _OPENCOLLECTIONREQUEST._serialized_start=62
  _OPENCOLLECTIONREQUEST._serialized_end=178
  _CLOSECOLLECTIONREQUEST._serialized_start=180
  _CLOSECOLLECTIONREQUEST._serialized_end=235
  _CHECKDATABASERESPONSE._serialized_start=237
  _CHECKDATABASERESPONSE._serialized_end=278
  _OPCHANGES._serialized_start=281
  _OPCHANGES._serialized_end=506
  _OPCHANGESWITHCOUNT._serialized_start=508
  _OPCHANGESWITHCOUNT._serialized_end=588
  _OPCHANGESWITHID._serialized_start=590
  _OPCHANGESWITHID._serialized_end=664
  _UNDOSTATUS._serialized_start=666
  _UNDOSTATUS._serialized_end=725
  _OPCHANGESAFTERUNDO._serialized_start=728
  _OPCHANGESAFTERUNDO._serialized_end=909
  _PROGRESS._serialized_start=912
  _PROGRESS._serialized_end=1524
  _PROGRESS_MEDIASYNC._serialized_start=1270
  _PROGRESS_MEDIASYNC._serialized_end=1330
  _PROGRESS_FULLSYNC._serialized_start=1332
  _PROGRESS_FULLSYNC._serialized_end=1378
  _PROGRESS_NORMALSYNC._serialized_start=1380
  _PROGRESS_NORMALSYNC._serialized_end=1439
  _PROGRESS_DATABASECHECK._serialized_start=1441
  _PROGRESS_DATABASECHECK._serialized_end=1515
  _CREATEBACKUPREQUEST._serialized_start=1526
  _CREATEBACKUPREQUEST._serialized_end=1614
  _COLLECTIONSERVICE._serialized_start=1617
  _COLLECTIONSERVICE._serialized_end=2475
# @@protoc_insertion_point(module_scope)
