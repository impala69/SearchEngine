# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sample.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sample.proto',
  package='sample',
  serialized_pb=_b('\n\x0csample.proto\x12\x06sample\"N\n\x04\x44\x61ta\x12\'\n\x0brepeatLinks\x18\x01 \x03(\x0b\x32\x12.sample.Data.Links\x1a\x1d\n\x05Links\x12\x14\n\x0c\x63ontainLinks\x18\x01 \x02(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DATA_LINKS = _descriptor.Descriptor(
  name='Links',
  full_name='sample.Data.Links',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='containLinks', full_name='sample.Data.Links.containLinks', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=73,
  serialized_end=102,
)

_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='sample.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='repeatLinks', full_name='sample.Data.repeatLinks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_DATA_LINKS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=102,
)

_DATA_LINKS.containing_type = _DATA
_DATA.fields_by_name['repeatLinks'].message_type = _DATA_LINKS
DESCRIPTOR.message_types_by_name['Data'] = _DATA

Data = _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), dict(

  Links = _reflection.GeneratedProtocolMessageType('Links', (_message.Message,), dict(
    DESCRIPTOR = _DATA_LINKS,
    __module__ = 'sample_pb2'
    # @@protoc_insertion_point(class_scope:sample.Data.Links)
    ))
  ,
  DESCRIPTOR = _DATA,
  __module__ = 'sample_pb2'
  # @@protoc_insertion_point(class_scope:sample.Data)
  ))
_sym_db.RegisterMessage(Data)
_sym_db.RegisterMessage(Data.Links)


# @@protoc_insertion_point(module_scope)
