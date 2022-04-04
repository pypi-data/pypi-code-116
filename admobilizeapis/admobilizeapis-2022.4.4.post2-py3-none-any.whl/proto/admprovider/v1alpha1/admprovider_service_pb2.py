# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: admobilize/admprovider/v1alpha1/admprovider_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from admobilize.proto.admprovider.v1alpha1 import resources_pb2 as admobilize_dot_admprovider_dot_v1alpha1_dot_resources__pb2
from admobilize.proto.vision.v1 import vision_pb2 as admobilize_dot_vision_dot_v1_dot_vision__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9admobilize/admprovider/v1alpha1/admprovider_service.proto\x12\x1f\x61\x64mobilize.admprovider.v1alpha1\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a/admobilize/admprovider/v1alpha1/resources.proto\x1a!admobilize/vision/v1/vision.proto\"\x85\x01\n\x10ProvisionRequest\x12\x1a\n\x12provisioning_token\x18\x01 \x01(\t\x12\x15\n\rmqtt_registry\x18\x02 \x01(\t\x12\x16\n\x0e\x61pplication_id\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65vice_name\x18\x04 \x01(\t\x12\x11\n\tdevice_id\x18\x05 \x01(\t\"S\n\x11ProvisionResponse\x12\x16\n\x0e\x61pplication_id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65vice_name\x18\x02 \x01(\t\x12\x11\n\tdevice_id\x18\x03 \x01(\t\":\n\x11StreamLogsRequest\x12\x13\n\x0b\x61pplication\x18\x01 \x01(\t\x12\x10\n\x08loglevel\x18\x02 \x01(\t\"V\n\x12StreamLogsResponse\x12@\n\x0blog_message\x18\x01 \x01(\x0b\x32+.admobilize.admprovider.v1alpha1.LogMessage\"#\n\x12StreamStateRequest\x12\r\n\x05\x64\x65lay\x18\x01 \x01(\x04\"O\n\x12SendCommandRequest\x12\x39\n\x07\x63ommand\x18\x01 \x01(\x0b\x32(.admobilize.admprovider.v1alpha1.Command\"Y\n\x13SendCommandResponse\x12\x42\n\x08response\x18\x01 \x01(\x0b\x32\x30.admobilize.admprovider.v1alpha1.CommandResponse\"a\n\x11GetStatusResponse\x12\x1a\n\x12\x61pplication_status\x18\x01 \x01(\t\x12\x17\n\x0f\x64\x61tabase_status\x18\x02 \x01(\t\x12\x17\n\x0f\x63ritical_errors\x18\x03 \x03(\t2\x93\t\n\x12\x41\x64mproviderService\x12t\n\tProvision\x12\x31.admobilize.admprovider.v1alpha1.ProvisionRequest\x1a\x32.admobilize.admprovider.v1alpha1.ProvisionResponse\"\x00\x12y\n\nStreamLogs\x12\x32.admobilize.admprovider.v1alpha1.StreamLogsRequest\x1a\x33.admobilize.admprovider.v1alpha1.StreamLogsResponse\"\x00\x30\x01\x12n\n\x0bStreamState\x12\x33.admobilize.admprovider.v1alpha1.StreamStateRequest\x1a&.admobilize.admprovider.v1alpha1.State\"\x00\x30\x01\x12R\n\x0cStreamFrames\x12\x16.google.protobuf.Empty\x1a&.admobilize.admprovider.v1alpha1.Frame\"\x00\x30\x01\x12R\n\x10StreamDetections\x12\x16.google.protobuf.Empty\x1a\".admobilize.vision.v1.VisionResult\"\x00\x30\x01\x12L\n\x08GetState\x12\x16.google.protobuf.Empty\x1a&.admobilize.admprovider.v1alpha1.State\"\x00\x12Y\n\tGetStatus\x12\x16.google.protobuf.Empty\x1a\x32.admobilize.admprovider.v1alpha1.GetStatusResponse\"\x00\x12O\n\x03Run\x12..admobilize.admprovider.v1alpha1.Configuration\x1a\x16.google.protobuf.Empty\"\x00\x12U\n\tSetConfig\x12..admobilize.admprovider.v1alpha1.Configuration\x1a\x16.google.protobuf.Empty\"\x00\x12U\n\tGetConfig\x12\x16.google.protobuf.Empty\x1a..admobilize.admprovider.v1alpha1.Configuration\"\x00\x12z\n\x0bSendCommand\x12\x33.admobilize.admprovider.v1alpha1.SendCommandRequest\x1a\x34.admobilize.admprovider.v1alpha1.SendCommandResponse\"\x00\x12P\n\x07SendLog\x12+.admobilize.admprovider.v1alpha1.LogMessage\x1a\x16.google.protobuf.Empty\"\x00\x42\xb0\x01\n#com.admobilize.admprovider.v1alpha1B\x17\x41\x64mproviderServiceProtoP\x01ZCbitbucket.org/admobilize/admobilizeapis-go/pkg/admprovider/v1alpha1\xa2\x02\x06\x41\x44MPRS\xaa\x02\x1f\x41\x64Mobilize.Admprovider.V1Alpha1b\x06proto3')



_PROVISIONREQUEST = DESCRIPTOR.message_types_by_name['ProvisionRequest']
_PROVISIONRESPONSE = DESCRIPTOR.message_types_by_name['ProvisionResponse']
_STREAMLOGSREQUEST = DESCRIPTOR.message_types_by_name['StreamLogsRequest']
_STREAMLOGSRESPONSE = DESCRIPTOR.message_types_by_name['StreamLogsResponse']
_STREAMSTATEREQUEST = DESCRIPTOR.message_types_by_name['StreamStateRequest']
_SENDCOMMANDREQUEST = DESCRIPTOR.message_types_by_name['SendCommandRequest']
_SENDCOMMANDRESPONSE = DESCRIPTOR.message_types_by_name['SendCommandResponse']
_GETSTATUSRESPONSE = DESCRIPTOR.message_types_by_name['GetStatusResponse']
ProvisionRequest = _reflection.GeneratedProtocolMessageType('ProvisionRequest', (_message.Message,), {
  'DESCRIPTOR' : _PROVISIONREQUEST,
  '__module__' : 'admobilize.admprovider.v1alpha1.admprovider_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.admprovider.v1alpha1.ProvisionRequest)
  })
_sym_db.RegisterMessage(ProvisionRequest)

ProvisionResponse = _reflection.GeneratedProtocolMessageType('ProvisionResponse', (_message.Message,), {
  'DESCRIPTOR' : _PROVISIONRESPONSE,
  '__module__' : 'admobilize.admprovider.v1alpha1.admprovider_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.admprovider.v1alpha1.ProvisionResponse)
  })
_sym_db.RegisterMessage(ProvisionResponse)

StreamLogsRequest = _reflection.GeneratedProtocolMessageType('StreamLogsRequest', (_message.Message,), {
  'DESCRIPTOR' : _STREAMLOGSREQUEST,
  '__module__' : 'admobilize.admprovider.v1alpha1.admprovider_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.admprovider.v1alpha1.StreamLogsRequest)
  })
_sym_db.RegisterMessage(StreamLogsRequest)

StreamLogsResponse = _reflection.GeneratedProtocolMessageType('StreamLogsResponse', (_message.Message,), {
  'DESCRIPTOR' : _STREAMLOGSRESPONSE,
  '__module__' : 'admobilize.admprovider.v1alpha1.admprovider_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.admprovider.v1alpha1.StreamLogsResponse)
  })
_sym_db.RegisterMessage(StreamLogsResponse)

StreamStateRequest = _reflection.GeneratedProtocolMessageType('StreamStateRequest', (_message.Message,), {
  'DESCRIPTOR' : _STREAMSTATEREQUEST,
  '__module__' : 'admobilize.admprovider.v1alpha1.admprovider_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.admprovider.v1alpha1.StreamStateRequest)
  })
_sym_db.RegisterMessage(StreamStateRequest)

SendCommandRequest = _reflection.GeneratedProtocolMessageType('SendCommandRequest', (_message.Message,), {
  'DESCRIPTOR' : _SENDCOMMANDREQUEST,
  '__module__' : 'admobilize.admprovider.v1alpha1.admprovider_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.admprovider.v1alpha1.SendCommandRequest)
  })
_sym_db.RegisterMessage(SendCommandRequest)

SendCommandResponse = _reflection.GeneratedProtocolMessageType('SendCommandResponse', (_message.Message,), {
  'DESCRIPTOR' : _SENDCOMMANDRESPONSE,
  '__module__' : 'admobilize.admprovider.v1alpha1.admprovider_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.admprovider.v1alpha1.SendCommandResponse)
  })
_sym_db.RegisterMessage(SendCommandResponse)

GetStatusResponse = _reflection.GeneratedProtocolMessageType('GetStatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSTATUSRESPONSE,
  '__module__' : 'admobilize.admprovider.v1alpha1.admprovider_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.admprovider.v1alpha1.GetStatusResponse)
  })
_sym_db.RegisterMessage(GetStatusResponse)

_ADMPROVIDERSERVICE = DESCRIPTOR.services_by_name['AdmproviderService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n#com.admobilize.admprovider.v1alpha1B\027AdmproviderServiceProtoP\001ZCbitbucket.org/admobilize/admobilizeapis-go/pkg/admprovider/v1alpha1\242\002\006ADMPRS\252\002\037AdMobilize.Admprovider.V1Alpha1'
  _PROVISIONREQUEST._serialized_start=238
  _PROVISIONREQUEST._serialized_end=371
  _PROVISIONRESPONSE._serialized_start=373
  _PROVISIONRESPONSE._serialized_end=456
  _STREAMLOGSREQUEST._serialized_start=458
  _STREAMLOGSREQUEST._serialized_end=516
  _STREAMLOGSRESPONSE._serialized_start=518
  _STREAMLOGSRESPONSE._serialized_end=604
  _STREAMSTATEREQUEST._serialized_start=606
  _STREAMSTATEREQUEST._serialized_end=641
  _SENDCOMMANDREQUEST._serialized_start=643
  _SENDCOMMANDREQUEST._serialized_end=722
  _SENDCOMMANDRESPONSE._serialized_start=724
  _SENDCOMMANDRESPONSE._serialized_end=813
  _GETSTATUSRESPONSE._serialized_start=815
  _GETSTATUSRESPONSE._serialized_end=912
  _ADMPROVIDERSERVICE._serialized_start=915
  _ADMPROVIDERSERVICE._serialized_end=2086
# @@protoc_insertion_point(module_scope)
