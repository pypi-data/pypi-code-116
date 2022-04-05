# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import Case_pb2 as Case__pb2
import Definitions_pb2 as Definitions__pb2
import PdmObject_pb2 as PdmObject__pb2


class CaseStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetGridCount = channel.unary_unary(
                '/rips.Case/GetGridCount',
                request_serializer=Case__pb2.CaseRequest.SerializeToString,
                response_deserializer=Case__pb2.GridCount.FromString,
                )
        self.GetCellCount = channel.unary_unary(
                '/rips.Case/GetCellCount',
                request_serializer=Case__pb2.CellInfoRequest.SerializeToString,
                response_deserializer=Case__pb2.CellCount.FromString,
                )
        self.GetCellInfoForActiveCells = channel.unary_stream(
                '/rips.Case/GetCellInfoForActiveCells',
                request_serializer=Case__pb2.CellInfoRequest.SerializeToString,
                response_deserializer=Case__pb2.CellInfoArray.FromString,
                )
        self.GetCellCenterForActiveCells = channel.unary_stream(
                '/rips.Case/GetCellCenterForActiveCells',
                request_serializer=Case__pb2.CellInfoRequest.SerializeToString,
                response_deserializer=Definitions__pb2.CellCenters.FromString,
                )
        self.GetCellCornersForActiveCells = channel.unary_stream(
                '/rips.Case/GetCellCornersForActiveCells',
                request_serializer=Case__pb2.CellInfoRequest.SerializeToString,
                response_deserializer=Definitions__pb2.CellCornersArray.FromString,
                )
        self.GetCoarseningInfoArray = channel.unary_unary(
                '/rips.Case/GetCoarseningInfoArray',
                request_serializer=Case__pb2.CaseRequest.SerializeToString,
                response_deserializer=Case__pb2.CoarseningInfoArray.FromString,
                )
        self.GetTimeSteps = channel.unary_unary(
                '/rips.Case/GetTimeSteps',
                request_serializer=Case__pb2.CaseRequest.SerializeToString,
                response_deserializer=Case__pb2.TimeStepDates.FromString,
                )
        self.GetSelectedCells = channel.unary_stream(
                '/rips.Case/GetSelectedCells',
                request_serializer=Case__pb2.CaseRequest.SerializeToString,
                response_deserializer=Case__pb2.SelectedCells.FromString,
                )
        self.GetDaysSinceStart = channel.unary_unary(
                '/rips.Case/GetDaysSinceStart',
                request_serializer=Case__pb2.CaseRequest.SerializeToString,
                response_deserializer=Case__pb2.DaysSinceStart.FromString,
                )
        self.GetCaseInfo = channel.unary_unary(
                '/rips.Case/GetCaseInfo',
                request_serializer=Case__pb2.CaseRequest.SerializeToString,
                response_deserializer=Case__pb2.CaseInfo.FromString,
                )
        self.GetPdmObject = channel.unary_unary(
                '/rips.Case/GetPdmObject',
                request_serializer=Case__pb2.CaseRequest.SerializeToString,
                response_deserializer=PdmObject__pb2.PdmObject.FromString,
                )
        self.GetReservoirBoundingBox = channel.unary_unary(
                '/rips.Case/GetReservoirBoundingBox',
                request_serializer=Case__pb2.CaseRequest.SerializeToString,
                response_deserializer=Case__pb2.BoundingBox.FromString,
                )


class CaseServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetGridCount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCellCount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCellInfoForActiveCells(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCellCenterForActiveCells(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCellCornersForActiveCells(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCoarseningInfoArray(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTimeSteps(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSelectedCells(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDaysSinceStart(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCaseInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPdmObject(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetReservoirBoundingBox(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CaseServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetGridCount': grpc.unary_unary_rpc_method_handler(
                    servicer.GetGridCount,
                    request_deserializer=Case__pb2.CaseRequest.FromString,
                    response_serializer=Case__pb2.GridCount.SerializeToString,
            ),
            'GetCellCount': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCellCount,
                    request_deserializer=Case__pb2.CellInfoRequest.FromString,
                    response_serializer=Case__pb2.CellCount.SerializeToString,
            ),
            'GetCellInfoForActiveCells': grpc.unary_stream_rpc_method_handler(
                    servicer.GetCellInfoForActiveCells,
                    request_deserializer=Case__pb2.CellInfoRequest.FromString,
                    response_serializer=Case__pb2.CellInfoArray.SerializeToString,
            ),
            'GetCellCenterForActiveCells': grpc.unary_stream_rpc_method_handler(
                    servicer.GetCellCenterForActiveCells,
                    request_deserializer=Case__pb2.CellInfoRequest.FromString,
                    response_serializer=Definitions__pb2.CellCenters.SerializeToString,
            ),
            'GetCellCornersForActiveCells': grpc.unary_stream_rpc_method_handler(
                    servicer.GetCellCornersForActiveCells,
                    request_deserializer=Case__pb2.CellInfoRequest.FromString,
                    response_serializer=Definitions__pb2.CellCornersArray.SerializeToString,
            ),
            'GetCoarseningInfoArray': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCoarseningInfoArray,
                    request_deserializer=Case__pb2.CaseRequest.FromString,
                    response_serializer=Case__pb2.CoarseningInfoArray.SerializeToString,
            ),
            'GetTimeSteps': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTimeSteps,
                    request_deserializer=Case__pb2.CaseRequest.FromString,
                    response_serializer=Case__pb2.TimeStepDates.SerializeToString,
            ),
            'GetSelectedCells': grpc.unary_stream_rpc_method_handler(
                    servicer.GetSelectedCells,
                    request_deserializer=Case__pb2.CaseRequest.FromString,
                    response_serializer=Case__pb2.SelectedCells.SerializeToString,
            ),
            'GetDaysSinceStart': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDaysSinceStart,
                    request_deserializer=Case__pb2.CaseRequest.FromString,
                    response_serializer=Case__pb2.DaysSinceStart.SerializeToString,
            ),
            'GetCaseInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCaseInfo,
                    request_deserializer=Case__pb2.CaseRequest.FromString,
                    response_serializer=Case__pb2.CaseInfo.SerializeToString,
            ),
            'GetPdmObject': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPdmObject,
                    request_deserializer=Case__pb2.CaseRequest.FromString,
                    response_serializer=PdmObject__pb2.PdmObject.SerializeToString,
            ),
            'GetReservoirBoundingBox': grpc.unary_unary_rpc_method_handler(
                    servicer.GetReservoirBoundingBox,
                    request_deserializer=Case__pb2.CaseRequest.FromString,
                    response_serializer=Case__pb2.BoundingBox.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'rips.Case', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Case(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetGridCount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rips.Case/GetGridCount',
            Case__pb2.CaseRequest.SerializeToString,
            Case__pb2.GridCount.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCellCount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rips.Case/GetCellCount',
            Case__pb2.CellInfoRequest.SerializeToString,
            Case__pb2.CellCount.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCellInfoForActiveCells(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/rips.Case/GetCellInfoForActiveCells',
            Case__pb2.CellInfoRequest.SerializeToString,
            Case__pb2.CellInfoArray.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCellCenterForActiveCells(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/rips.Case/GetCellCenterForActiveCells',
            Case__pb2.CellInfoRequest.SerializeToString,
            Definitions__pb2.CellCenters.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCellCornersForActiveCells(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/rips.Case/GetCellCornersForActiveCells',
            Case__pb2.CellInfoRequest.SerializeToString,
            Definitions__pb2.CellCornersArray.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCoarseningInfoArray(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rips.Case/GetCoarseningInfoArray',
            Case__pb2.CaseRequest.SerializeToString,
            Case__pb2.CoarseningInfoArray.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTimeSteps(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rips.Case/GetTimeSteps',
            Case__pb2.CaseRequest.SerializeToString,
            Case__pb2.TimeStepDates.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSelectedCells(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/rips.Case/GetSelectedCells',
            Case__pb2.CaseRequest.SerializeToString,
            Case__pb2.SelectedCells.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDaysSinceStart(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rips.Case/GetDaysSinceStart',
            Case__pb2.CaseRequest.SerializeToString,
            Case__pb2.DaysSinceStart.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCaseInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rips.Case/GetCaseInfo',
            Case__pb2.CaseRequest.SerializeToString,
            Case__pb2.CaseInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPdmObject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rips.Case/GetPdmObject',
            Case__pb2.CaseRequest.SerializeToString,
            PdmObject__pb2.PdmObject.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetReservoirBoundingBox(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rips.Case/GetReservoirBoundingBox',
            Case__pb2.CaseRequest.SerializeToString,
            Case__pb2.BoundingBox.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
