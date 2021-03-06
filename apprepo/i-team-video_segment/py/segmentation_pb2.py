# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='segmentation.proto',
  package='Segment',
  serialized_pb='\n\x12segmentation.proto\x12\x07Segment\"\xdd\x0e\n\x10SegmentationDesc\x12\x32\n\x06region\x18\x02 \x03(\x0b\x32\".Segment.SegmentationDesc.Region2D\x12;\n\thierarchy\x18\x03 \x03(\x0b\x32(.Segment.SegmentationDesc.HierarchyLevel\x12\x16\n\x0b\x66rame_width\x18\x04 \x01(\x05:\x01\x30\x12\x17\n\x0c\x66rame_height\x18\x05 \x01(\x05:\x01\x30\x12\x12\n\nchunk_size\x18\x06 \x01(\x05\x12\x15\n\roverlap_start\x18\x07 \x01(\x05\x12\x14\n\x08\x63hunk_id\x18\x08 \x01(\x05:\x02-1\x12\x1e\n\x13hierarchy_frame_idx\x18\t \x01(\x05:\x01\x30\x12\x43\n\x0b\x64\x65scriptors\x18\n \x03(\x0b\x32..Segment.SegmentationDesc.AggregatedDescriptor\x1a\x95\x01\n\rRasterization\x12H\n\nscan_inter\x18\x01 \x03(\x0b\x32\x34.Segment.SegmentationDesc.Rasterization.ScanInterval\x1a:\n\x0cScanInterval\x12\t\n\x01y\x18\x01 \x02(\x05\x12\x0e\n\x06left_x\x18\x02 \x02(\x05\x12\x0f\n\x07right_x\x18\x03 \x02(\x05\x1a\x93\x01\n\x0ePolygonization\x1a\x1d\n\x05Point\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\x1a\x62\n\tComponent\x12=\n\x05point\x18\x01 \x03(\x0b\x32..Segment.SegmentationDesc.Polygonization.Point\x12\x16\n\x0ehole_component\x18\x02 \x01(\x08\x1au\n\x0cShapeMoments\x12\x0c\n\x04size\x18\x01 \x01(\x02\x12\x0e\n\x06mean_x\x18\x02 \x01(\x02\x12\x0e\n\x06mean_y\x18\x03 \x01(\x02\x12\x11\n\tmoment_xx\x18\x04 \x01(\x02\x12\x11\n\tmoment_xy\x18\x05 \x01(\x02\x12\x11\n\tmoment_yy\x18\x06 \x01(\x02\x1a\xc9\x01\n\x08Region2D\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x37\n\x06raster\x18\x03 \x01(\x0b\x32\'.Segment.SegmentationDesc.Rasterization\x12\x39\n\x07polygon\x18\x04 \x01(\x0b\x32(.Segment.SegmentationDesc.Polygonization\x12=\n\rshape_moments\x18\x05 \x01(\x0b\x32&.Segment.SegmentationDesc.ShapeMoments\x1a\x90\x01\n\x0e\x43ompoundRegion\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0c\n\x04size\x18\x02 \x02(\x05\x12\x13\n\x0bneighbor_id\x18\x03 \x03(\x05\x12\x15\n\tparent_id\x18\x04 \x01(\x05:\x02-1\x12\x10\n\x08\x63hild_id\x18\x05 \x03(\x05\x12\x13\n\x0bstart_frame\x18\x06 \x01(\x05\x12\x11\n\tend_frame\x18\x07 \x01(\x05\x1aJ\n\x0eHierarchyLevel\x12\x38\n\x06region\x18\x02 \x03(\x0b\x32(.Segment.SegmentationDesc.CompoundRegion\x1a\xbc\x01\n\x14\x41ppearanceDescriptor\x12\x16\n\x0eluminance_bins\x18\x01 \x02(\x05\x12\x12\n\ncolor_bins\x18\x02 \x02(\x05\x12N\n\x0b\x63olor_entry\x18\x03 \x03(\x0b\x32\x39.Segment.SegmentationDesc.AppearanceDescriptor.ColorEntry\x1a(\n\nColorEntry\x12\x0b\n\x03idx\x18\x01 \x02(\x05\x12\r\n\x05value\x18\x02 \x02(\x02\x1a&\n\x0e\x46lowDescriptor\x12\x14\n\x0cvector_entry\x18\x01 \x03(\x02\x1a&\n\x11TextureDescriptor\x12\x11\n\tlbp_entry\x18\x01 \x03(\x02\x1a\x88\x01\n\x0fMatchDescriptor\x12\x43\n\x05tuple\x18\x01 \x03(\x0b\x32\x34.Segment.SegmentationDesc.MatchDescriptor.MatchTuple\x1a\x30\n\nMatchTuple\x12\x10\n\x08match_id\x18\x01 \x02(\x05\x12\x10\n\x08strength\x18\x02 \x01(\x02\x1a\x96\x02\n\x14\x41ggregatedDescriptor\x12\n\n\x02id\x18\x01 \x02(\x07\x12\x42\n\nappearance\x18\x02 \x01(\x0b\x32..Segment.SegmentationDesc.AppearanceDescriptor\x12\x36\n\x04\x66low\x18\x03 \x01(\x0b\x32(.Segment.SegmentationDesc.FlowDescriptor\x12<\n\x07texture\x18\x04 \x03(\x0b\x32+.Segment.SegmentationDesc.TextureDescriptor\x12\x38\n\x05match\x18\x05 \x01(\x0b\x32).Segment.SegmentationDesc.MatchDescriptor')




_SEGMENTATIONDESC_RASTERIZATION_SCANINTERVAL = descriptor.Descriptor(
  name='ScanInterval',
  full_name='Segment.SegmentationDesc.Rasterization.ScanInterval',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='y', full_name='Segment.SegmentationDesc.Rasterization.ScanInterval.y', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='left_x', full_name='Segment.SegmentationDesc.Rasterization.ScanInterval.left_x', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='right_x', full_name='Segment.SegmentationDesc.Rasterization.ScanInterval.right_x', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=472,
  serialized_end=530,
)

_SEGMENTATIONDESC_RASTERIZATION = descriptor.Descriptor(
  name='Rasterization',
  full_name='Segment.SegmentationDesc.Rasterization',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='scan_inter', full_name='Segment.SegmentationDesc.Rasterization.scan_inter', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_SEGMENTATIONDESC_RASTERIZATION_SCANINTERVAL, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=381,
  serialized_end=530,
)

_SEGMENTATIONDESC_POLYGONIZATION_POINT = descriptor.Descriptor(
  name='Point',
  full_name='Segment.SegmentationDesc.Polygonization.Point',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='x', full_name='Segment.SegmentationDesc.Polygonization.Point.x', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='y', full_name='Segment.SegmentationDesc.Polygonization.Point.y', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=551,
  serialized_end=580,
)

_SEGMENTATIONDESC_POLYGONIZATION_COMPONENT = descriptor.Descriptor(
  name='Component',
  full_name='Segment.SegmentationDesc.Polygonization.Component',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='point', full_name='Segment.SegmentationDesc.Polygonization.Component.point', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='hole_component', full_name='Segment.SegmentationDesc.Polygonization.Component.hole_component', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=582,
  serialized_end=680,
)

_SEGMENTATIONDESC_POLYGONIZATION = descriptor.Descriptor(
  name='Polygonization',
  full_name='Segment.SegmentationDesc.Polygonization',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_SEGMENTATIONDESC_POLYGONIZATION_POINT, _SEGMENTATIONDESC_POLYGONIZATION_COMPONENT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=533,
  serialized_end=680,
)

_SEGMENTATIONDESC_SHAPEMOMENTS = descriptor.Descriptor(
  name='ShapeMoments',
  full_name='Segment.SegmentationDesc.ShapeMoments',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='size', full_name='Segment.SegmentationDesc.ShapeMoments.size', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='mean_x', full_name='Segment.SegmentationDesc.ShapeMoments.mean_x', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='mean_y', full_name='Segment.SegmentationDesc.ShapeMoments.mean_y', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='moment_xx', full_name='Segment.SegmentationDesc.ShapeMoments.moment_xx', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='moment_xy', full_name='Segment.SegmentationDesc.ShapeMoments.moment_xy', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='moment_yy', full_name='Segment.SegmentationDesc.ShapeMoments.moment_yy', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=682,
  serialized_end=799,
)

_SEGMENTATIONDESC_REGION2D = descriptor.Descriptor(
  name='Region2D',
  full_name='Segment.SegmentationDesc.Region2D',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='Segment.SegmentationDesc.Region2D.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='raster', full_name='Segment.SegmentationDesc.Region2D.raster', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='polygon', full_name='Segment.SegmentationDesc.Region2D.polygon', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='shape_moments', full_name='Segment.SegmentationDesc.Region2D.shape_moments', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=802,
  serialized_end=1003,
)

_SEGMENTATIONDESC_COMPOUNDREGION = descriptor.Descriptor(
  name='CompoundRegion',
  full_name='Segment.SegmentationDesc.CompoundRegion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='Segment.SegmentationDesc.CompoundRegion.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='size', full_name='Segment.SegmentationDesc.CompoundRegion.size', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='neighbor_id', full_name='Segment.SegmentationDesc.CompoundRegion.neighbor_id', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='parent_id', full_name='Segment.SegmentationDesc.CompoundRegion.parent_id', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='child_id', full_name='Segment.SegmentationDesc.CompoundRegion.child_id', index=4,
      number=5, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='start_frame', full_name='Segment.SegmentationDesc.CompoundRegion.start_frame', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='end_frame', full_name='Segment.SegmentationDesc.CompoundRegion.end_frame', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1006,
  serialized_end=1150,
)

_SEGMENTATIONDESC_HIERARCHYLEVEL = descriptor.Descriptor(
  name='HierarchyLevel',
  full_name='Segment.SegmentationDesc.HierarchyLevel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='region', full_name='Segment.SegmentationDesc.HierarchyLevel.region', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1152,
  serialized_end=1226,
)

_SEGMENTATIONDESC_APPEARANCEDESCRIPTOR_COLORENTRY = descriptor.Descriptor(
  name='ColorEntry',
  full_name='Segment.SegmentationDesc.AppearanceDescriptor.ColorEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='idx', full_name='Segment.SegmentationDesc.AppearanceDescriptor.ColorEntry.idx', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='value', full_name='Segment.SegmentationDesc.AppearanceDescriptor.ColorEntry.value', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=1377,
  serialized_end=1417,
)

_SEGMENTATIONDESC_APPEARANCEDESCRIPTOR = descriptor.Descriptor(
  name='AppearanceDescriptor',
  full_name='Segment.SegmentationDesc.AppearanceDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='luminance_bins', full_name='Segment.SegmentationDesc.AppearanceDescriptor.luminance_bins', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='color_bins', full_name='Segment.SegmentationDesc.AppearanceDescriptor.color_bins', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='color_entry', full_name='Segment.SegmentationDesc.AppearanceDescriptor.color_entry', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_SEGMENTATIONDESC_APPEARANCEDESCRIPTOR_COLORENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1229,
  serialized_end=1417,
)

_SEGMENTATIONDESC_FLOWDESCRIPTOR = descriptor.Descriptor(
  name='FlowDescriptor',
  full_name='Segment.SegmentationDesc.FlowDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='vector_entry', full_name='Segment.SegmentationDesc.FlowDescriptor.vector_entry', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1419,
  serialized_end=1457,
)

_SEGMENTATIONDESC_TEXTUREDESCRIPTOR = descriptor.Descriptor(
  name='TextureDescriptor',
  full_name='Segment.SegmentationDesc.TextureDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='lbp_entry', full_name='Segment.SegmentationDesc.TextureDescriptor.lbp_entry', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1459,
  serialized_end=1497,
)

_SEGMENTATIONDESC_MATCHDESCRIPTOR_MATCHTUPLE = descriptor.Descriptor(
  name='MatchTuple',
  full_name='Segment.SegmentationDesc.MatchDescriptor.MatchTuple',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='match_id', full_name='Segment.SegmentationDesc.MatchDescriptor.MatchTuple.match_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='strength', full_name='Segment.SegmentationDesc.MatchDescriptor.MatchTuple.strength', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1588,
  serialized_end=1636,
)

_SEGMENTATIONDESC_MATCHDESCRIPTOR = descriptor.Descriptor(
  name='MatchDescriptor',
  full_name='Segment.SegmentationDesc.MatchDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='tuple', full_name='Segment.SegmentationDesc.MatchDescriptor.tuple', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_SEGMENTATIONDESC_MATCHDESCRIPTOR_MATCHTUPLE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1500,
  serialized_end=1636,
)

_SEGMENTATIONDESC_AGGREGATEDDESCRIPTOR = descriptor.Descriptor(
  name='AggregatedDescriptor',
  full_name='Segment.SegmentationDesc.AggregatedDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='Segment.SegmentationDesc.AggregatedDescriptor.id', index=0,
      number=1, type=7, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='appearance', full_name='Segment.SegmentationDesc.AggregatedDescriptor.appearance', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='flow', full_name='Segment.SegmentationDesc.AggregatedDescriptor.flow', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='texture', full_name='Segment.SegmentationDesc.AggregatedDescriptor.texture', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='match', full_name='Segment.SegmentationDesc.AggregatedDescriptor.match', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1639,
  serialized_end=1917,
)

_SEGMENTATIONDESC = descriptor.Descriptor(
  name='SegmentationDesc',
  full_name='Segment.SegmentationDesc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='region', full_name='Segment.SegmentationDesc.region', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='hierarchy', full_name='Segment.SegmentationDesc.hierarchy', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='frame_width', full_name='Segment.SegmentationDesc.frame_width', index=2,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='frame_height', full_name='Segment.SegmentationDesc.frame_height', index=3,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='chunk_size', full_name='Segment.SegmentationDesc.chunk_size', index=4,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='overlap_start', full_name='Segment.SegmentationDesc.overlap_start', index=5,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='chunk_id', full_name='Segment.SegmentationDesc.chunk_id', index=6,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='hierarchy_frame_idx', full_name='Segment.SegmentationDesc.hierarchy_frame_idx', index=7,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='descriptors', full_name='Segment.SegmentationDesc.descriptors', index=8,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_SEGMENTATIONDESC_RASTERIZATION, _SEGMENTATIONDESC_POLYGONIZATION, _SEGMENTATIONDESC_SHAPEMOMENTS, _SEGMENTATIONDESC_REGION2D, _SEGMENTATIONDESC_COMPOUNDREGION, _SEGMENTATIONDESC_HIERARCHYLEVEL, _SEGMENTATIONDESC_APPEARANCEDESCRIPTOR, _SEGMENTATIONDESC_FLOWDESCRIPTOR, _SEGMENTATIONDESC_TEXTUREDESCRIPTOR, _SEGMENTATIONDESC_MATCHDESCRIPTOR, _SEGMENTATIONDESC_AGGREGATEDDESCRIPTOR, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=32,
  serialized_end=1917,
)

_SEGMENTATIONDESC_RASTERIZATION_SCANINTERVAL.containing_type = _SEGMENTATIONDESC_RASTERIZATION;
_SEGMENTATIONDESC_RASTERIZATION.fields_by_name['scan_inter'].message_type = _SEGMENTATIONDESC_RASTERIZATION_SCANINTERVAL
_SEGMENTATIONDESC_RASTERIZATION.containing_type = _SEGMENTATIONDESC;
_SEGMENTATIONDESC_POLYGONIZATION_POINT.containing_type = _SEGMENTATIONDESC_POLYGONIZATION;
_SEGMENTATIONDESC_POLYGONIZATION_COMPONENT.fields_by_name['point'].message_type = _SEGMENTATIONDESC_POLYGONIZATION_POINT
_SEGMENTATIONDESC_POLYGONIZATION_COMPONENT.containing_type = _SEGMENTATIONDESC_POLYGONIZATION;
_SEGMENTATIONDESC_POLYGONIZATION.containing_type = _SEGMENTATIONDESC;
_SEGMENTATIONDESC_SHAPEMOMENTS.containing_type = _SEGMENTATIONDESC;
_SEGMENTATIONDESC_REGION2D.fields_by_name['raster'].message_type = _SEGMENTATIONDESC_RASTERIZATION
_SEGMENTATIONDESC_REGION2D.fields_by_name['polygon'].message_type = _SEGMENTATIONDESC_POLYGONIZATION
_SEGMENTATIONDESC_REGION2D.fields_by_name['shape_moments'].message_type = _SEGMENTATIONDESC_SHAPEMOMENTS
_SEGMENTATIONDESC_REGION2D.containing_type = _SEGMENTATIONDESC;
_SEGMENTATIONDESC_COMPOUNDREGION.containing_type = _SEGMENTATIONDESC;
_SEGMENTATIONDESC_HIERARCHYLEVEL.fields_by_name['region'].message_type = _SEGMENTATIONDESC_COMPOUNDREGION
_SEGMENTATIONDESC_HIERARCHYLEVEL.containing_type = _SEGMENTATIONDESC;
_SEGMENTATIONDESC_APPEARANCEDESCRIPTOR_COLORENTRY.containing_type = _SEGMENTATIONDESC_APPEARANCEDESCRIPTOR;
_SEGMENTATIONDESC_APPEARANCEDESCRIPTOR.fields_by_name['color_entry'].message_type = _SEGMENTATIONDESC_APPEARANCEDESCRIPTOR_COLORENTRY
_SEGMENTATIONDESC_APPEARANCEDESCRIPTOR.containing_type = _SEGMENTATIONDESC;
_SEGMENTATIONDESC_FLOWDESCRIPTOR.containing_type = _SEGMENTATIONDESC;
_SEGMENTATIONDESC_TEXTUREDESCRIPTOR.containing_type = _SEGMENTATIONDESC;
_SEGMENTATIONDESC_MATCHDESCRIPTOR_MATCHTUPLE.containing_type = _SEGMENTATIONDESC_MATCHDESCRIPTOR;
_SEGMENTATIONDESC_MATCHDESCRIPTOR.fields_by_name['tuple'].message_type = _SEGMENTATIONDESC_MATCHDESCRIPTOR_MATCHTUPLE
_SEGMENTATIONDESC_MATCHDESCRIPTOR.containing_type = _SEGMENTATIONDESC;
_SEGMENTATIONDESC_AGGREGATEDDESCRIPTOR.fields_by_name['appearance'].message_type = _SEGMENTATIONDESC_APPEARANCEDESCRIPTOR
_SEGMENTATIONDESC_AGGREGATEDDESCRIPTOR.fields_by_name['flow'].message_type = _SEGMENTATIONDESC_FLOWDESCRIPTOR
_SEGMENTATIONDESC_AGGREGATEDDESCRIPTOR.fields_by_name['texture'].message_type = _SEGMENTATIONDESC_TEXTUREDESCRIPTOR
_SEGMENTATIONDESC_AGGREGATEDDESCRIPTOR.fields_by_name['match'].message_type = _SEGMENTATIONDESC_MATCHDESCRIPTOR
_SEGMENTATIONDESC_AGGREGATEDDESCRIPTOR.containing_type = _SEGMENTATIONDESC;
_SEGMENTATIONDESC.fields_by_name['region'].message_type = _SEGMENTATIONDESC_REGION2D
_SEGMENTATIONDESC.fields_by_name['hierarchy'].message_type = _SEGMENTATIONDESC_HIERARCHYLEVEL
_SEGMENTATIONDESC.fields_by_name['descriptors'].message_type = _SEGMENTATIONDESC_AGGREGATEDDESCRIPTOR
DESCRIPTOR.message_types_by_name['SegmentationDesc'] = _SEGMENTATIONDESC

class SegmentationDesc(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class Rasterization(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    
    class ScanInterval(message.Message):
      __metaclass__ = reflection.GeneratedProtocolMessageType
      DESCRIPTOR = _SEGMENTATIONDESC_RASTERIZATION_SCANINTERVAL
      
      # @@protoc_insertion_point(class_scope:Segment.SegmentationDesc.Rasterization.ScanInterval)
    DESCRIPTOR = _SEGMENTATIONDESC_RASTERIZATION
    
    # @@protoc_insertion_point(class_scope:Segment.SegmentationDesc.Rasterization)
  
  class Polygonization(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    
    class Point(message.Message):
      __metaclass__ = reflection.GeneratedProtocolMessageType
      DESCRIPTOR = _SEGMENTATIONDESC_POLYGONIZATION_POINT
      
      # @@protoc_insertion_point(class_scope:Segment.SegmentationDesc.Polygonization.Point)
    
    class Component(message.Message):
      __metaclass__ = reflection.GeneratedProtocolMessageType
      DESCRIPTOR = _SEGMENTATIONDESC_POLYGONIZATION_COMPONENT
      
      # @@protoc_insertion_point(class_scope:Segment.SegmentationDesc.Polygonization.Component)
    DESCRIPTOR = _SEGMENTATIONDESC_POLYGONIZATION
    
    # @@protoc_insertion_point(class_scope:Segment.SegmentationDesc.Polygonization)
  
  class ShapeMoments(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _SEGMENTATIONDESC_SHAPEMOMENTS
    
    # @@protoc_insertion_point(class_scope:Segment.SegmentationDesc.ShapeMoments)
  
  class Region2D(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _SEGMENTATIONDESC_REGION2D
    
    # @@protoc_insertion_point(class_scope:Segment.SegmentationDesc.Region2D)
  
  class CompoundRegion(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _SEGMENTATIONDESC_COMPOUNDREGION
    
    # @@protoc_insertion_point(class_scope:Segment.SegmentationDesc.CompoundRegion)
  
  class HierarchyLevel(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _SEGMENTATIONDESC_HIERARCHYLEVEL
    
    # @@protoc_insertion_point(class_scope:Segment.SegmentationDesc.HierarchyLevel)
  
  class AppearanceDescriptor(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    
    class ColorEntry(message.Message):
      __metaclass__ = reflection.GeneratedProtocolMessageType
      DESCRIPTOR = _SEGMENTATIONDESC_APPEARANCEDESCRIPTOR_COLORENTRY
      
      # @@protoc_insertion_point(class_scope:Segment.SegmentationDesc.AppearanceDescriptor.ColorEntry)
    DESCRIPTOR = _SEGMENTATIONDESC_APPEARANCEDESCRIPTOR
    
    # @@protoc_insertion_point(class_scope:Segment.SegmentationDesc.AppearanceDescriptor)
  
  class FlowDescriptor(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _SEGMENTATIONDESC_FLOWDESCRIPTOR
    
    # @@protoc_insertion_point(class_scope:Segment.SegmentationDesc.FlowDescriptor)
  
  class TextureDescriptor(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _SEGMENTATIONDESC_TEXTUREDESCRIPTOR
    
    # @@protoc_insertion_point(class_scope:Segment.SegmentationDesc.TextureDescriptor)
  
  class MatchDescriptor(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    
    class MatchTuple(message.Message):
      __metaclass__ = reflection.GeneratedProtocolMessageType
      DESCRIPTOR = _SEGMENTATIONDESC_MATCHDESCRIPTOR_MATCHTUPLE
      
      # @@protoc_insertion_point(class_scope:Segment.SegmentationDesc.MatchDescriptor.MatchTuple)
    DESCRIPTOR = _SEGMENTATIONDESC_MATCHDESCRIPTOR
    
    # @@protoc_insertion_point(class_scope:Segment.SegmentationDesc.MatchDescriptor)
  
  class AggregatedDescriptor(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _SEGMENTATIONDESC_AGGREGATEDDESCRIPTOR
    
    # @@protoc_insertion_point(class_scope:Segment.SegmentationDesc.AggregatedDescriptor)
  DESCRIPTOR = _SEGMENTATIONDESC
  
  # @@protoc_insertion_point(class_scope:Segment.SegmentationDesc)

# @@protoc_insertion_point(module_scope)
