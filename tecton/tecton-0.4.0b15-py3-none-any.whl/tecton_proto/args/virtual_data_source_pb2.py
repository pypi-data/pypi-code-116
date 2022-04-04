# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tecton_proto/args/virtual_data_source.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tecton_proto.args import basic_info_pb2 as tecton__proto_dot_args_dot_basic__info__pb2
from tecton_proto.common import id_pb2 as tecton__proto_dot_common_dot_id__pb2
from tecton_proto.args import data_source_pb2 as tecton__proto_dot_args_dot_data__source__pb2
from tecton_proto.args import diff_options_pb2 as tecton__proto_dot_args_dot_diff__options__pb2
from tecton_proto.args import version_constraints_pb2 as tecton__proto_dot_args_dot_version__constraints__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tecton_proto/args/virtual_data_source.proto',
  package='tecton_proto.args',
  syntax='proto2',
  serialized_options=b'\n\017com.tecton.argsP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n+tecton_proto/args/virtual_data_source.proto\x12\x11tecton_proto.args\x1a\"tecton_proto/args/basic_info.proto\x1a\x1ctecton_proto/common/id.proto\x1a#tecton_proto/args/data_source.proto\x1a$tecton_proto/args/diff_options.proto\x1a+tecton_proto/args/version_constraints.proto\"\xc3\x06\n\x15VirtualDataSourceArgs\x12L\n\x16virtual_data_source_id\x18\x01 \x01(\x0b\x32\x17.tecton_proto.common.IdR\x13virtualDataSourceId\x12\x37\n\x04info\x18\x02 \x01(\x0b\x32\x1c.tecton_proto.args.BasicInfoB\x05\x92M\x02\x10\x01R\x04info\x12=\n\x07version\x18\n \x01(\x0e\x32#.tecton_proto.args.FrameworkVersionR\x07version\x12M\n\x0ehive_ds_config\x18\x03 \x01(\x0b\x32%.tecton_proto.args.HiveDataSourceArgsH\x00R\x0chiveDsConfig\x12M\n\x0e\x66ile_ds_config\x18\x04 \x01(\x0b\x32%.tecton_proto.args.FileDataSourceArgsH\x00R\x0c\x66ileDsConfig\x12Y\n\x12redshift_ds_config\x18\x07 \x01(\x0b\x32).tecton_proto.args.RedshiftDataSourceArgsH\x00R\x10redshiftDsConfig\x12\\\n\x13snowflake_ds_config\x18\x08 \x01(\x0b\x32*.tecton_proto.args.SnowflakeDataSourceArgsH\x00R\x11snowflakeDsConfig\x12V\n\x11kinesis_ds_config\x18\x05 \x01(\x0b\x32(.tecton_proto.args.KinesisDataSourceArgsH\x01R\x0fkinesisDsConfig\x12P\n\x0fkafka_ds_config\x18\x06 \x01(\x0b\x32&.tecton_proto.args.KafkaDataSourceArgsH\x01R\rkafkaDsConfig\x12<\n\x04type\x18\t \x01(\x0e\x32!.tecton_proto.args.DataSourceTypeB\x05\x92M\x02\x08\x03R\x04typeB\x11\n\x0f\x62\x61tch_ds_configB\x12\n\x10stream_ds_config*?\n\x0e\x44\x61taSourceType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05\x42\x41TCH\x10\x01\x12\x15\n\x11STREAM_WITH_BATCH\x10\x02\x42\x13\n\x0f\x63om.tecton.argsP\x01'
  ,
  dependencies=[tecton__proto_dot_args_dot_basic__info__pb2.DESCRIPTOR,tecton__proto_dot_common_dot_id__pb2.DESCRIPTOR,tecton__proto_dot_args_dot_data__source__pb2.DESCRIPTOR,tecton__proto_dot_args_dot_diff__options__pb2.DESCRIPTOR,tecton__proto_dot_args_dot_version__constraints__pb2.DESCRIPTOR,])

_DATASOURCETYPE = _descriptor.EnumDescriptor(
  name='DataSourceType',
  full_name='tecton_proto.args.DataSourceType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BATCH', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STREAM_WITH_BATCH', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1090,
  serialized_end=1153,
)
_sym_db.RegisterEnumDescriptor(_DATASOURCETYPE)

DataSourceType = enum_type_wrapper.EnumTypeWrapper(_DATASOURCETYPE)
UNKNOWN = 0
BATCH = 1
STREAM_WITH_BATCH = 2



_VIRTUALDATASOURCEARGS = _descriptor.Descriptor(
  name='VirtualDataSourceArgs',
  full_name='tecton_proto.args.VirtualDataSourceArgs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='virtual_data_source_id', full_name='tecton_proto.args.VirtualDataSourceArgs.virtual_data_source_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='virtualDataSourceId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='info', full_name='tecton_proto.args.VirtualDataSourceArgs.info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222M\002\020\001', json_name='info', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='tecton_proto.args.VirtualDataSourceArgs.version', index=2,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='version', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hive_ds_config', full_name='tecton_proto.args.VirtualDataSourceArgs.hive_ds_config', index=3,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='hiveDsConfig', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='file_ds_config', full_name='tecton_proto.args.VirtualDataSourceArgs.file_ds_config', index=4,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='fileDsConfig', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='redshift_ds_config', full_name='tecton_proto.args.VirtualDataSourceArgs.redshift_ds_config', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='redshiftDsConfig', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='snowflake_ds_config', full_name='tecton_proto.args.VirtualDataSourceArgs.snowflake_ds_config', index=6,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='snowflakeDsConfig', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='kinesis_ds_config', full_name='tecton_proto.args.VirtualDataSourceArgs.kinesis_ds_config', index=7,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='kinesisDsConfig', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='kafka_ds_config', full_name='tecton_proto.args.VirtualDataSourceArgs.kafka_ds_config', index=8,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='kafkaDsConfig', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='tecton_proto.args.VirtualDataSourceArgs.type', index=9,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222M\002\010\003', json_name='type', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='batch_ds_config', full_name='tecton_proto.args.VirtualDataSourceArgs.batch_ds_config',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='stream_ds_config', full_name='tecton_proto.args.VirtualDataSourceArgs.stream_ds_config',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=253,
  serialized_end=1088,
)

_VIRTUALDATASOURCEARGS.fields_by_name['virtual_data_source_id'].message_type = tecton__proto_dot_common_dot_id__pb2._ID
_VIRTUALDATASOURCEARGS.fields_by_name['info'].message_type = tecton__proto_dot_args_dot_basic__info__pb2._BASICINFO
_VIRTUALDATASOURCEARGS.fields_by_name['version'].enum_type = tecton__proto_dot_args_dot_version__constraints__pb2._FRAMEWORKVERSION
_VIRTUALDATASOURCEARGS.fields_by_name['hive_ds_config'].message_type = tecton__proto_dot_args_dot_data__source__pb2._HIVEDATASOURCEARGS
_VIRTUALDATASOURCEARGS.fields_by_name['file_ds_config'].message_type = tecton__proto_dot_args_dot_data__source__pb2._FILEDATASOURCEARGS
_VIRTUALDATASOURCEARGS.fields_by_name['redshift_ds_config'].message_type = tecton__proto_dot_args_dot_data__source__pb2._REDSHIFTDATASOURCEARGS
_VIRTUALDATASOURCEARGS.fields_by_name['snowflake_ds_config'].message_type = tecton__proto_dot_args_dot_data__source__pb2._SNOWFLAKEDATASOURCEARGS
_VIRTUALDATASOURCEARGS.fields_by_name['kinesis_ds_config'].message_type = tecton__proto_dot_args_dot_data__source__pb2._KINESISDATASOURCEARGS
_VIRTUALDATASOURCEARGS.fields_by_name['kafka_ds_config'].message_type = tecton__proto_dot_args_dot_data__source__pb2._KAFKADATASOURCEARGS
_VIRTUALDATASOURCEARGS.fields_by_name['type'].enum_type = _DATASOURCETYPE
_VIRTUALDATASOURCEARGS.oneofs_by_name['batch_ds_config'].fields.append(
  _VIRTUALDATASOURCEARGS.fields_by_name['hive_ds_config'])
_VIRTUALDATASOURCEARGS.fields_by_name['hive_ds_config'].containing_oneof = _VIRTUALDATASOURCEARGS.oneofs_by_name['batch_ds_config']
_VIRTUALDATASOURCEARGS.oneofs_by_name['batch_ds_config'].fields.append(
  _VIRTUALDATASOURCEARGS.fields_by_name['file_ds_config'])
_VIRTUALDATASOURCEARGS.fields_by_name['file_ds_config'].containing_oneof = _VIRTUALDATASOURCEARGS.oneofs_by_name['batch_ds_config']
_VIRTUALDATASOURCEARGS.oneofs_by_name['batch_ds_config'].fields.append(
  _VIRTUALDATASOURCEARGS.fields_by_name['redshift_ds_config'])
_VIRTUALDATASOURCEARGS.fields_by_name['redshift_ds_config'].containing_oneof = _VIRTUALDATASOURCEARGS.oneofs_by_name['batch_ds_config']
_VIRTUALDATASOURCEARGS.oneofs_by_name['batch_ds_config'].fields.append(
  _VIRTUALDATASOURCEARGS.fields_by_name['snowflake_ds_config'])
_VIRTUALDATASOURCEARGS.fields_by_name['snowflake_ds_config'].containing_oneof = _VIRTUALDATASOURCEARGS.oneofs_by_name['batch_ds_config']
_VIRTUALDATASOURCEARGS.oneofs_by_name['stream_ds_config'].fields.append(
  _VIRTUALDATASOURCEARGS.fields_by_name['kinesis_ds_config'])
_VIRTUALDATASOURCEARGS.fields_by_name['kinesis_ds_config'].containing_oneof = _VIRTUALDATASOURCEARGS.oneofs_by_name['stream_ds_config']
_VIRTUALDATASOURCEARGS.oneofs_by_name['stream_ds_config'].fields.append(
  _VIRTUALDATASOURCEARGS.fields_by_name['kafka_ds_config'])
_VIRTUALDATASOURCEARGS.fields_by_name['kafka_ds_config'].containing_oneof = _VIRTUALDATASOURCEARGS.oneofs_by_name['stream_ds_config']
DESCRIPTOR.message_types_by_name['VirtualDataSourceArgs'] = _VIRTUALDATASOURCEARGS
DESCRIPTOR.enum_types_by_name['DataSourceType'] = _DATASOURCETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VirtualDataSourceArgs = _reflection.GeneratedProtocolMessageType('VirtualDataSourceArgs', (_message.Message,), {
  'DESCRIPTOR' : _VIRTUALDATASOURCEARGS,
  '__module__' : 'tecton_proto.args.virtual_data_source_pb2'
  # @@protoc_insertion_point(class_scope:tecton_proto.args.VirtualDataSourceArgs)
  })
_sym_db.RegisterMessage(VirtualDataSourceArgs)


DESCRIPTOR._options = None
_VIRTUALDATASOURCEARGS.fields_by_name['info']._options = None
_VIRTUALDATASOURCEARGS.fields_by_name['type']._options = None
# @@protoc_insertion_point(module_scope)
