# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vald/vald.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from vald import payload_pb2 as vald_dot_payload__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='vald/vald.proto',
  package='vald',
  syntax='proto3',
  serialized_options=b'\n\016org.vdaas.valdB\007ValdApiP\001Z$github.com/vdaas/vald/apis/grpc/vald',
  serialized_pb=b'\n\x0fvald/vald.proto\x12\x04vald\x1a\x12vald/payload.proto\x1a\x1cgoogle/api/annotations.proto2\xda\x08\n\x04Vald\x12\x46\n\x06\x45xists\x12\x12.payload.Object.ID\x1a\x12.payload.Object.ID\"\x14\x82\xd3\xe4\x93\x02\x0e\x12\x0c/exists/{id}\x12O\n\x06Search\x12\x17.payload.Search.Request\x1a\x18.payload.Search.Response\"\x12\x82\xd3\xe4\x93\x02\x0c\"\x07/search:\x01*\x12U\n\nSearchByID\x12\x19.payload.Search.IDRequest\x1a\x18.payload.Search.Response\"\x12\x82\xd3\xe4\x93\x02\x0c\"\x07/search:\x01*\x12G\n\x0cStreamSearch\x12\x17.payload.Search.Request\x1a\x18.payload.Search.Response\"\x00(\x01\x30\x01\x12M\n\x10StreamSearchByID\x12\x19.payload.Search.IDRequest\x1a\x18.payload.Search.Response\"\x00(\x01\x30\x01\x12\x44\n\x06Insert\x12\x16.payload.Object.Vector\x1a\x0e.payload.Empty\"\x12\x82\xd3\xe4\x93\x02\x0c\"\x07/insert:\x01*\x12<\n\x0cStreamInsert\x12\x16.payload.Object.Vector\x1a\x0e.payload.Empty\"\x00(\x01\x30\x01\x12\x38\n\x0bMultiInsert\x12\x17.payload.Object.Vectors\x1a\x0e.payload.Empty\"\x00\x12\x44\n\x06Update\x12\x16.payload.Object.Vector\x1a\x0e.payload.Empty\"\x12\x82\xd3\xe4\x93\x02\x0c\"\x07/update:\x01*\x12<\n\x0cStreamUpdate\x12\x16.payload.Object.Vector\x1a\x0e.payload.Empty\"\x00(\x01\x30\x01\x12\x38\n\x0bMultiUpdate\x12\x17.payload.Object.Vectors\x1a\x0e.payload.Empty\"\x00\x12\x42\n\x06Remove\x12\x12.payload.Object.ID\x1a\x0e.payload.Empty\"\x14\x82\xd3\xe4\x93\x02\x0e*\x0c/remove/{id}\x12\x38\n\x0cStreamRemove\x12\x12.payload.Object.ID\x1a\x0e.payload.Empty\"\x00(\x01\x30\x01\x12\x34\n\x0bMultiRemove\x12\x13.payload.Object.IDs\x1a\x0e.payload.Empty\"\x00\x12Q\n\tGetObject\x12\x12.payload.Object.ID\x1a\x1a.payload.Backup.MetaVector\"\x14\x82\xd3\xe4\x93\x02\x0e\x12\x0c/object/{id}\x12G\n\x0fStreamGetObject\x12\x12.payload.Object.ID\x1a\x1a.payload.Backup.MetaVector\"\x00(\x01\x30\x01\x42\x41\n\x0eorg.vdaas.valdB\x07ValdApiP\x01Z$github.com/vdaas/vald/apis/grpc/valdb\x06proto3'
  ,
  dependencies=[vald_dot_payload__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_VALD = _descriptor.ServiceDescriptor(
  name='Vald',
  full_name='vald.Vald',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=76,
  serialized_end=1190,
  methods=[
  _descriptor.MethodDescriptor(
    name='Exists',
    full_name='vald.Vald.Exists',
    index=0,
    containing_service=None,
    input_type=vald_dot_payload__pb2._OBJECT_ID,
    output_type=vald_dot_payload__pb2._OBJECT_ID,
    serialized_options=b'\202\323\344\223\002\016\022\014/exists/{id}',
  ),
  _descriptor.MethodDescriptor(
    name='Search',
    full_name='vald.Vald.Search',
    index=1,
    containing_service=None,
    input_type=vald_dot_payload__pb2._SEARCH_REQUEST,
    output_type=vald_dot_payload__pb2._SEARCH_RESPONSE,
    serialized_options=b'\202\323\344\223\002\014\"\007/search:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='SearchByID',
    full_name='vald.Vald.SearchByID',
    index=2,
    containing_service=None,
    input_type=vald_dot_payload__pb2._SEARCH_IDREQUEST,
    output_type=vald_dot_payload__pb2._SEARCH_RESPONSE,
    serialized_options=b'\202\323\344\223\002\014\"\007/search:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='StreamSearch',
    full_name='vald.Vald.StreamSearch',
    index=3,
    containing_service=None,
    input_type=vald_dot_payload__pb2._SEARCH_REQUEST,
    output_type=vald_dot_payload__pb2._SEARCH_RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StreamSearchByID',
    full_name='vald.Vald.StreamSearchByID',
    index=4,
    containing_service=None,
    input_type=vald_dot_payload__pb2._SEARCH_IDREQUEST,
    output_type=vald_dot_payload__pb2._SEARCH_RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Insert',
    full_name='vald.Vald.Insert',
    index=5,
    containing_service=None,
    input_type=vald_dot_payload__pb2._OBJECT_VECTOR,
    output_type=vald_dot_payload__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002\014\"\007/insert:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='StreamInsert',
    full_name='vald.Vald.StreamInsert',
    index=6,
    containing_service=None,
    input_type=vald_dot_payload__pb2._OBJECT_VECTOR,
    output_type=vald_dot_payload__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='MultiInsert',
    full_name='vald.Vald.MultiInsert',
    index=7,
    containing_service=None,
    input_type=vald_dot_payload__pb2._OBJECT_VECTORS,
    output_type=vald_dot_payload__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='vald.Vald.Update',
    index=8,
    containing_service=None,
    input_type=vald_dot_payload__pb2._OBJECT_VECTOR,
    output_type=vald_dot_payload__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002\014\"\007/update:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='StreamUpdate',
    full_name='vald.Vald.StreamUpdate',
    index=9,
    containing_service=None,
    input_type=vald_dot_payload__pb2._OBJECT_VECTOR,
    output_type=vald_dot_payload__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='MultiUpdate',
    full_name='vald.Vald.MultiUpdate',
    index=10,
    containing_service=None,
    input_type=vald_dot_payload__pb2._OBJECT_VECTORS,
    output_type=vald_dot_payload__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Remove',
    full_name='vald.Vald.Remove',
    index=11,
    containing_service=None,
    input_type=vald_dot_payload__pb2._OBJECT_ID,
    output_type=vald_dot_payload__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002\016*\014/remove/{id}',
  ),
  _descriptor.MethodDescriptor(
    name='StreamRemove',
    full_name='vald.Vald.StreamRemove',
    index=12,
    containing_service=None,
    input_type=vald_dot_payload__pb2._OBJECT_ID,
    output_type=vald_dot_payload__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='MultiRemove',
    full_name='vald.Vald.MultiRemove',
    index=13,
    containing_service=None,
    input_type=vald_dot_payload__pb2._OBJECT_IDS,
    output_type=vald_dot_payload__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetObject',
    full_name='vald.Vald.GetObject',
    index=14,
    containing_service=None,
    input_type=vald_dot_payload__pb2._OBJECT_ID,
    output_type=vald_dot_payload__pb2._BACKUP_METAVECTOR,
    serialized_options=b'\202\323\344\223\002\016\022\014/object/{id}',
  ),
  _descriptor.MethodDescriptor(
    name='StreamGetObject',
    full_name='vald.Vald.StreamGetObject',
    index=15,
    containing_service=None,
    input_type=vald_dot_payload__pb2._OBJECT_ID,
    output_type=vald_dot_payload__pb2._BACKUP_METAVECTOR,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_VALD)

DESCRIPTOR.services_by_name['Vald'] = _VALD

# @@protoc_insertion_point(module_scope)
