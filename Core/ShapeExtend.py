# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
ShapeExtend module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_shapeextend.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _ShapeExtend
else:
    import _ShapeExtend

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _ShapeExtend.SWIG_PyInstanceMethod_New
_swig_new_static_method = _ShapeExtend.SWIG_PyStaticMethod_New

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
    __swig_destroy__ = _ShapeExtend.delete_SwigPyIterator
    value = _swig_new_instance_method(_ShapeExtend.SwigPyIterator_value)
    incr = _swig_new_instance_method(_ShapeExtend.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_ShapeExtend.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_ShapeExtend.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_ShapeExtend.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_ShapeExtend.SwigPyIterator_copy)
    next = _swig_new_instance_method(_ShapeExtend.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_ShapeExtend.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_ShapeExtend.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_ShapeExtend.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_ShapeExtend.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_ShapeExtend.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_ShapeExtend.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_ShapeExtend.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_ShapeExtend.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_ShapeExtend.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _ShapeExtend:
_ShapeExtend.SwigPyIterator_swigregister(SwigPyIterator)


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
import OCC.Core.Message
import OCC.Core.TopoDS
import OCC.Core.TopAbs
import OCC.Core.TopLoc
import OCC.Core.gp
import OCC.Core.Geom
import OCC.Core.GeomAbs
import OCC.Core.TColgp
import OCC.Core.TColStd
import OCC.Core.TCollection
import OCC.Core.TColGeom
import OCC.Core.TopTools
ShapeExtend_OK = _ShapeExtend.ShapeExtend_OK
ShapeExtend_DONE1 = _ShapeExtend.ShapeExtend_DONE1
ShapeExtend_DONE2 = _ShapeExtend.ShapeExtend_DONE2
ShapeExtend_DONE3 = _ShapeExtend.ShapeExtend_DONE3
ShapeExtend_DONE4 = _ShapeExtend.ShapeExtend_DONE4
ShapeExtend_DONE5 = _ShapeExtend.ShapeExtend_DONE5
ShapeExtend_DONE6 = _ShapeExtend.ShapeExtend_DONE6
ShapeExtend_DONE7 = _ShapeExtend.ShapeExtend_DONE7
ShapeExtend_DONE8 = _ShapeExtend.ShapeExtend_DONE8
ShapeExtend_DONE = _ShapeExtend.ShapeExtend_DONE
ShapeExtend_FAIL1 = _ShapeExtend.ShapeExtend_FAIL1
ShapeExtend_FAIL2 = _ShapeExtend.ShapeExtend_FAIL2
ShapeExtend_FAIL3 = _ShapeExtend.ShapeExtend_FAIL3
ShapeExtend_FAIL4 = _ShapeExtend.ShapeExtend_FAIL4
ShapeExtend_FAIL5 = _ShapeExtend.ShapeExtend_FAIL5
ShapeExtend_FAIL6 = _ShapeExtend.ShapeExtend_FAIL6
ShapeExtend_FAIL7 = _ShapeExtend.ShapeExtend_FAIL7
ShapeExtend_FAIL8 = _ShapeExtend.ShapeExtend_FAIL8
ShapeExtend_FAIL = _ShapeExtend.ShapeExtend_FAIL
ShapeExtend_Natural = _ShapeExtend.ShapeExtend_Natural
ShapeExtend_Uniform = _ShapeExtend.ShapeExtend_Uniform
ShapeExtend_Unitary = _ShapeExtend.ShapeExtend_Unitary
Handle_ShapeExtend_BasicMsgRegistrator_Create = _ShapeExtend.Handle_ShapeExtend_BasicMsgRegistrator_Create
Handle_ShapeExtend_BasicMsgRegistrator_DownCast = _ShapeExtend.Handle_ShapeExtend_BasicMsgRegistrator_DownCast
Handle_ShapeExtend_BasicMsgRegistrator_IsNull = _ShapeExtend.Handle_ShapeExtend_BasicMsgRegistrator_IsNull
Handle_ShapeExtend_ComplexCurve_Create = _ShapeExtend.Handle_ShapeExtend_ComplexCurve_Create
Handle_ShapeExtend_ComplexCurve_DownCast = _ShapeExtend.Handle_ShapeExtend_ComplexCurve_DownCast
Handle_ShapeExtend_ComplexCurve_IsNull = _ShapeExtend.Handle_ShapeExtend_ComplexCurve_IsNull
Handle_ShapeExtend_CompositeSurface_Create = _ShapeExtend.Handle_ShapeExtend_CompositeSurface_Create
Handle_ShapeExtend_CompositeSurface_DownCast = _ShapeExtend.Handle_ShapeExtend_CompositeSurface_DownCast
Handle_ShapeExtend_CompositeSurface_IsNull = _ShapeExtend.Handle_ShapeExtend_CompositeSurface_IsNull
Handle_ShapeExtend_WireData_Create = _ShapeExtend.Handle_ShapeExtend_WireData_Create
Handle_ShapeExtend_WireData_DownCast = _ShapeExtend.Handle_ShapeExtend_WireData_DownCast
Handle_ShapeExtend_WireData_IsNull = _ShapeExtend.Handle_ShapeExtend_WireData_IsNull
Handle_ShapeExtend_MsgRegistrator_Create = _ShapeExtend.Handle_ShapeExtend_MsgRegistrator_Create
Handle_ShapeExtend_MsgRegistrator_DownCast = _ShapeExtend.Handle_ShapeExtend_MsgRegistrator_DownCast
Handle_ShapeExtend_MsgRegistrator_IsNull = _ShapeExtend.Handle_ShapeExtend_MsgRegistrator_IsNull
class ShapeExtend_DataMapOfTransientListOfMsg(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_ShapeExtend.ShapeExtend_DataMapOfTransientListOfMsg_begin)
    end = _swig_new_instance_method(_ShapeExtend.ShapeExtend_DataMapOfTransientListOfMsg_end)
    cbegin = _swig_new_instance_method(_ShapeExtend.ShapeExtend_DataMapOfTransientListOfMsg_cbegin)
    cend = _swig_new_instance_method(_ShapeExtend.ShapeExtend_DataMapOfTransientListOfMsg_cend)

    def __init__(self, *args):
        _ShapeExtend.ShapeExtend_DataMapOfTransientListOfMsg_swiginit(self, _ShapeExtend.new_ShapeExtend_DataMapOfTransientListOfMsg(*args))
    Exchange = _swig_new_instance_method(_ShapeExtend.ShapeExtend_DataMapOfTransientListOfMsg_Exchange)
    Assign = _swig_new_instance_method(_ShapeExtend.ShapeExtend_DataMapOfTransientListOfMsg_Assign)
    Set = _swig_new_instance_method(_ShapeExtend.ShapeExtend_DataMapOfTransientListOfMsg_Set)
    ReSize = _swig_new_instance_method(_ShapeExtend.ShapeExtend_DataMapOfTransientListOfMsg_ReSize)
    Bind = _swig_new_instance_method(_ShapeExtend.ShapeExtend_DataMapOfTransientListOfMsg_Bind)
    Bound = _swig_new_instance_method(_ShapeExtend.ShapeExtend_DataMapOfTransientListOfMsg_Bound)
    IsBound = _swig_new_instance_method(_ShapeExtend.ShapeExtend_DataMapOfTransientListOfMsg_IsBound)
    UnBind = _swig_new_instance_method(_ShapeExtend.ShapeExtend_DataMapOfTransientListOfMsg_UnBind)
    Seek = _swig_new_instance_method(_ShapeExtend.ShapeExtend_DataMapOfTransientListOfMsg_Seek)
    Find = _swig_new_instance_method(_ShapeExtend.ShapeExtend_DataMapOfTransientListOfMsg_Find)
    ChangeSeek = _swig_new_instance_method(_ShapeExtend.ShapeExtend_DataMapOfTransientListOfMsg_ChangeSeek)
    ChangeFind = _swig_new_instance_method(_ShapeExtend.ShapeExtend_DataMapOfTransientListOfMsg_ChangeFind)
    __call__ = _swig_new_instance_method(_ShapeExtend.ShapeExtend_DataMapOfTransientListOfMsg___call__)
    Clear = _swig_new_instance_method(_ShapeExtend.ShapeExtend_DataMapOfTransientListOfMsg_Clear)
    __swig_destroy__ = _ShapeExtend.delete_ShapeExtend_DataMapOfTransientListOfMsg
    Size = _swig_new_instance_method(_ShapeExtend.ShapeExtend_DataMapOfTransientListOfMsg_Size)

# Register ShapeExtend_DataMapOfTransientListOfMsg in _ShapeExtend:
_ShapeExtend.ShapeExtend_DataMapOfTransientListOfMsg_swigregister(ShapeExtend_DataMapOfTransientListOfMsg)

class ShapeExtend_DataMapOfShapeListOfMsg(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_ShapeExtend.ShapeExtend_DataMapOfShapeListOfMsg_begin)
    end = _swig_new_instance_method(_ShapeExtend.ShapeExtend_DataMapOfShapeListOfMsg_end)
    cbegin = _swig_new_instance_method(_ShapeExtend.ShapeExtend_DataMapOfShapeListOfMsg_cbegin)
    cend = _swig_new_instance_method(_ShapeExtend.ShapeExtend_DataMapOfShapeListOfMsg_cend)

    def __init__(self, *args):
        _ShapeExtend.ShapeExtend_DataMapOfShapeListOfMsg_swiginit(self, _ShapeExtend.new_ShapeExtend_DataMapOfShapeListOfMsg(*args))
    Exchange = _swig_new_instance_method(_ShapeExtend.ShapeExtend_DataMapOfShapeListOfMsg_Exchange)
    Assign = _swig_new_instance_method(_ShapeExtend.ShapeExtend_DataMapOfShapeListOfMsg_Assign)
    Set = _swig_new_instance_method(_ShapeExtend.ShapeExtend_DataMapOfShapeListOfMsg_Set)
    ReSize = _swig_new_instance_method(_ShapeExtend.ShapeExtend_DataMapOfShapeListOfMsg_ReSize)
    Bind = _swig_new_instance_method(_ShapeExtend.ShapeExtend_DataMapOfShapeListOfMsg_Bind)
    Bound = _swig_new_instance_method(_ShapeExtend.ShapeExtend_DataMapOfShapeListOfMsg_Bound)
    IsBound = _swig_new_instance_method(_ShapeExtend.ShapeExtend_DataMapOfShapeListOfMsg_IsBound)
    UnBind = _swig_new_instance_method(_ShapeExtend.ShapeExtend_DataMapOfShapeListOfMsg_UnBind)
    Seek = _swig_new_instance_method(_ShapeExtend.ShapeExtend_DataMapOfShapeListOfMsg_Seek)
    Find = _swig_new_instance_method(_ShapeExtend.ShapeExtend_DataMapOfShapeListOfMsg_Find)
    ChangeSeek = _swig_new_instance_method(_ShapeExtend.ShapeExtend_DataMapOfShapeListOfMsg_ChangeSeek)
    ChangeFind = _swig_new_instance_method(_ShapeExtend.ShapeExtend_DataMapOfShapeListOfMsg_ChangeFind)
    __call__ = _swig_new_instance_method(_ShapeExtend.ShapeExtend_DataMapOfShapeListOfMsg___call__)
    Clear = _swig_new_instance_method(_ShapeExtend.ShapeExtend_DataMapOfShapeListOfMsg_Clear)
    __swig_destroy__ = _ShapeExtend.delete_ShapeExtend_DataMapOfShapeListOfMsg
    Size = _swig_new_instance_method(_ShapeExtend.ShapeExtend_DataMapOfShapeListOfMsg_Size)

# Register ShapeExtend_DataMapOfShapeListOfMsg in _ShapeExtend:
_ShapeExtend.ShapeExtend_DataMapOfShapeListOfMsg_swigregister(ShapeExtend_DataMapOfShapeListOfMsg)

class shapeextend(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    DecodeStatus = _swig_new_static_method(_ShapeExtend.shapeextend_DecodeStatus)
    EncodeStatus = _swig_new_static_method(_ShapeExtend.shapeextend_EncodeStatus)
    Init = _swig_new_static_method(_ShapeExtend.shapeextend_Init)

    __repr__ = _dumps_object


    def __init__(self):
        _ShapeExtend.shapeextend_swiginit(self, _ShapeExtend.new_shapeextend())
    __swig_destroy__ = _ShapeExtend.delete_shapeextend

# Register shapeextend in _ShapeExtend:
_ShapeExtend.shapeextend_swigregister(shapeextend)
shapeextend_DecodeStatus = _ShapeExtend.shapeextend_DecodeStatus
shapeextend_EncodeStatus = _ShapeExtend.shapeextend_EncodeStatus
shapeextend_Init = _ShapeExtend.shapeextend_Init

class ShapeExtend_BasicMsgRegistrator(OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Send = _swig_new_instance_method(_ShapeExtend.ShapeExtend_BasicMsgRegistrator_Send)

    def __init__(self, *args):
        r"""
        * Empty constructor.
        	:rtype: None
        """
        _ShapeExtend.ShapeExtend_BasicMsgRegistrator_swiginit(self, _ShapeExtend.new_ShapeExtend_BasicMsgRegistrator(*args))


    @staticmethod
    def DownCast(t):
      return Handle_ShapeExtend_BasicMsgRegistrator_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _ShapeExtend.delete_ShapeExtend_BasicMsgRegistrator

# Register ShapeExtend_BasicMsgRegistrator in _ShapeExtend:
_ShapeExtend.ShapeExtend_BasicMsgRegistrator_swigregister(ShapeExtend_BasicMsgRegistrator)

class ShapeExtend_ComplexCurve(OCC.Core.Geom.Geom_Curve):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    CheckConnectivity = _swig_new_instance_method(_ShapeExtend.ShapeExtend_ComplexCurve_CheckConnectivity)
    Curve = _swig_new_instance_method(_ShapeExtend.ShapeExtend_ComplexCurve_Curve)
    GetScaleFactor = _swig_new_instance_method(_ShapeExtend.ShapeExtend_ComplexCurve_GetScaleFactor)
    LocalToGlobal = _swig_new_instance_method(_ShapeExtend.ShapeExtend_ComplexCurve_LocalToGlobal)
    LocateParameter = _swig_new_instance_method(_ShapeExtend.ShapeExtend_ComplexCurve_LocateParameter)
    NbCurves = _swig_new_instance_method(_ShapeExtend.ShapeExtend_ComplexCurve_NbCurves)


    @staticmethod
    def DownCast(t):
      return Handle_ShapeExtend_ComplexCurve_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _ShapeExtend.delete_ShapeExtend_ComplexCurve

# Register ShapeExtend_ComplexCurve in _ShapeExtend:
_ShapeExtend.ShapeExtend_ComplexCurve_swigregister(ShapeExtend_ComplexCurve)

class ShapeExtend_CompositeSurface(OCC.Core.Geom.Geom_Surface):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    CheckConnectivity = _swig_new_instance_method(_ShapeExtend.ShapeExtend_CompositeSurface_CheckConnectivity)
    ComputeJointValues = _swig_new_instance_method(_ShapeExtend.ShapeExtend_CompositeSurface_ComputeJointValues)
    GlobalToLocal = _swig_new_instance_method(_ShapeExtend.ShapeExtend_CompositeSurface_GlobalToLocal)
    GlobalToLocalTransformation = _swig_new_instance_method(_ShapeExtend.ShapeExtend_CompositeSurface_GlobalToLocalTransformation)
    Init = _swig_new_instance_method(_ShapeExtend.ShapeExtend_CompositeSurface_Init)
    LocalToGlobal = _swig_new_instance_method(_ShapeExtend.ShapeExtend_CompositeSurface_LocalToGlobal)
    LocateUParameter = _swig_new_instance_method(_ShapeExtend.ShapeExtend_CompositeSurface_LocateUParameter)
    LocateUVPoint = _swig_new_instance_method(_ShapeExtend.ShapeExtend_CompositeSurface_LocateUVPoint)
    LocateVParameter = _swig_new_instance_method(_ShapeExtend.ShapeExtend_CompositeSurface_LocateVParameter)
    NbUPatches = _swig_new_instance_method(_ShapeExtend.ShapeExtend_CompositeSurface_NbUPatches)
    NbVPatches = _swig_new_instance_method(_ShapeExtend.ShapeExtend_CompositeSurface_NbVPatches)
    Patch = _swig_new_instance_method(_ShapeExtend.ShapeExtend_CompositeSurface_Patch)
    Patches = _swig_new_instance_method(_ShapeExtend.ShapeExtend_CompositeSurface_Patches)
    SetUFirstValue = _swig_new_instance_method(_ShapeExtend.ShapeExtend_CompositeSurface_SetUFirstValue)
    SetUJointValues = _swig_new_instance_method(_ShapeExtend.ShapeExtend_CompositeSurface_SetUJointValues)
    SetVFirstValue = _swig_new_instance_method(_ShapeExtend.ShapeExtend_CompositeSurface_SetVFirstValue)
    SetVJointValues = _swig_new_instance_method(_ShapeExtend.ShapeExtend_CompositeSurface_SetVJointValues)

    def __init__(self, *args):
        r"""
        * Empty constructor.
        	:rtype: None* Initializes by a grid of surfaces (calls Init()).
        	:param GridSurf:
        	:type GridSurf: TColGeom_HArray2OfSurface
        	:param param: default value is ShapeExtend_Natural
        	:type param: ShapeExtend_Parametrisation
        	:rtype: None* Initializes by a grid of surfaces (calls Init()).
        	:param GridSurf:
        	:type GridSurf: TColGeom_HArray2OfSurface
        	:param UJoints:
        	:type UJoints: TColStd_Array1OfReal
        	:param VJoints:
        	:type VJoints: TColStd_Array1OfReal
        	:rtype: None
        """
        _ShapeExtend.ShapeExtend_CompositeSurface_swiginit(self, _ShapeExtend.new_ShapeExtend_CompositeSurface(*args))
    UGlobalToLocal = _swig_new_instance_method(_ShapeExtend.ShapeExtend_CompositeSurface_UGlobalToLocal)
    UJointValue = _swig_new_instance_method(_ShapeExtend.ShapeExtend_CompositeSurface_UJointValue)
    UJointValues = _swig_new_instance_method(_ShapeExtend.ShapeExtend_CompositeSurface_UJointValues)
    ULocalToGlobal = _swig_new_instance_method(_ShapeExtend.ShapeExtend_CompositeSurface_ULocalToGlobal)
    VGlobalToLocal = _swig_new_instance_method(_ShapeExtend.ShapeExtend_CompositeSurface_VGlobalToLocal)
    VJointValue = _swig_new_instance_method(_ShapeExtend.ShapeExtend_CompositeSurface_VJointValue)
    VJointValues = _swig_new_instance_method(_ShapeExtend.ShapeExtend_CompositeSurface_VJointValues)
    VLocalToGlobal = _swig_new_instance_method(_ShapeExtend.ShapeExtend_CompositeSurface_VLocalToGlobal)
    Value = _swig_new_instance_method(_ShapeExtend.ShapeExtend_CompositeSurface_Value)


    @staticmethod
    def DownCast(t):
      return Handle_ShapeExtend_CompositeSurface_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _ShapeExtend.delete_ShapeExtend_CompositeSurface

# Register ShapeExtend_CompositeSurface in _ShapeExtend:
_ShapeExtend.ShapeExtend_CompositeSurface_swigregister(ShapeExtend_CompositeSurface)

class ShapeExtend_Explorer(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    CompoundFromSeq = _swig_new_instance_method(_ShapeExtend.ShapeExtend_Explorer_CompoundFromSeq)
    DispatchList = _swig_new_instance_method(_ShapeExtend.ShapeExtend_Explorer_DispatchList)
    ListFromSeq = _swig_new_instance_method(_ShapeExtend.ShapeExtend_Explorer_ListFromSeq)
    SeqFromCompound = _swig_new_instance_method(_ShapeExtend.ShapeExtend_Explorer_SeqFromCompound)
    SeqFromList = _swig_new_instance_method(_ShapeExtend.ShapeExtend_Explorer_SeqFromList)

    def __init__(self, *args):
        r"""
        * Creates an object Explorer
        	:rtype: None
        """
        _ShapeExtend.ShapeExtend_Explorer_swiginit(self, _ShapeExtend.new_ShapeExtend_Explorer(*args))
    ShapeType = _swig_new_instance_method(_ShapeExtend.ShapeExtend_Explorer_ShapeType)
    SortedCompound = _swig_new_instance_method(_ShapeExtend.ShapeExtend_Explorer_SortedCompound)

    __repr__ = _dumps_object

    __swig_destroy__ = _ShapeExtend.delete_ShapeExtend_Explorer

# Register ShapeExtend_Explorer in _ShapeExtend:
_ShapeExtend.ShapeExtend_Explorer_swigregister(ShapeExtend_Explorer)

class ShapeExtend_WireData(OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Add = _swig_new_instance_method(_ShapeExtend.ShapeExtend_WireData_Add)
    AddOriented = _swig_new_instance_method(_ShapeExtend.ShapeExtend_WireData_AddOriented)
    Clear = _swig_new_instance_method(_ShapeExtend.ShapeExtend_WireData_Clear)
    ComputeSeams = _swig_new_instance_method(_ShapeExtend.ShapeExtend_WireData_ComputeSeams)
    Edge = _swig_new_instance_method(_ShapeExtend.ShapeExtend_WireData_Edge)
    Index = _swig_new_instance_method(_ShapeExtend.ShapeExtend_WireData_Index)
    Init = _swig_new_instance_method(_ShapeExtend.ShapeExtend_WireData_Init)
    IsSeam = _swig_new_instance_method(_ShapeExtend.ShapeExtend_WireData_IsSeam)
    GetManifoldMode = _swig_new_instance_method(_ShapeExtend.ShapeExtend_WireData_GetManifoldMode)
    SetManifoldMode = _swig_new_instance_method(_ShapeExtend.ShapeExtend_WireData_SetManifoldMode)
    NbEdges = _swig_new_instance_method(_ShapeExtend.ShapeExtend_WireData_NbEdges)
    NbNonManifoldEdges = _swig_new_instance_method(_ShapeExtend.ShapeExtend_WireData_NbNonManifoldEdges)
    NonmanifoldEdge = _swig_new_instance_method(_ShapeExtend.ShapeExtend_WireData_NonmanifoldEdge)
    NonmanifoldEdges = _swig_new_instance_method(_ShapeExtend.ShapeExtend_WireData_NonmanifoldEdges)
    Remove = _swig_new_instance_method(_ShapeExtend.ShapeExtend_WireData_Remove)
    Reverse = _swig_new_instance_method(_ShapeExtend.ShapeExtend_WireData_Reverse)
    Set = _swig_new_instance_method(_ShapeExtend.ShapeExtend_WireData_Set)
    SetDegeneratedLast = _swig_new_instance_method(_ShapeExtend.ShapeExtend_WireData_SetDegeneratedLast)
    SetLast = _swig_new_instance_method(_ShapeExtend.ShapeExtend_WireData_SetLast)

    def __init__(self, *args):
        r"""
        * Empty constructor, creates empty wire with no edges
        	:rtype: None* Constructor initializing the data from TopoDS_Wire. Calls Init(wire,chained).
        	:param wire:
        	:type wire: TopoDS_Wire
        	:param chained: default value is Standard_True
        	:type chained: bool
        	:param theManifoldMode: default value is Standard_True
        	:type theManifoldMode: bool
        	:rtype: None
        """
        _ShapeExtend.ShapeExtend_WireData_swiginit(self, _ShapeExtend.new_ShapeExtend_WireData(*args))
    Wire = _swig_new_instance_method(_ShapeExtend.ShapeExtend_WireData_Wire)
    WireAPIMake = _swig_new_instance_method(_ShapeExtend.ShapeExtend_WireData_WireAPIMake)


    @staticmethod
    def DownCast(t):
      return Handle_ShapeExtend_WireData_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _ShapeExtend.delete_ShapeExtend_WireData

# Register ShapeExtend_WireData in _ShapeExtend:
_ShapeExtend.ShapeExtend_WireData_swigregister(ShapeExtend_WireData)

class ShapeExtend_MsgRegistrator(ShapeExtend_BasicMsgRegistrator):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    MapShape = _swig_new_instance_method(_ShapeExtend.ShapeExtend_MsgRegistrator_MapShape)
    MapTransient = _swig_new_instance_method(_ShapeExtend.ShapeExtend_MsgRegistrator_MapTransient)
    Send = _swig_new_instance_method(_ShapeExtend.ShapeExtend_MsgRegistrator_Send)

    def __init__(self, *args):
        r"""
        * Creates an object.
        	:rtype: None
        """
        _ShapeExtend.ShapeExtend_MsgRegistrator_swiginit(self, _ShapeExtend.new_ShapeExtend_MsgRegistrator(*args))


    @staticmethod
    def DownCast(t):
      return Handle_ShapeExtend_MsgRegistrator_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _ShapeExtend.delete_ShapeExtend_MsgRegistrator

# Register ShapeExtend_MsgRegistrator in _ShapeExtend:
_ShapeExtend.ShapeExtend_MsgRegistrator_swigregister(ShapeExtend_MsgRegistrator)



