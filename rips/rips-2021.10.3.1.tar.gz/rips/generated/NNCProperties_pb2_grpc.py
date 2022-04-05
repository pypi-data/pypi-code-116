# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import Case_pb2 as Case__pb2
import Definitions_pb2 as Definitions__pb2
import NNCProperties_pb2 as NNCProperties__pb2


class NNCPropertiesStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAvailableNNCProperties = channel.unary_unary(
                '/rips.NNCProperties/GetAvailableNNCProperties',
                request_serializer=Case__pb2.CaseRequest.SerializeToString,
                response_deserializer=NNCProperties__pb2.AvailableNNCProperties.FromString,
                )
        self.GetNNCConnections = channel.unary_stream(
                '/rips.NNCProperties/GetNNCConnections',
                request_serializer=Case__pb2.CaseRequest.SerializeToString,
                response_deserializer=NNCProperties__pb2.NNCConnections.FromString,
                )
        self.GetNNCValues = channel.unary_stream(
                '/rips.NNCProperties/GetNNCValues',
                request_serializer=NNCProperties__pb2.NNCValuesRequest.SerializeToString,
                response_deserializer=NNCProperties__pb2.NNCValues.FromString,
                )
        self.SetNNCValues = channel.stream_unary(
                '/rips.NNCProperties/SetNNCValues',
                request_serializer=NNCProperties__pb2.NNCValuesChunk.SerializeToString,
                response_deserializer=Definitions__pb2.ClientToServerStreamReply.FromString,
                )


class NNCPropertiesServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetAvailableNNCProperties(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNNCConnections(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNNCValues(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetNNCValues(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NNCPropertiesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAvailableNNCProperties': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAvailableNNCProperties,
                    request_deserializer=Case__pb2.CaseRequest.FromString,
                    response_serializer=NNCProperties__pb2.AvailableNNCProperties.SerializeToString,
            ),
            'GetNNCConnections': grpc.unary_stream_rpc_method_handler(
                    servicer.GetNNCConnections,
                    request_deserializer=Case__pb2.CaseRequest.FromString,
                    response_serializer=NNCProperties__pb2.NNCConnections.SerializeToString,
            ),
            'GetNNCValues': grpc.unary_stream_rpc_method_handler(
                    servicer.GetNNCValues,
                    request_deserializer=NNCProperties__pb2.NNCValuesRequest.FromString,
                    response_serializer=NNCProperties__pb2.NNCValues.SerializeToString,
            ),
            'SetNNCValues': grpc.stream_unary_rpc_method_handler(
                    servicer.SetNNCValues,
                    request_deserializer=NNCProperties__pb2.NNCValuesChunk.FromString,
                    response_serializer=Definitions__pb2.ClientToServerStreamReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'rips.NNCProperties', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NNCProperties(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetAvailableNNCProperties(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rips.NNCProperties/GetAvailableNNCProperties',
            Case__pb2.CaseRequest.SerializeToString,
            NNCProperties__pb2.AvailableNNCProperties.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetNNCConnections(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/rips.NNCProperties/GetNNCConnections',
            Case__pb2.CaseRequest.SerializeToString,
            NNCProperties__pb2.NNCConnections.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetNNCValues(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/rips.NNCProperties/GetNNCValues',
            NNCProperties__pb2.NNCValuesRequest.SerializeToString,
            NNCProperties__pb2.NNCValues.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetNNCValues(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/rips.NNCProperties/SetNNCValues',
            NNCProperties__pb2.NNCValuesChunk.SerializeToString,
            Definitions__pb2.ClientToServerStreamReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
