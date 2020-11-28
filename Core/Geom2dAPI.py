# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
Geom2dAPI module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_geom2dapi.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _Geom2dAPI
else:
    import _Geom2dAPI

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _Geom2dAPI.SWIG_PyInstanceMethod_New
_swig_new_static_method = _Geom2dAPI.SWIG_PyStaticMethod_New

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
    __swig_destroy__ = _Geom2dAPI.delete_SwigPyIterator
    value = _swig_new_instance_method(_Geom2dAPI.SwigPyIterator_value)
    incr = _swig_new_instance_method(_Geom2dAPI.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_Geom2dAPI.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_Geom2dAPI.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_Geom2dAPI.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_Geom2dAPI.SwigPyIterator_copy)
    next = _swig_new_instance_method(_Geom2dAPI.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_Geom2dAPI.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_Geom2dAPI.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_Geom2dAPI.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_Geom2dAPI.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_Geom2dAPI.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_Geom2dAPI.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_Geom2dAPI.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_Geom2dAPI.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_Geom2dAPI.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _Geom2dAPI:
_Geom2dAPI.SwigPyIterator_swigregister(SwigPyIterator)


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
import OCC.Core.Extrema
import OCC.Core.math
import OCC.Core.TColStd
import OCC.Core.TCollection
import OCC.Core.Message
import OCC.Core.gp
import OCC.Core.Adaptor3d
import OCC.Core.Geom
import OCC.Core.GeomAbs
import OCC.Core.TColgp
import OCC.Core.TopAbs
import OCC.Core.Adaptor2d
import OCC.Core.Geom2d
import OCC.Core.GeomAdaptor
import OCC.Core.Geom2dInt
import OCC.Core.IntRes2d
import OCC.Core.IntCurve
import OCC.Core.Intf
import OCC.Core.Bnd
import OCC.Core.BVH
import OCC.Core.Approx
import OCC.Core.AppCont
import OCC.Core.AppParCurves
class Geom2dAPI_ExtremaCurveCurve(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Distance = _swig_new_instance_method(_Geom2dAPI.Geom2dAPI_ExtremaCurveCurve_Distance)
    Extrema = _swig_new_instance_method(_Geom2dAPI.Geom2dAPI_ExtremaCurveCurve_Extrema)

    def __init__(self, *args):
        r"""
        * Computes the extrema between - the portion of the curve C1 limited by the two points of parameter (U1min,U1max), and - the portion of the curve C2 limited by the two points of parameter (U2min,U2max). Warning Use the function NbExtrema to obtain the number of solutions. If this algorithm fails, NbExtrema returns 0.
        	:param C1:
        	:type C1: Geom2d_Curve
        	:param C2:
        	:type C2: Geom2d_Curve
        	:param U1min:
        	:type U1min: float
        	:param U1max:
        	:type U1max: float
        	:param U2min:
        	:type U2min: float
        	:param U2max:
        	:type U2max: float
        	:rtype: None
        """
        _Geom2dAPI.Geom2dAPI_ExtremaCurveCurve_swiginit(self, _Geom2dAPI.new_Geom2dAPI_ExtremaCurveCurve(*args))
    LowerDistance = _swig_new_instance_method(_Geom2dAPI.Geom2dAPI_ExtremaCurveCurve_LowerDistance)
    LowerDistanceParameters = _swig_new_instance_method(_Geom2dAPI.Geom2dAPI_ExtremaCurveCurve_LowerDistanceParameters)
    NbExtrema = _swig_new_instance_method(_Geom2dAPI.Geom2dAPI_ExtremaCurveCurve_NbExtrema)
    NearestPoints = _swig_new_instance_method(_Geom2dAPI.Geom2dAPI_ExtremaCurveCurve_NearestPoints)
    Parameters = _swig_new_instance_method(_Geom2dAPI.Geom2dAPI_ExtremaCurveCurve_Parameters)
    Points = _swig_new_instance_method(_Geom2dAPI.Geom2dAPI_ExtremaCurveCurve_Points)

    __repr__ = _dumps_object

    __swig_destroy__ = _Geom2dAPI.delete_Geom2dAPI_ExtremaCurveCurve

# Register Geom2dAPI_ExtremaCurveCurve in _Geom2dAPI:
_Geom2dAPI.Geom2dAPI_ExtremaCurveCurve_swigregister(Geom2dAPI_ExtremaCurveCurve)

class Geom2dAPI_InterCurveCurve(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Create an empty intersector. Use the function Init for further initialization of the intersection algorithm by curves or curve.
        	:rtype: None* Creates an object and computes the intersections between the curves C1 and C2.
        	:param C1:
        	:type C1: Geom2d_Curve
        	:param C2:
        	:type C2: Geom2d_Curve
        	:param Tol: default value is 1.0e-6
        	:type Tol: float
        	:rtype: None* Creates an object and computes self-intersections of the curve C1. Tolerance value Tol, defaulted to 1.0e-6, defines the precision of computing the intersection points. In case of a tangential intersection, Tol also defines the size of intersection segments (limited portions of the curves) where the distance between all points from two curves (or a curve in case of self-intersection) is less than Tol. Warning Use functions NbPoints and NbSegments to obtain the number of solutions. If the algorithm finds no intersections NbPoints and NbSegments return 0.
        	:param C1:
        	:type C1: Geom2d_Curve
        	:param Tol: default value is 1.0e-6
        	:type Tol: float
        	:rtype: None
        """
        _Geom2dAPI.Geom2dAPI_InterCurveCurve_swiginit(self, _Geom2dAPI.new_Geom2dAPI_InterCurveCurve(*args))
    Init = _swig_new_instance_method(_Geom2dAPI.Geom2dAPI_InterCurveCurve_Init)
    Intersector = _swig_new_instance_method(_Geom2dAPI.Geom2dAPI_InterCurveCurve_Intersector)
    NbPoints = _swig_new_instance_method(_Geom2dAPI.Geom2dAPI_InterCurveCurve_NbPoints)
    NbSegments = _swig_new_instance_method(_Geom2dAPI.Geom2dAPI_InterCurveCurve_NbSegments)
    Point = _swig_new_instance_method(_Geom2dAPI.Geom2dAPI_InterCurveCurve_Point)
    Segment = _swig_new_instance_method(_Geom2dAPI.Geom2dAPI_InterCurveCurve_Segment)

    __repr__ = _dumps_object

    __swig_destroy__ = _Geom2dAPI.delete_Geom2dAPI_InterCurveCurve

# Register Geom2dAPI_InterCurveCurve in _Geom2dAPI:
_Geom2dAPI.Geom2dAPI_InterCurveCurve_swigregister(Geom2dAPI_InterCurveCurve)

class Geom2dAPI_Interpolate(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Curve = _swig_new_instance_method(_Geom2dAPI.Geom2dAPI_Interpolate_Curve)

    def __init__(self, *args):
        r"""
        * Tolerance is to check if the points are not too close to one an other It is also used to check if the tangent vector is not too small. There should be at least 2 points if PeriodicFlag is True then the curve will be periodic.
        	:param Points:
        	:type Points: TColgp_HArray1OfPnt2d
        	:param PeriodicFlag:
        	:type PeriodicFlag: bool
        	:param Tolerance:
        	:type Tolerance: float
        	:rtype: None* if PeriodicFlag is True then the curve will be periodic Warning: There should be as many parameters as there are points except if PeriodicFlag is True : then there should be one more parameter to close the curve
        	:param Points:
        	:type Points: TColgp_HArray1OfPnt2d
        	:param Parameters:
        	:type Parameters: TColStd_HArray1OfReal
        	:param PeriodicFlag:
        	:type PeriodicFlag: bool
        	:param Tolerance:
        	:type Tolerance: float
        	:rtype: None
        """
        _Geom2dAPI.Geom2dAPI_Interpolate_swiginit(self, _Geom2dAPI.new_Geom2dAPI_Interpolate(*args))
    IsDone = _swig_new_instance_method(_Geom2dAPI.Geom2dAPI_Interpolate_IsDone)
    Load = _swig_new_instance_method(_Geom2dAPI.Geom2dAPI_Interpolate_Load)
    Perform = _swig_new_instance_method(_Geom2dAPI.Geom2dAPI_Interpolate_Perform)

    __repr__ = _dumps_object

    __swig_destroy__ = _Geom2dAPI.delete_Geom2dAPI_Interpolate

# Register Geom2dAPI_Interpolate in _Geom2dAPI:
_Geom2dAPI.Geom2dAPI_Interpolate_swigregister(Geom2dAPI_Interpolate)

class Geom2dAPI_PointsToBSpline(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Curve = _swig_new_instance_method(_Geom2dAPI.Geom2dAPI_PointsToBSpline_Curve)

    def __init__(self, *args):
        r"""
        * Constructs an empty approximation algorithm. Use an Init function to define and build the BSpline curve.
        	:rtype: None* Approximate a BSpline Curve passing through an array of Point. The resulting BSpline will have the following properties: 1- his degree will be in the range [Degmin,Degmax] 2- his continuity will be at least <Continuity> 3- the distance from the point <Points> to the BSpline will be lower to Tol2D
        	:param Points:
        	:type Points: TColgp_Array1OfPnt2d
        	:param DegMin: default value is 3
        	:type DegMin: int
        	:param DegMax: default value is 8
        	:type DegMax: int
        	:param Continuity: default value is GeomAbs_C2
        	:type Continuity: GeomAbs_Shape
        	:param Tol2D: default value is 1.0e-6
        	:type Tol2D: float
        	:rtype: None* Approximate a BSpline Curve passing through an array of Point. Of coordinates : //! X = X0 + DX * (i-YValues.Lower()) Y = YValues(i) //! With i in the range YValues.Lower(), YValues.Upper() //! The BSpline will be parametrized from t = X0 to X0 + DX * (YValues.Upper() - YValues.Lower()) //! And will satisfy X(t) = t //! The resulting BSpline will have the following properties: 1- his degree will be in the range [Degmin,Degmax] 2- his continuity will be at least <Continuity> 3- the distance from the point <Points> to the BSpline will be lower to Tol2D
        	:param YValues:
        	:type YValues: TColStd_Array1OfReal
        	:param X0:
        	:type X0: float
        	:param DX:
        	:type DX: float
        	:param DegMin: default value is 3
        	:type DegMin: int
        	:param DegMax: default value is 8
        	:type DegMax: int
        	:param Continuity: default value is GeomAbs_C2
        	:type Continuity: GeomAbs_Shape
        	:param Tol2D: default value is 1.0e-6
        	:type Tol2D: float
        	:rtype: None* Approximate a BSpline Curve passing through an array of Point. The resulting BSpline will have the following properties: 1- his degree will be in the range [Degmin,Degmax] 2- his continuity will be at least <Continuity> 3- the distance from the point <Points> to the BSpline will be lower to Tol2D
        	:param Points:
        	:type Points: TColgp_Array1OfPnt2d
        	:param ParType:
        	:type ParType: Approx_ParametrizationType
        	:param DegMin: default value is 3
        	:type DegMin: int
        	:param DegMax: default value is 8
        	:type DegMax: int
        	:param Continuity: default value is GeomAbs_C2
        	:type Continuity: GeomAbs_Shape
        	:param Tol2D: default value is 1.0e-3
        	:type Tol2D: float
        	:rtype: None* Approximate a BSpline Curve passing through an array of Point, which parameters are given by the array <Parameters>. The resulting BSpline will have the following properties: 1- his degree will be in the range [Degmin,Degmax] 2- his continuity will be at least <Continuity> 3- the distance from the point <Points> to the BSpline will be lower to Tol2D
        	:param Points:
        	:type Points: TColgp_Array1OfPnt2d
        	:param Parameters:
        	:type Parameters: TColStd_Array1OfReal
        	:param DegMin: default value is 3
        	:type DegMin: int
        	:param DegMax: default value is 8
        	:type DegMax: int
        	:param Continuity: default value is GeomAbs_C2
        	:type Continuity: GeomAbs_Shape
        	:param Tol2D: default value is 1.0e-3
        	:type Tol2D: float
        	:rtype: None* Approximate a BSpline Curve passing through an array of Point using variational smoothing algorithm, which tries to minimize additional criterium: Weight1*CurveLength + Weight2*Curvature + Weight3*Torsion
        	:param Points:
        	:type Points: TColgp_Array1OfPnt2d
        	:param Weight1:
        	:type Weight1: float
        	:param Weight2:
        	:type Weight2: float
        	:param Weight3:
        	:type Weight3: float
        	:param DegMax: default value is 8
        	:type DegMax: int
        	:param Continuity: default value is GeomAbs_C2
        	:type Continuity: GeomAbs_Shape
        	:param Tol3D: default value is 1.0e-3
        	:type Tol3D: float
        	:rtype: None
        """
        _Geom2dAPI.Geom2dAPI_PointsToBSpline_swiginit(self, _Geom2dAPI.new_Geom2dAPI_PointsToBSpline(*args))
    Init = _swig_new_instance_method(_Geom2dAPI.Geom2dAPI_PointsToBSpline_Init)
    IsDone = _swig_new_instance_method(_Geom2dAPI.Geom2dAPI_PointsToBSpline_IsDone)

    __repr__ = _dumps_object

    __swig_destroy__ = _Geom2dAPI.delete_Geom2dAPI_PointsToBSpline

# Register Geom2dAPI_PointsToBSpline in _Geom2dAPI:
_Geom2dAPI.Geom2dAPI_PointsToBSpline_swigregister(Geom2dAPI_PointsToBSpline)

class Geom2dAPI_ProjectPointOnCurve(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Distance = _swig_new_instance_method(_Geom2dAPI.Geom2dAPI_ProjectPointOnCurve_Distance)
    Extrema = _swig_new_instance_method(_Geom2dAPI.Geom2dAPI_ProjectPointOnCurve_Extrema)

    def __init__(self, *args):
        r"""
        * Constructs an empty projector algorithm. Use an Init function to define the point and the curve on which it is going to work.
        	:rtype: None* Create the projection of a point <P> on a curve <Curve>
        	:param P:
        	:type P: gp_Pnt2d
        	:param Curve:
        	:type Curve: Geom2d_Curve
        	:rtype: None* Create the projection of a point <P> on a curve <Curve> limited by the two points of parameter Umin and Usup. Warning Use the function NbPoints to obtain the number of solutions. If projection fails, NbPoints returns 0.
        	:param P:
        	:type P: gp_Pnt2d
        	:param Curve:
        	:type Curve: Geom2d_Curve
        	:param Umin:
        	:type Umin: float
        	:param Usup:
        	:type Usup: float
        	:rtype: None
        """
        _Geom2dAPI.Geom2dAPI_ProjectPointOnCurve_swiginit(self, _Geom2dAPI.new_Geom2dAPI_ProjectPointOnCurve(*args))
    Init = _swig_new_instance_method(_Geom2dAPI.Geom2dAPI_ProjectPointOnCurve_Init)
    LowerDistance = _swig_new_instance_method(_Geom2dAPI.Geom2dAPI_ProjectPointOnCurve_LowerDistance)
    LowerDistanceParameter = _swig_new_instance_method(_Geom2dAPI.Geom2dAPI_ProjectPointOnCurve_LowerDistanceParameter)
    NbPoints = _swig_new_instance_method(_Geom2dAPI.Geom2dAPI_ProjectPointOnCurve_NbPoints)
    NearestPoint = _swig_new_instance_method(_Geom2dAPI.Geom2dAPI_ProjectPointOnCurve_NearestPoint)
    Parameter = _swig_new_instance_method(_Geom2dAPI.Geom2dAPI_ProjectPointOnCurve_Parameter)
    Point = _swig_new_instance_method(_Geom2dAPI.Geom2dAPI_ProjectPointOnCurve_Point)

    __repr__ = _dumps_object

    __swig_destroy__ = _Geom2dAPI.delete_Geom2dAPI_ProjectPointOnCurve

# Register Geom2dAPI_ProjectPointOnCurve in _Geom2dAPI:
_Geom2dAPI.Geom2dAPI_ProjectPointOnCurve_swigregister(Geom2dAPI_ProjectPointOnCurve)



