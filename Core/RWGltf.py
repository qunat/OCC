# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
RWGltf module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_rwgltf.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _RWGltf
else:
    import _RWGltf

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _RWGltf.SWIG_PyInstanceMethod_New
_swig_new_static_method = _RWGltf.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _RWGltf.delete_SwigPyIterator
    value = _swig_new_instance_method(_RWGltf.SwigPyIterator_value)
    incr = _swig_new_instance_method(_RWGltf.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_RWGltf.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_RWGltf.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_RWGltf.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_RWGltf.SwigPyIterator_copy)
    next = _swig_new_instance_method(_RWGltf.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_RWGltf.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_RWGltf.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_RWGltf.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_RWGltf.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_RWGltf.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_RWGltf.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_RWGltf.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_RWGltf.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_RWGltf.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _RWGltf:
_RWGltf.SwigPyIterator_swigregister(SwigPyIterator)


def _dumps_object(klass):
    """ Overwrite default string output for any wrapped object.
    By default, __repr__ method returns something like:
    <OCC.Core.TopoDS.TopoDS_Shape; proxy of <Swig Object of type 'TopoDS_Shape *' at 0x02BB0758> >
    This is too much verbose.
    We prefer :
    <class 'gp_Pnt'>
    or
    <class 'TopoDS_Shape'>
    """
    klass_name = str(klass.__class__).split(".")[3].split("'")[0]
    repr_string = "<class '" + klass_name + "'"
# for TopoDS_Shape, we also look for the base type
    if klass_name == "TopoDS_Shape":
        if klass.IsNull():
            repr_string += ": Null>"
            return repr_string
        st = klass.ShapeType()
        types = {OCC.Core.TopAbs.TopAbs_VERTEX: "Vertex",
                 OCC.Core.TopAbs.TopAbs_SOLID: "Solid",
                 OCC.Core.TopAbs.TopAbs_EDGE: "Edge",
                 OCC.Core.TopAbs.TopAbs_FACE: "Face",
                 OCC.Core.TopAbs.TopAbs_SHELL: "Shell",
                 OCC.Core.TopAbs.TopAbs_WIRE: "Wire",
                 OCC.Core.TopAbs.TopAbs_COMPOUND: "Compound",
                 OCC.Core.TopAbs.TopAbs_COMPSOLID: "Compsolid"}
        repr_string += "; Type:%s" % types[st]        
    elif hasattr(klass, "IsNull"):
        if klass.IsNull():
            repr_string += "; Null"
    repr_string += ">"
    return repr_string


from six import with_metaclass
import warnings
from OCC.Wrapper.wrapper_utils import Proxy, deprecated

import OCC.Core.Standard
import OCC.Core.NCollection
RWGltf_GltfPrimitiveMode_UNKNOWN = _RWGltf.RWGltf_GltfPrimitiveMode_UNKNOWN
RWGltf_GltfPrimitiveMode_Points = _RWGltf.RWGltf_GltfPrimitiveMode_Points
RWGltf_GltfPrimitiveMode_Lines = _RWGltf.RWGltf_GltfPrimitiveMode_Lines
RWGltf_GltfPrimitiveMode_LineLoop = _RWGltf.RWGltf_GltfPrimitiveMode_LineLoop
RWGltf_GltfPrimitiveMode_LineStrip = _RWGltf.RWGltf_GltfPrimitiveMode_LineStrip
RWGltf_GltfPrimitiveMode_Triangles = _RWGltf.RWGltf_GltfPrimitiveMode_Triangles
RWGltf_GltfPrimitiveMode_TriangleStrip = _RWGltf.RWGltf_GltfPrimitiveMode_TriangleStrip
RWGltf_GltfPrimitiveMode_TriangleFan = _RWGltf.RWGltf_GltfPrimitiveMode_TriangleFan
RWGltf_GltfBufferViewTarget_UNKNOWN = _RWGltf.RWGltf_GltfBufferViewTarget_UNKNOWN
RWGltf_GltfBufferViewTarget_ARRAY_BUFFER = _RWGltf.RWGltf_GltfBufferViewTarget_ARRAY_BUFFER
RWGltf_GltfBufferViewTarget_ELEMENT_ARRAY_BUFFER = _RWGltf.RWGltf_GltfBufferViewTarget_ELEMENT_ARRAY_BUFFER
RWGltf_GltfArrayType_UNKNOWN = _RWGltf.RWGltf_GltfArrayType_UNKNOWN
RWGltf_GltfArrayType_Indices = _RWGltf.RWGltf_GltfArrayType_Indices
RWGltf_GltfArrayType_Position = _RWGltf.RWGltf_GltfArrayType_Position
RWGltf_GltfArrayType_Normal = _RWGltf.RWGltf_GltfArrayType_Normal
RWGltf_GltfArrayType_Color = _RWGltf.RWGltf_GltfArrayType_Color
RWGltf_GltfArrayType_TCoord0 = _RWGltf.RWGltf_GltfArrayType_TCoord0
RWGltf_GltfArrayType_TCoord1 = _RWGltf.RWGltf_GltfArrayType_TCoord1
RWGltf_GltfArrayType_Joint = _RWGltf.RWGltf_GltfArrayType_Joint
RWGltf_GltfArrayType_Weight = _RWGltf.RWGltf_GltfArrayType_Weight
RWGltf_GltfRootElement_Asset = _RWGltf.RWGltf_GltfRootElement_Asset
RWGltf_GltfRootElement_Scenes = _RWGltf.RWGltf_GltfRootElement_Scenes
RWGltf_GltfRootElement_Scene = _RWGltf.RWGltf_GltfRootElement_Scene
RWGltf_GltfRootElement_Nodes = _RWGltf.RWGltf_GltfRootElement_Nodes
RWGltf_GltfRootElement_Meshes = _RWGltf.RWGltf_GltfRootElement_Meshes
RWGltf_GltfRootElement_Accessors = _RWGltf.RWGltf_GltfRootElement_Accessors
RWGltf_GltfRootElement_BufferViews = _RWGltf.RWGltf_GltfRootElement_BufferViews
RWGltf_GltfRootElement_Buffers = _RWGltf.RWGltf_GltfRootElement_Buffers
RWGltf_GltfRootElement_NB_MANDATORY = _RWGltf.RWGltf_GltfRootElement_NB_MANDATORY
RWGltf_GltfRootElement_Animations = _RWGltf.RWGltf_GltfRootElement_Animations
RWGltf_GltfRootElement_Materials = _RWGltf.RWGltf_GltfRootElement_Materials
RWGltf_GltfRootElement_Programs = _RWGltf.RWGltf_GltfRootElement_Programs
RWGltf_GltfRootElement_Samplers = _RWGltf.RWGltf_GltfRootElement_Samplers
RWGltf_GltfRootElement_Shaders = _RWGltf.RWGltf_GltfRootElement_Shaders
RWGltf_GltfRootElement_Skins = _RWGltf.RWGltf_GltfRootElement_Skins
RWGltf_GltfRootElement_Techniques = _RWGltf.RWGltf_GltfRootElement_Techniques
RWGltf_GltfRootElement_Textures = _RWGltf.RWGltf_GltfRootElement_Textures
RWGltf_GltfRootElement_Images = _RWGltf.RWGltf_GltfRootElement_Images
RWGltf_GltfRootElement_ExtensionsUsed = _RWGltf.RWGltf_GltfRootElement_ExtensionsUsed
RWGltf_GltfRootElement_ExtensionsRequired = _RWGltf.RWGltf_GltfRootElement_ExtensionsRequired
RWGltf_GltfRootElement_NB = _RWGltf.RWGltf_GltfRootElement_NB
RWGltf_GltfAccessorCompType_UNKNOWN = _RWGltf.RWGltf_GltfAccessorCompType_UNKNOWN
RWGltf_GltfAccessorCompType_Int8 = _RWGltf.RWGltf_GltfAccessorCompType_Int8
RWGltf_GltfAccessorCompType_UInt8 = _RWGltf.RWGltf_GltfAccessorCompType_UInt8
RWGltf_GltfAccessorCompType_Int16 = _RWGltf.RWGltf_GltfAccessorCompType_Int16
RWGltf_GltfAccessorCompType_UInt16 = _RWGltf.RWGltf_GltfAccessorCompType_UInt16
RWGltf_GltfAccessorCompType_UInt32 = _RWGltf.RWGltf_GltfAccessorCompType_UInt32
RWGltf_GltfAccessorCompType_Float32 = _RWGltf.RWGltf_GltfAccessorCompType_Float32
RWGltf_GltfAccessorLayout_UNKNOWN = _RWGltf.RWGltf_GltfAccessorLayout_UNKNOWN
RWGltf_GltfAccessorLayout_Scalar = _RWGltf.RWGltf_GltfAccessorLayout_Scalar
RWGltf_GltfAccessorLayout_Vec2 = _RWGltf.RWGltf_GltfAccessorLayout_Vec2
RWGltf_GltfAccessorLayout_Vec3 = _RWGltf.RWGltf_GltfAccessorLayout_Vec3
RWGltf_GltfAccessorLayout_Vec4 = _RWGltf.RWGltf_GltfAccessorLayout_Vec4
RWGltf_GltfAccessorLayout_Mat2 = _RWGltf.RWGltf_GltfAccessorLayout_Mat2
RWGltf_GltfAccessorLayout_Mat3 = _RWGltf.RWGltf_GltfAccessorLayout_Mat3
RWGltf_GltfAccessorLayout_Mat4 = _RWGltf.RWGltf_GltfAccessorLayout_Mat4
Handle_RWGltf_MaterialCommon_Create = _RWGltf.Handle_RWGltf_MaterialCommon_Create
Handle_RWGltf_MaterialCommon_DownCast = _RWGltf.Handle_RWGltf_MaterialCommon_DownCast
Handle_RWGltf_MaterialCommon_IsNull = _RWGltf.Handle_RWGltf_MaterialCommon_IsNull
Handle_RWGltf_MaterialMetallicRoughness_Create = _RWGltf.Handle_RWGltf_MaterialMetallicRoughness_Create
Handle_RWGltf_MaterialMetallicRoughness_DownCast = _RWGltf.Handle_RWGltf_MaterialMetallicRoughness_DownCast
Handle_RWGltf_MaterialMetallicRoughness_IsNull = _RWGltf.Handle_RWGltf_MaterialMetallicRoughness_IsNull
class RWGltf_GltfAccessor(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Id = property(_RWGltf.RWGltf_GltfAccessor_Id_get, _RWGltf.RWGltf_GltfAccessor_Id_set)
    ByteOffset = property(_RWGltf.RWGltf_GltfAccessor_ByteOffset_get, _RWGltf.RWGltf_GltfAccessor_ByteOffset_set)
    Count = property(_RWGltf.RWGltf_GltfAccessor_Count_get, _RWGltf.RWGltf_GltfAccessor_Count_set)
    ByteStride = property(_RWGltf.RWGltf_GltfAccessor_ByteStride_get, _RWGltf.RWGltf_GltfAccessor_ByteStride_set)
    Type = property(_RWGltf.RWGltf_GltfAccessor_Type_get, _RWGltf.RWGltf_GltfAccessor_Type_set)
    ComponentType = property(_RWGltf.RWGltf_GltfAccessor_ComponentType_get, _RWGltf.RWGltf_GltfAccessor_ComponentType_set)
    BndBox = property(_RWGltf.RWGltf_GltfAccessor_BndBox_get, _RWGltf.RWGltf_GltfAccessor_BndBox_set)

    def __init__(self, *args):
        r"""
        * //!< bounding box Empty constructor.
        	:rtype: None
        """
        _RWGltf.RWGltf_GltfAccessor_swiginit(self, _RWGltf.new_RWGltf_GltfAccessor(*args))

    __repr__ = _dumps_object

    __swig_destroy__ = _RWGltf.delete_RWGltf_GltfAccessor

# Register RWGltf_GltfAccessor in _RWGltf:
_RWGltf.RWGltf_GltfAccessor_swigregister(RWGltf_GltfAccessor)

class RWGltf_GltfBufferView(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Id = property(_RWGltf.RWGltf_GltfBufferView_Id_get, _RWGltf.RWGltf_GltfBufferView_Id_set)
    ByteOffset = property(_RWGltf.RWGltf_GltfBufferView_ByteOffset_get, _RWGltf.RWGltf_GltfBufferView_ByteOffset_set)
    ByteLength = property(_RWGltf.RWGltf_GltfBufferView_ByteLength_get, _RWGltf.RWGltf_GltfBufferView_ByteLength_set)
    ByteStride = property(_RWGltf.RWGltf_GltfBufferView_ByteStride_get, _RWGltf.RWGltf_GltfBufferView_ByteStride_set)
    Target = property(_RWGltf.RWGltf_GltfBufferView_Target_get, _RWGltf.RWGltf_GltfBufferView_Target_set)

    def __init__(self, *args):
        r""":rtype: None"""
        _RWGltf.RWGltf_GltfBufferView_swiginit(self, _RWGltf.new_RWGltf_GltfBufferView(*args))

    __repr__ = _dumps_object

    __swig_destroy__ = _RWGltf.delete_RWGltf_GltfBufferView

# Register RWGltf_GltfBufferView in _RWGltf:
_RWGltf.RWGltf_GltfBufferView_swigregister(RWGltf_GltfBufferView)

class RWGltf_GltfFace(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    NodePos = property(_RWGltf.RWGltf_GltfFace_NodePos_get, _RWGltf.RWGltf_GltfFace_NodePos_set)
    NodeNorm = property(_RWGltf.RWGltf_GltfFace_NodeNorm_get, _RWGltf.RWGltf_GltfFace_NodeNorm_set)
    NodeUV = property(_RWGltf.RWGltf_GltfFace_NodeUV_get, _RWGltf.RWGltf_GltfFace_NodeUV_set)
    Indices = property(_RWGltf.RWGltf_GltfFace_Indices_get, _RWGltf.RWGltf_GltfFace_Indices_set)

    __repr__ = _dumps_object


    def __init__(self):
        _RWGltf.RWGltf_GltfFace_swiginit(self, _RWGltf.new_RWGltf_GltfFace())
    __swig_destroy__ = _RWGltf.delete_RWGltf_GltfFace

# Register RWGltf_GltfFace in _RWGltf:
_RWGltf.RWGltf_GltfFace_swigregister(RWGltf_GltfFace)

class RWGltf_GltfPrimArrayData(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    StreamData = property(_RWGltf.RWGltf_GltfPrimArrayData_StreamData_get, _RWGltf.RWGltf_GltfPrimArrayData_StreamData_set)
    StreamUri = property(_RWGltf.RWGltf_GltfPrimArrayData_StreamUri_get, _RWGltf.RWGltf_GltfPrimArrayData_StreamUri_set)
    StreamOffset = property(_RWGltf.RWGltf_GltfPrimArrayData_StreamOffset_get, _RWGltf.RWGltf_GltfPrimArrayData_StreamOffset_set)
    Accessor = property(_RWGltf.RWGltf_GltfPrimArrayData_Accessor_get, _RWGltf.RWGltf_GltfPrimArrayData_Accessor_set)
    Type = property(_RWGltf.RWGltf_GltfPrimArrayData_Type_get, _RWGltf.RWGltf_GltfPrimArrayData_Type_set)

    def __init__(self, *args):
        r"""
        :rtype: None:param theType:
        	:type theType: RWGltf_GltfArrayType
        	:rtype: None
        """
        _RWGltf.RWGltf_GltfPrimArrayData_swiginit(self, _RWGltf.new_RWGltf_GltfPrimArrayData(*args))

    __repr__ = _dumps_object

    __swig_destroy__ = _RWGltf.delete_RWGltf_GltfPrimArrayData

# Register RWGltf_GltfPrimArrayData in _RWGltf:
_RWGltf.RWGltf_GltfPrimArrayData_swigregister(RWGltf_GltfPrimArrayData)

class RWGltf_MaterialCommon(OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    AmbientTexture = property(_RWGltf.RWGltf_MaterialCommon_AmbientTexture_get, _RWGltf.RWGltf_MaterialCommon_AmbientTexture_set)
    DiffuseTexture = property(_RWGltf.RWGltf_MaterialCommon_DiffuseTexture_get, _RWGltf.RWGltf_MaterialCommon_DiffuseTexture_set)
    SpecularTexture = property(_RWGltf.RWGltf_MaterialCommon_SpecularTexture_get, _RWGltf.RWGltf_MaterialCommon_SpecularTexture_set)
    Id = property(_RWGltf.RWGltf_MaterialCommon_Id_get, _RWGltf.RWGltf_MaterialCommon_Id_set)
    Name = property(_RWGltf.RWGltf_MaterialCommon_Name_get, _RWGltf.RWGltf_MaterialCommon_Name_set)
    AmbientColor = property(_RWGltf.RWGltf_MaterialCommon_AmbientColor_get, _RWGltf.RWGltf_MaterialCommon_AmbientColor_set)
    DiffuseColor = property(_RWGltf.RWGltf_MaterialCommon_DiffuseColor_get, _RWGltf.RWGltf_MaterialCommon_DiffuseColor_set)
    SpecularColor = property(_RWGltf.RWGltf_MaterialCommon_SpecularColor_get, _RWGltf.RWGltf_MaterialCommon_SpecularColor_set)
    EmissiveColor = property(_RWGltf.RWGltf_MaterialCommon_EmissiveColor_get, _RWGltf.RWGltf_MaterialCommon_EmissiveColor_set)
    Shininess = property(_RWGltf.RWGltf_MaterialCommon_Shininess_get, _RWGltf.RWGltf_MaterialCommon_Shininess_set)
    Transparency = property(_RWGltf.RWGltf_MaterialCommon_Transparency_get, _RWGltf.RWGltf_MaterialCommon_Transparency_set)

    def __init__(self, *args):
        r""":rtype: None"""
        _RWGltf.RWGltf_MaterialCommon_swiginit(self, _RWGltf.new_RWGltf_MaterialCommon(*args))


    @staticmethod
    def DownCast(t):
      return Handle_RWGltf_MaterialCommon_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _RWGltf.delete_RWGltf_MaterialCommon

# Register RWGltf_MaterialCommon in _RWGltf:
_RWGltf.RWGltf_MaterialCommon_swigregister(RWGltf_MaterialCommon)

class RWGltf_MaterialMetallicRoughness(OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    BaseColorTexture = property(_RWGltf.RWGltf_MaterialMetallicRoughness_BaseColorTexture_get, _RWGltf.RWGltf_MaterialMetallicRoughness_BaseColorTexture_set)
    MetallicRoughnessTexture = property(_RWGltf.RWGltf_MaterialMetallicRoughness_MetallicRoughnessTexture_get, _RWGltf.RWGltf_MaterialMetallicRoughness_MetallicRoughnessTexture_set)
    EmissiveTexture = property(_RWGltf.RWGltf_MaterialMetallicRoughness_EmissiveTexture_get, _RWGltf.RWGltf_MaterialMetallicRoughness_EmissiveTexture_set)
    OcclusionTexture = property(_RWGltf.RWGltf_MaterialMetallicRoughness_OcclusionTexture_get, _RWGltf.RWGltf_MaterialMetallicRoughness_OcclusionTexture_set)
    NormalTexture = property(_RWGltf.RWGltf_MaterialMetallicRoughness_NormalTexture_get, _RWGltf.RWGltf_MaterialMetallicRoughness_NormalTexture_set)
    Id = property(_RWGltf.RWGltf_MaterialMetallicRoughness_Id_get, _RWGltf.RWGltf_MaterialMetallicRoughness_Id_set)
    Name = property(_RWGltf.RWGltf_MaterialMetallicRoughness_Name_get, _RWGltf.RWGltf_MaterialMetallicRoughness_Name_set)
    BaseColor = property(_RWGltf.RWGltf_MaterialMetallicRoughness_BaseColor_get, _RWGltf.RWGltf_MaterialMetallicRoughness_BaseColor_set)
    EmissiveFactor = property(_RWGltf.RWGltf_MaterialMetallicRoughness_EmissiveFactor_get, _RWGltf.RWGltf_MaterialMetallicRoughness_EmissiveFactor_set)
    Metallic = property(_RWGltf.RWGltf_MaterialMetallicRoughness_Metallic_get, _RWGltf.RWGltf_MaterialMetallicRoughness_Metallic_set)
    Roughness = property(_RWGltf.RWGltf_MaterialMetallicRoughness_Roughness_get, _RWGltf.RWGltf_MaterialMetallicRoughness_Roughness_set)

    def __init__(self, *args):
        r"""
        * //!< roughness (or scale factor to the texture) within range [0.0, 1.0]; 1.0 by default
        	:rtype: None
        """
        _RWGltf.RWGltf_MaterialMetallicRoughness_swiginit(self, _RWGltf.new_RWGltf_MaterialMetallicRoughness(*args))


    @staticmethod
    def DownCast(t):
      return Handle_RWGltf_MaterialMetallicRoughness_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _RWGltf.delete_RWGltf_MaterialMetallicRoughness

# Register RWGltf_MaterialMetallicRoughness in _RWGltf:
_RWGltf.RWGltf_MaterialMetallicRoughness_swigregister(RWGltf_MaterialMetallicRoughness)



