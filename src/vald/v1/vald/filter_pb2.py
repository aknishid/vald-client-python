# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vald/v1/vald/filter.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from vald.v1.payload import payload_pb2 as vald_dot_v1_dot_payload_dot_payload__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='vald/v1/vald/filter.proto',
  package='vald.v1',
  syntax='proto3',
  serialized_options=b'\n\032org.vdaas.vald.api.v1.valdB\nValdFilterP\001Z\'github.com/vdaas/vald/apis/grpc/v1/vald\310\342\036\001\320\342\036\001\340\342\036\001\300\343\036\001\310\343\036\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19vald/v1/vald/filter.proto\x12\x07vald.v1\x1a\x1dvald/v1/payload/payload.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto2\xe8\x07\n\x06\x46ilter\x12h\n\x0cSearchObject\x12 .payload.v1.Search.ObjectRequest\x1a\x1b.payload.v1.Search.Response\"\x19\x82\xd3\xe4\x93\x02\x13\"\x0e/search/object:\x01*\x12_\n\x12StreamSearchObject\x12 .payload.v1.Search.ObjectRequest\x1a!.payload.v1.Search.StreamResponse\"\x00(\x01\x30\x01\x12_\n\x0cInsertObject\x12\x17.payload.v1.Object.Blob\x1a\x1b.payload.v1.Object.Location\"\x19\x82\xd3\xe4\x93\x02\x13\"\x0e/insert/object:\x01*\x12V\n\x12StreamInsertObject\x12\x17.payload.v1.Object.Blob\x1a!.payload.v1.Object.StreamLocation\"\x00(\x01\x30\x01\x12L\n\x11MultiInsertObject\x12\x17.payload.v1.Object.Blob\x1a\x1c.payload.v1.Object.Locations\"\x00\x12_\n\x0cUpdateObject\x12\x17.payload.v1.Object.Blob\x1a\x1b.payload.v1.Object.Location\"\x19\x82\xd3\xe4\x93\x02\x13\"\x0e/update/object:\x01*\x12V\n\x12StreamUpdateObject\x12\x17.payload.v1.Object.Blob\x1a!.payload.v1.Object.StreamLocation\"\x00(\x01\x30\x01\x12L\n\x11MultiUpdateObject\x12\x17.payload.v1.Object.Blob\x1a\x1c.payload.v1.Object.Locations\"\x00\x12_\n\x0cUpsertObject\x12\x17.payload.v1.Object.Blob\x1a\x1b.payload.v1.Object.Location\"\x19\x82\xd3\xe4\x93\x02\x13\"\x0e/upsert/object:\x01*\x12V\n\x12StreamUpsertObject\x12\x17.payload.v1.Object.Blob\x1a!.payload.v1.Object.StreamLocation\"\x00(\x01\x30\x01\x12L\n\x11MultiUpsertObject\x12\x17.payload.v1.Object.Blob\x1a\x1c.payload.v1.Object.Locations\"\x00\x42g\n\x1aorg.vdaas.vald.api.v1.valdB\nValdFilterP\x01Z\'github.com/vdaas/vald/apis/grpc/v1/vald\xc8\xe2\x1e\x01\xd0\xe2\x1e\x01\xe0\xe2\x1e\x01\xc0\xe3\x1e\x01\xc8\xe3\x1e\x01\x62\x06proto3'
  ,
  dependencies=[vald_dot_v1_dot_payload_dot_payload__pb2.DESCRIPTOR,gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_FILTER = _descriptor.ServiceDescriptor(
  name='Filter',
  full_name='vald.v1.Filter',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=122,
  serialized_end=1122,
  methods=[
  _descriptor.MethodDescriptor(
    name='SearchObject',
    full_name='vald.v1.Filter.SearchObject',
    index=0,
    containing_service=None,
    input_type=vald_dot_v1_dot_payload_dot_payload__pb2._SEARCH_OBJECTREQUEST,
    output_type=vald_dot_v1_dot_payload_dot_payload__pb2._SEARCH_RESPONSE,
    serialized_options=b'\202\323\344\223\002\023\"\016/search/object:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StreamSearchObject',
    full_name='vald.v1.Filter.StreamSearchObject',
    index=1,
    containing_service=None,
    input_type=vald_dot_v1_dot_payload_dot_payload__pb2._SEARCH_OBJECTREQUEST,
    output_type=vald_dot_v1_dot_payload_dot_payload__pb2._SEARCH_STREAMRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='InsertObject',
    full_name='vald.v1.Filter.InsertObject',
    index=2,
    containing_service=None,
    input_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_BLOB,
    output_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_LOCATION,
    serialized_options=b'\202\323\344\223\002\023\"\016/insert/object:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StreamInsertObject',
    full_name='vald.v1.Filter.StreamInsertObject',
    index=3,
    containing_service=None,
    input_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_BLOB,
    output_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_STREAMLOCATION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MultiInsertObject',
    full_name='vald.v1.Filter.MultiInsertObject',
    index=4,
    containing_service=None,
    input_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_BLOB,
    output_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_LOCATIONS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateObject',
    full_name='vald.v1.Filter.UpdateObject',
    index=5,
    containing_service=None,
    input_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_BLOB,
    output_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_LOCATION,
    serialized_options=b'\202\323\344\223\002\023\"\016/update/object:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StreamUpdateObject',
    full_name='vald.v1.Filter.StreamUpdateObject',
    index=6,
    containing_service=None,
    input_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_BLOB,
    output_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_STREAMLOCATION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MultiUpdateObject',
    full_name='vald.v1.Filter.MultiUpdateObject',
    index=7,
    containing_service=None,
    input_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_BLOB,
    output_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_LOCATIONS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpsertObject',
    full_name='vald.v1.Filter.UpsertObject',
    index=8,
    containing_service=None,
    input_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_BLOB,
    output_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_LOCATION,
    serialized_options=b'\202\323\344\223\002\023\"\016/upsert/object:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StreamUpsertObject',
    full_name='vald.v1.Filter.StreamUpsertObject',
    index=9,
    containing_service=None,
    input_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_BLOB,
    output_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_STREAMLOCATION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MultiUpsertObject',
    full_name='vald.v1.Filter.MultiUpsertObject',
    index=10,
    containing_service=None,
    input_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_BLOB,
    output_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_LOCATIONS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_FILTER)

DESCRIPTOR.services_by_name['Filter'] = _FILTER

# @@protoc_insertion_point(module_scope)
