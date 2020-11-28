# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
Draft module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_draft.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _Draft
else:
    import _Draft

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _Draft.SWIG_PyInstanceMethod_New
_swig_new_static_method = _Draft.SWIG_PyStaticMethod_New

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
    __swig_destroy__ = _Draft.delete_SwigPyIterator
    value = _swig_new_instance_method(_Draft.SwigPyIterator_value)
    incr = _swig_new_instance_method(_Draft.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_Draft.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_Draft.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_Draft.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_Draft.SwigPyIterator_copy)
    next = _swig_new_instance_method(_Draft.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_Draft.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_Draft.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_Draft.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_Draft.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_Draft.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_Draft.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_Draft.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_Draft.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_Draft.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _Draft:
_Draft.SwigPyIterator_swigregister(SwigPyIterator)


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
import OCC.Core.TopoDS
import OCC.Core.Message
import OCC.Core.TopAbs
import OCC.Core.TopLoc
import OCC.Core.gp
import OCC.Core.Geom2d
import OCC.Core.GeomAbs
import OCC.Core.TColgp
import OCC.Core.TColStd
import OCC.Core.TCollection
import OCC.Core.Geom
import OCC.Core.BRepTools
import OCC.Core.Bnd
import OCC.Core.BVH
import OCC.Core.TopTools
import OCC.Core.BRep
import OCC.Core.Poly
import OCC.Core.TShort
Draft_NoError = _Draft.Draft_NoError
Draft_FaceRecomputation = _Draft.Draft_FaceRecomputation
Draft_EdgeRecomputation = _Draft.Draft_EdgeRecomputation
Draft_VertexRecomputation = _Draft.Draft_VertexRecomputation
Handle_Draft_Modification_Create = _Draft.Handle_Draft_Modification_Create
Handle_Draft_Modification_DownCast = _Draft.Handle_Draft_Modification_DownCast
Handle_Draft_Modification_IsNull = _Draft.Handle_Draft_Modification_IsNull
class Draft_IndexedDataMapOfFaceFaceInfo(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfFaceFaceInfo_begin)
    end = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfFaceFaceInfo_end)
    cbegin = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfFaceFaceInfo_cbegin)
    cend = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfFaceFaceInfo_cend)

    def __init__(self, *args):
        _Draft.Draft_IndexedDataMapOfFaceFaceInfo_swiginit(self, _Draft.new_Draft_IndexedDataMapOfFaceFaceInfo(*args))
    Exchange = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfFaceFaceInfo_Exchange)
    Assign = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfFaceFaceInfo_Assign)
    Set = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfFaceFaceInfo_Set)
    ReSize = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfFaceFaceInfo_ReSize)
    Add = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfFaceFaceInfo_Add)
    Contains = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfFaceFaceInfo_Contains)
    Substitute = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfFaceFaceInfo_Substitute)
    Swap = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfFaceFaceInfo_Swap)
    RemoveLast = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfFaceFaceInfo_RemoveLast)
    RemoveFromIndex = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfFaceFaceInfo_RemoveFromIndex)
    RemoveKey = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfFaceFaceInfo_RemoveKey)
    FindKey = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfFaceFaceInfo_FindKey)
    FindFromIndex = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfFaceFaceInfo_FindFromIndex)
    ChangeFromIndex = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfFaceFaceInfo_ChangeFromIndex)
    __call__ = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfFaceFaceInfo___call__)
    FindIndex = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfFaceFaceInfo_FindIndex)
    ChangeFromKey = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfFaceFaceInfo_ChangeFromKey)
    Seek = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfFaceFaceInfo_Seek)
    ChangeSeek = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfFaceFaceInfo_ChangeSeek)
    FindFromKey = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfFaceFaceInfo_FindFromKey)
    Clear = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfFaceFaceInfo_Clear)
    __swig_destroy__ = _Draft.delete_Draft_IndexedDataMapOfFaceFaceInfo
    Size = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfFaceFaceInfo_Size)

# Register Draft_IndexedDataMapOfFaceFaceInfo in _Draft:
_Draft.Draft_IndexedDataMapOfFaceFaceInfo_swigregister(Draft_IndexedDataMapOfFaceFaceInfo)

class Draft_IndexedDataMapOfVertexVertexInfo(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfVertexVertexInfo_begin)
    end = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfVertexVertexInfo_end)
    cbegin = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfVertexVertexInfo_cbegin)
    cend = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfVertexVertexInfo_cend)

    def __init__(self, *args):
        _Draft.Draft_IndexedDataMapOfVertexVertexInfo_swiginit(self, _Draft.new_Draft_IndexedDataMapOfVertexVertexInfo(*args))
    Exchange = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfVertexVertexInfo_Exchange)
    Assign = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfVertexVertexInfo_Assign)
    Set = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfVertexVertexInfo_Set)
    ReSize = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfVertexVertexInfo_ReSize)
    Add = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfVertexVertexInfo_Add)
    Contains = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfVertexVertexInfo_Contains)
    Substitute = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfVertexVertexInfo_Substitute)
    Swap = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfVertexVertexInfo_Swap)
    RemoveLast = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfVertexVertexInfo_RemoveLast)
    RemoveFromIndex = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfVertexVertexInfo_RemoveFromIndex)
    RemoveKey = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfVertexVertexInfo_RemoveKey)
    FindKey = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfVertexVertexInfo_FindKey)
    FindFromIndex = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfVertexVertexInfo_FindFromIndex)
    ChangeFromIndex = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfVertexVertexInfo_ChangeFromIndex)
    __call__ = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfVertexVertexInfo___call__)
    FindIndex = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfVertexVertexInfo_FindIndex)
    ChangeFromKey = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfVertexVertexInfo_ChangeFromKey)
    Seek = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfVertexVertexInfo_Seek)
    ChangeSeek = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfVertexVertexInfo_ChangeSeek)
    FindFromKey = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfVertexVertexInfo_FindFromKey)
    Clear = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfVertexVertexInfo_Clear)
    __swig_destroy__ = _Draft.delete_Draft_IndexedDataMapOfVertexVertexInfo
    Size = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfVertexVertexInfo_Size)

# Register Draft_IndexedDataMapOfVertexVertexInfo in _Draft:
_Draft.Draft_IndexedDataMapOfVertexVertexInfo_swigregister(Draft_IndexedDataMapOfVertexVertexInfo)

class Draft_IndexedDataMapOfEdgeEdgeInfo(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfEdgeEdgeInfo_begin)
    end = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfEdgeEdgeInfo_end)
    cbegin = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfEdgeEdgeInfo_cbegin)
    cend = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfEdgeEdgeInfo_cend)

    def __init__(self, *args):
        _Draft.Draft_IndexedDataMapOfEdgeEdgeInfo_swiginit(self, _Draft.new_Draft_IndexedDataMapOfEdgeEdgeInfo(*args))
    Exchange = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfEdgeEdgeInfo_Exchange)
    Assign = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfEdgeEdgeInfo_Assign)
    Set = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfEdgeEdgeInfo_Set)
    ReSize = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfEdgeEdgeInfo_ReSize)
    Add = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfEdgeEdgeInfo_Add)
    Contains = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfEdgeEdgeInfo_Contains)
    Substitute = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfEdgeEdgeInfo_Substitute)
    Swap = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfEdgeEdgeInfo_Swap)
    RemoveLast = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfEdgeEdgeInfo_RemoveLast)
    RemoveFromIndex = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfEdgeEdgeInfo_RemoveFromIndex)
    RemoveKey = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfEdgeEdgeInfo_RemoveKey)
    FindKey = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfEdgeEdgeInfo_FindKey)
    FindFromIndex = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfEdgeEdgeInfo_FindFromIndex)
    ChangeFromIndex = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfEdgeEdgeInfo_ChangeFromIndex)
    __call__ = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfEdgeEdgeInfo___call__)
    FindIndex = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfEdgeEdgeInfo_FindIndex)
    ChangeFromKey = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfEdgeEdgeInfo_ChangeFromKey)
    Seek = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfEdgeEdgeInfo_Seek)
    ChangeSeek = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfEdgeEdgeInfo_ChangeSeek)
    FindFromKey = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfEdgeEdgeInfo_FindFromKey)
    Clear = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfEdgeEdgeInfo_Clear)
    __swig_destroy__ = _Draft.delete_Draft_IndexedDataMapOfEdgeEdgeInfo
    Size = _swig_new_instance_method(_Draft.Draft_IndexedDataMapOfEdgeEdgeInfo_Size)

# Register Draft_IndexedDataMapOfEdgeEdgeInfo in _Draft:
_Draft.Draft_IndexedDataMapOfEdgeEdgeInfo_swigregister(Draft_IndexedDataMapOfEdgeEdgeInfo)

class draft(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Angle = _swig_new_static_method(_Draft.draft_Angle)

    __repr__ = _dumps_object


    def __init__(self):
        _Draft.draft_swiginit(self, _Draft.new_draft())
    __swig_destroy__ = _Draft.delete_draft

# Register draft in _Draft:
_Draft.draft_swigregister(draft)
draft_Angle = _Draft.draft_Angle

class Draft_EdgeInfo(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Add = _swig_new_instance_method(_Draft.Draft_EdgeInfo_Add)
    ChangeFirstPC = _swig_new_instance_method(_Draft.Draft_EdgeInfo_ChangeFirstPC)
    ChangeGeometry = _swig_new_instance_method(_Draft.Draft_EdgeInfo_ChangeGeometry)
    ChangeSecondPC = _swig_new_instance_method(_Draft.Draft_EdgeInfo_ChangeSecondPC)

    def __init__(self, *args):
        r"""
        :rtype: None:param HasNewGeometry:
        	:type HasNewGeometry: bool
        	:rtype: None
        """
        _Draft.Draft_EdgeInfo_swiginit(self, _Draft.new_Draft_EdgeInfo(*args))
    FirstFace = _swig_new_instance_method(_Draft.Draft_EdgeInfo_FirstFace)
    FirstPC = _swig_new_instance_method(_Draft.Draft_EdgeInfo_FirstPC)
    Geometry = _swig_new_instance_method(_Draft.Draft_EdgeInfo_Geometry)
    IsTangent = _swig_new_instance_method(_Draft.Draft_EdgeInfo_IsTangent)
    NewGeometry = _swig_new_instance_method(_Draft.Draft_EdgeInfo_NewGeometry)
    RootFace = _swig_new_instance_method(_Draft.Draft_EdgeInfo_RootFace)
    SecondFace = _swig_new_instance_method(_Draft.Draft_EdgeInfo_SecondFace)
    SecondPC = _swig_new_instance_method(_Draft.Draft_EdgeInfo_SecondPC)
    SetNewGeometry = _swig_new_instance_method(_Draft.Draft_EdgeInfo_SetNewGeometry)
    Tangent = _swig_new_instance_method(_Draft.Draft_EdgeInfo_Tangent)
    Tolerance = _swig_new_instance_method(_Draft.Draft_EdgeInfo_Tolerance)

    __repr__ = _dumps_object

    __swig_destroy__ = _Draft.delete_Draft_EdgeInfo

# Register Draft_EdgeInfo in _Draft:
_Draft.Draft_EdgeInfo_swigregister(Draft_EdgeInfo)

class Draft_FaceInfo(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Add = _swig_new_instance_method(_Draft.Draft_FaceInfo_Add)
    ChangeCurve = _swig_new_instance_method(_Draft.Draft_FaceInfo_ChangeCurve)
    ChangeGeometry = _swig_new_instance_method(_Draft.Draft_FaceInfo_ChangeGeometry)
    Curve = _swig_new_instance_method(_Draft.Draft_FaceInfo_Curve)

    def __init__(self, *args):
        r"""
        :rtype: None:param S:
        	:type S: Geom_Surface
        	:param HasNewGeometry:
        	:type HasNewGeometry: bool
        	:rtype: None
        """
        _Draft.Draft_FaceInfo_swiginit(self, _Draft.new_Draft_FaceInfo(*args))
    FirstFace = _swig_new_instance_method(_Draft.Draft_FaceInfo_FirstFace)
    Geometry = _swig_new_instance_method(_Draft.Draft_FaceInfo_Geometry)
    NewGeometry = _swig_new_instance_method(_Draft.Draft_FaceInfo_NewGeometry)
    RootFace = _swig_new_instance_method(_Draft.Draft_FaceInfo_RootFace)
    SecondFace = _swig_new_instance_method(_Draft.Draft_FaceInfo_SecondFace)

    __repr__ = _dumps_object

    __swig_destroy__ = _Draft.delete_Draft_FaceInfo

# Register Draft_FaceInfo in _Draft:
_Draft.Draft_FaceInfo_swigregister(Draft_FaceInfo)

class Draft_Modification(OCC.Core.BRepTools.BRepTools_Modification):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Add = _swig_new_instance_method(_Draft.Draft_Modification_Add)
    Clear = _swig_new_instance_method(_Draft.Draft_Modification_Clear)
    ConnectedFaces = _swig_new_instance_method(_Draft.Draft_Modification_ConnectedFaces)

    def __init__(self, *args):
        r"""
        :param S:
        	:type S: TopoDS_Shape
        	:rtype: None
        """
        _Draft.Draft_Modification_swiginit(self, _Draft.new_Draft_Modification(*args))
    Error = _swig_new_instance_method(_Draft.Draft_Modification_Error)
    Init = _swig_new_instance_method(_Draft.Draft_Modification_Init)
    IsDone = _swig_new_instance_method(_Draft.Draft_Modification_IsDone)
    ModifiedFaces = _swig_new_instance_method(_Draft.Draft_Modification_ModifiedFaces)
    Perform = _swig_new_instance_method(_Draft.Draft_Modification_Perform)
    ProblematicShape = _swig_new_instance_method(_Draft.Draft_Modification_ProblematicShape)
    Remove = _swig_new_instance_method(_Draft.Draft_Modification_Remove)


    @staticmethod
    def DownCast(t):
      return Handle_Draft_Modification_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _Draft.delete_Draft_Modification

# Register Draft_Modification in _Draft:
_Draft.Draft_Modification_swigregister(Draft_Modification)

class Draft_VertexInfo(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Add = _swig_new_instance_method(_Draft.Draft_VertexInfo_Add)
    ChangeGeometry = _swig_new_instance_method(_Draft.Draft_VertexInfo_ChangeGeometry)
    GetChangeParameter = _swig_new_instance_method(_Draft.Draft_VertexInfo_GetChangeParameter)
    SetChangeParameter = _swig_new_instance_method(_Draft.Draft_VertexInfo_SetChangeParameter)

    def __init__(self, *args):
        r""":rtype: None"""
        _Draft.Draft_VertexInfo_swiginit(self, _Draft.new_Draft_VertexInfo(*args))
    Edge = _swig_new_instance_method(_Draft.Draft_VertexInfo_Edge)
    Geometry = _swig_new_instance_method(_Draft.Draft_VertexInfo_Geometry)
    InitEdgeIterator = _swig_new_instance_method(_Draft.Draft_VertexInfo_InitEdgeIterator)
    MoreEdge = _swig_new_instance_method(_Draft.Draft_VertexInfo_MoreEdge)
    NextEdge = _swig_new_instance_method(_Draft.Draft_VertexInfo_NextEdge)
    Parameter = _swig_new_instance_method(_Draft.Draft_VertexInfo_Parameter)

    __repr__ = _dumps_object

    __swig_destroy__ = _Draft.delete_Draft_VertexInfo

# Register Draft_VertexInfo in _Draft:
_Draft.Draft_VertexInfo_swigregister(Draft_VertexInfo)



