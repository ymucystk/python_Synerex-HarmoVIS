# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/geography/geography.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/geography/geography.proto',
  package='pagent',
  syntax='proto3',
  serialized_options=b'Z\"github.com/synerex/proto_geography',
  serialized_pb=b'\n\x1fproto/geography/geography.proto\x12\x06pagent\x1a\x1fgoogle/protobuf/timestamp.proto\"M\n\x03Geo\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x05\x12\r\n\x05label\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\x0c\x12\x0f\n\x07options\x18\x05 \x01(\t\" \n\x04Line\x12\x0c\n\x04\x66rom\x18\x01 \x03(\x01\x12\n\n\x02to\x18\x02 \x03(\x01\"B\n\x05Lines\x12\x1b\n\x05lines\x18\x01 \x03(\x0b\x32\x0c.pagent.Line\x12\r\n\x05width\x18\x02 \x01(\x05\x12\r\n\x05\x63olor\x18\x03 \x03(\x05\"!\n\x05Point\x12\x0b\n\x03lat\x18\x01 \x01(\x01\x12\x0b\n\x03lon\x18\x02 \x01(\x01\"C\n\x04Path\x12\x1d\n\x06points\x18\x01 \x03(\x0b\x32\r.pagent.Point\x12\r\n\x05width\x18\x02 \x01(\x05\x12\r\n\x05\x63olor\x18\x03 \x03(\x05\"$\n\x05Paths\x12\x1b\n\x05paths\x18\x01 \x03(\x0b\x32\x0c.pagent.Path\"I\n\x07Scatter\x12\x1d\n\x06points\x18\x01 \x03(\x0b\x32\r.pagent.Point\x12\x10\n\x08radiuses\x18\x02 \x03(\x05\x12\r\n\x05\x63olor\x18\x03 \x03(\x05\"B\n\tViewState\x12\x0b\n\x03lat\x18\x01 \x01(\x01\x12\x0b\n\x03lon\x18\x02 \x01(\x01\x12\x0c\n\x04zoom\x18\x03 \x01(\x05\x12\r\n\x05pitch\x18\x04 \x01(\x01\"\x1a\n\x07\x42\x65\x61ring\x12\x0f\n\x07\x62\x65\x61ring\x18\x01 \x01(\x01\"\x16\n\x05Pitch\x12\r\n\x05pitch\x18\x01 \x01(\x01\"\x1d\n\nClearMoves\x12\x0f\n\x07message\x18\x01 \x01(\t\"6\n\x07\x42\x61rData\x12\r\n\x05label\x18\x01 \x01(\t\x12\r\n\x05\x63olor\x18\x03 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x01\"\xb5\x02\n\x08\x42\x61rGraph\x12\n\n\x02id\x18\x01 \x01(\x05\x12&\n\x02ts\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\'\n\tshapeType\x18\x03 \x01(\x0e\x32\x14.pagent.BarShapeType\x12\'\n\tcolorType\x18\x04 \x01(\x0e\x32\x14.pagent.BarColorType\x12\r\n\x05\x63olor\x18\x05 \x01(\x05\x12\x0b\n\x03lat\x18\x06 \x01(\x01\x12\x0b\n\x03lon\x18\x07 \x01(\x01\x12\r\n\x05width\x18\x08 \x01(\x01\x12\x0e\n\x06radius\x18\t \x01(\x01\x12\x0b\n\x03min\x18\n \x01(\x01\x12\x0b\n\x03max\x18\x0b \x01(\x01\x12\x11\n\tareaColor\x18\x0c \x01(\x05\x12 \n\x07\x62\x61rData\x18\r \x03(\x0b\x32\x0f.pagent.BarData\x12\x0c\n\x04text\x18\x0e \x01(\t\"+\n\tBarGraphs\x12\x1e\n\x04\x62\x61rs\x18\x01 \x03(\x0b\x32\x10.pagent.BarGraph**\n\x0c\x42\x61rColorType\x12\x0c\n\x08\x46IXCOLOR\x10\x00\x12\x0c\n\x08VARCOLOR\x10\x01* \n\x0c\x42\x61rShapeType\x12\x07\n\x03\x42OX\x10\x00\x12\x07\n\x03HEX\x10\x01\x42$Z\"github.com/synerex/proto_geographyb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])

_BARCOLORTYPE = _descriptor.EnumDescriptor(
  name='BarColorType',
  full_name='pagent.BarColorType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FIXCOLOR', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VARCOLOR', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1038,
  serialized_end=1080,
)
_sym_db.RegisterEnumDescriptor(_BARCOLORTYPE)

BarColorType = enum_type_wrapper.EnumTypeWrapper(_BARCOLORTYPE)
_BARSHAPETYPE = _descriptor.EnumDescriptor(
  name='BarShapeType',
  full_name='pagent.BarShapeType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BOX', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HEX', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1082,
  serialized_end=1114,
)
_sym_db.RegisterEnumDescriptor(_BARSHAPETYPE)

BarShapeType = enum_type_wrapper.EnumTypeWrapper(_BARSHAPETYPE)
FIXCOLOR = 0
VARCOLOR = 1
BOX = 0
HEX = 1



_GEO = _descriptor.Descriptor(
  name='Geo',
  full_name='pagent.Geo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='pagent.Geo.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='pagent.Geo.id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='label', full_name='pagent.Geo.label', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='pagent.Geo.data', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='options', full_name='pagent.Geo.options', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=76,
  serialized_end=153,
)


_LINE = _descriptor.Descriptor(
  name='Line',
  full_name='pagent.Line',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='from', full_name='pagent.Line.from', index=0,
      number=1, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='to', full_name='pagent.Line.to', index=1,
      number=2, type=1, cpp_type=5, label=3,
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
  serialized_start=155,
  serialized_end=187,
)


_LINES = _descriptor.Descriptor(
  name='Lines',
  full_name='pagent.Lines',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lines', full_name='pagent.Lines.lines', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='pagent.Lines.width', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='color', full_name='pagent.Lines.color', index=2,
      number=3, type=5, cpp_type=1, label=3,
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
  serialized_start=189,
  serialized_end=255,
)


_POINT = _descriptor.Descriptor(
  name='Point',
  full_name='pagent.Point',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lat', full_name='pagent.Point.lat', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lon', full_name='pagent.Point.lon', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=257,
  serialized_end=290,
)


_PATH = _descriptor.Descriptor(
  name='Path',
  full_name='pagent.Path',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='points', full_name='pagent.Path.points', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='pagent.Path.width', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='color', full_name='pagent.Path.color', index=2,
      number=3, type=5, cpp_type=1, label=3,
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
  serialized_start=292,
  serialized_end=359,
)


_PATHS = _descriptor.Descriptor(
  name='Paths',
  full_name='pagent.Paths',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='paths', full_name='pagent.Paths.paths', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=361,
  serialized_end=397,
)


_SCATTER = _descriptor.Descriptor(
  name='Scatter',
  full_name='pagent.Scatter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='points', full_name='pagent.Scatter.points', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='radiuses', full_name='pagent.Scatter.radiuses', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='color', full_name='pagent.Scatter.color', index=2,
      number=3, type=5, cpp_type=1, label=3,
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
  serialized_start=399,
  serialized_end=472,
)


_VIEWSTATE = _descriptor.Descriptor(
  name='ViewState',
  full_name='pagent.ViewState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lat', full_name='pagent.ViewState.lat', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lon', full_name='pagent.ViewState.lon', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zoom', full_name='pagent.ViewState.zoom', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pitch', full_name='pagent.ViewState.pitch', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=474,
  serialized_end=540,
)


_BEARING = _descriptor.Descriptor(
  name='Bearing',
  full_name='pagent.Bearing',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bearing', full_name='pagent.Bearing.bearing', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=542,
  serialized_end=568,
)


_PITCH = _descriptor.Descriptor(
  name='Pitch',
  full_name='pagent.Pitch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pitch', full_name='pagent.Pitch.pitch', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=570,
  serialized_end=592,
)


_CLEARMOVES = _descriptor.Descriptor(
  name='ClearMoves',
  full_name='pagent.ClearMoves',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='pagent.ClearMoves.message', index=0,
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
  serialized_start=594,
  serialized_end=623,
)


_BARDATA = _descriptor.Descriptor(
  name='BarData',
  full_name='pagent.BarData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='pagent.BarData.label', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='color', full_name='pagent.BarData.color', index=1,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='pagent.BarData.value', index=2,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=625,
  serialized_end=679,
)


_BARGRAPH = _descriptor.Descriptor(
  name='BarGraph',
  full_name='pagent.BarGraph',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='pagent.BarGraph.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ts', full_name='pagent.BarGraph.ts', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shapeType', full_name='pagent.BarGraph.shapeType', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='colorType', full_name='pagent.BarGraph.colorType', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='color', full_name='pagent.BarGraph.color', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lat', full_name='pagent.BarGraph.lat', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lon', full_name='pagent.BarGraph.lon', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='pagent.BarGraph.width', index=7,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='radius', full_name='pagent.BarGraph.radius', index=8,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min', full_name='pagent.BarGraph.min', index=9,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max', full_name='pagent.BarGraph.max', index=10,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='areaColor', full_name='pagent.BarGraph.areaColor', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='barData', full_name='pagent.BarGraph.barData', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='pagent.BarGraph.text', index=13,
      number=14, type=9, cpp_type=9, label=1,
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
  serialized_start=682,
  serialized_end=991,
)


_BARGRAPHS = _descriptor.Descriptor(
  name='BarGraphs',
  full_name='pagent.BarGraphs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bars', full_name='pagent.BarGraphs.bars', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=993,
  serialized_end=1036,
)

_LINES.fields_by_name['lines'].message_type = _LINE
_PATH.fields_by_name['points'].message_type = _POINT
_PATHS.fields_by_name['paths'].message_type = _PATH
_SCATTER.fields_by_name['points'].message_type = _POINT
_BARGRAPH.fields_by_name['ts'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_BARGRAPH.fields_by_name['shapeType'].enum_type = _BARSHAPETYPE
_BARGRAPH.fields_by_name['colorType'].enum_type = _BARCOLORTYPE
_BARGRAPH.fields_by_name['barData'].message_type = _BARDATA
_BARGRAPHS.fields_by_name['bars'].message_type = _BARGRAPH
DESCRIPTOR.message_types_by_name['Geo'] = _GEO
DESCRIPTOR.message_types_by_name['Line'] = _LINE
DESCRIPTOR.message_types_by_name['Lines'] = _LINES
DESCRIPTOR.message_types_by_name['Point'] = _POINT
DESCRIPTOR.message_types_by_name['Path'] = _PATH
DESCRIPTOR.message_types_by_name['Paths'] = _PATHS
DESCRIPTOR.message_types_by_name['Scatter'] = _SCATTER
DESCRIPTOR.message_types_by_name['ViewState'] = _VIEWSTATE
DESCRIPTOR.message_types_by_name['Bearing'] = _BEARING
DESCRIPTOR.message_types_by_name['Pitch'] = _PITCH
DESCRIPTOR.message_types_by_name['ClearMoves'] = _CLEARMOVES
DESCRIPTOR.message_types_by_name['BarData'] = _BARDATA
DESCRIPTOR.message_types_by_name['BarGraph'] = _BARGRAPH
DESCRIPTOR.message_types_by_name['BarGraphs'] = _BARGRAPHS
DESCRIPTOR.enum_types_by_name['BarColorType'] = _BARCOLORTYPE
DESCRIPTOR.enum_types_by_name['BarShapeType'] = _BARSHAPETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Geo = _reflection.GeneratedProtocolMessageType('Geo', (_message.Message,), {
  'DESCRIPTOR' : _GEO,
  '__module__' : 'proto.geography.geography_pb2'
  # @@protoc_insertion_point(class_scope:pagent.Geo)
  })
_sym_db.RegisterMessage(Geo)

Line = _reflection.GeneratedProtocolMessageType('Line', (_message.Message,), {
  'DESCRIPTOR' : _LINE,
  '__module__' : 'proto.geography.geography_pb2'
  # @@protoc_insertion_point(class_scope:pagent.Line)
  })
_sym_db.RegisterMessage(Line)

Lines = _reflection.GeneratedProtocolMessageType('Lines', (_message.Message,), {
  'DESCRIPTOR' : _LINES,
  '__module__' : 'proto.geography.geography_pb2'
  # @@protoc_insertion_point(class_scope:pagent.Lines)
  })
_sym_db.RegisterMessage(Lines)

Point = _reflection.GeneratedProtocolMessageType('Point', (_message.Message,), {
  'DESCRIPTOR' : _POINT,
  '__module__' : 'proto.geography.geography_pb2'
  # @@protoc_insertion_point(class_scope:pagent.Point)
  })
_sym_db.RegisterMessage(Point)

Path = _reflection.GeneratedProtocolMessageType('Path', (_message.Message,), {
  'DESCRIPTOR' : _PATH,
  '__module__' : 'proto.geography.geography_pb2'
  # @@protoc_insertion_point(class_scope:pagent.Path)
  })
_sym_db.RegisterMessage(Path)

Paths = _reflection.GeneratedProtocolMessageType('Paths', (_message.Message,), {
  'DESCRIPTOR' : _PATHS,
  '__module__' : 'proto.geography.geography_pb2'
  # @@protoc_insertion_point(class_scope:pagent.Paths)
  })
_sym_db.RegisterMessage(Paths)

Scatter = _reflection.GeneratedProtocolMessageType('Scatter', (_message.Message,), {
  'DESCRIPTOR' : _SCATTER,
  '__module__' : 'proto.geography.geography_pb2'
  # @@protoc_insertion_point(class_scope:pagent.Scatter)
  })
_sym_db.RegisterMessage(Scatter)

ViewState = _reflection.GeneratedProtocolMessageType('ViewState', (_message.Message,), {
  'DESCRIPTOR' : _VIEWSTATE,
  '__module__' : 'proto.geography.geography_pb2'
  # @@protoc_insertion_point(class_scope:pagent.ViewState)
  })
_sym_db.RegisterMessage(ViewState)

Bearing = _reflection.GeneratedProtocolMessageType('Bearing', (_message.Message,), {
  'DESCRIPTOR' : _BEARING,
  '__module__' : 'proto.geography.geography_pb2'
  # @@protoc_insertion_point(class_scope:pagent.Bearing)
  })
_sym_db.RegisterMessage(Bearing)

Pitch = _reflection.GeneratedProtocolMessageType('Pitch', (_message.Message,), {
  'DESCRIPTOR' : _PITCH,
  '__module__' : 'proto.geography.geography_pb2'
  # @@protoc_insertion_point(class_scope:pagent.Pitch)
  })
_sym_db.RegisterMessage(Pitch)

ClearMoves = _reflection.GeneratedProtocolMessageType('ClearMoves', (_message.Message,), {
  'DESCRIPTOR' : _CLEARMOVES,
  '__module__' : 'proto.geography.geography_pb2'
  # @@protoc_insertion_point(class_scope:pagent.ClearMoves)
  })
_sym_db.RegisterMessage(ClearMoves)

BarData = _reflection.GeneratedProtocolMessageType('BarData', (_message.Message,), {
  'DESCRIPTOR' : _BARDATA,
  '__module__' : 'proto.geography.geography_pb2'
  # @@protoc_insertion_point(class_scope:pagent.BarData)
  })
_sym_db.RegisterMessage(BarData)

BarGraph = _reflection.GeneratedProtocolMessageType('BarGraph', (_message.Message,), {
  'DESCRIPTOR' : _BARGRAPH,
  '__module__' : 'proto.geography.geography_pb2'
  # @@protoc_insertion_point(class_scope:pagent.BarGraph)
  })
_sym_db.RegisterMessage(BarGraph)

BarGraphs = _reflection.GeneratedProtocolMessageType('BarGraphs', (_message.Message,), {
  'DESCRIPTOR' : _BARGRAPHS,
  '__module__' : 'proto.geography.geography_pb2'
  # @@protoc_insertion_point(class_scope:pagent.BarGraphs)
  })
_sym_db.RegisterMessage(BarGraphs)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
