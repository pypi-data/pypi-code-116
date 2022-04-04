# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: admobilize/datagateway/v1alpha1/datagateway_service.proto
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
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from admobilize.proto.common import entity_pb2 as admobilize_dot_common_dot_entity__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9admobilize/datagateway/v1alpha1/datagateway_service.proto\x12\x1f\x61\x64mobilize.datagateway.v1alpha1\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1e\x61\x64mobilize/common/entity.proto\"\xc6\x01\n\x03Job\x12\x0e\n\x06job_id\x18\x01 \x01(\t\x12;\n\x06status\x18\x02 \x01(\x0e\x32+.admobilize.datagateway.v1alpha1.Job.Status\x12\x0e\n\x06\x64\x65tail\x18\x03 \x01(\t\x12\x16\n\x0estatus_message\x18\x04 \x01(\t\x12\x11\n\tself_link\x18\x05 \x01(\t\"7\n\x06Status\x12\x0b\n\x07PENDING\x10\x00\x12\x0b\n\x07RUNNING\x10\x01\x12\x08\n\x04\x44ONE\x10\x03\x12\t\n\x05\x45RROR\x10\x04\"\xdf\x01\n\x10\x43reateJobRequest\x12.\n\nstart_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\nproject_id\x18\x03 \x01(\t\x12\x12\n\nproduct_id\x18\x04 \x01(\t\x12\x10\n\x08timezone\x18\x07 \x01(\t\x12\x12\n\nspeed_unit\x18\x08 \x01(\t\x12\x12\n\ndevice_ids\x18\x05 \x03(\t\x12\x0b\n\x03\x63ms\x18\x06 \x01(\t\"G\n\rGetJobRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12*\n\x06\x66ields\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"I\n\x14GetJobResultRequests\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\"2\n\x14\x45xportResultsRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x02 \x01(\t\"j\n\x15GetDatapointsResponse\x12\x0e\n\x06job_id\x18\x01 \x01(\t\x12\x14\n\x0cjob_complete\x18\x02 \x01(\x08\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\t\x12\x12\n\ndatapoints\x18\x04 \x01(\t\"K\n\x15\x45xportResultsResponse\x12\x0e\n\x06job_id\x18\x01 \x01(\t\x12\x14\n\x0cjob_complete\x18\x02 \x01(\x08\x12\x0c\n\x04urls\x18\x03 \x03(\t2\xe0\x04\n\x12\x44\x61taGatewayService\x12|\n\tCreateJob\x12\x31.admobilize.datagateway.v1alpha1.CreateJobRequest\x1a$.admobilize.datagateway.v1alpha1.Job\"\x16\x82\xd3\xe4\x93\x02\x10\"\x0e/v1alpha1/jobs\x12}\n\x06GetJob\x12..admobilize.datagateway.v1alpha1.GetJobRequest\x1a$.admobilize.datagateway.v1alpha1.Job\"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/v1alpha1/{id=jobs/*}\x12\xa5\x01\n\rGetJobResults\x12\x35.admobilize.datagateway.v1alpha1.GetJobResultRequests\x1a\x36.admobilize.datagateway.v1alpha1.GetDatapointsResponse\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/v1alpha1/{id=jobs/*}/results\x12\xa4\x01\n\rExportResults\x12\x35.admobilize.datagateway.v1alpha1.ExportResultsRequest\x1a\x36.admobilize.datagateway.v1alpha1.ExportResultsResponse\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/v1alpha1/{id=jobs/*}/exportB\xa8\x01\n#com.admobilize.datagateway.v1alpha1B\x10\x44\x61taGatewayProtoP\x01ZCbitbucket.org/admobilize/admobilizeapis-go/pkg/datagateway/v1alpha1\xa2\x02\x05\x41\x44MDG\xaa\x02\x1f\x41\x64Mobilize.DataGateway.V1Alpha1b\x06proto3')



_JOB = DESCRIPTOR.message_types_by_name['Job']
_CREATEJOBREQUEST = DESCRIPTOR.message_types_by_name['CreateJobRequest']
_GETJOBREQUEST = DESCRIPTOR.message_types_by_name['GetJobRequest']
_GETJOBRESULTREQUESTS = DESCRIPTOR.message_types_by_name['GetJobResultRequests']
_EXPORTRESULTSREQUEST = DESCRIPTOR.message_types_by_name['ExportResultsRequest']
_GETDATAPOINTSRESPONSE = DESCRIPTOR.message_types_by_name['GetDatapointsResponse']
_EXPORTRESULTSRESPONSE = DESCRIPTOR.message_types_by_name['ExportResultsResponse']
_JOB_STATUS = _JOB.enum_types_by_name['Status']
Job = _reflection.GeneratedProtocolMessageType('Job', (_message.Message,), {
  'DESCRIPTOR' : _JOB,
  '__module__' : 'admobilize.datagateway.v1alpha1.datagateway_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.datagateway.v1alpha1.Job)
  })
_sym_db.RegisterMessage(Job)

CreateJobRequest = _reflection.GeneratedProtocolMessageType('CreateJobRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEJOBREQUEST,
  '__module__' : 'admobilize.datagateway.v1alpha1.datagateway_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.datagateway.v1alpha1.CreateJobRequest)
  })
_sym_db.RegisterMessage(CreateJobRequest)

GetJobRequest = _reflection.GeneratedProtocolMessageType('GetJobRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETJOBREQUEST,
  '__module__' : 'admobilize.datagateway.v1alpha1.datagateway_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.datagateway.v1alpha1.GetJobRequest)
  })
_sym_db.RegisterMessage(GetJobRequest)

GetJobResultRequests = _reflection.GeneratedProtocolMessageType('GetJobResultRequests', (_message.Message,), {
  'DESCRIPTOR' : _GETJOBRESULTREQUESTS,
  '__module__' : 'admobilize.datagateway.v1alpha1.datagateway_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.datagateway.v1alpha1.GetJobResultRequests)
  })
_sym_db.RegisterMessage(GetJobResultRequests)

ExportResultsRequest = _reflection.GeneratedProtocolMessageType('ExportResultsRequest', (_message.Message,), {
  'DESCRIPTOR' : _EXPORTRESULTSREQUEST,
  '__module__' : 'admobilize.datagateway.v1alpha1.datagateway_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.datagateway.v1alpha1.ExportResultsRequest)
  })
_sym_db.RegisterMessage(ExportResultsRequest)

GetDatapointsResponse = _reflection.GeneratedProtocolMessageType('GetDatapointsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETDATAPOINTSRESPONSE,
  '__module__' : 'admobilize.datagateway.v1alpha1.datagateway_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.datagateway.v1alpha1.GetDatapointsResponse)
  })
_sym_db.RegisterMessage(GetDatapointsResponse)

ExportResultsResponse = _reflection.GeneratedProtocolMessageType('ExportResultsResponse', (_message.Message,), {
  'DESCRIPTOR' : _EXPORTRESULTSRESPONSE,
  '__module__' : 'admobilize.datagateway.v1alpha1.datagateway_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.datagateway.v1alpha1.ExportResultsResponse)
  })
_sym_db.RegisterMessage(ExportResultsResponse)

_DATAGATEWAYSERVICE = DESCRIPTOR.services_by_name['DataGatewayService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n#com.admobilize.datagateway.v1alpha1B\020DataGatewayProtoP\001ZCbitbucket.org/admobilize/admobilizeapis-go/pkg/datagateway/v1alpha1\242\002\005ADMDG\252\002\037AdMobilize.DataGateway.V1Alpha1'
  _DATAGATEWAYSERVICE.methods_by_name['CreateJob']._options = None
  _DATAGATEWAYSERVICE.methods_by_name['CreateJob']._serialized_options = b'\202\323\344\223\002\020\"\016/v1alpha1/jobs'
  _DATAGATEWAYSERVICE.methods_by_name['GetJob']._options = None
  _DATAGATEWAYSERVICE.methods_by_name['GetJob']._serialized_options = b'\202\323\344\223\002\027\022\025/v1alpha1/{id=jobs/*}'
  _DATAGATEWAYSERVICE.methods_by_name['GetJobResults']._options = None
  _DATAGATEWAYSERVICE.methods_by_name['GetJobResults']._serialized_options = b'\202\323\344\223\002\037\022\035/v1alpha1/{id=jobs/*}/results'
  _DATAGATEWAYSERVICE.methods_by_name['ExportResults']._options = None
  _DATAGATEWAYSERVICE.methods_by_name['ExportResults']._serialized_options = b'\202\323\344\223\002\036\022\034/v1alpha1/{id=jobs/*}/export'
  _JOB._serialized_start=253
  _JOB._serialized_end=451
  _JOB_STATUS._serialized_start=396
  _JOB_STATUS._serialized_end=451
  _CREATEJOBREQUEST._serialized_start=454
  _CREATEJOBREQUEST._serialized_end=677
  _GETJOBREQUEST._serialized_start=679
  _GETJOBREQUEST._serialized_end=750
  _GETJOBRESULTREQUESTS._serialized_start=752
  _GETJOBRESULTREQUESTS._serialized_end=825
  _EXPORTRESULTSREQUEST._serialized_start=827
  _EXPORTRESULTSREQUEST._serialized_end=877
  _GETDATAPOINTSRESPONSE._serialized_start=879
  _GETDATAPOINTSRESPONSE._serialized_end=985
  _EXPORTRESULTSRESPONSE._serialized_start=987
  _EXPORTRESULTSRESPONSE._serialized_end=1062
  _DATAGATEWAYSERVICE._serialized_start=1065
  _DATAGATEWAYSERVICE._serialized_end=1673
# @@protoc_insertion_point(module_scope)
