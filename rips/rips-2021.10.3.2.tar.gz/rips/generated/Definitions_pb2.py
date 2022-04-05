# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Definitions.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Definitions.proto',
  package='rips',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11\x44\x65\x66initions.proto\x12\x04rips\"\x07\n\x05\x45mpty\"9\n\x19\x43lientToServerStreamReply\x12\x1c\n\x14\x61\x63\x63\x65pted_value_count\x18\x01 \x01(\x03\"(\n\x05Vec3i\x12\t\n\x01i\x18\x01 \x01(\x05\x12\t\n\x01j\x18\x02 \x01(\x05\x12\t\n\x01k\x18\x03 \x01(\x05\"(\n\x05Vec3d\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\"+\n\x0b\x43\x65llCenters\x12\x1c\n\x07\x63\x65nters\x18\x01 \x03(\x0b\x32\x0b.rips.Vec3d\"\xd5\x01\n\x0b\x43\x65llCorners\x12\x17\n\x02\x63\x30\x18\x01 \x01(\x0b\x32\x0b.rips.Vec3d\x12\x17\n\x02\x63\x31\x18\x02 \x01(\x0b\x32\x0b.rips.Vec3d\x12\x17\n\x02\x63\x32\x18\x03 \x01(\x0b\x32\x0b.rips.Vec3d\x12\x17\n\x02\x63\x33\x18\x04 \x01(\x0b\x32\x0b.rips.Vec3d\x12\x17\n\x02\x63\x34\x18\x05 \x01(\x0b\x32\x0b.rips.Vec3d\x12\x17\n\x02\x63\x35\x18\x06 \x01(\x0b\x32\x0b.rips.Vec3d\x12\x17\n\x02\x63\x36\x18\x07 \x01(\x0b\x32\x0b.rips.Vec3d\x12\x17\n\x02\x63\x37\x18\x08 \x01(\x0b\x32\x0b.rips.Vec3d\"4\n\x10\x43\x65llCornersArray\x12 \n\x05\x63\x65lls\x18\x01 \x03(\x0b\x32\x11.rips.CellCornersb\x06proto3'
)




_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='rips.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=34,
)


_CLIENTTOSERVERSTREAMREPLY = _descriptor.Descriptor(
  name='ClientToServerStreamReply',
  full_name='rips.ClientToServerStreamReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='accepted_value_count', full_name='rips.ClientToServerStreamReply.accepted_value_count', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=93,
)


_VEC3I = _descriptor.Descriptor(
  name='Vec3i',
  full_name='rips.Vec3i',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='i', full_name='rips.Vec3i.i', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='j', full_name='rips.Vec3i.j', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='k', full_name='rips.Vec3i.k', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=95,
  serialized_end=135,
)


_VEC3D = _descriptor.Descriptor(
  name='Vec3d',
  full_name='rips.Vec3d',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='rips.Vec3d.x', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='rips.Vec3d.y', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='z', full_name='rips.Vec3d.z', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=137,
  serialized_end=177,
)


_CELLCENTERS = _descriptor.Descriptor(
  name='CellCenters',
  full_name='rips.CellCenters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='centers', full_name='rips.CellCenters.centers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=179,
  serialized_end=222,
)


_CELLCORNERS = _descriptor.Descriptor(
  name='CellCorners',
  full_name='rips.CellCorners',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='c0', full_name='rips.CellCorners.c0', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='c1', full_name='rips.CellCorners.c1', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='c2', full_name='rips.CellCorners.c2', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='c3', full_name='rips.CellCorners.c3', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='c4', full_name='rips.CellCorners.c4', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='c5', full_name='rips.CellCorners.c5', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='c6', full_name='rips.CellCorners.c6', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='c7', full_name='rips.CellCorners.c7', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=225,
  serialized_end=438,
)


_CELLCORNERSARRAY = _descriptor.Descriptor(
  name='CellCornersArray',
  full_name='rips.CellCornersArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cells', full_name='rips.CellCornersArray.cells', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=440,
  serialized_end=492,
)

_CELLCENTERS.fields_by_name['centers'].message_type = _VEC3D
_CELLCORNERS.fields_by_name['c0'].message_type = _VEC3D
_CELLCORNERS.fields_by_name['c1'].message_type = _VEC3D
_CELLCORNERS.fields_by_name['c2'].message_type = _VEC3D
_CELLCORNERS.fields_by_name['c3'].message_type = _VEC3D
_CELLCORNERS.fields_by_name['c4'].message_type = _VEC3D
_CELLCORNERS.fields_by_name['c5'].message_type = _VEC3D
_CELLCORNERS.fields_by_name['c6'].message_type = _VEC3D
_CELLCORNERS.fields_by_name['c7'].message_type = _VEC3D
_CELLCORNERSARRAY.fields_by_name['cells'].message_type = _CELLCORNERS
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['ClientToServerStreamReply'] = _CLIENTTOSERVERSTREAMREPLY
DESCRIPTOR.message_types_by_name['Vec3i'] = _VEC3I
DESCRIPTOR.message_types_by_name['Vec3d'] = _VEC3D
DESCRIPTOR.message_types_by_name['CellCenters'] = _CELLCENTERS
DESCRIPTOR.message_types_by_name['CellCorners'] = _CELLCORNERS
DESCRIPTOR.message_types_by_name['CellCornersArray'] = _CELLCORNERSARRAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'Definitions_pb2'
  # @@protoc_insertion_point(class_scope:rips.Empty)
  })
_sym_db.RegisterMessage(Empty)

ClientToServerStreamReply = _reflection.GeneratedProtocolMessageType('ClientToServerStreamReply', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTTOSERVERSTREAMREPLY,
  '__module__' : 'Definitions_pb2'
  # @@protoc_insertion_point(class_scope:rips.ClientToServerStreamReply)
  })
_sym_db.RegisterMessage(ClientToServerStreamReply)

Vec3i = _reflection.GeneratedProtocolMessageType('Vec3i', (_message.Message,), {
  'DESCRIPTOR' : _VEC3I,
  '__module__' : 'Definitions_pb2'
  # @@protoc_insertion_point(class_scope:rips.Vec3i)
  })
_sym_db.RegisterMessage(Vec3i)

Vec3d = _reflection.GeneratedProtocolMessageType('Vec3d', (_message.Message,), {
  'DESCRIPTOR' : _VEC3D,
  '__module__' : 'Definitions_pb2'
  # @@protoc_insertion_point(class_scope:rips.Vec3d)
  })
_sym_db.RegisterMessage(Vec3d)

CellCenters = _reflection.GeneratedProtocolMessageType('CellCenters', (_message.Message,), {
  'DESCRIPTOR' : _CELLCENTERS,
  '__module__' : 'Definitions_pb2'
  # @@protoc_insertion_point(class_scope:rips.CellCenters)
  })
_sym_db.RegisterMessage(CellCenters)

CellCorners = _reflection.GeneratedProtocolMessageType('CellCorners', (_message.Message,), {
  'DESCRIPTOR' : _CELLCORNERS,
  '__module__' : 'Definitions_pb2'
  # @@protoc_insertion_point(class_scope:rips.CellCorners)
  })
_sym_db.RegisterMessage(CellCorners)

CellCornersArray = _reflection.GeneratedProtocolMessageType('CellCornersArray', (_message.Message,), {
  'DESCRIPTOR' : _CELLCORNERSARRAY,
  '__module__' : 'Definitions_pb2'
  # @@protoc_insertion_point(class_scope:rips.CellCornersArray)
  })
_sym_db.RegisterMessage(CellCornersArray)


# @@protoc_insertion_point(module_scope)
