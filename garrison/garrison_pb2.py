# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: garrison.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='garrison.proto',
  package='garrison_server',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0egarrison.proto\x12\x0fgarrison_server\"+\n\rKeySetRequest\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\"9\n\x0eKeySetResponse\x12\x13\n\x0bkey_was_set\x18\x01 \x01(\x08\x12\x12\n\nkey_is_new\x18\x02 \x01(\x08\"\x1c\n\rKeyGetRequest\x12\x0b\n\x03key\x18\x01 \x01(\x0c\"3\n\x0eKeyGetResponse\x12\x12\n\nkey_exists\x18\x01 \x01(\x08\x12\r\n\x05value\x18\x02 \x01(\x0c\"\x1f\n\x10KeyDeleteRequest\x12\x0b\n\x03key\x18\x01 \x01(\x0c\"$\n\x11KeyDeleteResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\">\n\x0fQueuePopRequest\x12\x12\n\nqueue_name\x18\x01 \x01(\t\x12\x17\n\x0fnumber_of_items\x18\x02 \x01(\x04\"!\n\x10QueuePopResponse\x12\r\n\x05items\x18\x01 \x03(\x0c\"G\n\x10QueuePushRequest\x12\x12\n\nqueue_name\x18\x01 \x01(\t\x12\x10\n\x08priority\x18\x02 \x01(\t\x12\r\n\x05items\x18\x03 \x03(\x0c\"$\n\x11QueuePushResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"(\n\x12QueueDeleteRequest\x12\x12\n\nqueue_name\x18\x01 \x01(\t\"&\n\x13QueueDeleteResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"(\n\x12QueueLengthRequest\x12\x12\n\nqueue_name\x18\x01 \x01(\t\"+\n\x13QueueLengthResponse\x12\x14\n\x0cqueue_length\x18\x01 \x01(\x04\x32\xe8\x04\n\x0eGarrisonServer\x12L\n\x07key_set\x12\x1e.garrison_server.KeySetRequest\x1a\x1f.garrison_server.KeySetResponse\"\x00\x12L\n\x07key_get\x12\x1e.garrison_server.KeyGetRequest\x1a\x1f.garrison_server.KeyGetResponse\"\x00\x12U\n\nkey_delete\x12!.garrison_server.KeyDeleteRequest\x1a\".garrison_server.KeyDeleteResponse\"\x00\x12R\n\tqueue_pop\x12 .garrison_server.QueuePopRequest\x1a!.garrison_server.QueuePopResponse\"\x00\x12U\n\nqueue_push\x12!.garrison_server.QueuePushRequest\x1a\".garrison_server.QueuePushResponse\"\x00\x12[\n\x0cqueue_delete\x12#.garrison_server.QueueDeleteRequest\x1a$.garrison_server.QueueDeleteResponse\"\x00\x12[\n\x0cqueue_length\x12#.garrison_server.QueueLengthRequest\x1a$.garrison_server.QueueLengthResponse\"\x00\x62\x06proto3'
)




_KEYSETREQUEST = _descriptor.Descriptor(
  name='KeySetRequest',
  full_name='garrison_server.KeySetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='garrison_server.KeySetRequest.key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='garrison_server.KeySetRequest.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=78,
)


_KEYSETRESPONSE = _descriptor.Descriptor(
  name='KeySetResponse',
  full_name='garrison_server.KeySetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key_was_set', full_name='garrison_server.KeySetResponse.key_was_set', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key_is_new', full_name='garrison_server.KeySetResponse.key_is_new', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=80,
  serialized_end=137,
)


_KEYGETREQUEST = _descriptor.Descriptor(
  name='KeyGetRequest',
  full_name='garrison_server.KeyGetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='garrison_server.KeyGetRequest.key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=139,
  serialized_end=167,
)


_KEYGETRESPONSE = _descriptor.Descriptor(
  name='KeyGetResponse',
  full_name='garrison_server.KeyGetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key_exists', full_name='garrison_server.KeyGetResponse.key_exists', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='garrison_server.KeyGetResponse.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=169,
  serialized_end=220,
)


_KEYDELETEREQUEST = _descriptor.Descriptor(
  name='KeyDeleteRequest',
  full_name='garrison_server.KeyDeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='garrison_server.KeyDeleteRequest.key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=222,
  serialized_end=253,
)


_KEYDELETERESPONSE = _descriptor.Descriptor(
  name='KeyDeleteResponse',
  full_name='garrison_server.KeyDeleteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='garrison_server.KeyDeleteResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=255,
  serialized_end=291,
)


_QUEUEPOPREQUEST = _descriptor.Descriptor(
  name='QueuePopRequest',
  full_name='garrison_server.QueuePopRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='queue_name', full_name='garrison_server.QueuePopRequest.queue_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='number_of_items', full_name='garrison_server.QueuePopRequest.number_of_items', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=293,
  serialized_end=355,
)


_QUEUEPOPRESPONSE = _descriptor.Descriptor(
  name='QueuePopResponse',
  full_name='garrison_server.QueuePopResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='garrison_server.QueuePopResponse.items', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=357,
  serialized_end=390,
)


_QUEUEPUSHREQUEST = _descriptor.Descriptor(
  name='QueuePushRequest',
  full_name='garrison_server.QueuePushRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='queue_name', full_name='garrison_server.QueuePushRequest.queue_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='priority', full_name='garrison_server.QueuePushRequest.priority', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='items', full_name='garrison_server.QueuePushRequest.items', index=2,
      number=3, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=392,
  serialized_end=463,
)


_QUEUEPUSHRESPONSE = _descriptor.Descriptor(
  name='QueuePushResponse',
  full_name='garrison_server.QueuePushResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='garrison_server.QueuePushResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=465,
  serialized_end=501,
)


_QUEUEDELETEREQUEST = _descriptor.Descriptor(
  name='QueueDeleteRequest',
  full_name='garrison_server.QueueDeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='queue_name', full_name='garrison_server.QueueDeleteRequest.queue_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=503,
  serialized_end=543,
)


_QUEUEDELETERESPONSE = _descriptor.Descriptor(
  name='QueueDeleteResponse',
  full_name='garrison_server.QueueDeleteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='garrison_server.QueueDeleteResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=545,
  serialized_end=583,
)


_QUEUELENGTHREQUEST = _descriptor.Descriptor(
  name='QueueLengthRequest',
  full_name='garrison_server.QueueLengthRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='queue_name', full_name='garrison_server.QueueLengthRequest.queue_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=585,
  serialized_end=625,
)


_QUEUELENGTHRESPONSE = _descriptor.Descriptor(
  name='QueueLengthResponse',
  full_name='garrison_server.QueueLengthResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='queue_length', full_name='garrison_server.QueueLengthResponse.queue_length', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=627,
  serialized_end=670,
)

DESCRIPTOR.message_types_by_name['KeySetRequest'] = _KEYSETREQUEST
DESCRIPTOR.message_types_by_name['KeySetResponse'] = _KEYSETRESPONSE
DESCRIPTOR.message_types_by_name['KeyGetRequest'] = _KEYGETREQUEST
DESCRIPTOR.message_types_by_name['KeyGetResponse'] = _KEYGETRESPONSE
DESCRIPTOR.message_types_by_name['KeyDeleteRequest'] = _KEYDELETEREQUEST
DESCRIPTOR.message_types_by_name['KeyDeleteResponse'] = _KEYDELETERESPONSE
DESCRIPTOR.message_types_by_name['QueuePopRequest'] = _QUEUEPOPREQUEST
DESCRIPTOR.message_types_by_name['QueuePopResponse'] = _QUEUEPOPRESPONSE
DESCRIPTOR.message_types_by_name['QueuePushRequest'] = _QUEUEPUSHREQUEST
DESCRIPTOR.message_types_by_name['QueuePushResponse'] = _QUEUEPUSHRESPONSE
DESCRIPTOR.message_types_by_name['QueueDeleteRequest'] = _QUEUEDELETEREQUEST
DESCRIPTOR.message_types_by_name['QueueDeleteResponse'] = _QUEUEDELETERESPONSE
DESCRIPTOR.message_types_by_name['QueueLengthRequest'] = _QUEUELENGTHREQUEST
DESCRIPTOR.message_types_by_name['QueueLengthResponse'] = _QUEUELENGTHRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

KeySetRequest = _reflection.GeneratedProtocolMessageType('KeySetRequest', (_message.Message,), {
  'DESCRIPTOR' : _KEYSETREQUEST,
  '__module__' : 'garrison_pb2'
  # @@protoc_insertion_point(class_scope:garrison_server.KeySetRequest)
  })
_sym_db.RegisterMessage(KeySetRequest)

KeySetResponse = _reflection.GeneratedProtocolMessageType('KeySetResponse', (_message.Message,), {
  'DESCRIPTOR' : _KEYSETRESPONSE,
  '__module__' : 'garrison_pb2'
  # @@protoc_insertion_point(class_scope:garrison_server.KeySetResponse)
  })
_sym_db.RegisterMessage(KeySetResponse)

KeyGetRequest = _reflection.GeneratedProtocolMessageType('KeyGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _KEYGETREQUEST,
  '__module__' : 'garrison_pb2'
  # @@protoc_insertion_point(class_scope:garrison_server.KeyGetRequest)
  })
_sym_db.RegisterMessage(KeyGetRequest)

KeyGetResponse = _reflection.GeneratedProtocolMessageType('KeyGetResponse', (_message.Message,), {
  'DESCRIPTOR' : _KEYGETRESPONSE,
  '__module__' : 'garrison_pb2'
  # @@protoc_insertion_point(class_scope:garrison_server.KeyGetResponse)
  })
_sym_db.RegisterMessage(KeyGetResponse)

KeyDeleteRequest = _reflection.GeneratedProtocolMessageType('KeyDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _KEYDELETEREQUEST,
  '__module__' : 'garrison_pb2'
  # @@protoc_insertion_point(class_scope:garrison_server.KeyDeleteRequest)
  })
_sym_db.RegisterMessage(KeyDeleteRequest)

KeyDeleteResponse = _reflection.GeneratedProtocolMessageType('KeyDeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _KEYDELETERESPONSE,
  '__module__' : 'garrison_pb2'
  # @@protoc_insertion_point(class_scope:garrison_server.KeyDeleteResponse)
  })
_sym_db.RegisterMessage(KeyDeleteResponse)

QueuePopRequest = _reflection.GeneratedProtocolMessageType('QueuePopRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUEUEPOPREQUEST,
  '__module__' : 'garrison_pb2'
  # @@protoc_insertion_point(class_scope:garrison_server.QueuePopRequest)
  })
_sym_db.RegisterMessage(QueuePopRequest)

QueuePopResponse = _reflection.GeneratedProtocolMessageType('QueuePopResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUEUEPOPRESPONSE,
  '__module__' : 'garrison_pb2'
  # @@protoc_insertion_point(class_scope:garrison_server.QueuePopResponse)
  })
_sym_db.RegisterMessage(QueuePopResponse)

QueuePushRequest = _reflection.GeneratedProtocolMessageType('QueuePushRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUEUEPUSHREQUEST,
  '__module__' : 'garrison_pb2'
  # @@protoc_insertion_point(class_scope:garrison_server.QueuePushRequest)
  })
_sym_db.RegisterMessage(QueuePushRequest)

QueuePushResponse = _reflection.GeneratedProtocolMessageType('QueuePushResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUEUEPUSHRESPONSE,
  '__module__' : 'garrison_pb2'
  # @@protoc_insertion_point(class_scope:garrison_server.QueuePushResponse)
  })
_sym_db.RegisterMessage(QueuePushResponse)

QueueDeleteRequest = _reflection.GeneratedProtocolMessageType('QueueDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUEUEDELETEREQUEST,
  '__module__' : 'garrison_pb2'
  # @@protoc_insertion_point(class_scope:garrison_server.QueueDeleteRequest)
  })
_sym_db.RegisterMessage(QueueDeleteRequest)

QueueDeleteResponse = _reflection.GeneratedProtocolMessageType('QueueDeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUEUEDELETERESPONSE,
  '__module__' : 'garrison_pb2'
  # @@protoc_insertion_point(class_scope:garrison_server.QueueDeleteResponse)
  })
_sym_db.RegisterMessage(QueueDeleteResponse)

QueueLengthRequest = _reflection.GeneratedProtocolMessageType('QueueLengthRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUEUELENGTHREQUEST,
  '__module__' : 'garrison_pb2'
  # @@protoc_insertion_point(class_scope:garrison_server.QueueLengthRequest)
  })
_sym_db.RegisterMessage(QueueLengthRequest)

QueueLengthResponse = _reflection.GeneratedProtocolMessageType('QueueLengthResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUEUELENGTHRESPONSE,
  '__module__' : 'garrison_pb2'
  # @@protoc_insertion_point(class_scope:garrison_server.QueueLengthResponse)
  })
_sym_db.RegisterMessage(QueueLengthResponse)



_GARRISONSERVER = _descriptor.ServiceDescriptor(
  name='GarrisonServer',
  full_name='garrison_server.GarrisonServer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=673,
  serialized_end=1289,
  methods=[
  _descriptor.MethodDescriptor(
    name='key_set',
    full_name='garrison_server.GarrisonServer.key_set',
    index=0,
    containing_service=None,
    input_type=_KEYSETREQUEST,
    output_type=_KEYSETRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='key_get',
    full_name='garrison_server.GarrisonServer.key_get',
    index=1,
    containing_service=None,
    input_type=_KEYGETREQUEST,
    output_type=_KEYGETRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='key_delete',
    full_name='garrison_server.GarrisonServer.key_delete',
    index=2,
    containing_service=None,
    input_type=_KEYDELETEREQUEST,
    output_type=_KEYDELETERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='queue_pop',
    full_name='garrison_server.GarrisonServer.queue_pop',
    index=3,
    containing_service=None,
    input_type=_QUEUEPOPREQUEST,
    output_type=_QUEUEPOPRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='queue_push',
    full_name='garrison_server.GarrisonServer.queue_push',
    index=4,
    containing_service=None,
    input_type=_QUEUEPUSHREQUEST,
    output_type=_QUEUEPUSHRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='queue_delete',
    full_name='garrison_server.GarrisonServer.queue_delete',
    index=5,
    containing_service=None,
    input_type=_QUEUEDELETEREQUEST,
    output_type=_QUEUEDELETERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='queue_length',
    full_name='garrison_server.GarrisonServer.queue_length',
    index=6,
    containing_service=None,
    input_type=_QUEUELENGTHREQUEST,
    output_type=_QUEUELENGTHRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GARRISONSERVER)

DESCRIPTOR.services_by_name['GarrisonServer'] = _GARRISONSERVER

# @@protoc_insertion_point(module_scope)