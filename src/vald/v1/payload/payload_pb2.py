# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vald/v1/payload/payload.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from validate import validate_pb2 as validate_dot_validate__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dvald/v1/payload/payload.proto\x12\npayload.v1\x1a\x17validate/validate.proto\x1a\x17google/rpc/status.proto\"\xc8\x07\n\x06Search\x1aN\n\x07Request\x12\x18\n\x06vector\x18\x01 \x03(\x02\x42\x08\xfa\x42\x05\x92\x01\x02\x08\x02\x12)\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x19.payload.v1.Search.Config\x1a<\n\x0cMultiRequest\x12,\n\x08requests\x18\x01 \x03(\x0b\x32\x1a.payload.v1.Search.Request\x1a\x42\n\tIDRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12)\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x19.payload.v1.Search.Config\x1a@\n\x0eMultiIDRequest\x12.\n\x08requests\x18\x01 \x03(\x0b\x32\x1c.payload.v1.Search.IDRequest\x1ay\n\rObjectRequest\x12\x0e\n\x06object\x18\x01 \x01(\x0c\x12)\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x19.payload.v1.Search.Config\x12-\n\nvectorizer\x18\x03 \x01(\x0b\x32\x19.payload.v1.Filter.Target\x1aH\n\x12MultiObjectRequest\x12\x32\n\x08requests\x18\x01 \x03(\x0b\x32 .payload.v1.Search.ObjectRequest\x1a\xe5\x01\n\x06\x43onfig\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x14\n\x03num\x18\x02 \x01(\rB\x07\xfa\x42\x04*\x02(\x01\x12\x0e\n\x06radius\x18\x03 \x01(\x02\x12\x0f\n\x07\x65psilon\x18\x04 \x01(\x02\x12\x0f\n\x07timeout\x18\x05 \x01(\x03\x12\x32\n\x0fingress_filters\x18\x06 \x01(\x0b\x32\x19.payload.v1.Filter.Config\x12\x31\n\x0e\x65gress_filters\x18\x07 \x01(\x0b\x32\x19.payload.v1.Filter.Config\x12\x18\n\x07min_num\x18\x08 \x01(\rB\x07\xfa\x42\x04*\x02(\x00\x1aL\n\x08Response\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12,\n\x07results\x18\x02 \x03(\x0b\x32\x1b.payload.v1.Object.Distance\x1a;\n\tResponses\x12.\n\tresponses\x18\x01 \x03(\x0b\x32\x1b.payload.v1.Search.Response\x1ar\n\x0eStreamResponse\x12/\n\x08response\x18\x01 \x01(\x0b\x32\x1b.payload.v1.Search.ResponseH\x00\x12$\n\x06status\x18\x02 \x01(\x0b\x32\x12.google.rpc.StatusH\x00\x42\t\n\x07payload\"d\n\x06\x46ilter\x1a$\n\x06Target\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\r\x1a\x34\n\x06\x43onfig\x12*\n\x07targets\x18\x01 \x03(\x0b\x32\x19.payload.v1.Filter.Target\"\xfa\x03\n\x06Insert\x1ai\n\x07Request\x12\x33\n\x06vector\x18\x01 \x01(\x0b\x32\x19.payload.v1.Object.VectorB\x08\xfa\x42\x05\x92\x01\x02\x08\x02\x12)\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x19.payload.v1.Insert.Config\x1a<\n\x0cMultiRequest\x12,\n\x08requests\x18\x01 \x03(\x0b\x32\x1a.payload.v1.Insert.Request\x1a\x92\x01\n\rObjectRequest\x12\'\n\x06object\x18\x01 \x01(\x0b\x32\x17.payload.v1.Object.Blob\x12)\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x19.payload.v1.Insert.Config\x12-\n\nvectorizer\x18\x03 \x01(\x0b\x32\x19.payload.v1.Filter.Target\x1aH\n\x12MultiObjectRequest\x12\x32\n\x08requests\x18\x01 \x03(\x0b\x32 .payload.v1.Insert.ObjectRequest\x1ah\n\x06\x43onfig\x12\x1f\n\x17skip_strict_exist_check\x18\x01 \x01(\x08\x12*\n\x07\x66ilters\x18\x02 \x01(\x0b\x32\x19.payload.v1.Filter.Config\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\"\x9c\x04\n\x06Update\x1ai\n\x07Request\x12\x33\n\x06vector\x18\x01 \x01(\x0b\x32\x19.payload.v1.Object.VectorB\x08\xfa\x42\x05\x92\x01\x02\x08\x02\x12)\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x19.payload.v1.Update.Config\x1a<\n\x0cMultiRequest\x12,\n\x08requests\x18\x01 \x03(\x0b\x32\x1a.payload.v1.Update.Request\x1a\x92\x01\n\rObjectRequest\x12\'\n\x06object\x18\x01 \x01(\x0b\x32\x17.payload.v1.Object.Blob\x12)\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x19.payload.v1.Update.Config\x12-\n\nvectorizer\x18\x03 \x01(\x0b\x32\x19.payload.v1.Filter.Target\x1aH\n\x12MultiObjectRequest\x12\x32\n\x08requests\x18\x01 \x03(\x0b\x32 .payload.v1.Update.ObjectRequest\x1a\x89\x01\n\x06\x43onfig\x12\x1f\n\x17skip_strict_exist_check\x18\x01 \x01(\x08\x12*\n\x07\x66ilters\x18\x02 \x01(\x0b\x32\x19.payload.v1.Filter.Config\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\x12\x1f\n\x17\x64isable_balanced_update\x18\x04 \x01(\x08\"\x9c\x04\n\x06Upsert\x1ai\n\x07Request\x12\x33\n\x06vector\x18\x01 \x01(\x0b\x32\x19.payload.v1.Object.VectorB\x08\xfa\x42\x05\x92\x01\x02\x08\x02\x12)\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x19.payload.v1.Upsert.Config\x1a<\n\x0cMultiRequest\x12,\n\x08requests\x18\x01 \x03(\x0b\x32\x1a.payload.v1.Upsert.Request\x1a\x92\x01\n\rObjectRequest\x12\'\n\x06object\x18\x01 \x01(\x0b\x32\x17.payload.v1.Object.Blob\x12)\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x19.payload.v1.Upsert.Config\x12-\n\nvectorizer\x18\x03 \x01(\x0b\x32\x19.payload.v1.Filter.Target\x1aH\n\x12MultiObjectRequest\x12\x32\n\x08requests\x18\x01 \x03(\x0b\x32 .payload.v1.Upsert.ObjectRequest\x1a\x89\x01\n\x06\x43onfig\x12\x1f\n\x17skip_strict_exist_check\x18\x01 \x01(\x08\x12*\n\x07\x66ilters\x18\x02 \x01(\x0b\x32\x19.payload.v1.Filter.Config\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\x12\x1f\n\x17\x64isable_balanced_update\x18\x04 \x01(\x08\"\xdd\x01\n\x06Remove\x1aW\n\x07Request\x12!\n\x02id\x18\x01 \x01(\x0b\x32\x15.payload.v1.Object.ID\x12)\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x19.payload.v1.Remove.Config\x1a<\n\x0cMultiRequest\x12,\n\x08requests\x18\x01 \x03(\x0b\x32\x1a.payload.v1.Remove.Request\x1a<\n\x06\x43onfig\x12\x1f\n\x17skip_strict_exist_check\x18\x01 \x01(\x08\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\"\xc8\x07\n\x06Object\x1ah\n\rVectorRequest\x12+\n\x02id\x18\x01 \x01(\x0b\x32\x15.payload.v1.Object.IDB\x08\xfa\x42\x05\x92\x01\x02\x08\x02\x12*\n\x07\x66ilters\x18\x02 \x01(\x0b\x32\x19.payload.v1.Filter.Config\x1a(\n\x08\x44istance\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08\x64istance\x18\x02 \x01(\x02\x1ar\n\x0eStreamDistance\x12/\n\x08\x64istance\x18\x01 \x01(\x0b\x32\x1b.payload.v1.Object.DistanceH\x00\x12$\n\x06status\x18\x02 \x01(\x0b\x32\x12.google.rpc.StatusH\x00\x42\t\n\x07payload\x1a\x19\n\x02ID\x12\x13\n\x02id\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x1a\x12\n\x03IDs\x12\x0b\n\x03ids\x18\x01 \x03(\t\x1a\x37\n\x06Vector\x12\x13\n\x02id\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12\x18\n\x06vector\x18\x02 \x03(\x02\x42\x08\xfa\x42\x05\x92\x01\x02\x08\x02\x1a\x35\n\x07Vectors\x12*\n\x07vectors\x18\x01 \x03(\x0b\x32\x19.payload.v1.Object.Vector\x1al\n\x0cStreamVector\x12+\n\x06vector\x18\x01 \x01(\x0b\x32\x19.payload.v1.Object.VectorH\x00\x12$\n\x06status\x18\x02 \x01(\x0b\x32\x12.google.rpc.StatusH\x00\x42\t\n\x07payload\x1a.\n\rReshapeVector\x12\x0e\n\x06object\x18\x01 \x01(\x0c\x12\r\n\x05shape\x18\x02 \x03(\x05\x1a+\n\x04\x42lob\x12\x13\n\x02id\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12\x0e\n\x06object\x18\x02 \x01(\x0c\x1a\x66\n\nStreamBlob\x12\'\n\x04\x62lob\x18\x01 \x01(\x0b\x32\x17.payload.v1.Object.BlobH\x00\x12$\n\x06status\x18\x02 \x01(\x0b\x32\x12.google.rpc.StatusH\x00\x42\t\n\x07payload\x1a\x33\n\x08Location\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12\x0b\n\x03ips\x18\x03 \x03(\t\x1ar\n\x0eStreamLocation\x12/\n\x08location\x18\x01 \x01(\x0b\x32\x1b.payload.v1.Object.LocationH\x00\x12$\n\x06status\x18\x02 \x01(\x0b\x32\x12.google.rpc.StatusH\x00\x42\t\n\x07payload\x1a;\n\tLocations\x12.\n\tlocations\x18\x01 \x03(\x0b\x32\x1b.payload.v1.Object.Location\";\n\x07\x43ontrol\x1a\x30\n\x12\x43reateIndexRequest\x12\x1a\n\tpool_size\x18\x01 \x01(\rB\x07\xfa\x42\x04*\x02(\x00\"O\n\nDiscoverer\x1a\x41\n\x07Request\x12\x15\n\x04name\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12\x11\n\tnamespace\x18\x02 \x01(\t\x12\x0c\n\x04node\x18\x03 \x01(\t\"\x88\x06\n\x04Info\x1a\x97\x01\n\x05Index\x1aN\n\x05\x43ount\x12\x0e\n\x06stored\x18\x01 \x01(\r\x12\x13\n\x0buncommitted\x18\x02 \x01(\r\x12\x10\n\x08indexing\x18\x03 \x01(\x08\x12\x0e\n\x06saving\x18\x04 \x01(\x08\x1a>\n\x04UUID\x1a\x19\n\tCommitted\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x1a\x1b\n\x0bUncommitted\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x1a\xbe\x01\n\x03Pod\x12\x10\n\x08\x61pp_name\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tnamespace\x18\x03 \x01(\t\x12\x13\n\x02ip\x18\x04 \x01(\tB\x07\xfa\x42\x04r\x02x\x01\x12!\n\x03\x63pu\x18\x05 \x01(\x0b\x32\x14.payload.v1.Info.CPU\x12\'\n\x06memory\x18\x06 \x01(\x0b\x32\x17.payload.v1.Info.Memory\x12#\n\x04node\x18\x07 \x01(\x0b\x32\x15.payload.v1.Info.Node\x1a\xb3\x01\n\x04Node\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rinternal_addr\x18\x02 \x01(\t\x12\x15\n\rexternal_addr\x18\x03 \x01(\t\x12!\n\x03\x63pu\x18\x04 \x01(\x0b\x32\x14.payload.v1.Info.CPU\x12\'\n\x06memory\x18\x05 \x01(\x0b\x32\x17.payload.v1.Info.Memory\x12#\n\x04Pods\x18\x06 \x01(\x0b\x32\x15.payload.v1.Info.Pods\x1a\x34\n\x03\x43PU\x12\r\n\x05limit\x18\x01 \x01(\x01\x12\x0f\n\x07request\x18\x02 \x01(\x01\x12\r\n\x05usage\x18\x03 \x01(\x01\x1a\x37\n\x06Memory\x12\r\n\x05limit\x18\x01 \x01(\x01\x12\x0f\n\x07request\x18\x02 \x01(\x01\x12\r\n\x05usage\x18\x03 \x01(\x01\x1a\x34\n\x04Pods\x12,\n\x04pods\x18\x01 \x03(\x0b\x32\x14.payload.v1.Info.PodB\x08\xfa\x42\x05\x92\x01\x02\x08\x01\x1a\x37\n\x05Nodes\x12.\n\x05nodes\x18\x01 \x03(\x0b\x32\x15.payload.v1.Info.NodeB\x08\xfa\x42\x05\x92\x01\x02\x08\x01\x1a\x11\n\x03IPs\x12\n\n\x02ip\x18\x01 \x03(\t\"\x07\n\x05\x45mptyBZ\n\x1dorg.vdaas.vald.api.v1.payloadB\x0bValdPayloadP\x01Z*github.com/vdaas/vald/apis/grpc/v1/payloadb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vald.v1.payload.payload_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\035org.vdaas.vald.api.v1.payloadB\013ValdPayloadP\001Z*github.com/vdaas/vald/apis/grpc/v1/payload'
  _SEARCH_REQUEST.fields_by_name['vector']._options = None
  _SEARCH_REQUEST.fields_by_name['vector']._serialized_options = b'\372B\005\222\001\002\010\002'
  _SEARCH_CONFIG.fields_by_name['num']._options = None
  _SEARCH_CONFIG.fields_by_name['num']._serialized_options = b'\372B\004*\002(\001'
  _SEARCH_CONFIG.fields_by_name['min_num']._options = None
  _SEARCH_CONFIG.fields_by_name['min_num']._serialized_options = b'\372B\004*\002(\000'
  _INSERT_REQUEST.fields_by_name['vector']._options = None
  _INSERT_REQUEST.fields_by_name['vector']._serialized_options = b'\372B\005\222\001\002\010\002'
  _UPDATE_REQUEST.fields_by_name['vector']._options = None
  _UPDATE_REQUEST.fields_by_name['vector']._serialized_options = b'\372B\005\222\001\002\010\002'
  _UPSERT_REQUEST.fields_by_name['vector']._options = None
  _UPSERT_REQUEST.fields_by_name['vector']._serialized_options = b'\372B\005\222\001\002\010\002'
  _OBJECT_VECTORREQUEST.fields_by_name['id']._options = None
  _OBJECT_VECTORREQUEST.fields_by_name['id']._serialized_options = b'\372B\005\222\001\002\010\002'
  _OBJECT_ID.fields_by_name['id']._options = None
  _OBJECT_ID.fields_by_name['id']._serialized_options = b'\372B\004r\002\020\001'
  _OBJECT_VECTOR.fields_by_name['id']._options = None
  _OBJECT_VECTOR.fields_by_name['id']._serialized_options = b'\372B\004r\002\020\001'
  _OBJECT_VECTOR.fields_by_name['vector']._options = None
  _OBJECT_VECTOR.fields_by_name['vector']._serialized_options = b'\372B\005\222\001\002\010\002'
  _OBJECT_BLOB.fields_by_name['id']._options = None
  _OBJECT_BLOB.fields_by_name['id']._serialized_options = b'\372B\004r\002\020\001'
  _CONTROL_CREATEINDEXREQUEST.fields_by_name['pool_size']._options = None
  _CONTROL_CREATEINDEXREQUEST.fields_by_name['pool_size']._serialized_options = b'\372B\004*\002(\000'
  _DISCOVERER_REQUEST.fields_by_name['name']._options = None
  _DISCOVERER_REQUEST.fields_by_name['name']._serialized_options = b'\372B\004r\002\020\001'
  _INFO_POD.fields_by_name['ip']._options = None
  _INFO_POD.fields_by_name['ip']._serialized_options = b'\372B\004r\002x\001'
  _INFO_PODS.fields_by_name['pods']._options = None
  _INFO_PODS.fields_by_name['pods']._serialized_options = b'\372B\005\222\001\002\010\001'
  _INFO_NODES.fields_by_name['nodes']._options = None
  _INFO_NODES.fields_by_name['nodes']._serialized_options = b'\372B\005\222\001\002\010\001'
  _SEARCH._serialized_start=96
  _SEARCH._serialized_end=1064
  _SEARCH_REQUEST._serialized_start=106
  _SEARCH_REQUEST._serialized_end=184
  _SEARCH_MULTIREQUEST._serialized_start=186
  _SEARCH_MULTIREQUEST._serialized_end=246
  _SEARCH_IDREQUEST._serialized_start=248
  _SEARCH_IDREQUEST._serialized_end=314
  _SEARCH_MULTIIDREQUEST._serialized_start=316
  _SEARCH_MULTIIDREQUEST._serialized_end=380
  _SEARCH_OBJECTREQUEST._serialized_start=382
  _SEARCH_OBJECTREQUEST._serialized_end=503
  _SEARCH_MULTIOBJECTREQUEST._serialized_start=505
  _SEARCH_MULTIOBJECTREQUEST._serialized_end=577
  _SEARCH_CONFIG._serialized_start=580
  _SEARCH_CONFIG._serialized_end=809
  _SEARCH_RESPONSE._serialized_start=811
  _SEARCH_RESPONSE._serialized_end=887
  _SEARCH_RESPONSES._serialized_start=889
  _SEARCH_RESPONSES._serialized_end=948
  _SEARCH_STREAMRESPONSE._serialized_start=950
  _SEARCH_STREAMRESPONSE._serialized_end=1064
  _FILTER._serialized_start=1066
  _FILTER._serialized_end=1166
  _FILTER_TARGET._serialized_start=1076
  _FILTER_TARGET._serialized_end=1112
  _FILTER_CONFIG._serialized_start=1114
  _FILTER_CONFIG._serialized_end=1166
  _INSERT._serialized_start=1169
  _INSERT._serialized_end=1675
  _INSERT_REQUEST._serialized_start=1179
  _INSERT_REQUEST._serialized_end=1284
  _INSERT_MULTIREQUEST._serialized_start=1286
  _INSERT_MULTIREQUEST._serialized_end=1346
  _INSERT_OBJECTREQUEST._serialized_start=1349
  _INSERT_OBJECTREQUEST._serialized_end=1495
  _INSERT_MULTIOBJECTREQUEST._serialized_start=1497
  _INSERT_MULTIOBJECTREQUEST._serialized_end=1569
  _INSERT_CONFIG._serialized_start=1571
  _INSERT_CONFIG._serialized_end=1675
  _UPDATE._serialized_start=1678
  _UPDATE._serialized_end=2218
  _UPDATE_REQUEST._serialized_start=1688
  _UPDATE_REQUEST._serialized_end=1793
  _UPDATE_MULTIREQUEST._serialized_start=1795
  _UPDATE_MULTIREQUEST._serialized_end=1855
  _UPDATE_OBJECTREQUEST._serialized_start=1858
  _UPDATE_OBJECTREQUEST._serialized_end=2004
  _UPDATE_MULTIOBJECTREQUEST._serialized_start=2006
  _UPDATE_MULTIOBJECTREQUEST._serialized_end=2078
  _UPDATE_CONFIG._serialized_start=2081
  _UPDATE_CONFIG._serialized_end=2218
  _UPSERT._serialized_start=2221
  _UPSERT._serialized_end=2761
  _UPSERT_REQUEST._serialized_start=2231
  _UPSERT_REQUEST._serialized_end=2336
  _UPSERT_MULTIREQUEST._serialized_start=2338
  _UPSERT_MULTIREQUEST._serialized_end=2398
  _UPSERT_OBJECTREQUEST._serialized_start=2401
  _UPSERT_OBJECTREQUEST._serialized_end=2547
  _UPSERT_MULTIOBJECTREQUEST._serialized_start=2549
  _UPSERT_MULTIOBJECTREQUEST._serialized_end=2621
  _UPSERT_CONFIG._serialized_start=2081
  _UPSERT_CONFIG._serialized_end=2218
  _REMOVE._serialized_start=2764
  _REMOVE._serialized_end=2985
  _REMOVE_REQUEST._serialized_start=2774
  _REMOVE_REQUEST._serialized_end=2861
  _REMOVE_MULTIREQUEST._serialized_start=2863
  _REMOVE_MULTIREQUEST._serialized_end=2923
  _REMOVE_CONFIG._serialized_start=2925
  _REMOVE_CONFIG._serialized_end=2985
  _OBJECT._serialized_start=2988
  _OBJECT._serialized_end=3956
  _OBJECT_VECTORREQUEST._serialized_start=2998
  _OBJECT_VECTORREQUEST._serialized_end=3102
  _OBJECT_DISTANCE._serialized_start=3104
  _OBJECT_DISTANCE._serialized_end=3144
  _OBJECT_STREAMDISTANCE._serialized_start=3146
  _OBJECT_STREAMDISTANCE._serialized_end=3260
  _OBJECT_ID._serialized_start=3262
  _OBJECT_ID._serialized_end=3287
  _OBJECT_IDS._serialized_start=3289
  _OBJECT_IDS._serialized_end=3307
  _OBJECT_VECTOR._serialized_start=3309
  _OBJECT_VECTOR._serialized_end=3364
  _OBJECT_VECTORS._serialized_start=3366
  _OBJECT_VECTORS._serialized_end=3419
  _OBJECT_STREAMVECTOR._serialized_start=3421
  _OBJECT_STREAMVECTOR._serialized_end=3529
  _OBJECT_RESHAPEVECTOR._serialized_start=3531
  _OBJECT_RESHAPEVECTOR._serialized_end=3577
  _OBJECT_BLOB._serialized_start=3579
  _OBJECT_BLOB._serialized_end=3622
  _OBJECT_STREAMBLOB._serialized_start=3624
  _OBJECT_STREAMBLOB._serialized_end=3726
  _OBJECT_LOCATION._serialized_start=3728
  _OBJECT_LOCATION._serialized_end=3779
  _OBJECT_STREAMLOCATION._serialized_start=3781
  _OBJECT_STREAMLOCATION._serialized_end=3895
  _OBJECT_LOCATIONS._serialized_start=3897
  _OBJECT_LOCATIONS._serialized_end=3956
  _CONTROL._serialized_start=3958
  _CONTROL._serialized_end=4017
  _CONTROL_CREATEINDEXREQUEST._serialized_start=3969
  _CONTROL_CREATEINDEXREQUEST._serialized_end=4017
  _DISCOVERER._serialized_start=4019
  _DISCOVERER._serialized_end=4098
  _DISCOVERER_REQUEST._serialized_start=4033
  _DISCOVERER_REQUEST._serialized_end=4098
  _INFO._serialized_start=4101
  _INFO._serialized_end=4877
  _INFO_INDEX._serialized_start=4110
  _INFO_INDEX._serialized_end=4261
  _INFO_INDEX_COUNT._serialized_start=4119
  _INFO_INDEX_COUNT._serialized_end=4197
  _INFO_INDEX_UUID._serialized_start=4199
  _INFO_INDEX_UUID._serialized_end=4261
  _INFO_INDEX_UUID_COMMITTED._serialized_start=4207
  _INFO_INDEX_UUID_COMMITTED._serialized_end=4232
  _INFO_INDEX_UUID_UNCOMMITTED._serialized_start=4234
  _INFO_INDEX_UUID_UNCOMMITTED._serialized_end=4261
  _INFO_POD._serialized_start=4264
  _INFO_POD._serialized_end=4454
  _INFO_NODE._serialized_start=4457
  _INFO_NODE._serialized_end=4636
  _INFO_CPU._serialized_start=4638
  _INFO_CPU._serialized_end=4690
  _INFO_MEMORY._serialized_start=4692
  _INFO_MEMORY._serialized_end=4747
  _INFO_PODS._serialized_start=4749
  _INFO_PODS._serialized_end=4801
  _INFO_NODES._serialized_start=4803
  _INFO_NODES._serialized_end=4858
  _INFO_IPS._serialized_start=4860
  _INFO_IPS._serialized_end=4877
  _EMPTY._serialized_start=4879
  _EMPTY._serialized_end=4886
# @@protoc_insertion_point(module_scope)
