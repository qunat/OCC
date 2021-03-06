# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
Bisector module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_bisector.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _Bisector
else:
    import _Bisector

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _Bisector.SWIG_PyInstanceMethod_New
_swig_new_static_method = _Bisector.SWIG_PyStaticMethod_New

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
    __swig_destroy__ = _Bisector.delete_SwigPyIterator
    value = _swig_new_instance_method(_Bisector.SwigPyIterator_value)
    incr = _swig_new_instance_method(_Bisector.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_Bisector.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_Bisector.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_Bisector.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_Bisector.SwigPyIterator_copy)
    next = _swig_new_instance_method(_Bisector.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_Bisector.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_Bisector.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_Bisector.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_Bisector.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_Bisector.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_Bisector.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_Bisector.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_Bisector.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_Bisector.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _Bisector:
_Bisector.SwigPyIterator_swigregister(SwigPyIterator)


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
import OCC.Core.Geom2d
import OCC.Core.gp
import OCC.Core.GeomAbs
import OCC.Core.TColgp
import OCC.Core.TColStd
import OCC.Core.TCollection
import OCC.Core.math
import OCC.Core.Message
import OCC.Core.IntRes2d
Handle_Bisector_Curve_Create = _Bisector.Handle_Bisector_Curve_Create
Handle_Bisector_Curve_DownCast = _Bisector.Handle_Bisector_Curve_DownCast
Handle_Bisector_Curve_IsNull = _Bisector.Handle_Bisector_Curve_IsNull
Handle_Bisector_BisecAna_Create = _Bisector.Handle_Bisector_BisecAna_Create
Handle_Bisector_BisecAna_DownCast = _Bisector.Handle_Bisector_BisecAna_DownCast
Handle_Bisector_BisecAna_IsNull = _Bisector.Handle_Bisector_BisecAna_IsNull
Handle_Bisector_BisecCC_Create = _Bisector.Handle_Bisector_BisecCC_Create
Handle_Bisector_BisecCC_DownCast = _Bisector.Handle_Bisector_BisecCC_DownCast
Handle_Bisector_BisecCC_IsNull = _Bisector.Handle_Bisector_BisecCC_IsNull
Handle_Bisector_BisecPC_Create = _Bisector.Handle_Bisector_BisecPC_Create
Handle_Bisector_BisecPC_DownCast = _Bisector.Handle_Bisector_BisecPC_DownCast
Handle_Bisector_BisecPC_IsNull = _Bisector.Handle_Bisector_BisecPC_IsNull
class bisector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    IsConvex = _swig_new_static_method(_Bisector.bisector_IsConvex)

    __repr__ = _dumps_object


    def __init__(self):
        _Bisector.bisector_swiginit(self, _Bisector.new_bisector())
    __swig_destroy__ = _Bisector.delete_bisector

# Register bisector in _Bisector:
_Bisector.bisector_swigregister(bisector)
bisector_IsConvex = _Bisector.bisector_IsConvex

class Bisector_Bisec(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r""":rtype: None"""
        _Bisector.Bisector_Bisec_swiginit(self, _Bisector.new_Bisector_Bisec(*args))
    ChangeValue = _swig_new_instance_method(_Bisector.Bisector_Bisec_ChangeValue)
    Perform = _swig_new_instance_method(_Bisector.Bisector_Bisec_Perform)
    Value = _swig_new_instance_method(_Bisector.Bisector_Bisec_Value)

    __repr__ = _dumps_object

    __swig_destroy__ = _Bisector.delete_Bisector_Bisec

# Register Bisector_Bisec in _Bisector:
_Bisector.Bisector_Bisec_swigregister(Bisector_Bisec)

class Bisector_Curve(OCC.Core.Geom2d.Geom2d_Curve):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    IntervalFirst = _swig_new_instance_method(_Bisector.Bisector_Curve_IntervalFirst)
    IntervalLast = _swig_new_instance_method(_Bisector.Bisector_Curve_IntervalLast)
    IsExtendAtEnd = _swig_new_instance_method(_Bisector.Bisector_Curve_IsExtendAtEnd)
    IsExtendAtStart = _swig_new_instance_method(_Bisector.Bisector_Curve_IsExtendAtStart)
    NbIntervals = _swig_new_instance_method(_Bisector.Bisector_Curve_NbIntervals)
    Parameter = _swig_new_instance_method(_Bisector.Bisector_Curve_Parameter)


    @staticmethod
    def DownCast(t):
      return Handle_Bisector_Curve_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _Bisector.delete_Bisector_Curve

# Register Bisector_Curve in _Bisector:
_Bisector.Bisector_Curve_swigregister(Bisector_Curve)

class Bisector_FunctionH(OCC.Core.math.math_FunctionWithDerivative):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :param C2:
        	:type C2: Geom2d_Curve
        	:param P1:
        	:type P1: gp_Pnt2d
        	:param T1:
        	:type T1: gp_Vec2d
        	:rtype: None
        """
        _Bisector.Bisector_FunctionH_swiginit(self, _Bisector.new_Bisector_FunctionH(*args))

    __repr__ = _dumps_object

    __swig_destroy__ = _Bisector.delete_Bisector_FunctionH

# Register Bisector_FunctionH in _Bisector:
_Bisector.Bisector_FunctionH_swigregister(Bisector_FunctionH)

class Bisector_FunctionInter(OCC.Core.math.math_FunctionWithDerivative):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :rtype: None:param C:
        	:type C: Geom2d_Curve
        	:param Bis1:
        	:type Bis1: Bisector_Curve
        	:param Bis2:
        	:type Bis2: Bisector_Curve
        	:rtype: None
        """
        _Bisector.Bisector_FunctionInter_swiginit(self, _Bisector.new_Bisector_FunctionInter(*args))
    Perform = _swig_new_instance_method(_Bisector.Bisector_FunctionInter_Perform)

    __repr__ = _dumps_object

    __swig_destroy__ = _Bisector.delete_Bisector_FunctionInter

# Register Bisector_FunctionInter in _Bisector:
_Bisector.Bisector_FunctionInter_swigregister(Bisector_FunctionInter)

class Bisector_Inter(OCC.Core.IntRes2d.IntRes2d_Intersection):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :rtype: None* Intersection between 2 curves. C1 separates the element A and B. C2 separates the elements C et D. If B an C have the same geometry. <ComunElement> Has to be True. It Permits an optimiztion of the computation.
        	:param C1:
        	:type C1: Bisector_Bisec
        	:param D1:
        	:type D1: IntRes2d_Domain
        	:param C2:
        	:type C2: Bisector_Bisec
        	:param D2:
        	:type D2: IntRes2d_Domain
        	:param TolConf:
        	:type TolConf: float
        	:param Tol:
        	:type Tol: float
        	:param ComunElement:
        	:type ComunElement: bool
        	:rtype: None
        """
        _Bisector.Bisector_Inter_swiginit(self, _Bisector.new_Bisector_Inter(*args))
    Perform = _swig_new_instance_method(_Bisector.Bisector_Inter_Perform)

    __repr__ = _dumps_object

    __swig_destroy__ = _Bisector.delete_Bisector_Inter

# Register Bisector_Inter in _Bisector:
_Bisector.Bisector_Inter_swigregister(Bisector_Inter)

class Bisector_PointOnBis(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :rtype: None:param Param1:
        	:type Param1: float
        	:param Param2:
        	:type Param2: float
        	:param ParamBis:
        	:type ParamBis: float
        	:param Distance:
        	:type Distance: float
        	:param Point:
        	:type Point: gp_Pnt2d
        	:rtype: None
        """
        _Bisector.Bisector_PointOnBis_swiginit(self, _Bisector.new_Bisector_PointOnBis(*args))
    Distance = _swig_new_instance_method(_Bisector.Bisector_PointOnBis_Distance)
    Dump = _swig_new_instance_method(_Bisector.Bisector_PointOnBis_Dump)
    IsInfinite = _swig_new_instance_method(_Bisector.Bisector_PointOnBis_IsInfinite)
    ParamOnBis = _swig_new_instance_method(_Bisector.Bisector_PointOnBis_ParamOnBis)
    ParamOnC1 = _swig_new_instance_method(_Bisector.Bisector_PointOnBis_ParamOnC1)
    ParamOnC2 = _swig_new_instance_method(_Bisector.Bisector_PointOnBis_ParamOnC2)
    Point = _swig_new_instance_method(_Bisector.Bisector_PointOnBis_Point)

    __repr__ = _dumps_object

    __swig_destroy__ = _Bisector.delete_Bisector_PointOnBis

# Register Bisector_PointOnBis in _Bisector:
_Bisector.Bisector_PointOnBis_swigregister(Bisector_PointOnBis)

class Bisector_PolyBis(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Append = _swig_new_instance_method(_Bisector.Bisector_PolyBis_Append)

    def __init__(self, *args):
        r""":rtype: None"""
        _Bisector.Bisector_PolyBis_swiginit(self, _Bisector.new_Bisector_PolyBis(*args))
    First = _swig_new_instance_method(_Bisector.Bisector_PolyBis_First)
    Interval = _swig_new_instance_method(_Bisector.Bisector_PolyBis_Interval)
    IsEmpty = _swig_new_instance_method(_Bisector.Bisector_PolyBis_IsEmpty)
    Last = _swig_new_instance_method(_Bisector.Bisector_PolyBis_Last)
    Length = _swig_new_instance_method(_Bisector.Bisector_PolyBis_Length)
    Transform = _swig_new_instance_method(_Bisector.Bisector_PolyBis_Transform)
    Value = _swig_new_instance_method(_Bisector.Bisector_PolyBis_Value)

    __repr__ = _dumps_object

    __swig_destroy__ = _Bisector.delete_Bisector_PolyBis

# Register Bisector_PolyBis in _Bisector:
_Bisector.Bisector_PolyBis_swigregister(Bisector_PolyBis)

class Bisector_BisecAna(Bisector_Curve):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r""":rtype: None"""
        _Bisector.Bisector_BisecAna_swiginit(self, _Bisector.new_Bisector_BisecAna(*args))
    Dump = _swig_new_instance_method(_Bisector.Bisector_BisecAna_Dump)
    Geom2dCurve = _swig_new_instance_method(_Bisector.Bisector_BisecAna_Geom2dCurve)
    Init = _swig_new_instance_method(_Bisector.Bisector_BisecAna_Init)
    ParameterOfEndPoint = _swig_new_instance_method(_Bisector.Bisector_BisecAna_ParameterOfEndPoint)
    ParameterOfStartPoint = _swig_new_instance_method(_Bisector.Bisector_BisecAna_ParameterOfStartPoint)
    Perform = _swig_new_instance_method(_Bisector.Bisector_BisecAna_Perform)
    SetTrim = _swig_new_instance_method(_Bisector.Bisector_BisecAna_SetTrim)


    @staticmethod
    def DownCast(t):
      return Handle_Bisector_BisecAna_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _Bisector.delete_Bisector_BisecAna

# Register Bisector_BisecAna in _Bisector:
_Bisector.Bisector_BisecAna_swigregister(Bisector_BisecAna)

class Bisector_BisecCC(Bisector_Curve):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :rtype: None* Constructs the bisector between the curves <Cu1> and <Cu2>. //! <Side1> (resp <Side2>) = 1 if the bisector curve is on the left of <Cu1> (resp <Cu2>) else <Side1> (resp <Side2>) = -1. //! the Bisector is trimmed by the Point <Origin>. <DistMax> is used to trim the bisector.The distance between the points of the bisector and <Cu> is smaller than <DistMax>.
        	:param Cu1:
        	:type Cu1: Geom2d_Curve
        	:param Cu2:
        	:type Cu2: Geom2d_Curve
        	:param Side1:
        	:type Side1: float
        	:param Side2:
        	:type Side2: float
        	:param Origin:
        	:type Origin: gp_Pnt2d
        	:param DistMax: default value is 500
        	:type DistMax: float
        	:rtype: None
        """
        _Bisector.Bisector_BisecCC_swiginit(self, _Bisector.new_Bisector_BisecCC(*args))
    ChangeGuide = _swig_new_instance_method(_Bisector.Bisector_BisecCC_ChangeGuide)
    Curve = _swig_new_instance_method(_Bisector.Bisector_BisecCC_Curve)
    Dump = _swig_new_instance_method(_Bisector.Bisector_BisecCC_Dump)
    IntervalContinuity = _swig_new_instance_method(_Bisector.Bisector_BisecCC_IntervalContinuity)
    IsEmpty = _swig_new_instance_method(_Bisector.Bisector_BisecCC_IsEmpty)
    LinkBisCurve = _swig_new_instance_method(_Bisector.Bisector_BisecCC_LinkBisCurve)
    LinkCurveBis = _swig_new_instance_method(_Bisector.Bisector_BisecCC_LinkCurveBis)
    Perform = _swig_new_instance_method(_Bisector.Bisector_BisecCC_Perform)
    Polygon = _swig_new_instance_method(_Bisector.Bisector_BisecCC_Polygon)
    ValueAndDist = _swig_new_instance_method(_Bisector.Bisector_BisecCC_ValueAndDist)
    ValueByInt = _swig_new_instance_method(_Bisector.Bisector_BisecCC_ValueByInt)


    @staticmethod
    def DownCast(t):
      return Handle_Bisector_BisecCC_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _Bisector.delete_Bisector_BisecCC

# Register Bisector_BisecCC in _Bisector:
_Bisector.Bisector_BisecCC_swigregister(Bisector_BisecCC)

class Bisector_BisecPC(Bisector_Curve):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :rtype: None* Constructs the bisector between the point <P> and the curve <Cu>. <Side> = 1. if the bisector curve is on the Left of <Cu> else <Side> = -1. <DistMax> is used to trim the bisector.The distance between the points of the bisector and <Cu> is smaller than <DistMax>.
        	:param Cu:
        	:type Cu: Geom2d_Curve
        	:param P:
        	:type P: gp_Pnt2d
        	:param Side:
        	:type Side: float
        	:param DistMax: default value is 500
        	:type DistMax: float
        	:rtype: None* Constructs the bisector between the point <P> and the curve <Cu> Trimmed by <UMin> and <UMax> <Side> = 1. if the bisector curve is on the Left of <Cu> else <Side> = -1. Warning: the bisector is supposed all over defined between <UMin> and <UMax>.
        	:param Cu:
        	:type Cu: Geom2d_Curve
        	:param P:
        	:type P: gp_Pnt2d
        	:param Side:
        	:type Side: float
        	:param UMin:
        	:type UMin: float
        	:param UMax:
        	:type UMax: float
        	:rtype: None
        """
        _Bisector.Bisector_BisecPC_swiginit(self, _Bisector.new_Bisector_BisecPC(*args))
    Distance = _swig_new_instance_method(_Bisector.Bisector_BisecPC_Distance)
    Dump = _swig_new_instance_method(_Bisector.Bisector_BisecPC_Dump)
    IntervalContinuity = _swig_new_instance_method(_Bisector.Bisector_BisecPC_IntervalContinuity)
    IsEmpty = _swig_new_instance_method(_Bisector.Bisector_BisecPC_IsEmpty)
    LinkBisCurve = _swig_new_instance_method(_Bisector.Bisector_BisecPC_LinkBisCurve)
    LinkCurveBis = _swig_new_instance_method(_Bisector.Bisector_BisecPC_LinkCurveBis)
    Perform = _swig_new_instance_method(_Bisector.Bisector_BisecPC_Perform)


    @staticmethod
    def DownCast(t):
      return Handle_Bisector_BisecPC_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _Bisector.delete_Bisector_BisecPC

# Register Bisector_BisecPC in _Bisector:
_Bisector.Bisector_BisecPC_swigregister(Bisector_BisecPC)



