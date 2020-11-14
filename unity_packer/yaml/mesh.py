""" This file provides constants to fill in the yaml for the unity package format

replicating essentially this format:

(looking at this I am now realizing I could just write a really nice and easy parser to replicate this)
(parser will look at and fill in any fields with $$ enclosed)

Mesh:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  m_Name: $name$
  serializedVersion: 10
  m_SubMeshes:
  - serializedVersion: 2
    firstByte: 0
    indexCount: $index_count$
    topology: 0
    baseVertex: 0
    firstVertex: 0
    vertexCount: $vertex_count$
    localAABB:
      m_Center: {x: $m_center_x$, y: $m_center_y$, z: $m_center_z$}
      m_Extent: {x: $m_extent_x$, y: $m_extent_y$, z: $m_extent_z$}
  m_Shapes:
    vertices: []
    shapes: []
    channels: []
    fullWeights: []
  m_BindPose: []
  m_BoneNameHashes: 
  m_RootBoneNameHash: 0
  m_BonesAABB: []
  m_VariableBoneCountWeights:
    m_Data: 
  m_MeshCompression: 0
  m_IsReadable: 1
  m_KeepVertices: 0
  m_KeepIndices: 0
  m_IndexFormat: 0
  m_IndexBuffer: $m_index_buffer$
  m_VertexData:
    serializedVersion: 3
    m_VertexCount: $vertex_count$
    m_Channels:
    - stream: 0
      offset: 0
      format: 0
      dimension: 3
    - stream: 0
      offset: 12
      format: 0
      dimension: 3
    - stream: 0
      offset: 0
      format: 0
      dimension: 0
    - stream: 0
      offset: 0
      format: 0
      dimension: 0
    - stream: 0
      offset: 0
      format: 0
      dimension: 0
    - stream: 0
      offset: 0
      format: 0
      dimension: 0
    - stream: 0
      offset: 0
      format: 0
      dimension: 0
    - stream: 0
      offset: 0
      format: 0
      dimension: 0
    - stream: 0
      offset: 0
      format: 0
      dimension: 0
    - stream: 0
      offset: 0
      format: 0
      dimension: 0
    - stream: 0
      offset: 0
      format: 0
      dimension: 0
    - stream: 0
      offset: 0
      format: 0
      dimension: 0
    - stream: 0
      offset: 0
      format: 0
      dimension: 0
    - stream: 0
      offset: 0
      format: 0
      dimension: 0
    m_DataSize: $m_datasize$
    _typelessdata: $_typlessdata$
  m_CompressedMesh:
    m_Vertices:
      m_NumItems: 0
      m_Range: 0
      m_Start: 0
      m_Data: 
      m_BitSize: 0
    m_UV:
      m_NumItems: 0
      m_Range: 0
      m_Start: 0
      m_Data: 
      m_BitSize: 0
    m_Normals:
      m_NumItems: 0
      m_Range: 0
      m_Start: 0
      m_Data: 
      m_BitSize: 0
    m_Tangents:
      m_NumItems: 0
      m_Range: 0
      m_Start: 0
      m_Data: 
      m_BitSize: 0
    m_Weights:
      m_NumItems: 0
      m_Data: 
      m_BitSize: 0
    m_NormalSigns:
      m_NumItems: 0
      m_Data: 
      m_BitSize: 0
    m_TangentSigns:
      m_NumItems: 0
      m_Data: 
      m_BitSize: 0
    m_FloatColors:
      m_NumItems: 0
      m_Range: 0
      m_Start: 0
      m_Data: 
      m_BitSize: 0
    m_BoneIndices:
      m_NumItems: 0
      m_Data: 
      m_BitSize: 0
    m_Triangles:
      m_NumItems: 0
      m_Data: 
      m_BitSize: 0
    m_UVInfo: 0
  m_LocalAABB:
    m_Center: {x: $m_center_x$, y: $m_center_y$, z: $m_center_z$}
    m_Extent: {x: $m_extent_x$, y: $m_extent_y$, z: $m_extent_z$}
  m_MeshUsageFlags: 0
  m_BakedConvexCollisionMesh: 
  m_BakedTriangleCollisionMesh: 
  m_MeshMetrics[0]: 1
  m_MeshMetrics[1]: 1
  m_MeshOptimizationFlags: 1
  m_StreamData:
    serializedVersion: 2
    offset: 0
    size: 0
    path: 
--- !u!43 &$ref_id$
"""

# This is the mesh yaml that will be parsed and filled in
meshyaml = "Mesh:\r\n  m_ObjectHideFlags: 0\r\n  m_CorrespondingSourceObject: {fileID: 0}\r\n  m_PrefabInstance: {fileID: 0}\r\n  m_PrefabAsset: {fileID: 0}\r\n  m_Name: $name$\r\n  serializedVersion: 10\r\n  m_SubMeshes:\r\n  - serializedVersion: 2\r\n    firstByte: 0\r\n    indexCount: $index_count$\r\n    topology: 0\r\n    baseVertex: 0\r\n    firstVertex: 0\r\n    vertexCount: $vertex_count$\r\n    localAABB:\r\n      m_Center: {x: $m_center_x$, y: $m_center_y$, z: $m_center_z$}\r\n      m_Extent: {x: $m_extent_x$, y: $m_extent_y$, z: $m_extent_z$}\r\n  m_Shapes:\r\n    vertices: []\r\n    shapes: []\r\n    channels: []\r\n    fullWeights: []\r\n  m_BindPose: []\r\n  m_BoneNameHashes: \r\n  m_RootBoneNameHash: 0\r\n  m_BonesAABB: []\r\n  m_VariableBoneCountWeights:\r\n    m_Data: \r\n  m_MeshCompression: 0\r\n  m_IsReadable: 1\r\n  m_KeepVertices: 0\r\n  m_KeepIndices: 0\r\n  m_IndexFormat: 0\r\n  m_IndexBuffer: $m_index_buffer$\r\n  m_VertexData:\r\n    serializedVersion: 3\r\n    m_VertexCount: $vertex_count$\r\n    m_Channels:\r\n    - stream: 0\r\n      offset: 0\r\n      format: 0\r\n      dimension: 3\r\n    - stream: 0\r\n      offset: 12\r\n      format: 0\r\n      dimension: 3\r\n    - stream: 0\r\n      offset: 0\r\n      format: 0\r\n      dimension: 0\r\n    - stream: 0\r\n      offset: 0\r\n      format: 0\r\n      dimension: 0\r\n    - stream: 0\r\n      offset: 0\r\n      format: 0\r\n      dimension: 0\r\n    - stream: 0\r\n      offset: 0\r\n      format: 0\r\n      dimension: 0\r\n    - stream: 0\r\n      offset: 0\r\n      format: 0\r\n      dimension: 0\r\n    - stream: 0\r\n      offset: 0\r\n      format: 0\r\n      dimension: 0\r\n    - stream: 0\r\n      offset: 0\r\n      format: 0\r\n      dimension: 0\r\n    - stream: 0\r\n      offset: 0\r\n      format: 0\r\n      dimension: 0\r\n    - stream: 0\r\n      offset: 0\r\n      format: 0\r\n      dimension: 0\r\n    - stream: 0\r\n      offset: 0\r\n      format: 0\r\n      dimension: 0\r\n    - stream: 0\r\n      offset: 0\r\n      format: 0\r\n      dimension: 0\r\n    - stream: 0\r\n      offset: 0\r\n      format: 0\r\n      dimension: 0\r\n    m_DataSize: $m_datasize$\r\n    _typelessdata: $_typlessdata$\r\n  m_CompressedMesh:\r\n    m_Vertices:\r\n      m_NumItems: 0\r\n      m_Range: 0\r\n      m_Start: 0\r\n      m_Data: \r\n      m_BitSize: 0\r\n    m_UV:\r\n      m_NumItems: 0\r\n      m_Range: 0\r\n      m_Start: 0\r\n      m_Data: \r\n      m_BitSize: 0\r\n    m_Normals:\r\n      m_NumItems: 0\r\n      m_Range: 0\r\n      m_Start: 0\r\n      m_Data: \r\n      m_BitSize: 0\r\n    m_Tangents:\r\n      m_NumItems: 0\r\n      m_Range: 0\r\n      m_Start: 0\r\n      m_Data: \r\n      m_BitSize: 0\r\n    m_Weights:\r\n      m_NumItems: 0\r\n      m_Data: \r\n      m_BitSize: 0\r\n    m_NormalSigns:\r\n      m_NumItems: 0\r\n      m_Data: \r\n      m_BitSize: 0\r\n    m_TangentSigns:\r\n      m_NumItems: 0\r\n      m_Data: \r\n      m_BitSize: 0\r\n    m_FloatColors:\r\n      m_NumItems: 0\r\n      m_Range: 0\r\n      m_Start: 0\r\n      m_Data: \r\n      m_BitSize: 0\r\n    m_BoneIndices:\r\n      m_NumItems: 0\r\n      m_Data: \r\n      m_BitSize: 0\r\n    m_Triangles:\r\n      m_NumItems: 0\r\n      m_Data: \r\n      m_BitSize: 0\r\n    m_UVInfo: 0\r\n  m_LocalAABB:\r\n    m_Center: {x: $m_center_x$, y: $m_center_y$, z: $m_center_z$}\r\n    m_Extent: {x: $m_extent_x$, y: $m_extent_y$, z: $m_extent_z$}\r\n  m_MeshUsageFlags: 0\r\n  m_BakedConvexCollisionMesh: \r\n  m_BakedTriangleCollisionMesh: \r\n  m_MeshMetrics[0]: 1\r\n  m_MeshMetrics[1]: 1\r\n  m_MeshOptimizationFlags: 1\r\n  m_StreamData:\r\n    serializedVersion: 2\r\n    offset: 0\r\n    size: 0\r\n    path: \r\n--- !u!43 &$ref_id$"


#compressed_mesh = "     m_CompressedMesh:\r\n    m_Vertices:\r\n      m_NumItems: 0\r\n      m_Range: 0\r\n      m_Start: 0\r\n      m_Data: \r\n      m_BitSize: 0\r\n    m_UV:\r\n      m_NumItems: 0\r\n      m_Range: 0\r\n      m_Start: 0\r\n      m_Data: \r\n      m_BitSize: 0\r\n    m_Normals:\r\n      m_NumItems: 0\r\n      m_Range: 0\r\n      m_Start: 0\r\n      m_Data: \r\n      m_BitSize: 0\r\n    m_Tangents:\r\n      m_NumItems: 0\r\n      m_Range: 0\r\n      m_Start: 0\r\n      m_Data: \r\n      m_BitSize: 0\r\n    m_Weights:\r\n      m_NumItems: 0\r\n      m_Data: \r\n      m_BitSize: 0\r\n    m_NormalSigns:\r\n      m_NumItems: 0\r\n      m_Data: \r\n      m_BitSize: 0\r\n    m_TangentSigns:\r\n      m_NumItems: 0\r\n      m_Data: \r\n      m_BitSize: 0\r\n    m_FloatColors:\r\n      m_NumItems: 0\r\n      m_Range: 0\r\n      m_Start: 0\r\n      m_Data: \r\n      m_BitSize: 0\r\n    m_BoneIndices:\r\n      m_NumItems: 0\r\n      m_Data: \r\n      m_BitSize: 0\r\n    m_Triangles:\r\n      m_NumItems: 0\r\n      m_Data: \r\n      m_BitSize: 0\r\n    m_UVInfo: 0"
#vertex_channel = "    m_Channels:\r\n    - stream: 0\r\n      offset: 0\r\n      format: 0\r\n      dimension: 3\r\n    - stream: 0\r\n      offset: 12\r\n      format: 0\r\n      dimension: 3\r\n    - stream: 0\r\n      offset: 0\r\n      format: 0\r\n      dimension: 0\r\n    - stream: 0\r\n      offset: 0\r\n      format: 0\r\n      dimension: 0\r\n    - stream: 0\r\n      offset: 0\r\n      format: 0\r\n      dimension: 0\r\n    - stream: 0\r\n      offset: 0\r\n      format: 0\r\n      dimension: 0\r\n    - stream: 0\r\n      offset: 0\r\n      format: 0\r\n      dimension: 0\r\n    - stream: 0\r\n      offset: 0\r\n      format: 0\r\n      dimension: 0\r\n    - stream: 0\r\n      offset: 0\r\n      format: 0\r\n      dimension: 0\r\n    - stream: 0\r\n      offset: 0\r\n      format: 0\r\n      dimension: 0\r\n    - stream: 0\r\n      offset: 0\r\n      format: 0\r\n      dimension: 0\r\n    - stream: 0\r\n      offset: 0\r\n      format: 0\r\n      dimension: 0\r\n    - stream: 0\r\n      offset: 0\r\n      format: 0\r\n      dimension: 0\r\n    - stream: 0\r\n      offset: 0\r\n      format: 0\r\n      dimension: 0"
#m_shapes = "  m_Shapes:\r\n    vertices: []\r\n    shapes: []\r\n    channels: []\r\n    fullWeights: []"
#m_bindpose = "  m_BindPose: []\r\n  m_BoneNameHashes: \r\n  m_RootBoneNameHash: 0\r\n  m_BonesAABB: []\r\n  m_VariableBoneCountWeights:\r\n    m_Data: \r\n  m_MeshCompression: 0\r\n  m_IsReadable: 1\r\n  m_KeepVertices: 0\r\n  m_KeepIndices: 0\r\n  m_IndexFormat: 0"
#m_meshusage = "  m_MeshUsageFlags: 0\r\n  m_BakedConvexCollisionMesh: \r\n  m_BakedTriangleCollisionMesh: \r\n  m_MeshMetrics[0]: 1\r\n  m_MeshMetrics[1]: 1\r\n  m_MeshOptimizationFlags: 1\r\n  m_StreamData:\r\n    serializedVersion: 2\r\n    offset: 0\r\n    size: 0\r\n    path: "
#path_prefix = " \r\n--- !u!43 &"