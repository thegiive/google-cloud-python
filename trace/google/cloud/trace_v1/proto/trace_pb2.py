# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/devtools/cloudtrace_v1/proto/trace.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/devtools/cloudtrace_v1/proto/trace.proto',
  package='google.devtools.cloudtrace.v1',
  syntax='proto3',
  serialized_pb=_b('\n/google/devtools/cloudtrace_v1/proto/trace.proto\x12\x1dgoogle.devtools.cloudtrace.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"f\n\x05Trace\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x10\n\x08trace_id\x18\x02 \x01(\t\x12\x37\n\x05spans\x18\x03 \x03(\x0b\x32(.google.devtools.cloudtrace.v1.TraceSpan\">\n\x06Traces\x12\x34\n\x06traces\x18\x01 \x03(\x0b\x32$.google.devtools.cloudtrace.v1.Trace\"\x9d\x03\n\tTraceSpan\x12\x0f\n\x07span_id\x18\x01 \x01(\x06\x12?\n\x04kind\x18\x02 \x01(\x0e\x32\x31.google.devtools.cloudtrace.v1.TraceSpan.SpanKind\x12\x0c\n\x04name\x18\x03 \x01(\t\x12.\n\nstart_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x16\n\x0eparent_span_id\x18\x06 \x01(\x06\x12\x44\n\x06labels\x18\x07 \x03(\x0b\x32\x34.google.devtools.cloudtrace.v1.TraceSpan.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"E\n\x08SpanKind\x12\x19\n\x15SPAN_KIND_UNSPECIFIED\x10\x00\x12\x0e\n\nRPC_SERVER\x10\x01\x12\x0e\n\nRPC_CLIENT\x10\x02\"\xe7\x02\n\x11ListTracesRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12G\n\x04view\x18\x02 \x01(\x0e\x32\x39.google.devtools.cloudtrace.v1.ListTracesRequest.ViewType\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12.\n\nstart_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06\x66ilter\x18\x07 \x01(\t\x12\x10\n\x08order_by\x18\x08 \x01(\t\"N\n\x08ViewType\x12\x19\n\x15VIEW_TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07MINIMAL\x10\x01\x12\x0c\n\x08ROOTSPAN\x10\x02\x12\x0c\n\x08\x43OMPLETE\x10\x03\"c\n\x12ListTracesResponse\x12\x34\n\x06traces\x18\x01 \x03(\x0b\x32$.google.devtools.cloudtrace.v1.Trace\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"7\n\x0fGetTraceRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x10\n\x08trace_id\x18\x02 \x01(\t\"_\n\x12PatchTracesRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x35\n\x06traces\x18\x02 \x01(\x0b\x32%.google.devtools.cloudtrace.v1.Traces2\xd1\x03\n\x0cTraceService\x12\x9b\x01\n\nListTraces\x12\x30.google.devtools.cloudtrace.v1.ListTracesRequest\x1a\x31.google.devtools.cloudtrace.v1.ListTracesResponse\"(\x82\xd3\xe4\x93\x02\"\x12 /v1/projects/{project_id}/traces\x12\x95\x01\n\x08GetTrace\x12..google.devtools.cloudtrace.v1.GetTraceRequest\x1a$.google.devtools.cloudtrace.v1.Trace\"3\x82\xd3\xe4\x93\x02-\x12+/v1/projects/{project_id}/traces/{trace_id}\x12\x8a\x01\n\x0bPatchTraces\x12\x31.google.devtools.cloudtrace.v1.PatchTracesRequest\x1a\x16.google.protobuf.Empty\"0\x82\xd3\xe4\x93\x02*2 /v1/projects/{project_id}/traces:\x06tracesB\xaa\x01\n!com.google.devtools.cloudtrace.v1B\nTraceProtoP\x01ZGgoogle.golang.org/genproto/googleapis/devtools/cloudtrace/v1;cloudtrace\xaa\x02\x15Google.Cloud.Trace.V1\xca\x02\x15Google\\Cloud\\Trace\\V1b\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])



_TRACESPAN_SPANKIND = _descriptor.EnumDescriptor(
  name='SpanKind',
  full_name='google.devtools.cloudtrace.v1.TraceSpan.SpanKind',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SPAN_KIND_UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RPC_SERVER', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RPC_CLIENT', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=687,
  serialized_end=756,
)
_sym_db.RegisterEnumDescriptor(_TRACESPAN_SPANKIND)

_LISTTRACESREQUEST_VIEWTYPE = _descriptor.EnumDescriptor(
  name='ViewType',
  full_name='google.devtools.cloudtrace.v1.ListTracesRequest.ViewType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='VIEW_TYPE_UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MINIMAL', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROOTSPAN', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPLETE', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1040,
  serialized_end=1118,
)
_sym_db.RegisterEnumDescriptor(_LISTTRACESREQUEST_VIEWTYPE)


_TRACE = _descriptor.Descriptor(
  name='Trace',
  full_name='google.devtools.cloudtrace.v1.Trace',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='project_id', full_name='google.devtools.cloudtrace.v1.Trace.project_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trace_id', full_name='google.devtools.cloudtrace.v1.Trace.trace_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spans', full_name='google.devtools.cloudtrace.v1.Trace.spans', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=174,
  serialized_end=276,
)


_TRACES = _descriptor.Descriptor(
  name='Traces',
  full_name='google.devtools.cloudtrace.v1.Traces',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='traces', full_name='google.devtools.cloudtrace.v1.Traces.traces', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=278,
  serialized_end=340,
)


_TRACESPAN_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='google.devtools.cloudtrace.v1.TraceSpan.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.devtools.cloudtrace.v1.TraceSpan.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.devtools.cloudtrace.v1.TraceSpan.LabelsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=640,
  serialized_end=685,
)

_TRACESPAN = _descriptor.Descriptor(
  name='TraceSpan',
  full_name='google.devtools.cloudtrace.v1.TraceSpan',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='span_id', full_name='google.devtools.cloudtrace.v1.TraceSpan.span_id', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kind', full_name='google.devtools.cloudtrace.v1.TraceSpan.kind', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.devtools.cloudtrace.v1.TraceSpan.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='google.devtools.cloudtrace.v1.TraceSpan.start_time', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='google.devtools.cloudtrace.v1.TraceSpan.end_time', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parent_span_id', full_name='google.devtools.cloudtrace.v1.TraceSpan.parent_span_id', index=5,
      number=6, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='google.devtools.cloudtrace.v1.TraceSpan.labels', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TRACESPAN_LABELSENTRY, ],
  enum_types=[
    _TRACESPAN_SPANKIND,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=343,
  serialized_end=756,
)


_LISTTRACESREQUEST = _descriptor.Descriptor(
  name='ListTracesRequest',
  full_name='google.devtools.cloudtrace.v1.ListTracesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='project_id', full_name='google.devtools.cloudtrace.v1.ListTracesRequest.project_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='view', full_name='google.devtools.cloudtrace.v1.ListTracesRequest.view', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='google.devtools.cloudtrace.v1.ListTracesRequest.page_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.devtools.cloudtrace.v1.ListTracesRequest.page_token', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='google.devtools.cloudtrace.v1.ListTracesRequest.start_time', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='google.devtools.cloudtrace.v1.ListTracesRequest.end_time', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter', full_name='google.devtools.cloudtrace.v1.ListTracesRequest.filter', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order_by', full_name='google.devtools.cloudtrace.v1.ListTracesRequest.order_by', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LISTTRACESREQUEST_VIEWTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=759,
  serialized_end=1118,
)


_LISTTRACESRESPONSE = _descriptor.Descriptor(
  name='ListTracesResponse',
  full_name='google.devtools.cloudtrace.v1.ListTracesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='traces', full_name='google.devtools.cloudtrace.v1.ListTracesResponse.traces', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='google.devtools.cloudtrace.v1.ListTracesResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1120,
  serialized_end=1219,
)


_GETTRACEREQUEST = _descriptor.Descriptor(
  name='GetTraceRequest',
  full_name='google.devtools.cloudtrace.v1.GetTraceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='project_id', full_name='google.devtools.cloudtrace.v1.GetTraceRequest.project_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trace_id', full_name='google.devtools.cloudtrace.v1.GetTraceRequest.trace_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1221,
  serialized_end=1276,
)


_PATCHTRACESREQUEST = _descriptor.Descriptor(
  name='PatchTracesRequest',
  full_name='google.devtools.cloudtrace.v1.PatchTracesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='project_id', full_name='google.devtools.cloudtrace.v1.PatchTracesRequest.project_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='traces', full_name='google.devtools.cloudtrace.v1.PatchTracesRequest.traces', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1278,
  serialized_end=1373,
)

_TRACE.fields_by_name['spans'].message_type = _TRACESPAN
_TRACES.fields_by_name['traces'].message_type = _TRACE
_TRACESPAN_LABELSENTRY.containing_type = _TRACESPAN
_TRACESPAN.fields_by_name['kind'].enum_type = _TRACESPAN_SPANKIND
_TRACESPAN.fields_by_name['start_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TRACESPAN.fields_by_name['end_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TRACESPAN.fields_by_name['labels'].message_type = _TRACESPAN_LABELSENTRY
_TRACESPAN_SPANKIND.containing_type = _TRACESPAN
_LISTTRACESREQUEST.fields_by_name['view'].enum_type = _LISTTRACESREQUEST_VIEWTYPE
_LISTTRACESREQUEST.fields_by_name['start_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LISTTRACESREQUEST.fields_by_name['end_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LISTTRACESREQUEST_VIEWTYPE.containing_type = _LISTTRACESREQUEST
_LISTTRACESRESPONSE.fields_by_name['traces'].message_type = _TRACE
_PATCHTRACESREQUEST.fields_by_name['traces'].message_type = _TRACES
DESCRIPTOR.message_types_by_name['Trace'] = _TRACE
DESCRIPTOR.message_types_by_name['Traces'] = _TRACES
DESCRIPTOR.message_types_by_name['TraceSpan'] = _TRACESPAN
DESCRIPTOR.message_types_by_name['ListTracesRequest'] = _LISTTRACESREQUEST
DESCRIPTOR.message_types_by_name['ListTracesResponse'] = _LISTTRACESRESPONSE
DESCRIPTOR.message_types_by_name['GetTraceRequest'] = _GETTRACEREQUEST
DESCRIPTOR.message_types_by_name['PatchTracesRequest'] = _PATCHTRACESREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Trace = _reflection.GeneratedProtocolMessageType('Trace', (_message.Message,), dict(
  DESCRIPTOR = _TRACE,
  __module__ = 'google.devtools.cloudtrace_v1.proto.trace_pb2'
  ,
  __doc__ = """A trace describes how long it takes for an application to perform an
  operation. It consists of a set of spans, each of which represent a
  single timed event within the operation.
  
  
  Attributes:
      project_id:
          Project ID of the Cloud project where the trace data is
          stored.
      trace_id:
          Globally unique identifier for the trace. This identifier is a
          128-bit numeric value formatted as a 32-byte hex string.
      spans:
          Collection of spans in the trace.
  """,
  # @@protoc_insertion_point(class_scope:google.devtools.cloudtrace.v1.Trace)
  ))
_sym_db.RegisterMessage(Trace)

Traces = _reflection.GeneratedProtocolMessageType('Traces', (_message.Message,), dict(
  DESCRIPTOR = _TRACES,
  __module__ = 'google.devtools.cloudtrace_v1.proto.trace_pb2'
  ,
  __doc__ = """List of new or updated traces.
  
  
  Attributes:
      traces:
          List of traces.
  """,
  # @@protoc_insertion_point(class_scope:google.devtools.cloudtrace.v1.Traces)
  ))
_sym_db.RegisterMessage(Traces)

TraceSpan = _reflection.GeneratedProtocolMessageType('TraceSpan', (_message.Message,), dict(

  LabelsEntry = _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), dict(
    DESCRIPTOR = _TRACESPAN_LABELSENTRY,
    __module__ = 'google.devtools.cloudtrace_v1.proto.trace_pb2'
    # @@protoc_insertion_point(class_scope:google.devtools.cloudtrace.v1.TraceSpan.LabelsEntry)
    ))
  ,
  DESCRIPTOR = _TRACESPAN,
  __module__ = 'google.devtools.cloudtrace_v1.proto.trace_pb2'
  ,
  __doc__ = """A span represents a single timed event within a trace. Spans can be
  nested and form a trace tree. Often, a trace contains a root span that
  describes the end-to-end latency of an operation and, optionally, one or
  more subspans for its suboperations. Spans do not need to be contiguous.
  There may be gaps between spans in a trace.
  
  
  Attributes:
      span_id:
          Identifier for the span. Must be a 64-bit integer other than 0
          and unique within a trace.
      kind:
          Distinguishes between spans generated in a particular context.
          For example, two spans with the same name may be distinguished
          using ``RPC_CLIENT`` and ``RPC_SERVER`` to identify queueing
          latency associated with the span.
      name:
          Name of the span. Must be less than 128 bytes. The span name
          is sanitized and displayed in the Stackdriver Trace tool in
          the {% dynamic print site\_values.console\_name %}. The name
          may be a method name or some other per-call site name. For the
          same executable and the same call point, a best practice is to
          use a consistent name, which makes it easier to correlate
          cross-trace spans.
      start_time:
          Start time of the span in nanoseconds from the UNIX epoch.
      end_time:
          End time of the span in nanoseconds from the UNIX epoch.
      parent_span_id:
          ID of the parent span, if any. Optional.
      labels:
          Collection of labels associated with the span. Label keys must
          be less than 128 bytes. Label values must be less than 16
          kilobytes (10MB for ``/stacktrace`` values).  Some predefined
          label keys exist, or you may create your own. When creating
          your own, we recommend the following formats:  -
          ``/category/product/key`` for agents of well-known products
          (e.g.    ``/db/mongodb/read_size``). -
          ``short_host/path/key`` for domain-specific keys (e.g.
          ``foo.com/myproduct/bar``)  Predefined labels include:  -
          ``/agent`` -  ``/component`` -  ``/error/message`` -
          ``/error/name`` -  ``/http/client_city`` -
          ``/http/client_country`` -  ``/http/client_protocol`` -
          ``/http/client_region`` -  ``/http/host`` -  ``/http/method``
          -  ``/http/path`` -  ``/http/redirected_url`` -
          ``/http/request/size`` -  ``/http/response/size`` -
          ``/http/route`` -  ``/http/status_code`` -  ``/http/url`` -
          ``/http/user_agent`` -  ``/pid`` -  ``/stacktrace`` -
          ``/tid``
  """,
  # @@protoc_insertion_point(class_scope:google.devtools.cloudtrace.v1.TraceSpan)
  ))
_sym_db.RegisterMessage(TraceSpan)
_sym_db.RegisterMessage(TraceSpan.LabelsEntry)

ListTracesRequest = _reflection.GeneratedProtocolMessageType('ListTracesRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTTRACESREQUEST,
  __module__ = 'google.devtools.cloudtrace_v1.proto.trace_pb2'
  ,
  __doc__ = """The request message for the ``ListTraces`` method. All fields are
  required unless specified.
  
  
  Attributes:
      project_id:
          ID of the Cloud project where the trace data is stored.
      view:
          Type of data returned for traces in the list. Optional.
          Default is ``MINIMAL``.
      page_size:
          Maximum number of traces to return. If not specified or <= 0,
          the implementation selects a reasonable value. The
          implementation may return fewer traces than the requested page
          size. Optional.
      page_token:
          Token identifying the page of results to return. If provided,
          use the value of the ``next_page_token`` field from a previous
          request. Optional.
      start_time:
          Start of the time interval (inclusive) during which the trace
          data was collected from the application.
      end_time:
          End of the time interval (inclusive) during which the trace
          data was collected from the application.
      filter:
          An optional filter against labels for the request.  By
          default, searches use prefix matching. To specify exact match,
          prepend a plus symbol (``+``) to the search term. Multiple
          terms are ANDed. Syntax:  -  ``root:NAME_PREFIX`` or
          ``NAME_PREFIX``: Return traces where any root    span starts
          with ``NAME_PREFIX``. -  ``+root:NAME`` or ``+NAME``: Return
          traces where any root span's name    is exactly ``NAME``. -
          ``span:NAME_PREFIX``: Return traces where any span starts with
          ``NAME_PREFIX``. -  ``+span:NAME``: Return traces where any
          span's name is exactly    ``NAME``. -  ``latency:DURATION``:
          Return traces whose overall latency is greater    or equal to
          than ``DURATION``. Accepted units are nanoseconds    (``ns``),
          milliseconds (``ms``), and seconds (``s``). Default is
          ``ms``. For example, ``latency:24ms`` returns traces whose
          overall    latency is greater than or equal to 24
          milliseconds. -  ``label:LABEL_KEY``: Return all traces
          containing the specified label    key (exact match, case-
          sensitive) regardless of the key:value pair's    value
          (including empty values). -  ``LABEL_KEY:VALUE_PREFIX``:
          Return all traces containing the    specified label key (exact
          match, case-sensitive) whose value starts    with
          ``VALUE_PREFIX``. Both a key and a value must be specified. -
          ``+LABEL_KEY:VALUE``: Return all traces containing a key:value
          pair    exactly matching the specified text. Both a key and a
          value must be    specified. -  ``method:VALUE``: Equivalent to
          ``/http/method:VALUE``. -  ``url:VALUE``: Equivalent to
          ``/http/url:VALUE``.
      order_by:
          Field used to sort the returned traces. Optional. Can be one
          of the following:  -  ``trace_id`` -  ``name`` (``name`` field
          of root span in the trace) -  ``duration`` (difference between
          ``end_time`` and ``start_time``    fields of the root span) -
          ``start`` (``start_time`` field of the root span)  Descending
          order can be specified by appending ``desc`` to the sort field
          (for example, ``name desc``).  Only one sort field is
          permitted.
  """,
  # @@protoc_insertion_point(class_scope:google.devtools.cloudtrace.v1.ListTracesRequest)
  ))
_sym_db.RegisterMessage(ListTracesRequest)

ListTracesResponse = _reflection.GeneratedProtocolMessageType('ListTracesResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTTRACESRESPONSE,
  __module__ = 'google.devtools.cloudtrace_v1.proto.trace_pb2'
  ,
  __doc__ = """The response message for the ``ListTraces`` method.
  
  
  Attributes:
      traces:
          List of trace records returned.
      next_page_token:
          If defined, indicates that there are more traces that match
          the request and that this value should be passed to the next
          request to continue retrieving additional traces.
  """,
  # @@protoc_insertion_point(class_scope:google.devtools.cloudtrace.v1.ListTracesResponse)
  ))
_sym_db.RegisterMessage(ListTracesResponse)

GetTraceRequest = _reflection.GeneratedProtocolMessageType('GetTraceRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETTRACEREQUEST,
  __module__ = 'google.devtools.cloudtrace_v1.proto.trace_pb2'
  ,
  __doc__ = """The request message for the ``GetTrace`` method.
  
  
  Attributes:
      project_id:
          ID of the Cloud project where the trace data is stored.
      trace_id:
          ID of the trace to return.
  """,
  # @@protoc_insertion_point(class_scope:google.devtools.cloudtrace.v1.GetTraceRequest)
  ))
_sym_db.RegisterMessage(GetTraceRequest)

PatchTracesRequest = _reflection.GeneratedProtocolMessageType('PatchTracesRequest', (_message.Message,), dict(
  DESCRIPTOR = _PATCHTRACESREQUEST,
  __module__ = 'google.devtools.cloudtrace_v1.proto.trace_pb2'
  ,
  __doc__ = """The request message for the ``PatchTraces`` method.
  
  
  Attributes:
      project_id:
          ID of the Cloud project where the trace data is stored.
      traces:
          The body of the message.
  """,
  # @@protoc_insertion_point(class_scope:google.devtools.cloudtrace.v1.PatchTracesRequest)
  ))
_sym_db.RegisterMessage(PatchTracesRequest)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n!com.google.devtools.cloudtrace.v1B\nTraceProtoP\001ZGgoogle.golang.org/genproto/googleapis/devtools/cloudtrace/v1;cloudtrace\252\002\025Google.Cloud.Trace.V1\312\002\025Google\\Cloud\\Trace\\V1'))
_TRACESPAN_LABELSENTRY.has_options = True
_TRACESPAN_LABELSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))

_TRACESERVICE = _descriptor.ServiceDescriptor(
  name='TraceService',
  full_name='google.devtools.cloudtrace.v1.TraceService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1376,
  serialized_end=1841,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListTraces',
    full_name='google.devtools.cloudtrace.v1.TraceService.ListTraces',
    index=0,
    containing_service=None,
    input_type=_LISTTRACESREQUEST,
    output_type=_LISTTRACESRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\"\022 /v1/projects/{project_id}/traces')),
  ),
  _descriptor.MethodDescriptor(
    name='GetTrace',
    full_name='google.devtools.cloudtrace.v1.TraceService.GetTrace',
    index=1,
    containing_service=None,
    input_type=_GETTRACEREQUEST,
    output_type=_TRACE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002-\022+/v1/projects/{project_id}/traces/{trace_id}')),
  ),
  _descriptor.MethodDescriptor(
    name='PatchTraces',
    full_name='google.devtools.cloudtrace.v1.TraceService.PatchTraces',
    index=2,
    containing_service=None,
    input_type=_PATCHTRACESREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002*2 /v1/projects/{project_id}/traces:\006traces')),
  ),
])
_sym_db.RegisterServiceDescriptor(_TRACESERVICE)

DESCRIPTOR.services_by_name['TraceService'] = _TRACESERVICE

# @@protoc_insertion_point(module_scope)
