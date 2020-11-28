# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
TDataXtd module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_tdataxtd.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _TDataXtd
else:
    import _TDataXtd

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _TDataXtd.SWIG_PyInstanceMethod_New
_swig_new_static_method = _TDataXtd.SWIG_PyStaticMethod_New

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
    __swig_destroy__ = _TDataXtd.delete_SwigPyIterator
    value = _swig_new_instance_method(_TDataXtd.SwigPyIterator_value)
    incr = _swig_new_instance_method(_TDataXtd.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_TDataXtd.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_TDataXtd.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_TDataXtd.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_TDataXtd.SwigPyIterator_copy)
    next = _swig_new_instance_method(_TDataXtd.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_TDataXtd.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_TDataXtd.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_TDataXtd.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_TDataXtd.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_TDataXtd.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_TDataXtd.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_TDataXtd.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_TDataXtd.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_TDataXtd.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _TDataXtd:
_TDataXtd.SwigPyIterator_swigregister(SwigPyIterator)


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
import OCC.Core.TDF
import OCC.Core.TCollection
import OCC.Core.TColStd
import OCC.Core.gp
import OCC.Core.TNaming
import OCC.Core.TopTools
import OCC.Core.TopoDS
import OCC.Core.Message
import OCC.Core.TopAbs
import OCC.Core.TopLoc
import OCC.Core.TDataStd
import OCC.Core.Quantity
import OCC.Core.Poly
import OCC.Core.TColgp
import OCC.Core.TShort
TDataXtd_RADIUS = _TDataXtd.TDataXtd_RADIUS
TDataXtd_DIAMETER = _TDataXtd.TDataXtd_DIAMETER
TDataXtd_MINOR_RADIUS = _TDataXtd.TDataXtd_MINOR_RADIUS
TDataXtd_MAJOR_RADIUS = _TDataXtd.TDataXtd_MAJOR_RADIUS
TDataXtd_TANGENT = _TDataXtd.TDataXtd_TANGENT
TDataXtd_PARALLEL = _TDataXtd.TDataXtd_PARALLEL
TDataXtd_PERPENDICULAR = _TDataXtd.TDataXtd_PERPENDICULAR
TDataXtd_CONCENTRIC = _TDataXtd.TDataXtd_CONCENTRIC
TDataXtd_COINCIDENT = _TDataXtd.TDataXtd_COINCIDENT
TDataXtd_DISTANCE = _TDataXtd.TDataXtd_DISTANCE
TDataXtd_ANGLE = _TDataXtd.TDataXtd_ANGLE
TDataXtd_EQUAL_RADIUS = _TDataXtd.TDataXtd_EQUAL_RADIUS
TDataXtd_SYMMETRY = _TDataXtd.TDataXtd_SYMMETRY
TDataXtd_MIDPOINT = _TDataXtd.TDataXtd_MIDPOINT
TDataXtd_EQUAL_DISTANCE = _TDataXtd.TDataXtd_EQUAL_DISTANCE
TDataXtd_FIX = _TDataXtd.TDataXtd_FIX
TDataXtd_RIGID = _TDataXtd.TDataXtd_RIGID
TDataXtd_FROM = _TDataXtd.TDataXtd_FROM
TDataXtd_AXIS = _TDataXtd.TDataXtd_AXIS
TDataXtd_MATE = _TDataXtd.TDataXtd_MATE
TDataXtd_ALIGN_FACES = _TDataXtd.TDataXtd_ALIGN_FACES
TDataXtd_ALIGN_AXES = _TDataXtd.TDataXtd_ALIGN_AXES
TDataXtd_AXES_ANGLE = _TDataXtd.TDataXtd_AXES_ANGLE
TDataXtd_FACES_ANGLE = _TDataXtd.TDataXtd_FACES_ANGLE
TDataXtd_ROUND = _TDataXtd.TDataXtd_ROUND
TDataXtd_OFFSET = _TDataXtd.TDataXtd_OFFSET
TDataXtd_ANY_GEOM = _TDataXtd.TDataXtd_ANY_GEOM
TDataXtd_POINT = _TDataXtd.TDataXtd_POINT
TDataXtd_LINE = _TDataXtd.TDataXtd_LINE
TDataXtd_CIRCLE = _TDataXtd.TDataXtd_CIRCLE
TDataXtd_ELLIPSE = _TDataXtd.TDataXtd_ELLIPSE
TDataXtd_SPLINE = _TDataXtd.TDataXtd_SPLINE
TDataXtd_PLANE = _TDataXtd.TDataXtd_PLANE
TDataXtd_CYLINDER = _TDataXtd.TDataXtd_CYLINDER
Handle_TDataXtd_Axis_Create = _TDataXtd.Handle_TDataXtd_Axis_Create
Handle_TDataXtd_Axis_DownCast = _TDataXtd.Handle_TDataXtd_Axis_DownCast
Handle_TDataXtd_Axis_IsNull = _TDataXtd.Handle_TDataXtd_Axis_IsNull
Handle_TDataXtd_Constraint_Create = _TDataXtd.Handle_TDataXtd_Constraint_Create
Handle_TDataXtd_Constraint_DownCast = _TDataXtd.Handle_TDataXtd_Constraint_DownCast
Handle_TDataXtd_Constraint_IsNull = _TDataXtd.Handle_TDataXtd_Constraint_IsNull
Handle_TDataXtd_Geometry_Create = _TDataXtd.Handle_TDataXtd_Geometry_Create
Handle_TDataXtd_Geometry_DownCast = _TDataXtd.Handle_TDataXtd_Geometry_DownCast
Handle_TDataXtd_Geometry_IsNull = _TDataXtd.Handle_TDataXtd_Geometry_IsNull
Handle_TDataXtd_Pattern_Create = _TDataXtd.Handle_TDataXtd_Pattern_Create
Handle_TDataXtd_Pattern_DownCast = _TDataXtd.Handle_TDataXtd_Pattern_DownCast
Handle_TDataXtd_Pattern_IsNull = _TDataXtd.Handle_TDataXtd_Pattern_IsNull
Handle_TDataXtd_Placement_Create = _TDataXtd.Handle_TDataXtd_Placement_Create
Handle_TDataXtd_Placement_DownCast = _TDataXtd.Handle_TDataXtd_Placement_DownCast
Handle_TDataXtd_Placement_IsNull = _TDataXtd.Handle_TDataXtd_Placement_IsNull
Handle_TDataXtd_Plane_Create = _TDataXtd.Handle_TDataXtd_Plane_Create
Handle_TDataXtd_Plane_DownCast = _TDataXtd.Handle_TDataXtd_Plane_DownCast
Handle_TDataXtd_Plane_IsNull = _TDataXtd.Handle_TDataXtd_Plane_IsNull
Handle_TDataXtd_Point_Create = _TDataXtd.Handle_TDataXtd_Point_Create
Handle_TDataXtd_Point_DownCast = _TDataXtd.Handle_TDataXtd_Point_DownCast
Handle_TDataXtd_Point_IsNull = _TDataXtd.Handle_TDataXtd_Point_IsNull
Handle_TDataXtd_Position_Create = _TDataXtd.Handle_TDataXtd_Position_Create
Handle_TDataXtd_Position_DownCast = _TDataXtd.Handle_TDataXtd_Position_DownCast
Handle_TDataXtd_Position_IsNull = _TDataXtd.Handle_TDataXtd_Position_IsNull
Handle_TDataXtd_Presentation_Create = _TDataXtd.Handle_TDataXtd_Presentation_Create
Handle_TDataXtd_Presentation_DownCast = _TDataXtd.Handle_TDataXtd_Presentation_DownCast
Handle_TDataXtd_Presentation_IsNull = _TDataXtd.Handle_TDataXtd_Presentation_IsNull
Handle_TDataXtd_Shape_Create = _TDataXtd.Handle_TDataXtd_Shape_Create
Handle_TDataXtd_Shape_DownCast = _TDataXtd.Handle_TDataXtd_Shape_DownCast
Handle_TDataXtd_Shape_IsNull = _TDataXtd.Handle_TDataXtd_Shape_IsNull
Handle_TDataXtd_Triangulation_Create = _TDataXtd.Handle_TDataXtd_Triangulation_Create
Handle_TDataXtd_Triangulation_DownCast = _TDataXtd.Handle_TDataXtd_Triangulation_DownCast
Handle_TDataXtd_Triangulation_IsNull = _TDataXtd.Handle_TDataXtd_Triangulation_IsNull
Handle_TDataXtd_PatternStd_Create = _TDataXtd.Handle_TDataXtd_PatternStd_Create
Handle_TDataXtd_PatternStd_DownCast = _TDataXtd.Handle_TDataXtd_PatternStd_DownCast
Handle_TDataXtd_PatternStd_IsNull = _TDataXtd.Handle_TDataXtd_PatternStd_IsNull
Handle_TDataXtd_HArray1OfTrsf_Create = _TDataXtd.Handle_TDataXtd_HArray1OfTrsf_Create
Handle_TDataXtd_HArray1OfTrsf_DownCast = _TDataXtd.Handle_TDataXtd_HArray1OfTrsf_DownCast
Handle_TDataXtd_HArray1OfTrsf_IsNull = _TDataXtd.Handle_TDataXtd_HArray1OfTrsf_IsNull
class TDataXtd_Array1OfTrsf(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_TDataXtd.TDataXtd_Array1OfTrsf_begin)
    end = _swig_new_instance_method(_TDataXtd.TDataXtd_Array1OfTrsf_end)
    cbegin = _swig_new_instance_method(_TDataXtd.TDataXtd_Array1OfTrsf_cbegin)
    cend = _swig_new_instance_method(_TDataXtd.TDataXtd_Array1OfTrsf_cend)

    def __init__(self, *args):
        _TDataXtd.TDataXtd_Array1OfTrsf_swiginit(self, _TDataXtd.new_TDataXtd_Array1OfTrsf(*args))
    Init = _swig_new_instance_method(_TDataXtd.TDataXtd_Array1OfTrsf_Init)
    Size = _swig_new_instance_method(_TDataXtd.TDataXtd_Array1OfTrsf_Size)
    Length = _swig_new_instance_method(_TDataXtd.TDataXtd_Array1OfTrsf_Length)
    IsEmpty = _swig_new_instance_method(_TDataXtd.TDataXtd_Array1OfTrsf_IsEmpty)
    Lower = _swig_new_instance_method(_TDataXtd.TDataXtd_Array1OfTrsf_Lower)
    Upper = _swig_new_instance_method(_TDataXtd.TDataXtd_Array1OfTrsf_Upper)
    IsDeletable = _swig_new_instance_method(_TDataXtd.TDataXtd_Array1OfTrsf_IsDeletable)
    IsAllocated = _swig_new_instance_method(_TDataXtd.TDataXtd_Array1OfTrsf_IsAllocated)
    Assign = _swig_new_instance_method(_TDataXtd.TDataXtd_Array1OfTrsf_Assign)
    Move = _swig_new_instance_method(_TDataXtd.TDataXtd_Array1OfTrsf_Move)
    Set = _swig_new_instance_method(_TDataXtd.TDataXtd_Array1OfTrsf_Set)
    First = _swig_new_instance_method(_TDataXtd.TDataXtd_Array1OfTrsf_First)
    ChangeFirst = _swig_new_instance_method(_TDataXtd.TDataXtd_Array1OfTrsf_ChangeFirst)
    Last = _swig_new_instance_method(_TDataXtd.TDataXtd_Array1OfTrsf_Last)
    ChangeLast = _swig_new_instance_method(_TDataXtd.TDataXtd_Array1OfTrsf_ChangeLast)
    Value = _swig_new_instance_method(_TDataXtd.TDataXtd_Array1OfTrsf_Value)
    ChangeValue = _swig_new_instance_method(_TDataXtd.TDataXtd_Array1OfTrsf_ChangeValue)
    __call__ = _swig_new_instance_method(_TDataXtd.TDataXtd_Array1OfTrsf___call__)
    SetValue = _swig_new_instance_method(_TDataXtd.TDataXtd_Array1OfTrsf_SetValue)
    Resize = _swig_new_instance_method(_TDataXtd.TDataXtd_Array1OfTrsf_Resize)
    __swig_destroy__ = _TDataXtd.delete_TDataXtd_Array1OfTrsf

    def __getitem__(self, index):
        if index + self.Lower() > self.Upper():
            raise IndexError("index out of range")
        else:
            return self.Value(index + self.Lower())

    def __setitem__(self, index, value):
        if index + self.Lower() > self.Upper():
            raise IndexError("index out of range")
        else:
            self.SetValue(index + self.Lower(), value)

    def __len__(self):
        return self.Length()

    def __iter__(self):
        self.low = self.Lower()
        self.up = self.Upper()
        self.current = self.Lower() - 1
        return self

    def next(self):
        if self.current >= self.Upper():
            raise StopIteration
        else:
            self.current += 1
        return self.Value(self.current)

    __next__ = next


# Register TDataXtd_Array1OfTrsf in _TDataXtd:
_TDataXtd.TDataXtd_Array1OfTrsf_swigregister(TDataXtd_Array1OfTrsf)

class tdataxtd(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    IDList = _swig_new_static_method(_TDataXtd.tdataxtd_IDList)
    Print = _swig_new_static_method(_TDataXtd.tdataxtd_Print)

    __repr__ = _dumps_object


    def __init__(self):
        _TDataXtd.tdataxtd_swiginit(self, _TDataXtd.new_tdataxtd())
    __swig_destroy__ = _TDataXtd.delete_tdataxtd

# Register tdataxtd in _TDataXtd:
_TDataXtd.tdataxtd_swigregister(tdataxtd)
tdataxtd_IDList = _TDataXtd.tdataxtd_IDList
tdataxtd_Print = _TDataXtd.tdataxtd_Print

class TDataXtd_Axis(OCC.Core.TDF.TDF_Attribute):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    DumpToString = _swig_new_instance_method(_TDataXtd.TDataXtd_Axis_DumpToString)
    GetID = _swig_new_static_method(_TDataXtd.TDataXtd_Axis_GetID)
    Set = _swig_new_static_method(_TDataXtd.TDataXtd_Axis_Set)

    def __init__(self, *args):
        r""":rtype: None"""
        _TDataXtd.TDataXtd_Axis_swiginit(self, _TDataXtd.new_TDataXtd_Axis(*args))


    @staticmethod
    def DownCast(t):
      return Handle_TDataXtd_Axis_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _TDataXtd.delete_TDataXtd_Axis

# Register TDataXtd_Axis in _TDataXtd:
_TDataXtd.TDataXtd_Axis_swigregister(TDataXtd_Axis)
TDataXtd_Axis_GetID = _TDataXtd.TDataXtd_Axis_GetID
TDataXtd_Axis_Set = _TDataXtd.TDataXtd_Axis_Set

class TDataXtd_Constraint(OCC.Core.TDF.TDF_Attribute):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    ClearGeometries = _swig_new_instance_method(_TDataXtd.TDataXtd_Constraint_ClearGeometries)
    CollectChildConstraints = _swig_new_static_method(_TDataXtd.TDataXtd_Constraint_CollectChildConstraints)
    DumpToString = _swig_new_instance_method(_TDataXtd.TDataXtd_Constraint_DumpToString)
    GetGeometry = _swig_new_instance_method(_TDataXtd.TDataXtd_Constraint_GetGeometry)
    GetID = _swig_new_static_method(_TDataXtd.TDataXtd_Constraint_GetID)
    GetPlane = _swig_new_instance_method(_TDataXtd.TDataXtd_Constraint_GetPlane)
    GetType = _swig_new_instance_method(_TDataXtd.TDataXtd_Constraint_GetType)
    GetValue = _swig_new_instance_method(_TDataXtd.TDataXtd_Constraint_GetValue)
    Inverted = _swig_new_instance_method(_TDataXtd.TDataXtd_Constraint_Inverted)
    IsDimension = _swig_new_instance_method(_TDataXtd.TDataXtd_Constraint_IsDimension)
    IsPlanar = _swig_new_instance_method(_TDataXtd.TDataXtd_Constraint_IsPlanar)
    NbGeometries = _swig_new_instance_method(_TDataXtd.TDataXtd_Constraint_NbGeometries)
    Reversed = _swig_new_instance_method(_TDataXtd.TDataXtd_Constraint_Reversed)
    Set = _swig_new_instance_method(_TDataXtd.TDataXtd_Constraint_Set)
    SetGeometry = _swig_new_instance_method(_TDataXtd.TDataXtd_Constraint_SetGeometry)
    SetPlane = _swig_new_instance_method(_TDataXtd.TDataXtd_Constraint_SetPlane)
    SetType = _swig_new_instance_method(_TDataXtd.TDataXtd_Constraint_SetType)
    SetValue = _swig_new_instance_method(_TDataXtd.TDataXtd_Constraint_SetValue)

    def __init__(self, *args):
        r""":rtype: None"""
        _TDataXtd.TDataXtd_Constraint_swiginit(self, _TDataXtd.new_TDataXtd_Constraint(*args))
    Verified = _swig_new_instance_method(_TDataXtd.TDataXtd_Constraint_Verified)


    @staticmethod
    def DownCast(t):
      return Handle_TDataXtd_Constraint_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _TDataXtd.delete_TDataXtd_Constraint

# Register TDataXtd_Constraint in _TDataXtd:
_TDataXtd.TDataXtd_Constraint_swigregister(TDataXtd_Constraint)
TDataXtd_Constraint_CollectChildConstraints = _TDataXtd.TDataXtd_Constraint_CollectChildConstraints
TDataXtd_Constraint_GetID = _TDataXtd.TDataXtd_Constraint_GetID

class TDataXtd_Geometry(OCC.Core.TDF.TDF_Attribute):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Axis = _swig_new_static_method(_TDataXtd.TDataXtd_Geometry_Axis)
    Circle = _swig_new_static_method(_TDataXtd.TDataXtd_Geometry_Circle)
    Cylinder = _swig_new_static_method(_TDataXtd.TDataXtd_Geometry_Cylinder)
    DumpToString = _swig_new_instance_method(_TDataXtd.TDataXtd_Geometry_DumpToString)
    Ellipse = _swig_new_static_method(_TDataXtd.TDataXtd_Geometry_Ellipse)
    GetID = _swig_new_static_method(_TDataXtd.TDataXtd_Geometry_GetID)
    GetType = _swig_new_instance_method(_TDataXtd.TDataXtd_Geometry_GetType)
    Line = _swig_new_static_method(_TDataXtd.TDataXtd_Geometry_Line)
    Plane = _swig_new_static_method(_TDataXtd.TDataXtd_Geometry_Plane)
    Point = _swig_new_static_method(_TDataXtd.TDataXtd_Geometry_Point)
    Set = _swig_new_static_method(_TDataXtd.TDataXtd_Geometry_Set)
    SetType = _swig_new_instance_method(_TDataXtd.TDataXtd_Geometry_SetType)

    def __init__(self, *args):
        r"""
        * This and the next methods are used to retrieve underlying geometry of the NamedShape, even if noone Geometry Attribute is associated . if not found or not compliant geometry return False.
        	:rtype: None
        """
        _TDataXtd.TDataXtd_Geometry_swiginit(self, _TDataXtd.new_TDataXtd_Geometry(*args))
    Type = _swig_new_static_method(_TDataXtd.TDataXtd_Geometry_Type)


    @staticmethod
    def DownCast(t):
      return Handle_TDataXtd_Geometry_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _TDataXtd.delete_TDataXtd_Geometry

# Register TDataXtd_Geometry in _TDataXtd:
_TDataXtd.TDataXtd_Geometry_swigregister(TDataXtd_Geometry)
TDataXtd_Geometry_Axis = _TDataXtd.TDataXtd_Geometry_Axis
TDataXtd_Geometry_Circle = _TDataXtd.TDataXtd_Geometry_Circle
TDataXtd_Geometry_Cylinder = _TDataXtd.TDataXtd_Geometry_Cylinder
TDataXtd_Geometry_Ellipse = _TDataXtd.TDataXtd_Geometry_Ellipse
TDataXtd_Geometry_GetID = _TDataXtd.TDataXtd_Geometry_GetID
TDataXtd_Geometry_Line = _TDataXtd.TDataXtd_Geometry_Line
TDataXtd_Geometry_Plane = _TDataXtd.TDataXtd_Geometry_Plane
TDataXtd_Geometry_Point = _TDataXtd.TDataXtd_Geometry_Point
TDataXtd_Geometry_Set = _TDataXtd.TDataXtd_Geometry_Set
TDataXtd_Geometry_Type = _TDataXtd.TDataXtd_Geometry_Type

class TDataXtd_Pattern(OCC.Core.TDF.TDF_Attribute):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    ComputeTrsfs = _swig_new_instance_method(_TDataXtd.TDataXtd_Pattern_ComputeTrsfs)
    GetID = _swig_new_static_method(_TDataXtd.TDataXtd_Pattern_GetID)
    NbTrsfs = _swig_new_instance_method(_TDataXtd.TDataXtd_Pattern_NbTrsfs)
    PatternID = _swig_new_instance_method(_TDataXtd.TDataXtd_Pattern_PatternID)


    @staticmethod
    def DownCast(t):
      return Handle_TDataXtd_Pattern_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _TDataXtd.delete_TDataXtd_Pattern

# Register TDataXtd_Pattern in _TDataXtd:
_TDataXtd.TDataXtd_Pattern_swigregister(TDataXtd_Pattern)
TDataXtd_Pattern_GetID = _TDataXtd.TDataXtd_Pattern_GetID

class TDataXtd_Placement(OCC.Core.TDF.TDF_Attribute):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    DumpToString = _swig_new_instance_method(_TDataXtd.TDataXtd_Placement_DumpToString)
    GetID = _swig_new_static_method(_TDataXtd.TDataXtd_Placement_GetID)
    Set = _swig_new_static_method(_TDataXtd.TDataXtd_Placement_Set)

    def __init__(self, *args):
        r""":rtype: None"""
        _TDataXtd.TDataXtd_Placement_swiginit(self, _TDataXtd.new_TDataXtd_Placement(*args))


    @staticmethod
    def DownCast(t):
      return Handle_TDataXtd_Placement_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _TDataXtd.delete_TDataXtd_Placement

# Register TDataXtd_Placement in _TDataXtd:
_TDataXtd.TDataXtd_Placement_swigregister(TDataXtd_Placement)
TDataXtd_Placement_GetID = _TDataXtd.TDataXtd_Placement_GetID
TDataXtd_Placement_Set = _TDataXtd.TDataXtd_Placement_Set

class TDataXtd_Plane(OCC.Core.TDF.TDF_Attribute):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    DumpToString = _swig_new_instance_method(_TDataXtd.TDataXtd_Plane_DumpToString)
    GetID = _swig_new_static_method(_TDataXtd.TDataXtd_Plane_GetID)
    Set = _swig_new_static_method(_TDataXtd.TDataXtd_Plane_Set)

    def __init__(self, *args):
        r""":rtype: None"""
        _TDataXtd.TDataXtd_Plane_swiginit(self, _TDataXtd.new_TDataXtd_Plane(*args))


    @staticmethod
    def DownCast(t):
      return Handle_TDataXtd_Plane_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _TDataXtd.delete_TDataXtd_Plane

# Register TDataXtd_Plane in _TDataXtd:
_TDataXtd.TDataXtd_Plane_swigregister(TDataXtd_Plane)
TDataXtd_Plane_GetID = _TDataXtd.TDataXtd_Plane_GetID
TDataXtd_Plane_Set = _TDataXtd.TDataXtd_Plane_Set

class TDataXtd_Point(OCC.Core.TDF.TDF_Attribute):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    DumpToString = _swig_new_instance_method(_TDataXtd.TDataXtd_Point_DumpToString)
    GetID = _swig_new_static_method(_TDataXtd.TDataXtd_Point_GetID)
    Set = _swig_new_static_method(_TDataXtd.TDataXtd_Point_Set)

    def __init__(self, *args):
        r""":rtype: None"""
        _TDataXtd.TDataXtd_Point_swiginit(self, _TDataXtd.new_TDataXtd_Point(*args))


    @staticmethod
    def DownCast(t):
      return Handle_TDataXtd_Point_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _TDataXtd.delete_TDataXtd_Point

# Register TDataXtd_Point in _TDataXtd:
_TDataXtd.TDataXtd_Point_swigregister(TDataXtd_Point)
TDataXtd_Point_GetID = _TDataXtd.TDataXtd_Point_GetID
TDataXtd_Point_Set = _TDataXtd.TDataXtd_Point_Set

class TDataXtd_Position(OCC.Core.TDF.TDF_Attribute):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Get = _swig_new_static_method(_TDataXtd.TDataXtd_Position_Get)
    GetID = _swig_new_static_method(_TDataXtd.TDataXtd_Position_GetID)
    GetPosition = _swig_new_instance_method(_TDataXtd.TDataXtd_Position_GetPosition)
    Set = _swig_new_static_method(_TDataXtd.TDataXtd_Position_Set)
    SetPosition = _swig_new_instance_method(_TDataXtd.TDataXtd_Position_SetPosition)

    def __init__(self, *args):
        r""":rtype: None"""
        _TDataXtd.TDataXtd_Position_swiginit(self, _TDataXtd.new_TDataXtd_Position(*args))


    @staticmethod
    def DownCast(t):
      return Handle_TDataXtd_Position_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _TDataXtd.delete_TDataXtd_Position

# Register TDataXtd_Position in _TDataXtd:
_TDataXtd.TDataXtd_Position_swigregister(TDataXtd_Position)
TDataXtd_Position_Get = _TDataXtd.TDataXtd_Position_Get
TDataXtd_Position_GetID = _TDataXtd.TDataXtd_Position_GetID
TDataXtd_Position_Set = _TDataXtd.TDataXtd_Position_Set

class TDataXtd_Presentation(OCC.Core.TDF.TDF_Attribute):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    AddSelectionMode = _swig_new_instance_method(_TDataXtd.TDataXtd_Presentation_AddSelectionMode)
    Color = _swig_new_instance_method(_TDataXtd.TDataXtd_Presentation_Color)
    GetDriverGUID = _swig_new_instance_method(_TDataXtd.TDataXtd_Presentation_GetDriverGUID)
    GetID = _swig_new_static_method(_TDataXtd.TDataXtd_Presentation_GetID)
    GetNbSelectionModes = _swig_new_instance_method(_TDataXtd.TDataXtd_Presentation_GetNbSelectionModes)
    HasOwnColor = _swig_new_instance_method(_TDataXtd.TDataXtd_Presentation_HasOwnColor)
    HasOwnMaterial = _swig_new_instance_method(_TDataXtd.TDataXtd_Presentation_HasOwnMaterial)
    HasOwnMode = _swig_new_instance_method(_TDataXtd.TDataXtd_Presentation_HasOwnMode)
    HasOwnSelectionMode = _swig_new_instance_method(_TDataXtd.TDataXtd_Presentation_HasOwnSelectionMode)
    HasOwnTransparency = _swig_new_instance_method(_TDataXtd.TDataXtd_Presentation_HasOwnTransparency)
    HasOwnWidth = _swig_new_instance_method(_TDataXtd.TDataXtd_Presentation_HasOwnWidth)
    IsDisplayed = _swig_new_instance_method(_TDataXtd.TDataXtd_Presentation_IsDisplayed)
    MaterialIndex = _swig_new_instance_method(_TDataXtd.TDataXtd_Presentation_MaterialIndex)
    Mode = _swig_new_instance_method(_TDataXtd.TDataXtd_Presentation_Mode)
    SelectionMode = _swig_new_instance_method(_TDataXtd.TDataXtd_Presentation_SelectionMode)
    Set = _swig_new_static_method(_TDataXtd.TDataXtd_Presentation_Set)
    SetColor = _swig_new_instance_method(_TDataXtd.TDataXtd_Presentation_SetColor)
    SetDisplayed = _swig_new_instance_method(_TDataXtd.TDataXtd_Presentation_SetDisplayed)
    SetDriverGUID = _swig_new_instance_method(_TDataXtd.TDataXtd_Presentation_SetDriverGUID)
    SetMaterialIndex = _swig_new_instance_method(_TDataXtd.TDataXtd_Presentation_SetMaterialIndex)
    SetMode = _swig_new_instance_method(_TDataXtd.TDataXtd_Presentation_SetMode)
    SetSelectionMode = _swig_new_instance_method(_TDataXtd.TDataXtd_Presentation_SetSelectionMode)
    SetTransparency = _swig_new_instance_method(_TDataXtd.TDataXtd_Presentation_SetTransparency)
    SetWidth = _swig_new_instance_method(_TDataXtd.TDataXtd_Presentation_SetWidth)

    def __init__(self, *args):
        r"""
        * //!@name Attribute mechanics Empty constructor
        	:rtype: None
        """
        _TDataXtd.TDataXtd_Presentation_swiginit(self, _TDataXtd.new_TDataXtd_Presentation(*args))
    Transparency = _swig_new_instance_method(_TDataXtd.TDataXtd_Presentation_Transparency)
    Unset = _swig_new_static_method(_TDataXtd.TDataXtd_Presentation_Unset)
    UnsetColor = _swig_new_instance_method(_TDataXtd.TDataXtd_Presentation_UnsetColor)
    UnsetMaterial = _swig_new_instance_method(_TDataXtd.TDataXtd_Presentation_UnsetMaterial)
    UnsetMode = _swig_new_instance_method(_TDataXtd.TDataXtd_Presentation_UnsetMode)
    UnsetSelectionMode = _swig_new_instance_method(_TDataXtd.TDataXtd_Presentation_UnsetSelectionMode)
    UnsetTransparency = _swig_new_instance_method(_TDataXtd.TDataXtd_Presentation_UnsetTransparency)
    UnsetWidth = _swig_new_instance_method(_TDataXtd.TDataXtd_Presentation_UnsetWidth)
    Width = _swig_new_instance_method(_TDataXtd.TDataXtd_Presentation_Width)


    @staticmethod
    def DownCast(t):
      return Handle_TDataXtd_Presentation_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _TDataXtd.delete_TDataXtd_Presentation

# Register TDataXtd_Presentation in _TDataXtd:
_TDataXtd.TDataXtd_Presentation_swigregister(TDataXtd_Presentation)
TDataXtd_Presentation_GetID = _TDataXtd.TDataXtd_Presentation_GetID
TDataXtd_Presentation_Set = _TDataXtd.TDataXtd_Presentation_Set
TDataXtd_Presentation_Unset = _TDataXtd.TDataXtd_Presentation_Unset

class TDataXtd_Shape(OCC.Core.TDF.TDF_Attribute):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    DumpToString = _swig_new_instance_method(_TDataXtd.TDataXtd_Shape_DumpToString)
    Find = _swig_new_static_method(_TDataXtd.TDataXtd_Shape_Find)
    Get = _swig_new_static_method(_TDataXtd.TDataXtd_Shape_Get)
    GetID = _swig_new_static_method(_TDataXtd.TDataXtd_Shape_GetID)
    New = _swig_new_static_method(_TDataXtd.TDataXtd_Shape_New)
    Set = _swig_new_static_method(_TDataXtd.TDataXtd_Shape_Set)

    def __init__(self, *args):
        r""":rtype: None"""
        _TDataXtd.TDataXtd_Shape_swiginit(self, _TDataXtd.new_TDataXtd_Shape(*args))


    @staticmethod
    def DownCast(t):
      return Handle_TDataXtd_Shape_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _TDataXtd.delete_TDataXtd_Shape

# Register TDataXtd_Shape in _TDataXtd:
_TDataXtd.TDataXtd_Shape_swigregister(TDataXtd_Shape)
TDataXtd_Shape_Find = _TDataXtd.TDataXtd_Shape_Find
TDataXtd_Shape_Get = _TDataXtd.TDataXtd_Shape_Get
TDataXtd_Shape_GetID = _TDataXtd.TDataXtd_Shape_GetID
TDataXtd_Shape_New = _TDataXtd.TDataXtd_Shape_New
TDataXtd_Shape_Set = _TDataXtd.TDataXtd_Shape_Set

class TDataXtd_Triangulation(OCC.Core.TDF.TDF_Attribute):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Deflection = _swig_new_instance_method(_TDataXtd.TDataXtd_Triangulation_Deflection)
    DumpToString = _swig_new_instance_method(_TDataXtd.TDataXtd_Triangulation_DumpToString)
    Get = _swig_new_instance_method(_TDataXtd.TDataXtd_Triangulation_Get)
    GetID = _swig_new_static_method(_TDataXtd.TDataXtd_Triangulation_GetID)
    HasNormals = _swig_new_instance_method(_TDataXtd.TDataXtd_Triangulation_HasNormals)
    HasUVNodes = _swig_new_instance_method(_TDataXtd.TDataXtd_Triangulation_HasUVNodes)
    NbNodes = _swig_new_instance_method(_TDataXtd.TDataXtd_Triangulation_NbNodes)
    NbTriangles = _swig_new_instance_method(_TDataXtd.TDataXtd_Triangulation_NbTriangles)
    Node = _swig_new_instance_method(_TDataXtd.TDataXtd_Triangulation_Node)
    Normal = _swig_new_instance_method(_TDataXtd.TDataXtd_Triangulation_Normal)
    RemoveUVNodes = _swig_new_instance_method(_TDataXtd.TDataXtd_Triangulation_RemoveUVNodes)
    Set = _swig_new_instance_method(_TDataXtd.TDataXtd_Triangulation_Set)
    SetNode = _swig_new_instance_method(_TDataXtd.TDataXtd_Triangulation_SetNode)
    SetNormal = _swig_new_instance_method(_TDataXtd.TDataXtd_Triangulation_SetNormal)
    SetNormals = _swig_new_instance_method(_TDataXtd.TDataXtd_Triangulation_SetNormals)
    SetTriangle = _swig_new_instance_method(_TDataXtd.TDataXtd_Triangulation_SetTriangle)
    SetUVNode = _swig_new_instance_method(_TDataXtd.TDataXtd_Triangulation_SetUVNode)

    def __init__(self, *args):
        r"""
        * Object methods A constructor. Don't use it directly, use please the static method Set(), which returns the attribute attached to a label.
        	:rtype: None
        """
        _TDataXtd.TDataXtd_Triangulation_swiginit(self, _TDataXtd.new_TDataXtd_Triangulation(*args))
    Triangle = _swig_new_instance_method(_TDataXtd.TDataXtd_Triangulation_Triangle)
    UVNode = _swig_new_instance_method(_TDataXtd.TDataXtd_Triangulation_UVNode)


    @staticmethod
    def DownCast(t):
      return Handle_TDataXtd_Triangulation_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _TDataXtd.delete_TDataXtd_Triangulation

# Register TDataXtd_Triangulation in _TDataXtd:
_TDataXtd.TDataXtd_Triangulation_swigregister(TDataXtd_Triangulation)
TDataXtd_Triangulation_GetID = _TDataXtd.TDataXtd_Triangulation_GetID

class TDataXtd_PatternStd(TDataXtd_Pattern):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Axis1 = _swig_new_instance_method(_TDataXtd.TDataXtd_PatternStd_Axis1)
    Axis1Reversed = _swig_new_instance_method(_TDataXtd.TDataXtd_PatternStd_Axis1Reversed)
    Axis2 = _swig_new_instance_method(_TDataXtd.TDataXtd_PatternStd_Axis2)
    Axis2Reversed = _swig_new_instance_method(_TDataXtd.TDataXtd_PatternStd_Axis2Reversed)
    DumpToString = _swig_new_instance_method(_TDataXtd.TDataXtd_PatternStd_DumpToString)
    GetPatternID = _swig_new_static_method(_TDataXtd.TDataXtd_PatternStd_GetPatternID)
    Mirror = _swig_new_instance_method(_TDataXtd.TDataXtd_PatternStd_Mirror)
    NbInstances1 = _swig_new_instance_method(_TDataXtd.TDataXtd_PatternStd_NbInstances1)
    NbInstances2 = _swig_new_instance_method(_TDataXtd.TDataXtd_PatternStd_NbInstances2)
    Set = _swig_new_static_method(_TDataXtd.TDataXtd_PatternStd_Set)
    Signature = _swig_new_instance_method(_TDataXtd.TDataXtd_PatternStd_Signature)

    def __init__(self, *args):
        r""":rtype: None"""
        _TDataXtd.TDataXtd_PatternStd_swiginit(self, _TDataXtd.new_TDataXtd_PatternStd(*args))
    Value1 = _swig_new_instance_method(_TDataXtd.TDataXtd_PatternStd_Value1)
    Value2 = _swig_new_instance_method(_TDataXtd.TDataXtd_PatternStd_Value2)


    @staticmethod
    def DownCast(t):
      return Handle_TDataXtd_PatternStd_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _TDataXtd.delete_TDataXtd_PatternStd

# Register TDataXtd_PatternStd in _TDataXtd:
_TDataXtd.TDataXtd_PatternStd_swigregister(TDataXtd_PatternStd)
TDataXtd_PatternStd_GetPatternID = _TDataXtd.TDataXtd_PatternStd_GetPatternID
TDataXtd_PatternStd_Set = _TDataXtd.TDataXtd_PatternStd_Set

class TDataXtd_HArray1OfTrsf(TDataXtd_Array1OfTrsf, OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _TDataXtd.TDataXtd_HArray1OfTrsf_swiginit(self, _TDataXtd.new_TDataXtd_HArray1OfTrsf(*args))
    Array1 = _swig_new_instance_method(_TDataXtd.TDataXtd_HArray1OfTrsf_Array1)
    ChangeArray1 = _swig_new_instance_method(_TDataXtd.TDataXtd_HArray1OfTrsf_ChangeArray1)


    @staticmethod
    def DownCast(t):
      return Handle_TDataXtd_HArray1OfTrsf_DownCast(t)

    __swig_destroy__ = _TDataXtd.delete_TDataXtd_HArray1OfTrsf

# Register TDataXtd_HArray1OfTrsf in _TDataXtd:
_TDataXtd.TDataXtd_HArray1OfTrsf_swigregister(TDataXtd_HArray1OfTrsf)



