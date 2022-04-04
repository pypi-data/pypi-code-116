# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: admobilize/devicemanagement/v2/resources.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from admobilize.proto.common import job_pb2 as admobilize_dot_common_dot_job__pb2
from admobilize.proto.common import admobilize_types_pb2 as admobilize_dot_common_dot_admobilize__types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.admobilize/devicemanagement/v2/resources.proto\x12\x1e\x61\x64mobilize.devicemanagement.v2\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1b\x61\x64mobilize/common/job.proto\x1a(admobilize/common/admobilize_types.proto\"Z\n\nLogMessage\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08severity\x18\x02 \x01(\t\x12\x0b\n\x03msg\x18\x03 \x01(\t\"\xf5\x01\n\x08Solution\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x1b\n\x13\x62igquery_table_name\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\x0f\n\x07version\x18\x05 \x01(\t\x12!\n\x19\x64\x65\x66\x61ult_install_config_id\x18\x06 \x01(\t\x12\x0e\n\x06schema\x18\x07 \x01(\t\x12/\n\x0b\x63reate_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x88\x02\n\x15SolutionConfiguration\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\'\n\x06\x63onfig\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x34\n\x0bsolution_id\x18\x04 \x01(\x0e\x32\x1f.admobilize.common.SolutionName\x12\x14\n\x0c\x64isplay_name\x18\x05 \x01(\t\x12/\n\x0b\x63reate_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x94\x04\n\x12ProjectPreferences\x12P\n\nspeed_unit\x18\x01 \x01(\x0e\x32<.admobilize.devicemanagement.v2.ProjectPreferences.SpeedUnit\x12\x18\n\x10max_session_time\x18\x02 \x01(\x02\x12\x16\n\x0emax_dwell_time\x18\x03 \x01(\x02\x12\x16\n\x0eview_threshold\x18\x04 \x01(\x02\x12\x13\n\x0bview_metric\x18\x05 \x01(\t\x12\x10\n\x08timezone\x18\x06 \x01(\t\x12\x1d\n\x15min_confidence_gender\x18\x07 \x01(\x02\x12\x1d\n\x15max_confidence_gender\x18\x08 \x01(\x02\x12\x1a\n\x12min_confidence_age\x18\t \x01(\x02\x12\x1a\n\x12max_confidence_age\x18\n \x01(\x02\x12\x1e\n\x16min_confidence_emotion\x18\x0b \x01(\x02\x12\x1e\n\x16max_confidence_emotion\x18\x0c \x01(\x02\x12 \n\x18\x65nable_anomaly_detection\x18\r \x01(\x08\"c\n\tSpeedUnit\x12\x1a\n\x16SPEED_UNIT_NOT_DEFINED\x10\x00\x12\x12\n\x0eMILES_PER_HOUR\x10\x01\x12\x0f\n\x0bKM_PER_HOUR\x10\x02\x12\x15\n\x11METERS_PER_SECOND\x10\x03\"\xc6\x04\n\x07Project\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x03 \x01(\t\x12\x10\n\x08owner_id\x18\x04 \x01(\t\x12\x43\n\x06labels\x18\x05 \x03(\x0b\x32\x33.admobilize.devicemanagement.v2.Project.LabelsEntry\x12\x0c\n\x04tags\x18\x06 \x03(\t\x12\x15\n\rdevices_count\x18\x07 \x01(\x05\x12/\n\x0b\x63reate_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12@\n\x14\x65nabled_integrations\x18\n \x03(\x0e\x32\".admobilize.common.IntegrationName\x12:\n\x11\x65nabled_solutions\x18\x0b \x03(\x0e\x32\x1f.admobilize.common.SolutionName\x12G\n\x0bpreferences\x18\x0c \x01(\x0b\x32\x32.admobilize.devicemanagement.v2.ProjectPreferences\x12\x1a\n\x12provisioning_token\x18\r \x01(\t\x12\x1b\n\x13\x64\x65vices_count_limit\x18\x0e \x01(\x05\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x91\x03\n\x0b\x44\x65viceState\x12\x1b\n\x13\x61\x64mprovider_version\x18\x01 \x01(\t\x12\x0e\n\x06\x62\x61lena\x18\x02 \x01(\x08\x12\x10\n\x08platform\x18\x03 \x01(\t\x12\x10\n\x08timezone\x18\x04 \x01(\t\x12.\n\nstart_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1e\n\x16\x64\x65tections_since_start\x18\x06 \x01(\x04\x12\x37\n\x13last_detection_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x15\n\rmalos_running\x18\x08 \x01(\x08\x12\x1a\n\x12\x64\x65tections_to_send\x18\t \x01(\x04\x12\x0e\n\x06status\x18\n \x01(\t\x12\x15\n\rmalos_version\x18\x0b \x01(\t\x12\x1d\n\x15\x64\x65tections_per_second\x18\x0c \x01(\x02\x12/\n\x0bupdate_time\x18\r \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xd3\x01\n\x0c\x44\x65viceConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x30\n\x0fsolution_config\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\"\n\x1a\x64\x65\x66\x61ult_solution_config_id\x18\x03 \x01(\t\x12/\n\x0e\x64\x65\x66\x61ult_config\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\x12.\n\rcustom_config\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\"(\n\tPublicKey\x12\x0e\n\x06\x66ormat\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\"a\n\x11\x44\x65viceCredentials\x12\x0c\n\x04name\x18\x01 \x01(\t\x12>\n\x0bpublic_keys\x18\x02 \x03(\x0b\x32).admobilize.devicemanagement.v2.PublicKey\"\xe2\x02\n\x13\x44\x65viceIotCoreStatus\x12\x39\n\x15last_config_send_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\x0flast_event_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\x0flast_error_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x37\n\x13last_heartbeat_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x38\n\x14last_config_ack_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\x0flast_state_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xdb\x04\n\x06\x44\x65vice\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x03 \x01(\t\x12\x12\n\ncreator_id\x18\x04 \x01(\t\x12\x12\n\nproject_id\x18\x05 \x01(\t\x12\x1a\n\x12provisioning_token\x18\x06 \x01(\t\x12#\n\x1bprovisioning_token_was_used\x18\x07 \x01(\x08\x12/\n\x0b\x63reate_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x42\n\x06labels\x18\n \x03(\x0b\x32\x32.admobilize.devicemanagement.v2.Device.LabelsEntry\x12\x0c\n\x04tags\x18\x0b \x03(\t\x12\x10\n\x08\x61rchived\x18\x0c \x01(\x08\x12\x31\n\x08solution\x18\r \x01(\x0e\x32\x1f.admobilize.common.SolutionName\x12\x38\n\x0cintegrations\x18\x0e \x03(\x0e\x32\".admobilize.common.IntegrationName\x12:\n\x05state\x18\x0f \x01(\x0b\x32+.admobilize.devicemanagement.v2.DeviceState\x12\x1a\n\x12\x65nable_auto_update\x18\x10 \x01(\x08\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x8c\x01\n\x13\x44\x65viceWithPublicKey\x12\x36\n\x06\x64\x65vice\x18\x01 \x01(\x0b\x32&.admobilize.devicemanagement.v2.Device\x12=\n\npublic_key\x18\x02 \x01(\x0b\x32).admobilize.devicemanagement.v2.PublicKey\"\xe6\x01\n\x07License\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x31\n\x08solution\x18\x03 \x01(\x0e\x32\x1f.admobilize.common.SolutionName\x12\x11\n\tdevice_id\x18\x04 \x01(\t\x12.\n\nvalid_from\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bvalid_until\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1a\n\x12\x61\x63\x63ount_admin_name\x18\x07 \x01(\t\"\x89\x02\n\x13MoveDevicesMetadata\x12/\n\x0b\x63reate_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\ndevice_ids\x18\x03 \x03(\t\x12\x1e\n\x16\x64\x65stination_project_id\x18\x04 \x01(\t\x12\x19\n\x11source_project_id\x18\x05 \x01(\t\x12$\n\x04jobs\x18\x06 \x03(\x0b\x32\x16.admobilize.common.Job\x12\x1e\n\x16requested_cancellation\x18\x07 \x01(\x08\"\xa5\x02\n\x1aRestoreDevicesDataMetadata\x12/\n\x0b\x63reate_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\ndevice_ids\x18\x03 \x03(\t\x12\x1e\n\x16\x64\x65stination_project_id\x18\x04 \x01(\t\x12\x1c\n\x14\x64\x65stination_table_id\x18\x05 \x01(\t\x12\x10\n\x08truncate\x18\x06 \x01(\x08\x12$\n\x04jobs\x18\x07 \x03(\x0b\x32\x16.admobilize.common.Job\x12\x1e\n\x16requested_cancellation\x18\x08 \x01(\x08\x42\xa0\x01\n\"com.admobilize.devicemanagement.v2B\x0b\x44\x65viceProtoP\x01ZBbitbucket.org/admobilize/admobilizeapis-go/pkg/devicemanagement/v2\xa2\x02\x05\x41\x44MDM\xaa\x02\x1e\x41\x64Mobilize.DeviceManagement.V2b\x06proto3')



_LOGMESSAGE = DESCRIPTOR.message_types_by_name['LogMessage']
_SOLUTION = DESCRIPTOR.message_types_by_name['Solution']
_SOLUTIONCONFIGURATION = DESCRIPTOR.message_types_by_name['SolutionConfiguration']
_PROJECTPREFERENCES = DESCRIPTOR.message_types_by_name['ProjectPreferences']
_PROJECT = DESCRIPTOR.message_types_by_name['Project']
_PROJECT_LABELSENTRY = _PROJECT.nested_types_by_name['LabelsEntry']
_DEVICESTATE = DESCRIPTOR.message_types_by_name['DeviceState']
_DEVICECONFIG = DESCRIPTOR.message_types_by_name['DeviceConfig']
_PUBLICKEY = DESCRIPTOR.message_types_by_name['PublicKey']
_DEVICECREDENTIALS = DESCRIPTOR.message_types_by_name['DeviceCredentials']
_DEVICEIOTCORESTATUS = DESCRIPTOR.message_types_by_name['DeviceIotCoreStatus']
_DEVICE = DESCRIPTOR.message_types_by_name['Device']
_DEVICE_LABELSENTRY = _DEVICE.nested_types_by_name['LabelsEntry']
_DEVICEWITHPUBLICKEY = DESCRIPTOR.message_types_by_name['DeviceWithPublicKey']
_LICENSE = DESCRIPTOR.message_types_by_name['License']
_MOVEDEVICESMETADATA = DESCRIPTOR.message_types_by_name['MoveDevicesMetadata']
_RESTOREDEVICESDATAMETADATA = DESCRIPTOR.message_types_by_name['RestoreDevicesDataMetadata']
_PROJECTPREFERENCES_SPEEDUNIT = _PROJECTPREFERENCES.enum_types_by_name['SpeedUnit']
LogMessage = _reflection.GeneratedProtocolMessageType('LogMessage', (_message.Message,), {
  'DESCRIPTOR' : _LOGMESSAGE,
  '__module__' : 'admobilize.devicemanagement.v2.resources_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.devicemanagement.v2.LogMessage)
  })
_sym_db.RegisterMessage(LogMessage)

Solution = _reflection.GeneratedProtocolMessageType('Solution', (_message.Message,), {
  'DESCRIPTOR' : _SOLUTION,
  '__module__' : 'admobilize.devicemanagement.v2.resources_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.devicemanagement.v2.Solution)
  })
_sym_db.RegisterMessage(Solution)

SolutionConfiguration = _reflection.GeneratedProtocolMessageType('SolutionConfiguration', (_message.Message,), {
  'DESCRIPTOR' : _SOLUTIONCONFIGURATION,
  '__module__' : 'admobilize.devicemanagement.v2.resources_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.devicemanagement.v2.SolutionConfiguration)
  })
_sym_db.RegisterMessage(SolutionConfiguration)

ProjectPreferences = _reflection.GeneratedProtocolMessageType('ProjectPreferences', (_message.Message,), {
  'DESCRIPTOR' : _PROJECTPREFERENCES,
  '__module__' : 'admobilize.devicemanagement.v2.resources_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.devicemanagement.v2.ProjectPreferences)
  })
_sym_db.RegisterMessage(ProjectPreferences)

Project = _reflection.GeneratedProtocolMessageType('Project', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _PROJECT_LABELSENTRY,
    '__module__' : 'admobilize.devicemanagement.v2.resources_pb2'
    # @@protoc_insertion_point(class_scope:admobilize.devicemanagement.v2.Project.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _PROJECT,
  '__module__' : 'admobilize.devicemanagement.v2.resources_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.devicemanagement.v2.Project)
  })
_sym_db.RegisterMessage(Project)
_sym_db.RegisterMessage(Project.LabelsEntry)

DeviceState = _reflection.GeneratedProtocolMessageType('DeviceState', (_message.Message,), {
  'DESCRIPTOR' : _DEVICESTATE,
  '__module__' : 'admobilize.devicemanagement.v2.resources_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.devicemanagement.v2.DeviceState)
  })
_sym_db.RegisterMessage(DeviceState)

DeviceConfig = _reflection.GeneratedProtocolMessageType('DeviceConfig', (_message.Message,), {
  'DESCRIPTOR' : _DEVICECONFIG,
  '__module__' : 'admobilize.devicemanagement.v2.resources_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.devicemanagement.v2.DeviceConfig)
  })
_sym_db.RegisterMessage(DeviceConfig)

PublicKey = _reflection.GeneratedProtocolMessageType('PublicKey', (_message.Message,), {
  'DESCRIPTOR' : _PUBLICKEY,
  '__module__' : 'admobilize.devicemanagement.v2.resources_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.devicemanagement.v2.PublicKey)
  })
_sym_db.RegisterMessage(PublicKey)

DeviceCredentials = _reflection.GeneratedProtocolMessageType('DeviceCredentials', (_message.Message,), {
  'DESCRIPTOR' : _DEVICECREDENTIALS,
  '__module__' : 'admobilize.devicemanagement.v2.resources_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.devicemanagement.v2.DeviceCredentials)
  })
_sym_db.RegisterMessage(DeviceCredentials)

DeviceIotCoreStatus = _reflection.GeneratedProtocolMessageType('DeviceIotCoreStatus', (_message.Message,), {
  'DESCRIPTOR' : _DEVICEIOTCORESTATUS,
  '__module__' : 'admobilize.devicemanagement.v2.resources_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.devicemanagement.v2.DeviceIotCoreStatus)
  })
_sym_db.RegisterMessage(DeviceIotCoreStatus)

Device = _reflection.GeneratedProtocolMessageType('Device', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _DEVICE_LABELSENTRY,
    '__module__' : 'admobilize.devicemanagement.v2.resources_pb2'
    # @@protoc_insertion_point(class_scope:admobilize.devicemanagement.v2.Device.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _DEVICE,
  '__module__' : 'admobilize.devicemanagement.v2.resources_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.devicemanagement.v2.Device)
  })
_sym_db.RegisterMessage(Device)
_sym_db.RegisterMessage(Device.LabelsEntry)

DeviceWithPublicKey = _reflection.GeneratedProtocolMessageType('DeviceWithPublicKey', (_message.Message,), {
  'DESCRIPTOR' : _DEVICEWITHPUBLICKEY,
  '__module__' : 'admobilize.devicemanagement.v2.resources_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.devicemanagement.v2.DeviceWithPublicKey)
  })
_sym_db.RegisterMessage(DeviceWithPublicKey)

License = _reflection.GeneratedProtocolMessageType('License', (_message.Message,), {
  'DESCRIPTOR' : _LICENSE,
  '__module__' : 'admobilize.devicemanagement.v2.resources_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.devicemanagement.v2.License)
  })
_sym_db.RegisterMessage(License)

MoveDevicesMetadata = _reflection.GeneratedProtocolMessageType('MoveDevicesMetadata', (_message.Message,), {
  'DESCRIPTOR' : _MOVEDEVICESMETADATA,
  '__module__' : 'admobilize.devicemanagement.v2.resources_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.devicemanagement.v2.MoveDevicesMetadata)
  })
_sym_db.RegisterMessage(MoveDevicesMetadata)

RestoreDevicesDataMetadata = _reflection.GeneratedProtocolMessageType('RestoreDevicesDataMetadata', (_message.Message,), {
  'DESCRIPTOR' : _RESTOREDEVICESDATAMETADATA,
  '__module__' : 'admobilize.devicemanagement.v2.resources_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.devicemanagement.v2.RestoreDevicesDataMetadata)
  })
_sym_db.RegisterMessage(RestoreDevicesDataMetadata)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"com.admobilize.devicemanagement.v2B\013DeviceProtoP\001ZBbitbucket.org/admobilize/admobilizeapis-go/pkg/devicemanagement/v2\242\002\005ADMDM\252\002\036AdMobilize.DeviceManagement.V2'
  _PROJECT_LABELSENTRY._options = None
  _PROJECT_LABELSENTRY._serialized_options = b'8\001'
  _DEVICE_LABELSENTRY._options = None
  _DEVICE_LABELSENTRY._serialized_options = b'8\001'
  _LOGMESSAGE._serialized_start=216
  _LOGMESSAGE._serialized_end=306
  _SOLUTION._serialized_start=309
  _SOLUTION._serialized_end=554
  _SOLUTIONCONFIGURATION._serialized_start=557
  _SOLUTIONCONFIGURATION._serialized_end=821
  _PROJECTPREFERENCES._serialized_start=824
  _PROJECTPREFERENCES._serialized_end=1356
  _PROJECTPREFERENCES_SPEEDUNIT._serialized_start=1257
  _PROJECTPREFERENCES_SPEEDUNIT._serialized_end=1356
  _PROJECT._serialized_start=1359
  _PROJECT._serialized_end=1941
  _PROJECT_LABELSENTRY._serialized_start=1896
  _PROJECT_LABELSENTRY._serialized_end=1941
  _DEVICESTATE._serialized_start=1944
  _DEVICESTATE._serialized_end=2345
  _DEVICECONFIG._serialized_start=2348
  _DEVICECONFIG._serialized_end=2559
  _PUBLICKEY._serialized_start=2561
  _PUBLICKEY._serialized_end=2601
  _DEVICECREDENTIALS._serialized_start=2603
  _DEVICECREDENTIALS._serialized_end=2700
  _DEVICEIOTCORESTATUS._serialized_start=2703
  _DEVICEIOTCORESTATUS._serialized_end=3057
  _DEVICE._serialized_start=3060
  _DEVICE._serialized_end=3663
  _DEVICE_LABELSENTRY._serialized_start=1896
  _DEVICE_LABELSENTRY._serialized_end=1941
  _DEVICEWITHPUBLICKEY._serialized_start=3666
  _DEVICEWITHPUBLICKEY._serialized_end=3806
  _LICENSE._serialized_start=3809
  _LICENSE._serialized_end=4039
  _MOVEDEVICESMETADATA._serialized_start=4042
  _MOVEDEVICESMETADATA._serialized_end=4307
  _RESTOREDEVICESDATAMETADATA._serialized_start=4310
  _RESTOREDEVICESDATAMETADATA._serialized_end=4603
# @@protoc_insertion_point(module_scope)
