# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import csi_pb2 as csi__pb2


class IdentityStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetPluginInfo = channel.unary_unary(
        '/csi.v0.Identity/GetPluginInfo',
        request_serializer=csi__pb2.GetPluginInfoRequest.SerializeToString,
        response_deserializer=csi__pb2.GetPluginInfoResponse.FromString,
        )
    self.GetPluginCapabilities = channel.unary_unary(
        '/csi.v0.Identity/GetPluginCapabilities',
        request_serializer=csi__pb2.GetPluginCapabilitiesRequest.SerializeToString,
        response_deserializer=csi__pb2.GetPluginCapabilitiesResponse.FromString,
        )
    self.Probe = channel.unary_unary(
        '/csi.v0.Identity/Probe',
        request_serializer=csi__pb2.ProbeRequest.SerializeToString,
        response_deserializer=csi__pb2.ProbeResponse.FromString,
        )


class IdentityServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetPluginInfo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetPluginCapabilities(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Probe(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_IdentityServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetPluginInfo': grpc.unary_unary_rpc_method_handler(
          servicer.GetPluginInfo,
          request_deserializer=csi__pb2.GetPluginInfoRequest.FromString,
          response_serializer=csi__pb2.GetPluginInfoResponse.SerializeToString,
      ),
      'GetPluginCapabilities': grpc.unary_unary_rpc_method_handler(
          servicer.GetPluginCapabilities,
          request_deserializer=csi__pb2.GetPluginCapabilitiesRequest.FromString,
          response_serializer=csi__pb2.GetPluginCapabilitiesResponse.SerializeToString,
      ),
      'Probe': grpc.unary_unary_rpc_method_handler(
          servicer.Probe,
          request_deserializer=csi__pb2.ProbeRequest.FromString,
          response_serializer=csi__pb2.ProbeResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'csi.v0.Identity', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class ControllerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateVolume = channel.unary_unary(
        '/csi.v0.Controller/CreateVolume',
        request_serializer=csi__pb2.CreateVolumeRequest.SerializeToString,
        response_deserializer=csi__pb2.CreateVolumeResponse.FromString,
        )
    self.DeleteVolume = channel.unary_unary(
        '/csi.v0.Controller/DeleteVolume',
        request_serializer=csi__pb2.DeleteVolumeRequest.SerializeToString,
        response_deserializer=csi__pb2.DeleteVolumeResponse.FromString,
        )
    self.ControllerPublishVolume = channel.unary_unary(
        '/csi.v0.Controller/ControllerPublishVolume',
        request_serializer=csi__pb2.ControllerPublishVolumeRequest.SerializeToString,
        response_deserializer=csi__pb2.ControllerPublishVolumeResponse.FromString,
        )
    self.ControllerUnpublishVolume = channel.unary_unary(
        '/csi.v0.Controller/ControllerUnpublishVolume',
        request_serializer=csi__pb2.ControllerUnpublishVolumeRequest.SerializeToString,
        response_deserializer=csi__pb2.ControllerUnpublishVolumeResponse.FromString,
        )
    self.ValidateVolumeCapabilities = channel.unary_unary(
        '/csi.v0.Controller/ValidateVolumeCapabilities',
        request_serializer=csi__pb2.ValidateVolumeCapabilitiesRequest.SerializeToString,
        response_deserializer=csi__pb2.ValidateVolumeCapabilitiesResponse.FromString,
        )
    self.ListVolumes = channel.unary_unary(
        '/csi.v0.Controller/ListVolumes',
        request_serializer=csi__pb2.ListVolumesRequest.SerializeToString,
        response_deserializer=csi__pb2.ListVolumesResponse.FromString,
        )
    self.GetCapacity = channel.unary_unary(
        '/csi.v0.Controller/GetCapacity',
        request_serializer=csi__pb2.GetCapacityRequest.SerializeToString,
        response_deserializer=csi__pb2.GetCapacityResponse.FromString,
        )
    self.ControllerGetCapabilities = channel.unary_unary(
        '/csi.v0.Controller/ControllerGetCapabilities',
        request_serializer=csi__pb2.ControllerGetCapabilitiesRequest.SerializeToString,
        response_deserializer=csi__pb2.ControllerGetCapabilitiesResponse.FromString,
        )


class ControllerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def CreateVolume(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteVolume(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ControllerPublishVolume(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ControllerUnpublishVolume(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ValidateVolumeCapabilities(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListVolumes(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetCapacity(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ControllerGetCapabilities(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ControllerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateVolume': grpc.unary_unary_rpc_method_handler(
          servicer.CreateVolume,
          request_deserializer=csi__pb2.CreateVolumeRequest.FromString,
          response_serializer=csi__pb2.CreateVolumeResponse.SerializeToString,
      ),
      'DeleteVolume': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteVolume,
          request_deserializer=csi__pb2.DeleteVolumeRequest.FromString,
          response_serializer=csi__pb2.DeleteVolumeResponse.SerializeToString,
      ),
      'ControllerPublishVolume': grpc.unary_unary_rpc_method_handler(
          servicer.ControllerPublishVolume,
          request_deserializer=csi__pb2.ControllerPublishVolumeRequest.FromString,
          response_serializer=csi__pb2.ControllerPublishVolumeResponse.SerializeToString,
      ),
      'ControllerUnpublishVolume': grpc.unary_unary_rpc_method_handler(
          servicer.ControllerUnpublishVolume,
          request_deserializer=csi__pb2.ControllerUnpublishVolumeRequest.FromString,
          response_serializer=csi__pb2.ControllerUnpublishVolumeResponse.SerializeToString,
      ),
      'ValidateVolumeCapabilities': grpc.unary_unary_rpc_method_handler(
          servicer.ValidateVolumeCapabilities,
          request_deserializer=csi__pb2.ValidateVolumeCapabilitiesRequest.FromString,
          response_serializer=csi__pb2.ValidateVolumeCapabilitiesResponse.SerializeToString,
      ),
      'ListVolumes': grpc.unary_unary_rpc_method_handler(
          servicer.ListVolumes,
          request_deserializer=csi__pb2.ListVolumesRequest.FromString,
          response_serializer=csi__pb2.ListVolumesResponse.SerializeToString,
      ),
      'GetCapacity': grpc.unary_unary_rpc_method_handler(
          servicer.GetCapacity,
          request_deserializer=csi__pb2.GetCapacityRequest.FromString,
          response_serializer=csi__pb2.GetCapacityResponse.SerializeToString,
      ),
      'ControllerGetCapabilities': grpc.unary_unary_rpc_method_handler(
          servicer.ControllerGetCapabilities,
          request_deserializer=csi__pb2.ControllerGetCapabilitiesRequest.FromString,
          response_serializer=csi__pb2.ControllerGetCapabilitiesResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'csi.v0.Controller', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class NodeStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.NodeStageVolume = channel.unary_unary(
        '/csi.v0.Node/NodeStageVolume',
        request_serializer=csi__pb2.NodeStageVolumeRequest.SerializeToString,
        response_deserializer=csi__pb2.NodeStageVolumeResponse.FromString,
        )
    self.NodeUnstageVolume = channel.unary_unary(
        '/csi.v0.Node/NodeUnstageVolume',
        request_serializer=csi__pb2.NodeUnstageVolumeRequest.SerializeToString,
        response_deserializer=csi__pb2.NodeUnstageVolumeResponse.FromString,
        )
    self.NodePublishVolume = channel.unary_unary(
        '/csi.v0.Node/NodePublishVolume',
        request_serializer=csi__pb2.NodePublishVolumeRequest.SerializeToString,
        response_deserializer=csi__pb2.NodePublishVolumeResponse.FromString,
        )
    self.NodeUnpublishVolume = channel.unary_unary(
        '/csi.v0.Node/NodeUnpublishVolume',
        request_serializer=csi__pb2.NodeUnpublishVolumeRequest.SerializeToString,
        response_deserializer=csi__pb2.NodeUnpublishVolumeResponse.FromString,
        )
    self.NodeGetId = channel.unary_unary(
        '/csi.v0.Node/NodeGetId',
        request_serializer=csi__pb2.NodeGetIdRequest.SerializeToString,
        response_deserializer=csi__pb2.NodeGetIdResponse.FromString,
        )
    self.NodeGetCapabilities = channel.unary_unary(
        '/csi.v0.Node/NodeGetCapabilities',
        request_serializer=csi__pb2.NodeGetCapabilitiesRequest.SerializeToString,
        response_deserializer=csi__pb2.NodeGetCapabilitiesResponse.FromString,
        )


class NodeServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def NodeStageVolume(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def NodeUnstageVolume(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def NodePublishVolume(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def NodeUnpublishVolume(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def NodeGetId(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def NodeGetCapabilities(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_NodeServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'NodeStageVolume': grpc.unary_unary_rpc_method_handler(
          servicer.NodeStageVolume,
          request_deserializer=csi__pb2.NodeStageVolumeRequest.FromString,
          response_serializer=csi__pb2.NodeStageVolumeResponse.SerializeToString,
      ),
      'NodeUnstageVolume': grpc.unary_unary_rpc_method_handler(
          servicer.NodeUnstageVolume,
          request_deserializer=csi__pb2.NodeUnstageVolumeRequest.FromString,
          response_serializer=csi__pb2.NodeUnstageVolumeResponse.SerializeToString,
      ),
      'NodePublishVolume': grpc.unary_unary_rpc_method_handler(
          servicer.NodePublishVolume,
          request_deserializer=csi__pb2.NodePublishVolumeRequest.FromString,
          response_serializer=csi__pb2.NodePublishVolumeResponse.SerializeToString,
      ),
      'NodeUnpublishVolume': grpc.unary_unary_rpc_method_handler(
          servicer.NodeUnpublishVolume,
          request_deserializer=csi__pb2.NodeUnpublishVolumeRequest.FromString,
          response_serializer=csi__pb2.NodeUnpublishVolumeResponse.SerializeToString,
      ),
      'NodeGetId': grpc.unary_unary_rpc_method_handler(
          servicer.NodeGetId,
          request_deserializer=csi__pb2.NodeGetIdRequest.FromString,
          response_serializer=csi__pb2.NodeGetIdResponse.SerializeToString,
      ),
      'NodeGetCapabilities': grpc.unary_unary_rpc_method_handler(
          servicer.NodeGetCapabilities,
          request_deserializer=csi__pb2.NodeGetCapabilitiesRequest.FromString,
          response_serializer=csi__pb2.NodeGetCapabilitiesResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'csi.v0.Node', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
