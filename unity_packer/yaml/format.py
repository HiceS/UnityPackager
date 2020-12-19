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
meshyaml = "--- !u!43 &$ref_id$ \nMesh:\n  m_ObjectHideFlags: 0\n  m_CorrespondingSourceObject: {fileID: 0}\n  m_PrefabInstance: {fileID: 0}\n  m_PrefabAsset: {fileID: 0}\n  m_Name: $name$\n  serializedVersion: 10\n  m_SubMeshes:\n  - serializedVersion: 2\n    firstByte: 0\n    indexCount: $index_count$\n    topology: 0\n    baseVertex: 0\n    firstVertex: 0\n    vertexCount: $vertex_count$\n    localAABB:\n      m_Center: {x: $m_center_x$, y: $m_center_y$, z: $m_center_z$}\n      m_Extent: {x: $m_extent_x$, y: $m_extent_y$, z: $m_extent_z$}\n  m_Shapes:\n    vertices: []\n    shapes: []\n    channels: []\n    fullWeights: []\n  m_BindPose: []\n  m_BoneNameHashes: \n  m_RootBoneNameHash: 0\n  m_BonesAABB: []\n  m_VariableBoneCountWeights:\n    m_Data: \n  m_MeshCompression: 0\n  m_IsReadable: 1\n  m_KeepVertices: 1\n  m_KeepIndices: 1\n  m_IndexFormat: 0\n  m_IndexBuffer: $m_index_buffer$\n  m_VertexData:\n    serializedVersion: 3\n    m_VertexCount: $vertex_count$\n    m_Channels:\n    - stream: 0\n      offset: 0\n      format: 0\n      dimension: 3\n    - stream: 0\n      offset: 12\n      format: 0\n      dimension: 3\n    - stream: 0\n      offset: 0\n      format: 0\n      dimension: 0\n    - stream: 0\n      offset: 0\n      format: 0\n      dimension: 0\n    - stream: 0\n      offset: 0\n      format: 0\n      dimension: 0\n    - stream: 0\n      offset: 0\n      format: 0\n      dimension: 0\n    - stream: 0\n      offset: 0\n      format: 0\n      dimension: 0\n    - stream: 0\n      offset: 0\n      format: 0\n      dimension: 0\n    - stream: 0\n      offset: 0\n      format: 0\n      dimension: 0\n    - stream: 0\n      offset: 0\n      format: 0\n      dimension: 0\n    - stream: 0\n      offset: 0\n      format: 0\n      dimension: 0\n    - stream: 0\n      offset: 0\n      format: 0\n      dimension: 0\n    - stream: 0\n      offset: 0\n      format: 0\n      dimension: 0\n    - stream: 0\n      offset: 0\n      format: 0\n      dimension: 0\n    m_DataSize: $m_datasize$\n    _typelessdata: $_typlessdata$\n  m_CompressedMesh:\n    m_Vertices:\n      m_NumItems: 0\n      m_Range: 0\n      m_Start: 0\n      m_Data: \n      m_BitSize: 0\n    m_UV:\n      m_NumItems: 0\n      m_Range: 0\n      m_Start: 0\n      m_Data: \n      m_BitSize: 0\n    m_Normals:\n      m_NumItems: 0\n      m_Range: 0\n      m_Start: 0\n      m_Data: \n      m_BitSize: 0\n    m_Tangents:\n      m_NumItems: 0\n      m_Range: 0\n      m_Start: 0\n      m_Data: \n      m_BitSize: 0\n    m_Weights:\n      m_NumItems: 0\n      m_Data: \n      m_BitSize: 0\n    m_NormalSigns:\n      m_NumItems: 0\n      m_Data: \n      m_BitSize: 0\n    m_TangentSigns:\n      m_NumItems: 0\n      m_Data: \n      m_BitSize: 0\n    m_FloatColors:\n      m_NumItems: 0\n      m_Range: 0\n      m_Start: 0\n      m_Data: \n      m_BitSize: 0\n    m_BoneIndices:\n      m_NumItems: 0\n      m_Data: \n      m_BitSize: 0\n    m_Triangles:\n      m_NumItems: 0\n      m_Data: \n      m_BitSize: 0\n    m_UVInfo: 0\n  m_LocalAABB:\n    m_Center: {x: $m_center_x$, y: $m_center_y$, z: $m_center_z$}\n    m_Extent: {x: $m_extent_x$, y: $m_extent_y$, z: $m_extent_z$}\n  m_MeshUsageFlags: 0\n  m_BakedConvexCollisionMesh: \n  m_BakedTriangleCollisionMesh: \n  m_MeshMetrics[0]: 1\n  m_MeshMetrics[1]: 1\n  m_MeshOptimizationFlags: 1\n  m_StreamData:\n    serializedVersion: 2\n    offset: 0\n    size: 0\n    path: \n"


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

assetmeta = "fileFormatVersion: 2\nguid: $ref_id$\nNativeFormatImporter:\n  externalObjects: {}\n  mainObjectFileID: 0\n  userData: \n  assetBundleName: \n  assetBundleVariant: \n"


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

assetTag = "%YAML 1.1\n%TAG !u! tag:autodesk.com,2020:\n"


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
    "Transform": "4",
    "MonoBehaviour": "114",
    "MeshCollider": "64",
    "MeshFilter": "33",
    "MeshRenderer": "23",
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

gameobjectYaml = "--- !u!1 &$ref_id$\nGameObject:\n  m_ObjectHideFlags: 0\n  m_CorrespondingSourceObject: {fileID: 0}\n  m_PrefabInstance: {fileID: 0}\n  m_PrefabAsset: {fileID: 0}\n  serializedVersion: 6\n  m_Component: $components$\n  m_Layer: 0\n  m_Name: $name$\n  m_TagString: Fusion\n  m_Icon: {fileID: 0}\n  m_NavMeshLayer: 0\n  m_StaticEditorFlags: 0\n  m_IsActive: 1\n"


"""
Components

Get a full list of this before assembling gameobject yaml

components are lists of gameobject components that are contained.

they link all the behaviours and transform to the gameobject

  - component: $com_ref$

$comp_ref$ is the uuid of the object with {fileID: $ref_id}
"""

componentYaml = "  - component: $comp_ref$\n"


""" Transform YAML

Transforms hold the position and hierarchical data for the entire model

--- !u!4 &$ref_id$
Transform:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  m_GameObject: {fileID: $gameobject$}
  m_LocalRotation: {$rotation_quat}
  m_LocalPosition: {$position_vec3$}
  m_LocalScale: {$scale_vec3$}
  m_Children: $children$
  m_Father: {fileID: $parent$}
  m_RootOrder: 0
  m_LocalEulerAnglesHint: {$eulerangle_vec3}

$children$ is a fileID list of 1st level child transforms
$gameobject$ is the refid of the attached gameobject 
$eulerangle_vec3$ can be ignored for now just zero out

"""

transformYaml = "--- !u!4 &$ref_id$\nTransform:\n  m_ObjectHideFlags: 0\n  m_CorrespondingSourceObject: {fileID: 0}\n  m_PrefabInstance: {fileID: 0}\n  m_PrefabAsset: {fileID: 0}\n  m_GameObject: $gameobject$\n  m_LocalRotation: {$rotation_quat$}\n  m_LocalPosition: {$position_vec3$}\n  m_LocalScale: {$scale_vec3$}\n  m_Children: $children$\n  m_Father: {fileID: $parent$}\n  m_RootOrder: 0\n  m_LocalEulerAnglesHint: {$eulerangle_vec3$}\n"


""" MeshFilter

--- !u!33 &3755533088138507875
MeshFilter:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  m_GameObject: {fileID: 669977875962663881}
  m_Mesh: {fileID: -6721464313969591390, guid: 5c92ab0f3bea0294eae6ee449cd7a915, type: 2}

"""

meshFilterYaml = "--- !u!33 &$ref_id$\nMeshFilter:\n  m_ObjectHideFlags: 0\n  m_CorrespondingSourceObject: {fileID: 0}\n  m_PrefabInstance: {fileID: 0}\n  m_PrefabAsset: {fileID: 0}\n  m_GameObject: $gameobject_fileID$\n  m_Mesh: $mesh_ref_fileID$\n"


""" MeshRenderer

Meshrenderer links the meshfilter to the mats etc

--- !u!23 &6226678516181316638
MeshRenderer:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  m_GameObject: {fileID: 669977875962663881}
  m_Enabled: 1
  m_CastShadows: 1
  m_ReceiveShadows: 1
  m_DynamicOccludee: 1
  m_MotionVectors: 1
  m_LightProbeUsage: 1
  m_ReflectionProbeUsage: 1
  m_RayTracingMode: 2
  m_RayTraceProcedural: 0
  m_RenderingLayerMask: 1
  m_RendererPriority: 0
  m_Materials:
  - {fileID: 0}
  m_StaticBatchInfo:
    firstSubMesh: 0
    subMeshCount: 0
  m_StaticBatchRoot: {fileID: 0}
  m_ProbeAnchor: {fileID: 0}
  m_LightProbeVolumeOverride: {fileID: 0}
  m_ScaleInLightmap: 1
  m_ReceiveGI: 1
  m_PreserveUVs: 0
  m_IgnoreNormalsForChartDetection: 0
  m_ImportantGI: 0
  m_StitchLightmapSeams: 1
  m_SelectedEditorRenderState: 3
  m_MinimumChartSize: 4
  m_AutoUVMaxDistance: 0.5
  m_AutoUVMaxAngle: 89
  m_LightmapParameters: {fileID: 0}
  m_SortingLayerID: 0
  m_SortingLayer: 0
  m_SortingOrder: 0
  m_AdditionalVertexStreams: {fileID: 0}
"""

meshRendererYaml = "--- !u!23 &$ref_id$\nMeshRenderer:\n  m_ObjectHideFlags: 0\n  m_CorrespondingSourceObject: {fileID: 0}\n  m_PrefabInstance: {fileID: 0}\n  m_PrefabAsset: {fileID: 0}\n  m_GameObject: $gameobject_fileID$\n  m_Enabled: 1\n  m_CastShadows: 1\n  m_ReceiveShadows: 1\n  m_DynamicOccludee: 1\n  m_MotionVectors: 1\n  m_LightProbeUsage: 1\n  m_ReflectionProbeUsage: 1\n  m_RayTracingMode: 2\n  m_RayTraceProcedural: 0\n  m_RenderingLayerMask: 1\n  m_RendererPriority: 0\n  m_Materials: $materials$\n  m_StaticBatchInfo:\n    firstSubMesh: 0\n    subMeshCount: 0\n  m_StaticBatchRoot: {fileID: 0}\n  m_ProbeAnchor: {fileID: 0}\n  m_LightProbeVolumeOverride: {fileID: 0}\n  m_ScaleInLightmap: 1\n  m_ReceiveGI: 1\n  m_PreserveUVs: 0\n  m_IgnoreNormalsForChartDetection: 0\n  m_ImportantGI: 0\n  m_StitchLightmapSeams: 1\n  m_SelectedEditorRenderState: 3\n  m_MinimumChartSize: 4\n  m_AutoUVMaxDistance: 0.5\n  m_AutoUVMaxAngle: 89\n  m_LightmapParameters: {fileID: 0}\n  m_SortingLayerID: 0\n  m_SortingLayer: 0\n  m_SortingOrder: 0\n  m_AdditionalVertexStreams: {fileID: 0}\n"

""" Material from basic 3D application with regular shader


"""

matBasicYaml = "--- !u!21 &$ref_id$\nMaterial:\n  serializedVersion: 6\n  m_ObjectHideFlags: 0\n  m_CorrespondingSourceObject: {fileID: 0}\n  m_PrefabInstance: {fileID: 0}\n  m_PrefabAsset: {fileID: 0}\n  m_Name: $name$\n  m_Shader: {fileID: 46, guid: 0000000000000000f000000000000000, type: 0}\n  m_ShaderKeywords: \n  m_LightmapFlags: 4\n  m_EnableInstancingVariants: 0\n  m_DoubleSidedGI: 0\n  m_CustomRenderQueue: -1\n  stringTagMap: {}\n  disabledShaderPasses: []\n  m_SavedProperties:\n    serializedVersion: 3\n    m_TexEnvs:\n    - _BumpMap:\n        m_Texture: {fileID: 0}\n        m_Scale: {x: 1, y: 1}\n        m_Offset: {x: 0, y: 0}\n    - _DetailAlbedoMap:\n        m_Texture: {fileID: 0}\n        m_Scale: {x: 1, y: 1}\n        m_Offset: {x: 0, y: 0}\n    - _DetailMask:\n        m_Texture: {fileID: 0}\n        m_Scale: {x: 1, y: 1}\n        m_Offset: {x: 0, y: 0}\n    - _DetailNormalMap:\n        m_Texture: {fileID: 0}\n        m_Scale: {x: 1, y: 1}\n        m_Offset: {x: 0, y: 0}\n    - _EmissionMap:\n        m_Texture: {fileID: 0}\n        m_Scale: {x: 1, y: 1}\n        m_Offset: {x: 0, y: 0}\n    - _MainTex:\n        m_Texture: {fileID: 0}\n        m_Scale: {x: 1, y: 1}\n        m_Offset: {x: 0, y: 0}\n    - _MetallicGlossMap:\n        m_Texture: {fileID: 0}\n        m_Scale: {x: 1, y: 1}\n        m_Offset: {x: 0, y: 0}\n    - _OcclusionMap:\n        m_Texture: {fileID: 0}\n        m_Scale: {x: 1, y: 1}\n        m_Offset: {x: 0, y: 0}\n    - _ParallaxMap:\n        m_Texture: {fileID: 0}\n        m_Scale: {x: 1, y: 1}\n        m_Offset: {x: 0, y: 0}\n    m_Floats:\n    - _BumpScale: 1\n    - _Cutoff: 0.5\n    - _DetailNormalMapScale: 1\n    - _DstBlend: 0\n    - _GlossMapScale: 1\n    - _Glossiness: $smoothness$\n    - _GlossyReflections: 1\n    - _Metallic: $metallic$\n    - _Mode: 0\n    - _OcclusionStrength: 1\n    - _Parallax: 0.02\n    - _SmoothnessTextureChannel: 0\n    - _SpecularHighlights: 1\n    - _SrcBlend: 1\n    - _UVSec: 0\n    - _ZWrite: 1\n    m_Colors:\n    - _Color: {r: $albedo_r$, g: $albedo_g$, b: $albedo_b$, a: $albedo_a$}\n    - _EmissionColor: {r: 0, g: 0, b: 0, a: 1}\n  m_BuildTextureStacks: []\n"


"""
script_file_ref ->
  {fileID: 11500000, guid: b0a637dba5cf9a7429d2f64ccb998f9e, type: 3}
"""
monoScriptReference = "--- !u!114 &$ref_id$\nMonoBehaviour:\n  m_ObjectHideFlags: 0\n  m_CorrespondingSourceObject: {fileID: 0}\n  m_PrefabInstance: {fileID: 0}\n  m_PrefabAsset: {fileID: 0}\n  m_GameObject: $gameobject_fileID$\n  m_Enabled: 1\n  m_EditorHideFlags: 0\n  m_Script: $script_file_ref$\n  m_Name: \n  m_EditorClassIdentifier: \n  centerOfMass: {$centerOfMass$}\n  mass: $mass$\n  surfaceArea: $surface_area$\n"

"""
  Mesh Collider
  For now always convex and they can change it

  $ref_id$
  $gameobject_fileID$
  $mesh_ref_fileID$
"""
meshCollider = "--- !u!64 &$red_id$\nMeshCollider:\n  m_ObjectHideFlags: 0\n  m_CorrespondingSourceObject: {fileID: 0}\n  m_PrefabInstance: {fileID: 0}\n  m_PrefabAsset: {fileID: 0}\n  m_GameObject: $gameobject_fileID$\n  m_Material: {fileID: 0}\n  m_IsTrigger: 0\n  m_Enabled: 1\n  serializedVersion: 4\n  m_Convex: 1\n  m_CookingOptions: 30\n  m_Mesh: $mesh_ref_fileID$\n"


"""
  RigidBody

  $ref_id$
  $gameobject_fileID$
  $mass$

  for now no custom materials or anything
"""
rigidBodyYaml = "--- !u!54 &$red_id$\nRigidbody:\n  m_ObjectHideFlags: 0\n  m_CorrespondingSourceObject: {fileID: 0}\n  m_PrefabInstance: {fileID: 0}\n  m_PrefabAsset: {fileID: 0}\n  m_GameObject: $gameobject_fileID$\n  serializedVersion: 2\n  m_Mass: $mass$\n  m_Drag: 0\n  m_AngularDrag: 0.05\n  m_UseGravity: 1\n  m_IsKinematic: 0\n  m_Interpolate: 0\n  m_Constraints: 0\n  m_CollisionDetection: 0\n"