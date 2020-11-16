""" This file provides constants to fill in the yaml for the unity package format

replicating essentially this format:

(looking at this I am now realizing I could just write a really nice and easy parser to replicate this)
(parser will look at and fill in any fields with $$ enclosed)


--- !u!43 &$ref_id$
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
    [useless stuff]
    m_DataSize: $m_datasize$
    _typelessdata: $_typlessdata$
  m_CompressedMesh:
    [useless stuff]
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
"""

# This is the mesh yaml that will be parsed and filled in
meshyaml = "--- !u!43 &$ref_id$ \r\nMesh:\r\n  m_ObjectHideFlags: 0\r\n  m_CorrespondingSourceObject: {fileID: 0}\r\n  m_PrefabInstance: {fileID: 0}\r\n  m_PrefabAsset: {fileID: 0}\r\n  m_Name: $name$\r\n  serializedVersion: 10\r\n  m_SubMeshes:\r\n  - serializedVersion: 2\r\n    firstByte: 0\r\n    indexCount: $index_count$\r\n    topology: 0\r\n    baseVertex: 0\r\n    firstVertex: 0\r\n    vertexCount: $vertex_count$\r\n    localAABB:\r\n      m_Center: {x: $m_center_x$, y: $m_center_y$, z: $m_center_z$}\r\n      m_Extent: {x: $m_extent_x$, y: $m_extent_y$, z: $m_extent_z$}\r\n  m_Shapes:\r\n    vertices: []\r\n    shapes: []\r\n    channels: []\r\n    fullWeights: []\r\n  m_BindPose: []\r\n  m_BoneNameHashes: \r\n  m_RootBoneNameHash: 0\r\n  m_BonesAABB: []\r\n  m_VariableBoneCountWeights:\r\n    m_Data: \r\n  m_MeshCompression: 0\r\n  m_IsReadable: 1\r\n  m_KeepVertices: 0\r\n  m_KeepIndices: 0\r\n  m_IndexFormat: 0\r\n  m_IndexBuffer: $m_index_buffer$\r\n  m_VertexData:\r\n    serializedVersion: 3\r\n    m_VertexCount: $vertex_count$\r\n    m_Channels:\r\n    - stream: 0\r\n      offset: 0\r\n      format: 0\r\n      dimension: 3\r\n    - stream: 0\r\n      offset: 12\r\n      format: 0\r\n      dimension: 3\r\n    - stream: 0\r\n      offset: 0\r\n      format: 0\r\n      dimension: 0\r\n    - stream: 0\r\n      offset: 0\r\n      format: 0\r\n      dimension: 0\r\n    - stream: 0\r\n      offset: 0\r\n      format: 0\r\n      dimension: 0\r\n    - stream: 0\r\n      offset: 0\r\n      format: 0\r\n      dimension: 0\r\n    - stream: 0\r\n      offset: 0\r\n      format: 0\r\n      dimension: 0\r\n    - stream: 0\r\n      offset: 0\r\n      format: 0\r\n      dimension: 0\r\n    - stream: 0\r\n      offset: 0\r\n      format: 0\r\n      dimension: 0\r\n    - stream: 0\r\n      offset: 0\r\n      format: 0\r\n      dimension: 0\r\n    - stream: 0\r\n      offset: 0\r\n      format: 0\r\n      dimension: 0\r\n    - stream: 0\r\n      offset: 0\r\n      format: 0\r\n      dimension: 0\r\n    - stream: 0\r\n      offset: 0\r\n      format: 0\r\n      dimension: 0\r\n    - stream: 0\r\n      offset: 0\r\n      format: 0\r\n      dimension: 0\r\n    m_DataSize: $m_datasize$\r\n    _typelessdata: $_typlessdata$\r\n  m_CompressedMesh:\r\n    m_Vertices:\r\n      m_NumItems: 0\r\n      m_Range: 0\r\n      m_Start: 0\r\n      m_Data: \r\n      m_BitSize: 0\r\n    m_UV:\r\n      m_NumItems: 0\r\n      m_Range: 0\r\n      m_Start: 0\r\n      m_Data: \r\n      m_BitSize: 0\r\n    m_Normals:\r\n      m_NumItems: 0\r\n      m_Range: 0\r\n      m_Start: 0\r\n      m_Data: \r\n      m_BitSize: 0\r\n    m_Tangents:\r\n      m_NumItems: 0\r\n      m_Range: 0\r\n      m_Start: 0\r\n      m_Data: \r\n      m_BitSize: 0\r\n    m_Weights:\r\n      m_NumItems: 0\r\n      m_Data: \r\n      m_BitSize: 0\r\n    m_NormalSigns:\r\n      m_NumItems: 0\r\n      m_Data: \r\n      m_BitSize: 0\r\n    m_TangentSigns:\r\n      m_NumItems: 0\r\n      m_Data: \r\n      m_BitSize: 0\r\n    m_FloatColors:\r\n      m_NumItems: 0\r\n      m_Range: 0\r\n      m_Start: 0\r\n      m_Data: \r\n      m_BitSize: 0\r\n    m_BoneIndices:\r\n      m_NumItems: 0\r\n      m_Data: \r\n      m_BitSize: 0\r\n    m_Triangles:\r\n      m_NumItems: 0\r\n      m_Data: \r\n      m_BitSize: 0\r\n    m_UVInfo: 0\r\n  m_LocalAABB:\r\n    m_Center: {x: $m_center_x$, y: $m_center_y$, z: $m_center_z$}\r\n    m_Extent: {x: $m_extent_x$, y: $m_extent_y$, z: $m_extent_z$}\r\n  m_MeshUsageFlags: 0\r\n  m_BakedConvexCollisionMesh: \r\n  m_BakedTriangleCollisionMesh: \r\n  m_MeshMetrics[0]: 1\r\n  m_MeshMetrics[1]: 1\r\n  m_MeshOptimizationFlags: 1\r\n  m_StreamData:\r\n    serializedVersion: 2\r\n    offset: 0\r\n    size: 0\r\n    path: \r\n"


"""
This is the assetmeta file extracted format

in this case $ref_id$ referes to the package uuid

fileFormatVersion: 2
guid: $ref_id$
NativeFormatImporter:
  externalObjects: {}
  mainObjectFileID: 0
  userData: 
"""

assetmeta = "fileFormatVersion: 2\r\nguid: $ref_id$\r\nNativeFormatImporter:\r\n  externalObjects: {}\r\n  mainObjectFileID: 0\r\n  userData: \r\n  assetBundleName: \r\n  assetBundleVariant: \r\n"


""" Pathname format for the pathname file

Where name is the name of the overall file,
this isn't yaml but it fits here imo

TODO: add dynamic path
"""

pathname = "Assets/Imported/$name$.prefab"


"""
  Asset Tag is added to the top of a asset file


%YAML 1.1
%TAG !u! tag:unity3d.com,2011:
"""

assetTag = "%YAML 1.1\r\n%TAG !u! tag:autodesk.com,2011:\r\n"



"""
GUID TAGS

guid tags are part of the reference ID

Keeping these to construct my own in the future and keep track

Examples:

   |-----| <-------- This changes 
--- !u!33 &4396483931008730516

   |-----| <-------- This changes 
--- !u!64 &8239074249474088091

   |-----| <-------- This changes 
--- !u!23 &4272737615453238113
"""

guidTags = {
  "GameObject": "1",
  "Transform":  "4",
  "MonoBehaviour": "114",
  "MeshCollider": "64",
  "MeshFilter": "33",
  "MeshRenderer": "23"
}


"""
GameObject serialized yaml object

--- !u!1 &$ref_id$
GameObject:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  serializedVersion: 6
  m_Component:
  $components$
  m_Layer: 0
  m_Name: $name$
  m_TagString: Fusion
  m_Icon: {fileID: 0}
  m_NavMeshLayer: 0
  m_StaticEditorFlags: 0
  m_IsActive: 1

$components$ in this case is a custom list of many children?
"""

gameobjectYaml = "--- !u!1 &$ref_id$\r\nGameObject:\r\n  m_ObjectHideFlags: 0\r\n  m_CorrespondingSourceObject: {fileID: 0}\r\n  m_PrefabInstance: {fileID: 0}\r\n  m_PrefabAsset: {fileID: 0}\r\n  serializedVersion: 6\r\n  m_Component:\r\n  $components$\r\n  m_Layer: 0\r\n  m_Name: $name$\r\n  m_TagString: Fusion\r\n  m_Icon: {fileID: 0}\r\n  m_NavMeshLayer: 0\r\n  m_StaticEditorFlags: 0\r\n  m_IsActive: 1"


"""
Components

Get a full list of this before assembling gameobject yaml

components are lists of gameobject components that are contained.

they link all the behaviours and transform to the gameobject

  - component: {fileID: $ref_id$}

$ref_id$ is the uuid of the object - minus the tag code
"""

componentYaml = "  - component: {fileID: $ref_id$}\r\n"
