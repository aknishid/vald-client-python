# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vald/agent.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from vald import payload_pb2 as vald_dot_payload__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='vald/agent.proto',
  package='agent',
  syntax='proto3',
  serialized_options=b'\n\024org.vdaas.vald.agentB\tValdAgentP\001Z%github.com/vdaas/vald/apis/grpc/agent',
  serialized_pb=b'\n\x10vald/agent.proto\x12\x05\x61gent\x1a\x12vald/payload.proto\x1a\x1cgoogle/api/annotations.proto2\xa5\x0b\n\x05\x41gent\x12\x46\n\x06\x45xists\x12\x12.payload.Object.ID\x1a\x12.payload.Object.ID\"\x14\x82\xd3\xe4\x93\x02\x0e\x12\x0c/exists/{id}\x12O\n\x06Search\x12\x17.payload.Search.Request\x1a\x18.payload.Search.Response\"\x12\x82\xd3\xe4\x93\x02\x0c\"\x07/search:\x01*\x12X\n\nSearchByID\x12\x19.payload.Search.IDRequest\x1a\x18.payload.Search.Response\"\x15\x82\xd3\xe4\x93\x02\x0f\"\n/search/id:\x01*\x12G\n\x0cStreamSearch\x12\x17.payload.Search.Request\x1a\x18.payload.Search.Response\"\x00(\x01\x30\x01\x12M\n\x10StreamSearchByID\x12\x19.payload.Search.IDRequest\x1a\x18.payload.Search.Response\"\x00(\x01\x30\x01\x12\x44\n\x06Insert\x12\x16.payload.Object.Vector\x1a\x0e.payload.Empty\"\x12\x82\xd3\xe4\x93\x02\x0c\"\x07/insert:\x01*\x12<\n\x0cStreamInsert\x12\x16.payload.Object.Vector\x1a\x0e.payload.Empty\"\x00(\x01\x30\x01\x12\x38\n\x0bMultiInsert\x12\x17.payload.Object.Vectors\x1a\x0e.payload.Empty\"\x00\x12\x44\n\x06Update\x12\x16.payload.Object.Vector\x1a\x0e.payload.Empty\"\x12\x82\xd3\xe4\x93\x02\x0c\"\x07/update:\x01*\x12<\n\x0cStreamUpdate\x12\x16.payload.Object.Vector\x1a\x0e.payload.Empty\"\x00(\x01\x30\x01\x12\x38\n\x0bMultiUpdate\x12\x17.payload.Object.Vectors\x1a\x0e.payload.Empty\"\x00\x12\x42\n\x06Remove\x12\x12.payload.Object.ID\x1a\x0e.payload.Empty\"\x14\x82\xd3\xe4\x93\x02\x0e*\x0c/remove/{id}\x12\x38\n\x0cStreamRemove\x12\x12.payload.Object.ID\x1a\x0e.payload.Empty\"\x00(\x01\x30\x01\x12\x34\n\x0bMultiRemove\x12\x13.payload.Object.IDs\x1a\x0e.payload.Empty\"\x00\x12M\n\tGetObject\x12\x12.payload.Object.ID\x1a\x16.payload.Object.Vector\"\x14\x82\xd3\xe4\x93\x02\x0e\x12\x0c/object/{id}\x12\x43\n\x0fStreamGetObject\x12\x12.payload.Object.ID\x1a\x16.payload.Object.Vector\"\x00(\x01\x30\x01\x12Z\n\x0b\x43reateIndex\x12$.payload.Controll.CreateIndexRequest\x1a\x0e.payload.Empty\"\x15\x82\xd3\xe4\x93\x02\x0f\x12\r/index/create\x12@\n\tSaveIndex\x12\x0e.payload.Empty\x1a\x0e.payload.Empty\"\x13\x82\xd3\xe4\x93\x02\r\x12\x0b/index/save\x12h\n\x12\x43reateAndSaveIndex\x12$.payload.Controll.CreateIndexRequest\x1a\x0e.payload.Empty\"\x1c\x82\xd3\xe4\x93\x02\x16\x12\x14/index/createandsave\x12\x45\n\tIndexInfo\x12\x0e.payload.Empty\x1a\x13.payload.Info.Index\"\x13\x82\xd3\xe4\x93\x02\r\x12\x0b/index/infoBJ\n\x14org.vdaas.vald.agentB\tValdAgentP\x01Z%github.com/vdaas/vald/apis/grpc/agentb\x06proto3'
  ,
  dependencies=[vald_dot_payload__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_AGENT = _descriptor.ServiceDescriptor(
  name='Agent',
  full_name='agent.Agent',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=78,
  serialized_end=1523,
  methods=[
  _descriptor.MethodDescriptor(
    name='Exists',
    full_name='agent.Agent.Exists',
    index=0,
    containing_service=None,
    input_type=vald_dot_payload__pb2._OBJECT_ID,
    output_type=vald_dot_payload__pb2._OBJECT_ID,
    serialized_options=b'\202\323\344\223\002\016\022\014/exists/{id}',
  ),
  _descriptor.MethodDescriptor(
    name='Search',
    full_name='agent.Agent.Search',
    index=1,
    containing_service=None,
    input_type=vald_dot_payload__pb2._SEARCH_REQUEST,
    output_type=vald_dot_payload__pb2._SEARCH_RESPONSE,
    serialized_options=b'\202\323\344\223\002\014\"\007/search:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='SearchByID',
    full_name='agent.Agent.SearchByID',
    index=2,
    containing_service=None,
    input_type=vald_dot_payload__pb2._SEARCH_IDREQUEST,
    output_type=vald_dot_payload__pb2._SEARCH_RESPONSE,
    serialized_options=b'\202\323\344\223\002\017\"\n/search/id:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='StreamSearch',
    full_name='agent.Agent.StreamSearch',
    index=3,
    containing_service=None,
    input_type=vald_dot_payload__pb2._SEARCH_REQUEST,
    output_type=vald_dot_payload__pb2._SEARCH_RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StreamSearchByID',
    full_name='agent.Agent.StreamSearchByID',
    index=4,
    containing_service=None,
    input_type=vald_dot_payload__pb2._SEARCH_IDREQUEST,
    output_type=vald_dot_payload__pb2._SEARCH_RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Insert',
    full_name='agent.Agent.Insert',
    index=5,
    containing_service=None,
    input_type=vald_dot_payload__pb2._OBJECT_VECTOR,
    output_type=vald_dot_payload__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002\014\"\007/insert:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='StreamInsert',
    full_name='agent.Agent.StreamInsert',
    index=6,
    containing_service=None,
    input_type=vald_dot_payload__pb2._OBJECT_VECTOR,
    output_type=vald_dot_payload__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='MultiInsert',
    full_name='agent.Agent.MultiInsert',
    index=7,
    containing_service=None,
    input_type=vald_dot_payload__pb2._OBJECT_VECTORS,
    output_type=vald_dot_payload__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='agent.Agent.Update',
    index=8,
    containing_service=None,
    input_type=vald_dot_payload__pb2._OBJECT_VECTOR,
    output_type=vald_dot_payload__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002\014\"\007/update:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='StreamUpdate',
    full_name='agent.Agent.StreamUpdate',
    index=9,
    containing_service=None,
    input_type=vald_dot_payload__pb2._OBJECT_VECTOR,
    output_type=vald_dot_payload__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='MultiUpdate',
    full_name='agent.Agent.MultiUpdate',
    index=10,
    containing_service=None,
    input_type=vald_dot_payload__pb2._OBJECT_VECTORS,
    output_type=vald_dot_payload__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Remove',
    full_name='agent.Agent.Remove',
    index=11,
    containing_service=None,
    input_type=vald_dot_payload__pb2._OBJECT_ID,
    output_type=vald_dot_payload__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002\016*\014/remove/{id}',
  ),
  _descriptor.MethodDescriptor(
    name='StreamRemove',
    full_name='agent.Agent.StreamRemove',
    index=12,
    containing_service=None,
    input_type=vald_dot_payload__pb2._OBJECT_ID,
    output_type=vald_dot_payload__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='MultiRemove',
    full_name='agent.Agent.MultiRemove',
    index=13,
    containing_service=None,
    input_type=vald_dot_payload__pb2._OBJECT_IDS,
    output_type=vald_dot_payload__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetObject',
    full_name='agent.Agent.GetObject',
    index=14,
    containing_service=None,
    input_type=vald_dot_payload__pb2._OBJECT_ID,
    output_type=vald_dot_payload__pb2._OBJECT_VECTOR,
    serialized_options=b'\202\323\344\223\002\016\022\014/object/{id}',
  ),
  _descriptor.MethodDescriptor(
    name='StreamGetObject',
    full_name='agent.Agent.StreamGetObject',
    index=15,
    containing_service=None,
    input_type=vald_dot_payload__pb2._OBJECT_ID,
    output_type=vald_dot_payload__pb2._OBJECT_VECTOR,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreateIndex',
    full_name='agent.Agent.CreateIndex',
    index=16,
    containing_service=None,
    input_type=vald_dot_payload__pb2._CONTROLL_CREATEINDEXREQUEST,
    output_type=vald_dot_payload__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002\017\022\r/index/create',
  ),
  _descriptor.MethodDescriptor(
    name='SaveIndex',
    full_name='agent.Agent.SaveIndex',
    index=17,
    containing_service=None,
    input_type=vald_dot_payload__pb2._EMPTY,
    output_type=vald_dot_payload__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002\r\022\013/index/save',
  ),
  _descriptor.MethodDescriptor(
    name='CreateAndSaveIndex',
    full_name='agent.Agent.CreateAndSaveIndex',
    index=18,
    containing_service=None,
    input_type=vald_dot_payload__pb2._CONTROLL_CREATEINDEXREQUEST,
    output_type=vald_dot_payload__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002\026\022\024/index/createandsave',
  ),
  _descriptor.MethodDescriptor(
    name='IndexInfo',
    full_name='agent.Agent.IndexInfo',
    index=19,
    containing_service=None,
    input_type=vald_dot_payload__pb2._EMPTY,
    output_type=vald_dot_payload__pb2._INFO_INDEX,
    serialized_options=b'\202\323\344\223\002\r\022\013/index/info',
  ),
])
_sym_db.RegisterServiceDescriptor(_AGENT)

DESCRIPTOR.services_by_name['Agent'] = _AGENT

# @@protoc_insertion_point(module_scope)
