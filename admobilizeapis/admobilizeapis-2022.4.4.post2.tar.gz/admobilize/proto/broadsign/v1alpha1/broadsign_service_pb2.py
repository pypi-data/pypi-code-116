# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: admobilize/broadsign/v1alpha1/broadsign_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from admobilize.proto.common import job_pb2 as admobilize_dot_common_dot_job__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from admobilize.proto.broadsign.v1alpha1 import resources_pb2 as admobilize_dot_broadsign_dot_v1alpha1_dot_resources__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5admobilize/broadsign/v1alpha1/broadsign_service.proto\x12\x1d\x61\x64mobilize.broadsign.v1alpha1\x1a\x1cgoogle/api/annotations.proto\x1a\x1b\x61\x64mobilize/common/job.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a-admobilize/broadsign/v1alpha1/resources.proto\"\x8f\x01\n\rReportRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x16\n\x0estart_datetime\x18\x02 \x01(\t\x12\x14\n\x0c\x65nd_datetime\x18\x03 \x01(\t\x12\x0f\n\x07\x64\x65vices\x18\x04 \x03(\t\x12\x1a\n\x12\x64\x65stination_format\x18\n \x01(\t\x12\x13\n\x0b\x63ompression\x18\x0b \x01(\t\"A\n\x15GetCredentialsRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65vice\x18\x02 \x01(\t\x12\x0c\n\x04user\x18\x03 \x01(\t\"\x7f\n\x16ListCredentialsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x11\n\tpage_size\x18\x64 \x01(\x05\x12\x12\n\npage_token\x18\x65 \x01(\t\"X\n\x17\x43reateCredentialRequest\x12=\n\ncredential\x18\x01 \x01(\x0b\x32).admobilize.broadsign.v1alpha1.Credential\"\x89\x01\n\x17UpdateCredentialRequest\x12=\n\ncredential\x18\x01 \x01(\x0b\x32).admobilize.broadsign.v1alpha1.Credential\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"r\n\x17ListCredentialsResponse\x12>\n\x0b\x63redentials\x18\x01 \x03(\x0b\x32).admobilize.broadsign.v1alpha1.Credential\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"%\n\x17\x44\x65leteCredentialRequest\x12\n\n\x02id\x18\x01 \x01(\t\"=\n\x11GetMappingRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65vice\x18\x02 \x01(\t\x12\x0c\n\x04user\x18\x03 \x01(\t\"|\n\x13ListMappingsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x11\n\tpage_size\x18\x64 \x01(\x05\x12\x12\n\npage_token\x18\x65 \x01(\t\"i\n\x14ListMappingsResponse\x12\x38\n\x08mappings\x18\x01 \x03(\x0b\x32&.admobilize.broadsign.v1alpha1.Mapping\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"O\n\x14\x43reateMappingRequest\x12\x37\n\x07mapping\x18\x01 \x01(\x0b\x32&.admobilize.broadsign.v1alpha1.Mapping\"\x80\x01\n\x14UpdateMappingRequest\x12\x37\n\x07mapping\x18\x01 \x01(\x0b\x32&.admobilize.broadsign.v1alpha1.Mapping\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"\"\n\x14\x44\x65leteMappingRequest\x12\n\n\x02id\x18\x01 \x01(\t2\xe1\x0f\n\x10\x42roadsignService\x12\x8d\x01\n\x0c\x43reateReport\x12,.admobilize.broadsign.v1alpha1.ReportRequest\x1a\x16.admobilize.common.Job\"7\x82\xd3\xe4\x93\x02\x31\"//v1alpha1/broadsign/{parent=projects/*}/reports\x12\x92\x02\n\x0eGetCredentials\x12\x34.admobilize.broadsign.v1alpha1.GetCredentialsRequest\x1a\x36.admobilize.broadsign.v1alpha1.ListCredentialsResponse\"\x91\x01\x82\xd3\xe4\x93\x02\x8a\x01\x12,/v1alpha1/broadsign/users/{user}/credentialsZ&\x12$/v1alpha1/broadsign/credentials/{id}Z2\x12\x30/v1alpha1/broadsign/devices/{device}/credentials\x12\xa9\x01\n\x0fListCredentials\x12\x35.admobilize.broadsign.v1alpha1.ListCredentialsRequest\x1a\x36.admobilize.broadsign.v1alpha1.ListCredentialsResponse\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/v1alpha1/broadsign/credentials\x12\xaa\x01\n\x10\x43reateCredential\x12\x36.admobilize.broadsign.v1alpha1.CreateCredentialRequest\x1a).admobilize.broadsign.v1alpha1.Credential\"3\x82\xd3\xe4\x93\x02-\"\x1f/v1alpha1/broadsign/credentials:\ncredential\x12\x90\x01\n\x10\x44\x65leteCredential\x12\x36.admobilize.broadsign.v1alpha1.DeleteCredentialRequest\x1a\x16.google.protobuf.Empty\",\x82\xd3\xe4\x93\x02&*$/v1alpha1/broadsign/credentials/{id}\x12\xba\x01\n\x10UpdateCredential\x12\x36.admobilize.broadsign.v1alpha1.UpdateCredentialRequest\x1a).admobilize.broadsign.v1alpha1.Credential\"C\x82\xd3\xe4\x93\x02=2//v1alpha1/broadsign/credentials/{credential.id}:\ncredential\x12\x8b\x02\n\x0bGetMappings\x12\x30.admobilize.broadsign.v1alpha1.GetMappingRequest\x1a\x33.admobilize.broadsign.v1alpha1.ListMappingsResponse\"\x94\x01\x82\xd3\xe4\x93\x02\x8d\x01\x12-/v1alpha1/broadsign/credentials/{id}/mappingsZ+\x12)/v1alpha1/broadsign/users/{user}/mappingsZ/\x12-/v1alpha1/broadsign/devices/{device}/mappings\x12\x9d\x01\n\x0cListMappings\x12\x32.admobilize.broadsign.v1alpha1.ListMappingsRequest\x1a\x33.admobilize.broadsign.v1alpha1.ListMappingsResponse\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/v1alpha1/broadsign/mappings\x12\x9b\x01\n\rCreateMapping\x12\x33.admobilize.broadsign.v1alpha1.CreateMappingRequest\x1a&.admobilize.broadsign.v1alpha1.Mapping\"-\x82\xd3\xe4\x93\x02\'\"\x1c/v1alpha1/broadsign/mappings:\x07mapping\x12\x87\x01\n\rDeleteMapping\x12\x33.admobilize.broadsign.v1alpha1.DeleteMappingRequest\x1a\x16.google.protobuf.Empty\")\x82\xd3\xe4\x93\x02#*!/v1alpha1/broadsign/mappings/{id}\x12\xa8\x01\n\rUpdateMapping\x12\x33.admobilize.broadsign.v1alpha1.UpdateMappingRequest\x1a&.admobilize.broadsign.v1alpha1.Mapping\":\x82\xd3\xe4\x93\x02\x34\x32)/v1alpha1/broadsign/mappings/{mapping.id}:\x07mappingB\xa9\x01\n!com.admobilize.broadsign.v1alpha1B\x15\x42roadsignServiceProtoP\x01ZAbitbucket.org/admobilize/admobilizeapis-go/pkg/broadsign/v1alpha1\xa2\x02\x07\x41\x44MBRDS\xaa\x02\x1d\x41\x64Mobilize.Broadsign.V1Alpha1b\x06proto3')



_REPORTREQUEST = DESCRIPTOR.message_types_by_name['ReportRequest']
_GETCREDENTIALSREQUEST = DESCRIPTOR.message_types_by_name['GetCredentialsRequest']
_LISTCREDENTIALSREQUEST = DESCRIPTOR.message_types_by_name['ListCredentialsRequest']
_CREATECREDENTIALREQUEST = DESCRIPTOR.message_types_by_name['CreateCredentialRequest']
_UPDATECREDENTIALREQUEST = DESCRIPTOR.message_types_by_name['UpdateCredentialRequest']
_LISTCREDENTIALSRESPONSE = DESCRIPTOR.message_types_by_name['ListCredentialsResponse']
_DELETECREDENTIALREQUEST = DESCRIPTOR.message_types_by_name['DeleteCredentialRequest']
_GETMAPPINGREQUEST = DESCRIPTOR.message_types_by_name['GetMappingRequest']
_LISTMAPPINGSREQUEST = DESCRIPTOR.message_types_by_name['ListMappingsRequest']
_LISTMAPPINGSRESPONSE = DESCRIPTOR.message_types_by_name['ListMappingsResponse']
_CREATEMAPPINGREQUEST = DESCRIPTOR.message_types_by_name['CreateMappingRequest']
_UPDATEMAPPINGREQUEST = DESCRIPTOR.message_types_by_name['UpdateMappingRequest']
_DELETEMAPPINGREQUEST = DESCRIPTOR.message_types_by_name['DeleteMappingRequest']
ReportRequest = _reflection.GeneratedProtocolMessageType('ReportRequest', (_message.Message,), {
  'DESCRIPTOR' : _REPORTREQUEST,
  '__module__' : 'admobilize.broadsign.v1alpha1.broadsign_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.broadsign.v1alpha1.ReportRequest)
  })
_sym_db.RegisterMessage(ReportRequest)

GetCredentialsRequest = _reflection.GeneratedProtocolMessageType('GetCredentialsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCREDENTIALSREQUEST,
  '__module__' : 'admobilize.broadsign.v1alpha1.broadsign_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.broadsign.v1alpha1.GetCredentialsRequest)
  })
_sym_db.RegisterMessage(GetCredentialsRequest)

ListCredentialsRequest = _reflection.GeneratedProtocolMessageType('ListCredentialsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTCREDENTIALSREQUEST,
  '__module__' : 'admobilize.broadsign.v1alpha1.broadsign_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.broadsign.v1alpha1.ListCredentialsRequest)
  })
_sym_db.RegisterMessage(ListCredentialsRequest)

CreateCredentialRequest = _reflection.GeneratedProtocolMessageType('CreateCredentialRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATECREDENTIALREQUEST,
  '__module__' : 'admobilize.broadsign.v1alpha1.broadsign_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.broadsign.v1alpha1.CreateCredentialRequest)
  })
_sym_db.RegisterMessage(CreateCredentialRequest)

UpdateCredentialRequest = _reflection.GeneratedProtocolMessageType('UpdateCredentialRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATECREDENTIALREQUEST,
  '__module__' : 'admobilize.broadsign.v1alpha1.broadsign_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.broadsign.v1alpha1.UpdateCredentialRequest)
  })
_sym_db.RegisterMessage(UpdateCredentialRequest)

ListCredentialsResponse = _reflection.GeneratedProtocolMessageType('ListCredentialsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTCREDENTIALSRESPONSE,
  '__module__' : 'admobilize.broadsign.v1alpha1.broadsign_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.broadsign.v1alpha1.ListCredentialsResponse)
  })
_sym_db.RegisterMessage(ListCredentialsResponse)

DeleteCredentialRequest = _reflection.GeneratedProtocolMessageType('DeleteCredentialRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETECREDENTIALREQUEST,
  '__module__' : 'admobilize.broadsign.v1alpha1.broadsign_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.broadsign.v1alpha1.DeleteCredentialRequest)
  })
_sym_db.RegisterMessage(DeleteCredentialRequest)

GetMappingRequest = _reflection.GeneratedProtocolMessageType('GetMappingRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETMAPPINGREQUEST,
  '__module__' : 'admobilize.broadsign.v1alpha1.broadsign_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.broadsign.v1alpha1.GetMappingRequest)
  })
_sym_db.RegisterMessage(GetMappingRequest)

ListMappingsRequest = _reflection.GeneratedProtocolMessageType('ListMappingsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTMAPPINGSREQUEST,
  '__module__' : 'admobilize.broadsign.v1alpha1.broadsign_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.broadsign.v1alpha1.ListMappingsRequest)
  })
_sym_db.RegisterMessage(ListMappingsRequest)

ListMappingsResponse = _reflection.GeneratedProtocolMessageType('ListMappingsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTMAPPINGSRESPONSE,
  '__module__' : 'admobilize.broadsign.v1alpha1.broadsign_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.broadsign.v1alpha1.ListMappingsResponse)
  })
_sym_db.RegisterMessage(ListMappingsResponse)

CreateMappingRequest = _reflection.GeneratedProtocolMessageType('CreateMappingRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEMAPPINGREQUEST,
  '__module__' : 'admobilize.broadsign.v1alpha1.broadsign_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.broadsign.v1alpha1.CreateMappingRequest)
  })
_sym_db.RegisterMessage(CreateMappingRequest)

UpdateMappingRequest = _reflection.GeneratedProtocolMessageType('UpdateMappingRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEMAPPINGREQUEST,
  '__module__' : 'admobilize.broadsign.v1alpha1.broadsign_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.broadsign.v1alpha1.UpdateMappingRequest)
  })
_sym_db.RegisterMessage(UpdateMappingRequest)

DeleteMappingRequest = _reflection.GeneratedProtocolMessageType('DeleteMappingRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEMAPPINGREQUEST,
  '__module__' : 'admobilize.broadsign.v1alpha1.broadsign_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.broadsign.v1alpha1.DeleteMappingRequest)
  })
_sym_db.RegisterMessage(DeleteMappingRequest)

_BROADSIGNSERVICE = DESCRIPTOR.services_by_name['BroadsignService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n!com.admobilize.broadsign.v1alpha1B\025BroadsignServiceProtoP\001ZAbitbucket.org/admobilize/admobilizeapis-go/pkg/broadsign/v1alpha1\242\002\007ADMBRDS\252\002\035AdMobilize.Broadsign.V1Alpha1'
  _BROADSIGNSERVICE.methods_by_name['CreateReport']._options = None
  _BROADSIGNSERVICE.methods_by_name['CreateReport']._serialized_options = b'\202\323\344\223\0021\"//v1alpha1/broadsign/{parent=projects/*}/reports'
  _BROADSIGNSERVICE.methods_by_name['GetCredentials']._options = None
  _BROADSIGNSERVICE.methods_by_name['GetCredentials']._serialized_options = b'\202\323\344\223\002\212\001\022,/v1alpha1/broadsign/users/{user}/credentialsZ&\022$/v1alpha1/broadsign/credentials/{id}Z2\0220/v1alpha1/broadsign/devices/{device}/credentials'
  _BROADSIGNSERVICE.methods_by_name['ListCredentials']._options = None
  _BROADSIGNSERVICE.methods_by_name['ListCredentials']._serialized_options = b'\202\323\344\223\002!\022\037/v1alpha1/broadsign/credentials'
  _BROADSIGNSERVICE.methods_by_name['CreateCredential']._options = None
  _BROADSIGNSERVICE.methods_by_name['CreateCredential']._serialized_options = b'\202\323\344\223\002-\"\037/v1alpha1/broadsign/credentials:\ncredential'
  _BROADSIGNSERVICE.methods_by_name['DeleteCredential']._options = None
  _BROADSIGNSERVICE.methods_by_name['DeleteCredential']._serialized_options = b'\202\323\344\223\002&*$/v1alpha1/broadsign/credentials/{id}'
  _BROADSIGNSERVICE.methods_by_name['UpdateCredential']._options = None
  _BROADSIGNSERVICE.methods_by_name['UpdateCredential']._serialized_options = b'\202\323\344\223\002=2//v1alpha1/broadsign/credentials/{credential.id}:\ncredential'
  _BROADSIGNSERVICE.methods_by_name['GetMappings']._options = None
  _BROADSIGNSERVICE.methods_by_name['GetMappings']._serialized_options = b'\202\323\344\223\002\215\001\022-/v1alpha1/broadsign/credentials/{id}/mappingsZ+\022)/v1alpha1/broadsign/users/{user}/mappingsZ/\022-/v1alpha1/broadsign/devices/{device}/mappings'
  _BROADSIGNSERVICE.methods_by_name['ListMappings']._options = None
  _BROADSIGNSERVICE.methods_by_name['ListMappings']._serialized_options = b'\202\323\344\223\002\036\022\034/v1alpha1/broadsign/mappings'
  _BROADSIGNSERVICE.methods_by_name['CreateMapping']._options = None
  _BROADSIGNSERVICE.methods_by_name['CreateMapping']._serialized_options = b'\202\323\344\223\002\'\"\034/v1alpha1/broadsign/mappings:\007mapping'
  _BROADSIGNSERVICE.methods_by_name['DeleteMapping']._options = None
  _BROADSIGNSERVICE.methods_by_name['DeleteMapping']._serialized_options = b'\202\323\344\223\002#*!/v1alpha1/broadsign/mappings/{id}'
  _BROADSIGNSERVICE.methods_by_name['UpdateMapping']._options = None
  _BROADSIGNSERVICE.methods_by_name['UpdateMapping']._serialized_options = b'\202\323\344\223\00242)/v1alpha1/broadsign/mappings/{mapping.id}:\007mapping'
  _REPORTREQUEST._serialized_start=258
  _REPORTREQUEST._serialized_end=401
  _GETCREDENTIALSREQUEST._serialized_start=403
  _GETCREDENTIALSREQUEST._serialized_end=468
  _LISTCREDENTIALSREQUEST._serialized_start=470
  _LISTCREDENTIALSREQUEST._serialized_end=597
  _CREATECREDENTIALREQUEST._serialized_start=599
  _CREATECREDENTIALREQUEST._serialized_end=687
  _UPDATECREDENTIALREQUEST._serialized_start=690
  _UPDATECREDENTIALREQUEST._serialized_end=827
  _LISTCREDENTIALSRESPONSE._serialized_start=829
  _LISTCREDENTIALSRESPONSE._serialized_end=943
  _DELETECREDENTIALREQUEST._serialized_start=945
  _DELETECREDENTIALREQUEST._serialized_end=982
  _GETMAPPINGREQUEST._serialized_start=984
  _GETMAPPINGREQUEST._serialized_end=1045
  _LISTMAPPINGSREQUEST._serialized_start=1047
  _LISTMAPPINGSREQUEST._serialized_end=1171
  _LISTMAPPINGSRESPONSE._serialized_start=1173
  _LISTMAPPINGSRESPONSE._serialized_end=1278
  _CREATEMAPPINGREQUEST._serialized_start=1280
  _CREATEMAPPINGREQUEST._serialized_end=1359
  _UPDATEMAPPINGREQUEST._serialized_start=1362
  _UPDATEMAPPINGREQUEST._serialized_end=1490
  _DELETEMAPPINGREQUEST._serialized_start=1492
  _DELETEMAPPINGREQUEST._serialized_end=1526
  _BROADSIGNSERVICE._serialized_start=1529
  _BROADSIGNSERVICE._serialized_end=3546
# @@protoc_insertion_point(module_scope)
