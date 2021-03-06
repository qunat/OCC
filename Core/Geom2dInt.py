# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
Geom2dInt module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_geom2dint.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _Geom2dInt
else:
    import _Geom2dInt

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _Geom2dInt.SWIG_PyInstanceMethod_New
_swig_new_static_method = _Geom2dInt.SWIG_PyStaticMethod_New

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
    __swig_destroy__ = _Geom2dInt.delete_SwigPyIterator
    value = _swig_new_instance_method(_Geom2dInt.SwigPyIterator_value)
    incr = _swig_new_instance_method(_Geom2dInt.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_Geom2dInt.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_Geom2dInt.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_Geom2dInt.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_Geom2dInt.SwigPyIterator_copy)
    next = _swig_new_instance_method(_Geom2dInt.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_Geom2dInt.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_Geom2dInt.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_Geom2dInt.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_Geom2dInt.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_Geom2dInt.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_Geom2dInt.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_Geom2dInt.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_Geom2dInt.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_Geom2dInt.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _Geom2dInt:
_Geom2dInt.SwigPyIterator_swigregister(SwigPyIterator)


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
import OCC.Core.Adaptor2d
import OCC.Core.Geom2d
import OCC.Core.gp
import OCC.Core.GeomAbs
import OCC.Core.TColgp
import OCC.Core.TColStd
import OCC.Core.TCollection
import OCC.Core.IntRes2d
import OCC.Core.math
import OCC.Core.Message
import OCC.Core.IntCurve
import OCC.Core.Extrema
import OCC.Core.Adaptor3d
import OCC.Core.Geom
import OCC.Core.TopAbs
import OCC.Core.GeomAdaptor
import OCC.Core.Intf
import OCC.Core.Bnd
import OCC.Core.BVH
class Geom2dInt_ExactIntersectionPointOfTheIntPCurvePCurveOfGInter(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    AnErrorOccurred = _swig_new_instance_method(_Geom2dInt.Geom2dInt_ExactIntersectionPointOfTheIntPCurvePCurveOfGInter_AnErrorOccurred)

    def __init__(self, *args):
        r"""
        :param C1:
        	:type C1: Adaptor2d_Curve2d
        	:param C2:
        	:type C2: Adaptor2d_Curve2d
        	:param Tol:
        	:type Tol: float
        	:rtype: None
        """
        _Geom2dInt.Geom2dInt_ExactIntersectionPointOfTheIntPCurvePCurveOfGInter_swiginit(self, _Geom2dInt.new_Geom2dInt_ExactIntersectionPointOfTheIntPCurvePCurveOfGInter(*args))
    NbRoots = _swig_new_instance_method(_Geom2dInt.Geom2dInt_ExactIntersectionPointOfTheIntPCurvePCurveOfGInter_NbRoots)
    Perform = _swig_new_instance_method(_Geom2dInt.Geom2dInt_ExactIntersectionPointOfTheIntPCurvePCurveOfGInter_Perform)
    Roots = _swig_new_instance_method(_Geom2dInt.Geom2dInt_ExactIntersectionPointOfTheIntPCurvePCurveOfGInter_Roots)

    __repr__ = _dumps_object

    __swig_destroy__ = _Geom2dInt.delete_Geom2dInt_ExactIntersectionPointOfTheIntPCurvePCurveOfGInter

# Register Geom2dInt_ExactIntersectionPointOfTheIntPCurvePCurveOfGInter in _Geom2dInt:
_Geom2dInt.Geom2dInt_ExactIntersectionPointOfTheIntPCurvePCurveOfGInter_swigregister(Geom2dInt_ExactIntersectionPointOfTheIntPCurvePCurveOfGInter)

class Geom2dInt_GInter(OCC.Core.IntRes2d.IntRes2d_Intersection):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    ComputeDomain = _swig_new_instance_method(_Geom2dInt.Geom2dInt_GInter_ComputeDomain)

    def __init__(self, *args):
        r"""
        * Empty constructor.
        	:rtype: None* Self Intersection of a curve
        	:param C:
        	:type C: Adaptor2d_Curve2d
        	:param TolConf:
        	:type TolConf: float
        	:param Tol:
        	:type Tol: float
        	:rtype: None* Self Intersection of a curve with a domain.
        	:param C:
        	:type C: Adaptor2d_Curve2d
        	:param D:
        	:type D: IntRes2d_Domain
        	:param TolConf:
        	:type TolConf: float
        	:param Tol:
        	:type Tol: float
        	:rtype: None* Intersection between 2 curves.
        	:param C1:
        	:type C1: Adaptor2d_Curve2d
        	:param C2:
        	:type C2: Adaptor2d_Curve2d
        	:param TolConf:
        	:type TolConf: float
        	:param Tol:
        	:type Tol: float
        	:rtype: None* Intersection between 2 curves.
        	:param C1:
        	:type C1: Adaptor2d_Curve2d
        	:param D1:
        	:type D1: IntRes2d_Domain
        	:param C2:
        	:type C2: Adaptor2d_Curve2d
        	:param TolConf:
        	:type TolConf: float
        	:param Tol:
        	:type Tol: float
        	:rtype: None* Intersection between 2 curves.
        	:param C1:
        	:type C1: Adaptor2d_Curve2d
        	:param C2:
        	:type C2: Adaptor2d_Curve2d
        	:param D2:
        	:type D2: IntRes2d_Domain
        	:param TolConf:
        	:type TolConf: float
        	:param Tol:
        	:type Tol: float
        	:rtype: None* Intersection between 2 curves.
        	:param C1:
        	:type C1: Adaptor2d_Curve2d
        	:param D1:
        	:type D1: IntRes2d_Domain
        	:param C2:
        	:type C2: Adaptor2d_Curve2d
        	:param D2:
        	:type D2: IntRes2d_Domain
        	:param TolConf:
        	:type TolConf: float
        	:param Tol:
        	:type Tol: float
        	:rtype: None
        """
        _Geom2dInt.Geom2dInt_GInter_swiginit(self, _Geom2dInt.new_Geom2dInt_GInter(*args))
    GetMinNbSamples = _swig_new_instance_method(_Geom2dInt.Geom2dInt_GInter_GetMinNbSamples)
    Perform = _swig_new_instance_method(_Geom2dInt.Geom2dInt_GInter_Perform)
    SetMinNbSamples = _swig_new_instance_method(_Geom2dInt.Geom2dInt_GInter_SetMinNbSamples)

    __repr__ = _dumps_object

    __swig_destroy__ = _Geom2dInt.delete_Geom2dInt_GInter

# Register Geom2dInt_GInter in _Geom2dInt:
_Geom2dInt.Geom2dInt_GInter_swigregister(Geom2dInt_GInter)

class Geom2dInt_Geom2dCurveTool(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Circle = _swig_new_static_method(_Geom2dInt.Geom2dInt_Geom2dCurveTool_Circle)
    D0 = _swig_new_static_method(_Geom2dInt.Geom2dInt_Geom2dCurveTool_D0)
    D1 = _swig_new_static_method(_Geom2dInt.Geom2dInt_Geom2dCurveTool_D1)
    D2 = _swig_new_static_method(_Geom2dInt.Geom2dInt_Geom2dCurveTool_D2)
    D3 = _swig_new_static_method(_Geom2dInt.Geom2dInt_Geom2dCurveTool_D3)
    DN = _swig_new_static_method(_Geom2dInt.Geom2dInt_Geom2dCurveTool_DN)
    Degree = _swig_new_static_method(_Geom2dInt.Geom2dInt_Geom2dCurveTool_Degree)
    Ellipse = _swig_new_static_method(_Geom2dInt.Geom2dInt_Geom2dCurveTool_Ellipse)
    EpsX = _swig_new_static_method(_Geom2dInt.Geom2dInt_Geom2dCurveTool_EpsX)
    FirstParameter = _swig_new_static_method(_Geom2dInt.Geom2dInt_Geom2dCurveTool_FirstParameter)
    GetInterval = _swig_new_static_method(_Geom2dInt.Geom2dInt_Geom2dCurveTool_GetInterval)
    GetType = _swig_new_static_method(_Geom2dInt.Geom2dInt_Geom2dCurveTool_GetType)
    Hyperbola = _swig_new_static_method(_Geom2dInt.Geom2dInt_Geom2dCurveTool_Hyperbola)
    Intervals = _swig_new_static_method(_Geom2dInt.Geom2dInt_Geom2dCurveTool_Intervals)
    LastParameter = _swig_new_static_method(_Geom2dInt.Geom2dInt_Geom2dCurveTool_LastParameter)
    Line = _swig_new_static_method(_Geom2dInt.Geom2dInt_Geom2dCurveTool_Line)
    NbIntervals = _swig_new_static_method(_Geom2dInt.Geom2dInt_Geom2dCurveTool_NbIntervals)
    NbSamples = _swig_new_static_method(_Geom2dInt.Geom2dInt_Geom2dCurveTool_NbSamples)
    Parabola = _swig_new_static_method(_Geom2dInt.Geom2dInt_Geom2dCurveTool_Parabola)
    Value = _swig_new_static_method(_Geom2dInt.Geom2dInt_Geom2dCurveTool_Value)

    __repr__ = _dumps_object


    def __init__(self):
        _Geom2dInt.Geom2dInt_Geom2dCurveTool_swiginit(self, _Geom2dInt.new_Geom2dInt_Geom2dCurveTool())
    __swig_destroy__ = _Geom2dInt.delete_Geom2dInt_Geom2dCurveTool

# Register Geom2dInt_Geom2dCurveTool in _Geom2dInt:
_Geom2dInt.Geom2dInt_Geom2dCurveTool_swigregister(Geom2dInt_Geom2dCurveTool)
Geom2dInt_Geom2dCurveTool_Circle = _Geom2dInt.Geom2dInt_Geom2dCurveTool_Circle
Geom2dInt_Geom2dCurveTool_D0 = _Geom2dInt.Geom2dInt_Geom2dCurveTool_D0
Geom2dInt_Geom2dCurveTool_D1 = _Geom2dInt.Geom2dInt_Geom2dCurveTool_D1
Geom2dInt_Geom2dCurveTool_D2 = _Geom2dInt.Geom2dInt_Geom2dCurveTool_D2
Geom2dInt_Geom2dCurveTool_D3 = _Geom2dInt.Geom2dInt_Geom2dCurveTool_D3
Geom2dInt_Geom2dCurveTool_DN = _Geom2dInt.Geom2dInt_Geom2dCurveTool_DN
Geom2dInt_Geom2dCurveTool_Degree = _Geom2dInt.Geom2dInt_Geom2dCurveTool_Degree
Geom2dInt_Geom2dCurveTool_Ellipse = _Geom2dInt.Geom2dInt_Geom2dCurveTool_Ellipse
Geom2dInt_Geom2dCurveTool_EpsX = _Geom2dInt.Geom2dInt_Geom2dCurveTool_EpsX
Geom2dInt_Geom2dCurveTool_FirstParameter = _Geom2dInt.Geom2dInt_Geom2dCurveTool_FirstParameter
Geom2dInt_Geom2dCurveTool_GetInterval = _Geom2dInt.Geom2dInt_Geom2dCurveTool_GetInterval
Geom2dInt_Geom2dCurveTool_GetType = _Geom2dInt.Geom2dInt_Geom2dCurveTool_GetType
Geom2dInt_Geom2dCurveTool_Hyperbola = _Geom2dInt.Geom2dInt_Geom2dCurveTool_Hyperbola
Geom2dInt_Geom2dCurveTool_Intervals = _Geom2dInt.Geom2dInt_Geom2dCurveTool_Intervals
Geom2dInt_Geom2dCurveTool_LastParameter = _Geom2dInt.Geom2dInt_Geom2dCurveTool_LastParameter
Geom2dInt_Geom2dCurveTool_Line = _Geom2dInt.Geom2dInt_Geom2dCurveTool_Line
Geom2dInt_Geom2dCurveTool_NbIntervals = _Geom2dInt.Geom2dInt_Geom2dCurveTool_NbIntervals
Geom2dInt_Geom2dCurveTool_NbSamples = _Geom2dInt.Geom2dInt_Geom2dCurveTool_NbSamples
Geom2dInt_Geom2dCurveTool_Parabola = _Geom2dInt.Geom2dInt_Geom2dCurveTool_Parabola
Geom2dInt_Geom2dCurveTool_Value = _Geom2dInt.Geom2dInt_Geom2dCurveTool_Value

class Geom2dInt_IntConicCurveOfGInter(OCC.Core.IntRes2d.IntRes2d_Intersection):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Empty constructor.
        	:rtype: None* Intersection between a line and a parametric curve.
        	:param L:
        	:type L: gp_Lin2d
        	:param D1:
        	:type D1: IntRes2d_Domain
        	:param PCurve:
        	:type PCurve: Adaptor2d_Curve2d
        	:param D2:
        	:type D2: IntRes2d_Domain
        	:param TolConf:
        	:type TolConf: float
        	:param Tol:
        	:type Tol: float
        	:rtype: None* Intersection between a line and a parametric curve.
        	:param C:
        	:type C: gp_Circ2d
        	:param D1:
        	:type D1: IntRes2d_Domain
        	:param PCurve:
        	:type PCurve: Adaptor2d_Curve2d
        	:param D2:
        	:type D2: IntRes2d_Domain
        	:param TolConf:
        	:type TolConf: float
        	:param Tol:
        	:type Tol: float
        	:rtype: None* Intersection between an ellipse and a parametric curve.
        	:param E:
        	:type E: gp_Elips2d
        	:param D1:
        	:type D1: IntRes2d_Domain
        	:param PCurve:
        	:type PCurve: Adaptor2d_Curve2d
        	:param D2:
        	:type D2: IntRes2d_Domain
        	:param TolConf:
        	:type TolConf: float
        	:param Tol:
        	:type Tol: float
        	:rtype: None* Intersection between a parabola and a parametric curve.
        	:param Prb:
        	:type Prb: gp_Parab2d
        	:param D1:
        	:type D1: IntRes2d_Domain
        	:param PCurve:
        	:type PCurve: Adaptor2d_Curve2d
        	:param D2:
        	:type D2: IntRes2d_Domain
        	:param TolConf:
        	:type TolConf: float
        	:param Tol:
        	:type Tol: float
        	:rtype: None* Intersection between the main branch of an hyperbola and a parametric curve.
        	:param H:
        	:type H: gp_Hypr2d
        	:param D1:
        	:type D1: IntRes2d_Domain
        	:param PCurve:
        	:type PCurve: Adaptor2d_Curve2d
        	:param D2:
        	:type D2: IntRes2d_Domain
        	:param TolConf:
        	:type TolConf: float
        	:param Tol:
        	:type Tol: float
        	:rtype: None
        """
        _Geom2dInt.Geom2dInt_IntConicCurveOfGInter_swiginit(self, _Geom2dInt.new_Geom2dInt_IntConicCurveOfGInter(*args))
    Perform = _swig_new_instance_method(_Geom2dInt.Geom2dInt_IntConicCurveOfGInter_Perform)

    __repr__ = _dumps_object

    __swig_destroy__ = _Geom2dInt.delete_Geom2dInt_IntConicCurveOfGInter

# Register Geom2dInt_IntConicCurveOfGInter in _Geom2dInt:
_Geom2dInt.Geom2dInt_IntConicCurveOfGInter_swigregister(Geom2dInt_IntConicCurveOfGInter)

class Geom2dInt_MyImpParToolOfTheIntersectorOfTheIntConicCurveOfGInter(OCC.Core.math.math_FunctionWithDerivative):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Constructor of the class.
        	:param IT:
        	:type IT: IntCurve_IConicTool
        	:param PC:
        	:type PC: Adaptor2d_Curve2d
        	:rtype: None
        """
        _Geom2dInt.Geom2dInt_MyImpParToolOfTheIntersectorOfTheIntConicCurveOfGInter_swiginit(self, _Geom2dInt.new_Geom2dInt_MyImpParToolOfTheIntersectorOfTheIntConicCurveOfGInter(*args))

    __repr__ = _dumps_object

    __swig_destroy__ = _Geom2dInt.delete_Geom2dInt_MyImpParToolOfTheIntersectorOfTheIntConicCurveOfGInter

# Register Geom2dInt_MyImpParToolOfTheIntersectorOfTheIntConicCurveOfGInter in _Geom2dInt:
_Geom2dInt.Geom2dInt_MyImpParToolOfTheIntersectorOfTheIntConicCurveOfGInter_swigregister(Geom2dInt_MyImpParToolOfTheIntersectorOfTheIntConicCurveOfGInter)

class Geom2dInt_PCLocFOfTheLocateExtPCOfTheProjPCurOfGInter(OCC.Core.math.math_FunctionWithDerivative):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :rtype: None:param P:
        	:type P: gp_Pnt2d
        	:param C:
        	:type C: Adaptor2d_Curve2d
        	:rtype: None
        """
        _Geom2dInt.Geom2dInt_PCLocFOfTheLocateExtPCOfTheProjPCurOfGInter_swiginit(self, _Geom2dInt.new_Geom2dInt_PCLocFOfTheLocateExtPCOfTheProjPCurOfGInter(*args))
    Initialize = _swig_new_instance_method(_Geom2dInt.Geom2dInt_PCLocFOfTheLocateExtPCOfTheProjPCurOfGInter_Initialize)
    IsMin = _swig_new_instance_method(_Geom2dInt.Geom2dInt_PCLocFOfTheLocateExtPCOfTheProjPCurOfGInter_IsMin)
    NbExt = _swig_new_instance_method(_Geom2dInt.Geom2dInt_PCLocFOfTheLocateExtPCOfTheProjPCurOfGInter_NbExt)
    Point = _swig_new_instance_method(_Geom2dInt.Geom2dInt_PCLocFOfTheLocateExtPCOfTheProjPCurOfGInter_Point)
    SearchOfTolerance = _swig_new_instance_method(_Geom2dInt.Geom2dInt_PCLocFOfTheLocateExtPCOfTheProjPCurOfGInter_SearchOfTolerance)
    SetPoint = _swig_new_instance_method(_Geom2dInt.Geom2dInt_PCLocFOfTheLocateExtPCOfTheProjPCurOfGInter_SetPoint)
    SquareDistance = _swig_new_instance_method(_Geom2dInt.Geom2dInt_PCLocFOfTheLocateExtPCOfTheProjPCurOfGInter_SquareDistance)
    SubIntervalInitialize = _swig_new_instance_method(_Geom2dInt.Geom2dInt_PCLocFOfTheLocateExtPCOfTheProjPCurOfGInter_SubIntervalInitialize)

    __repr__ = _dumps_object

    __swig_destroy__ = _Geom2dInt.delete_Geom2dInt_PCLocFOfTheLocateExtPCOfTheProjPCurOfGInter

# Register Geom2dInt_PCLocFOfTheLocateExtPCOfTheProjPCurOfGInter in _Geom2dInt:
_Geom2dInt.Geom2dInt_PCLocFOfTheLocateExtPCOfTheProjPCurOfGInter_swigregister(Geom2dInt_PCLocFOfTheLocateExtPCOfTheProjPCurOfGInter)

class Geom2dInt_TheCurveLocatorOfTheProjPCurOfGInter(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    __repr__ = _dumps_object


    def __init__(self):
        _Geom2dInt.Geom2dInt_TheCurveLocatorOfTheProjPCurOfGInter_swiginit(self, _Geom2dInt.new_Geom2dInt_TheCurveLocatorOfTheProjPCurOfGInter())
    __swig_destroy__ = _Geom2dInt.delete_Geom2dInt_TheCurveLocatorOfTheProjPCurOfGInter

# Register Geom2dInt_TheCurveLocatorOfTheProjPCurOfGInter in _Geom2dInt:
_Geom2dInt.Geom2dInt_TheCurveLocatorOfTheProjPCurOfGInter_swigregister(Geom2dInt_TheCurveLocatorOfTheProjPCurOfGInter)

class Geom2dInt_TheDistBetweenPCurvesOfTheIntPCurvePCurveOfGInter(OCC.Core.math.math_FunctionSetWithDerivatives):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :param curve1:
        	:type curve1: Adaptor2d_Curve2d
        	:param curve2:
        	:type curve2: Adaptor2d_Curve2d
        	:rtype: None
        """
        _Geom2dInt.Geom2dInt_TheDistBetweenPCurvesOfTheIntPCurvePCurveOfGInter_swiginit(self, _Geom2dInt.new_Geom2dInt_TheDistBetweenPCurvesOfTheIntPCurvePCurveOfGInter(*args))

    __repr__ = _dumps_object

    __swig_destroy__ = _Geom2dInt.delete_Geom2dInt_TheDistBetweenPCurvesOfTheIntPCurvePCurveOfGInter

# Register Geom2dInt_TheDistBetweenPCurvesOfTheIntPCurvePCurveOfGInter in _Geom2dInt:
_Geom2dInt.Geom2dInt_TheDistBetweenPCurvesOfTheIntPCurvePCurveOfGInter_swigregister(Geom2dInt_TheDistBetweenPCurvesOfTheIntPCurvePCurveOfGInter)

class Geom2dInt_TheIntConicCurveOfGInter(OCC.Core.IntRes2d.IntRes2d_Intersection):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Empty constructor.
        	:rtype: None* Intersection between a line and a parametric curve.
        	:param L:
        	:type L: gp_Lin2d
        	:param D1:
        	:type D1: IntRes2d_Domain
        	:param PCurve:
        	:type PCurve: Adaptor2d_Curve2d
        	:param D2:
        	:type D2: IntRes2d_Domain
        	:param TolConf:
        	:type TolConf: float
        	:param Tol:
        	:type Tol: float
        	:rtype: None* Intersection between a line and a parametric curve.
        	:param C:
        	:type C: gp_Circ2d
        	:param D1:
        	:type D1: IntRes2d_Domain
        	:param PCurve:
        	:type PCurve: Adaptor2d_Curve2d
        	:param D2:
        	:type D2: IntRes2d_Domain
        	:param TolConf:
        	:type TolConf: float
        	:param Tol:
        	:type Tol: float
        	:rtype: None* Intersection between an ellipse and a parametric curve.
        	:param E:
        	:type E: gp_Elips2d
        	:param D1:
        	:type D1: IntRes2d_Domain
        	:param PCurve:
        	:type PCurve: Adaptor2d_Curve2d
        	:param D2:
        	:type D2: IntRes2d_Domain
        	:param TolConf:
        	:type TolConf: float
        	:param Tol:
        	:type Tol: float
        	:rtype: None* Intersection between a parabola and a parametric curve.
        	:param Prb:
        	:type Prb: gp_Parab2d
        	:param D1:
        	:type D1: IntRes2d_Domain
        	:param PCurve:
        	:type PCurve: Adaptor2d_Curve2d
        	:param D2:
        	:type D2: IntRes2d_Domain
        	:param TolConf:
        	:type TolConf: float
        	:param Tol:
        	:type Tol: float
        	:rtype: None* Intersection between the main branch of an hyperbola and a parametric curve.
        	:param H:
        	:type H: gp_Hypr2d
        	:param D1:
        	:type D1: IntRes2d_Domain
        	:param PCurve:
        	:type PCurve: Adaptor2d_Curve2d
        	:param D2:
        	:type D2: IntRes2d_Domain
        	:param TolConf:
        	:type TolConf: float
        	:param Tol:
        	:type Tol: float
        	:rtype: None
        """
        _Geom2dInt.Geom2dInt_TheIntConicCurveOfGInter_swiginit(self, _Geom2dInt.new_Geom2dInt_TheIntConicCurveOfGInter(*args))
    Perform = _swig_new_instance_method(_Geom2dInt.Geom2dInt_TheIntConicCurveOfGInter_Perform)

    __repr__ = _dumps_object

    __swig_destroy__ = _Geom2dInt.delete_Geom2dInt_TheIntConicCurveOfGInter

# Register Geom2dInt_TheIntConicCurveOfGInter in _Geom2dInt:
_Geom2dInt.Geom2dInt_TheIntConicCurveOfGInter_swigregister(Geom2dInt_TheIntConicCurveOfGInter)

class Geom2dInt_TheIntPCurvePCurveOfGInter(OCC.Core.IntRes2d.IntRes2d_Intersection):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r""":rtype: None"""
        _Geom2dInt.Geom2dInt_TheIntPCurvePCurveOfGInter_swiginit(self, _Geom2dInt.new_Geom2dInt_TheIntPCurvePCurveOfGInter(*args))
    GetMinNbSamples = _swig_new_instance_method(_Geom2dInt.Geom2dInt_TheIntPCurvePCurveOfGInter_GetMinNbSamples)
    Perform = _swig_new_instance_method(_Geom2dInt.Geom2dInt_TheIntPCurvePCurveOfGInter_Perform)
    SetMinNbSamples = _swig_new_instance_method(_Geom2dInt.Geom2dInt_TheIntPCurvePCurveOfGInter_SetMinNbSamples)

    __repr__ = _dumps_object

    __swig_destroy__ = _Geom2dInt.delete_Geom2dInt_TheIntPCurvePCurveOfGInter

# Register Geom2dInt_TheIntPCurvePCurveOfGInter in _Geom2dInt:
_Geom2dInt.Geom2dInt_TheIntPCurvePCurveOfGInter_swigregister(Geom2dInt_TheIntPCurvePCurveOfGInter)

class Geom2dInt_TheIntersectorOfTheIntConicCurveOfGInter(OCC.Core.IntRes2d.IntRes2d_Intersection):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    And_Domaine_Objet1_Intersections = _swig_new_instance_method(_Geom2dInt.Geom2dInt_TheIntersectorOfTheIntConicCurveOfGInter_And_Domaine_Objet1_Intersections)
    FindU = _swig_new_instance_method(_Geom2dInt.Geom2dInt_TheIntersectorOfTheIntConicCurveOfGInter_FindU)
    FindV = _swig_new_instance_method(_Geom2dInt.Geom2dInt_TheIntersectorOfTheIntConicCurveOfGInter_FindV)

    def __init__(self, *args):
        r"""
        * Empty constructor.
        	:rtype: None* Intersection between an implicit curve and a parametrised curve. The exception ConstructionError is raised if the domain of the parametrised curve does not verify HasFirstPoint and HasLastPoint return True.
        	:param ITool:
        	:type ITool: IntCurve_IConicTool
        	:param Dom1:
        	:type Dom1: IntRes2d_Domain
        	:param PCurve:
        	:type PCurve: Adaptor2d_Curve2d
        	:param Dom2:
        	:type Dom2: IntRes2d_Domain
        	:param TolConf:
        	:type TolConf: float
        	:param Tol:
        	:type Tol: float
        	:rtype: None
        """
        _Geom2dInt.Geom2dInt_TheIntersectorOfTheIntConicCurveOfGInter_swiginit(self, _Geom2dInt.new_Geom2dInt_TheIntersectorOfTheIntConicCurveOfGInter(*args))
    Perform = _swig_new_instance_method(_Geom2dInt.Geom2dInt_TheIntersectorOfTheIntConicCurveOfGInter_Perform)

    __repr__ = _dumps_object

    __swig_destroy__ = _Geom2dInt.delete_Geom2dInt_TheIntersectorOfTheIntConicCurveOfGInter

# Register Geom2dInt_TheIntersectorOfTheIntConicCurveOfGInter in _Geom2dInt:
_Geom2dInt.Geom2dInt_TheIntersectorOfTheIntConicCurveOfGInter_swigregister(Geom2dInt_TheIntersectorOfTheIntConicCurveOfGInter)

class Geom2dInt_TheLocateExtPCOfTheProjPCurOfGInter(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :rtype: None* Calculates the distance with a close point. The close point is defined by the parameter value U0. The function F(u)=distance(P,C(u)) has an extremum when g(u)=dF/du=0. The algorithm searchs a zero near the close point. TolU is used to decide to stop the iterations. At the nth iteration, the criteria is: abs(Un - Un-1) < TolU.
        	:param P:
        	:type P: gp_Pnt2d
        	:param C:
        	:type C: Adaptor2d_Curve2d
        	:param U0:
        	:type U0: float
        	:param TolU:
        	:type TolU: float
        	:rtype: None* Calculates the distance with a close point. The close point is defined by the parameter value U0. The function F(u)=distance(P,C(u)) has an extremum when g(u)=dF/du=0. The algorithm searchs a zero near the close point. Zeros are searched between Umin et Usup. TolU is used to decide to stop the iterations. At the nth iteration, the criteria is: abs(Un - Un-1) < TolU.
        	:param P:
        	:type P: gp_Pnt2d
        	:param C:
        	:type C: Adaptor2d_Curve2d
        	:param U0:
        	:type U0: float
        	:param Umin:
        	:type Umin: float
        	:param Usup:
        	:type Usup: float
        	:param TolU:
        	:type TolU: float
        	:rtype: None
        """
        _Geom2dInt.Geom2dInt_TheLocateExtPCOfTheProjPCurOfGInter_swiginit(self, _Geom2dInt.new_Geom2dInt_TheLocateExtPCOfTheProjPCurOfGInter(*args))
    Initialize = _swig_new_instance_method(_Geom2dInt.Geom2dInt_TheLocateExtPCOfTheProjPCurOfGInter_Initialize)
    IsDone = _swig_new_instance_method(_Geom2dInt.Geom2dInt_TheLocateExtPCOfTheProjPCurOfGInter_IsDone)
    IsMin = _swig_new_instance_method(_Geom2dInt.Geom2dInt_TheLocateExtPCOfTheProjPCurOfGInter_IsMin)
    Perform = _swig_new_instance_method(_Geom2dInt.Geom2dInt_TheLocateExtPCOfTheProjPCurOfGInter_Perform)
    Point = _swig_new_instance_method(_Geom2dInt.Geom2dInt_TheLocateExtPCOfTheProjPCurOfGInter_Point)
    SquareDistance = _swig_new_instance_method(_Geom2dInt.Geom2dInt_TheLocateExtPCOfTheProjPCurOfGInter_SquareDistance)

    __repr__ = _dumps_object

    __swig_destroy__ = _Geom2dInt.delete_Geom2dInt_TheLocateExtPCOfTheProjPCurOfGInter

# Register Geom2dInt_TheLocateExtPCOfTheProjPCurOfGInter in _Geom2dInt:
_Geom2dInt.Geom2dInt_TheLocateExtPCOfTheProjPCurOfGInter_swigregister(Geom2dInt_TheLocateExtPCOfTheProjPCurOfGInter)

class Geom2dInt_ThePolygon2dOfTheIntPCurvePCurveOfGInter(OCC.Core.Intf.Intf_Polygon2d):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    ApproxParamOnCurve = _swig_new_instance_method(_Geom2dInt.Geom2dInt_ThePolygon2dOfTheIntPCurvePCurveOfGInter_ApproxParamOnCurve)
    AutoIntersectionIsPossible = _swig_new_instance_method(_Geom2dInt.Geom2dInt_ThePolygon2dOfTheIntPCurvePCurveOfGInter_AutoIntersectionIsPossible)
    CalculRegion = _swig_new_instance_method(_Geom2dInt.Geom2dInt_ThePolygon2dOfTheIntPCurvePCurveOfGInter_CalculRegion)
    Closed = _swig_new_instance_method(_Geom2dInt.Geom2dInt_ThePolygon2dOfTheIntPCurvePCurveOfGInter_Closed)
    ComputeWithBox = _swig_new_instance_method(_Geom2dInt.Geom2dInt_ThePolygon2dOfTheIntPCurvePCurveOfGInter_ComputeWithBox)
    Dump = _swig_new_instance_method(_Geom2dInt.Geom2dInt_ThePolygon2dOfTheIntPCurvePCurveOfGInter_Dump)

    def __init__(self, *args):
        r"""
        * Compute a polygon on the domain of the curve.
        	:param Curve:
        	:type Curve: Adaptor2d_Curve2d
        	:param NbPnt:
        	:type NbPnt: int
        	:param Domain:
        	:type Domain: IntRes2d_Domain
        	:param Tol:
        	:type Tol: float
        	:rtype: None
        """
        _Geom2dInt.Geom2dInt_ThePolygon2dOfTheIntPCurvePCurveOfGInter_swiginit(self, _Geom2dInt.new_Geom2dInt_ThePolygon2dOfTheIntPCurvePCurveOfGInter(*args))
    InfParameter = _swig_new_instance_method(_Geom2dInt.Geom2dInt_ThePolygon2dOfTheIntPCurvePCurveOfGInter_InfParameter)
    SetDeflectionOverEstimation = _swig_new_instance_method(_Geom2dInt.Geom2dInt_ThePolygon2dOfTheIntPCurvePCurveOfGInter_SetDeflectionOverEstimation)
    SupParameter = _swig_new_instance_method(_Geom2dInt.Geom2dInt_ThePolygon2dOfTheIntPCurvePCurveOfGInter_SupParameter)

    __repr__ = _dumps_object

    __swig_destroy__ = _Geom2dInt.delete_Geom2dInt_ThePolygon2dOfTheIntPCurvePCurveOfGInter

# Register Geom2dInt_ThePolygon2dOfTheIntPCurvePCurveOfGInter in _Geom2dInt:
_Geom2dInt.Geom2dInt_ThePolygon2dOfTheIntPCurvePCurveOfGInter_swigregister(Geom2dInt_ThePolygon2dOfTheIntPCurvePCurveOfGInter)

class Geom2dInt_TheProjPCurOfGInter(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    FindParameter = _swig_new_static_method(_Geom2dInt.Geom2dInt_TheProjPCurOfGInter_FindParameter)

    __repr__ = _dumps_object


    def __init__(self):
        _Geom2dInt.Geom2dInt_TheProjPCurOfGInter_swiginit(self, _Geom2dInt.new_Geom2dInt_TheProjPCurOfGInter())
    __swig_destroy__ = _Geom2dInt.delete_Geom2dInt_TheProjPCurOfGInter

# Register Geom2dInt_TheProjPCurOfGInter in _Geom2dInt:
_Geom2dInt.Geom2dInt_TheProjPCurOfGInter_swigregister(Geom2dInt_TheProjPCurOfGInter)
Geom2dInt_TheProjPCurOfGInter_FindParameter = _Geom2dInt.Geom2dInt_TheProjPCurOfGInter_FindParameter



