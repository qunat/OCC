# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
GeomConvert module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_geomconvert.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _GeomConvert
else:
    import _GeomConvert

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _GeomConvert.SWIG_PyInstanceMethod_New
_swig_new_static_method = _GeomConvert.SWIG_PyStaticMethod_New

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
    __swig_destroy__ = _GeomConvert.delete_SwigPyIterator
    value = _swig_new_instance_method(_GeomConvert.SwigPyIterator_value)
    incr = _swig_new_instance_method(_GeomConvert.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_GeomConvert.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_GeomConvert.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_GeomConvert.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_GeomConvert.SwigPyIterator_copy)
    next = _swig_new_instance_method(_GeomConvert.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_GeomConvert.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_GeomConvert.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_GeomConvert.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_GeomConvert.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_GeomConvert.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_GeomConvert.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_GeomConvert.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_GeomConvert.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_GeomConvert.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _GeomConvert:
_GeomConvert.SwigPyIterator_swigregister(SwigPyIterator)


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
import OCC.Core.Geom
import OCC.Core.gp
import OCC.Core.GeomAbs
import OCC.Core.TColgp
import OCC.Core.TColStd
import OCC.Core.TCollection
import OCC.Core.TColGeom
import OCC.Core.Convert
import OCC.Core.Adaptor3d
import OCC.Core.TopAbs
import OCC.Core.Adaptor2d
import OCC.Core.Geom2d
import OCC.Core.math
import OCC.Core.Message
class geomconvert(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    C0BSplineToArrayOfC1BSplineCurve = _swig_new_static_method(_GeomConvert.geomconvert_C0BSplineToArrayOfC1BSplineCurve)
    C0BSplineToC1BSplineCurve = _swig_new_static_method(_GeomConvert.geomconvert_C0BSplineToC1BSplineCurve)
    ConcatC1 = _swig_new_static_method(_GeomConvert.geomconvert_ConcatC1)
    ConcatG1 = _swig_new_static_method(_GeomConvert.geomconvert_ConcatG1)
    CurveToBSplineCurve = _swig_new_static_method(_GeomConvert.geomconvert_CurveToBSplineCurve)
    SplitBSplineCurve = _swig_new_static_method(_GeomConvert.geomconvert_SplitBSplineCurve)
    SplitBSplineSurface = _swig_new_static_method(_GeomConvert.geomconvert_SplitBSplineSurface)
    SurfaceToBSplineSurface = _swig_new_static_method(_GeomConvert.geomconvert_SurfaceToBSplineSurface)

    __repr__ = _dumps_object


    def __init__(self):
        _GeomConvert.geomconvert_swiginit(self, _GeomConvert.new_geomconvert())
    __swig_destroy__ = _GeomConvert.delete_geomconvert

# Register geomconvert in _GeomConvert:
_GeomConvert.geomconvert_swigregister(geomconvert)
geomconvert_C0BSplineToArrayOfC1BSplineCurve = _GeomConvert.geomconvert_C0BSplineToArrayOfC1BSplineCurve
geomconvert_C0BSplineToC1BSplineCurve = _GeomConvert.geomconvert_C0BSplineToC1BSplineCurve
geomconvert_ConcatC1 = _GeomConvert.geomconvert_ConcatC1
geomconvert_ConcatG1 = _GeomConvert.geomconvert_ConcatG1
geomconvert_CurveToBSplineCurve = _GeomConvert.geomconvert_CurveToBSplineCurve
geomconvert_SplitBSplineCurve = _GeomConvert.geomconvert_SplitBSplineCurve
geomconvert_SplitBSplineSurface = _GeomConvert.geomconvert_SplitBSplineSurface
geomconvert_SurfaceToBSplineSurface = _GeomConvert.geomconvert_SurfaceToBSplineSurface

class GeomConvert_ApproxCurve(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Curve = _swig_new_instance_method(_GeomConvert.GeomConvert_ApproxCurve_Curve)
    DumpToString = _swig_new_instance_method(_GeomConvert.GeomConvert_ApproxCurve_DumpToString)

    def __init__(self, *args):
        r"""
        * Constructs a curve approximation framework defined by - - the conic Curve, - the tolerance value Tol3d, - the degree of continuity Order, - the maximum number of segments MaxSegments allowed in the resulting BSpline curve, and - the highest degree MaxDeg which the polynomial defining the BSpline curve may have.
        	:param Curve:
        	:type Curve: Geom_Curve
        	:param Tol3d:
        	:type Tol3d: float
        	:param Order:
        	:type Order: GeomAbs_Shape
        	:param MaxSegments:
        	:type MaxSegments: int
        	:param MaxDegree:
        	:type MaxDegree: int
        	:rtype: None* Constructs a curve approximation framework defined by - - the Curve, - the tolerance value Tol3d, - the degree of continuity Order, - the maximum number of segments MaxSegments allowed in the resulting BSpline curve, and - the highest degree MaxDeg which the polynomial defining the BSpline curve may have.
        	:param Curve:
        	:type Curve: Adaptor3d_HCurve
        	:param Tol3d:
        	:type Tol3d: float
        	:param Order:
        	:type Order: GeomAbs_Shape
        	:param MaxSegments:
        	:type MaxSegments: int
        	:param MaxDegree:
        	:type MaxDegree: int
        	:rtype: None
        """
        _GeomConvert.GeomConvert_ApproxCurve_swiginit(self, _GeomConvert.new_GeomConvert_ApproxCurve(*args))
    HasResult = _swig_new_instance_method(_GeomConvert.GeomConvert_ApproxCurve_HasResult)
    IsDone = _swig_new_instance_method(_GeomConvert.GeomConvert_ApproxCurve_IsDone)
    MaxError = _swig_new_instance_method(_GeomConvert.GeomConvert_ApproxCurve_MaxError)

    __repr__ = _dumps_object

    __swig_destroy__ = _GeomConvert.delete_GeomConvert_ApproxCurve

# Register GeomConvert_ApproxCurve in _GeomConvert:
_GeomConvert.GeomConvert_ApproxCurve_swigregister(GeomConvert_ApproxCurve)

class GeomConvert_ApproxSurface(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    DumpToString = _swig_new_instance_method(_GeomConvert.GeomConvert_ApproxSurface_DumpToString)

    def __init__(self, *args):
        r"""
        * Constructs a surface approximation framework defined by - the conic Surf - the tolerance value Tol3d - the degree of continuity UContinuity, VContinuity in the directions of the U and V parameters - the highest degree MaxDegU, MaxDegV which the polynomial defining the BSpline curve may have in the directions of the U and V parameters - the maximum number of segments MaxSegments allowed in the resulting BSpline curve - the index of precision PrecisCode.
        	:param Surf:
        	:type Surf: Geom_Surface
        	:param Tol3d:
        	:type Tol3d: float
        	:param UContinuity:
        	:type UContinuity: GeomAbs_Shape
        	:param VContinuity:
        	:type VContinuity: GeomAbs_Shape
        	:param MaxDegU:
        	:type MaxDegU: int
        	:param MaxDegV:
        	:type MaxDegV: int
        	:param MaxSegments:
        	:type MaxSegments: int
        	:param PrecisCode:
        	:type PrecisCode: int
        	:rtype: None* Constructs a surface approximation framework defined by - the Surf - the tolerance value Tol3d - the degree of continuity UContinuity, VContinuity in the directions of the U and V parameters - the highest degree MaxDegU, MaxDegV which the polynomial defining the BSpline curve may have in the directions of the U and V parameters - the maximum number of segments MaxSegments allowed in the resulting BSpline curve - the index of precision PrecisCode.
        	:param Surf:
        	:type Surf: Adaptor3d_HSurface
        	:param Tol3d:
        	:type Tol3d: float
        	:param UContinuity:
        	:type UContinuity: GeomAbs_Shape
        	:param VContinuity:
        	:type VContinuity: GeomAbs_Shape
        	:param MaxDegU:
        	:type MaxDegU: int
        	:param MaxDegV:
        	:type MaxDegV: int
        	:param MaxSegments:
        	:type MaxSegments: int
        	:param PrecisCode:
        	:type PrecisCode: int
        	:rtype: None
        """
        _GeomConvert.GeomConvert_ApproxSurface_swiginit(self, _GeomConvert.new_GeomConvert_ApproxSurface(*args))
    HasResult = _swig_new_instance_method(_GeomConvert.GeomConvert_ApproxSurface_HasResult)
    IsDone = _swig_new_instance_method(_GeomConvert.GeomConvert_ApproxSurface_IsDone)
    MaxError = _swig_new_instance_method(_GeomConvert.GeomConvert_ApproxSurface_MaxError)
    Surface = _swig_new_instance_method(_GeomConvert.GeomConvert_ApproxSurface_Surface)

    __repr__ = _dumps_object

    __swig_destroy__ = _GeomConvert.delete_GeomConvert_ApproxSurface

# Register GeomConvert_ApproxSurface in _GeomConvert:
_GeomConvert.GeomConvert_ApproxSurface_swigregister(GeomConvert_ApproxSurface)

class GeomConvert_BSplineCurveKnotSplitting(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Determines points at which the BSpline curve BasisCurve should be split in order to obtain arcs with a degree of continuity equal to ContinuityRange. These points are knot values of BasisCurve. They are identified by indices in the knots table of BasisCurve. Use the available interrogation functions to access computed values, followed by the global function SplitBSplineCurve (provided by the package GeomConvert) to split the curve. Exceptions Standard_RangeError if ContinuityRange is less than zero.
        	:param BasisCurve:
        	:type BasisCurve: Geom_BSplineCurve
        	:param ContinuityRange:
        	:type ContinuityRange: int
        	:rtype: None
        """
        _GeomConvert.GeomConvert_BSplineCurveKnotSplitting_swiginit(self, _GeomConvert.new_GeomConvert_BSplineCurveKnotSplitting(*args))
    NbSplits = _swig_new_instance_method(_GeomConvert.GeomConvert_BSplineCurveKnotSplitting_NbSplits)
    SplitValue = _swig_new_instance_method(_GeomConvert.GeomConvert_BSplineCurveKnotSplitting_SplitValue)
    Splitting = _swig_new_instance_method(_GeomConvert.GeomConvert_BSplineCurveKnotSplitting_Splitting)

    __repr__ = _dumps_object

    __swig_destroy__ = _GeomConvert.delete_GeomConvert_BSplineCurveKnotSplitting

# Register GeomConvert_BSplineCurveKnotSplitting in _GeomConvert:
_GeomConvert.GeomConvert_BSplineCurveKnotSplitting_swigregister(GeomConvert_BSplineCurveKnotSplitting)

class GeomConvert_BSplineCurveToBezierCurve(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Arc = _swig_new_instance_method(_GeomConvert.GeomConvert_BSplineCurveToBezierCurve_Arc)
    Arcs = _swig_new_instance_method(_GeomConvert.GeomConvert_BSplineCurveToBezierCurve_Arcs)

    def __init__(self, *args):
        r"""
        * Computes all the data needed to convert the BSpline curve BasisCurve into a series of adjacent Bezier arcs.
        	:param BasisCurve:
        	:type BasisCurve: Geom_BSplineCurve
        	:rtype: None* Computes all the data needed to convert the portion of the BSpline curve BasisCurve limited by the two parameter values U1 and U2 into a series of adjacent Bezier arcs. The result consists of a series of BasisCurve arcs limited by points corresponding to knot values of the curve. Use the available interrogation functions to ascertain the number of computed Bezier arcs, and then to construct each individual Bezier curve (or all Bezier curves). Note: ParametricTolerance is not used. Raises DomainError if U1 or U2 are out of the parametric bounds of the basis curve [FirstParameter, LastParameter]. The Tolerance criterion is ParametricTolerance. Raised if Abs (U2 - U1) <= ParametricTolerance.
        	:param BasisCurve:
        	:type BasisCurve: Geom_BSplineCurve
        	:param U1:
        	:type U1: float
        	:param U2:
        	:type U2: float
        	:param ParametricTolerance:
        	:type ParametricTolerance: float
        	:rtype: None
        """
        _GeomConvert.GeomConvert_BSplineCurveToBezierCurve_swiginit(self, _GeomConvert.new_GeomConvert_BSplineCurveToBezierCurve(*args))
    Knots = _swig_new_instance_method(_GeomConvert.GeomConvert_BSplineCurveToBezierCurve_Knots)
    NbArcs = _swig_new_instance_method(_GeomConvert.GeomConvert_BSplineCurveToBezierCurve_NbArcs)

    __repr__ = _dumps_object

    __swig_destroy__ = _GeomConvert.delete_GeomConvert_BSplineCurveToBezierCurve

# Register GeomConvert_BSplineCurveToBezierCurve in _GeomConvert:
_GeomConvert.GeomConvert_BSplineCurveToBezierCurve_swigregister(GeomConvert_BSplineCurveToBezierCurve)

class GeomConvert_BSplineSurfaceKnotSplitting(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Determines the u- and v-isoparametric curves along which the BSpline surface BasisSurface should be split in order to obtain patches with a degree of continuity equal to UContinuityRange in the u parametric direction, and to VContinuityRange in the v parametric direction. These isoparametric curves are defined by parameters, which are BasisSurface knot values in the u or v parametric direction. They are identified by indices in the BasisSurface knots table in the corresponding parametric direction. Use the available interrogation functions to access computed values, followed by the global function SplitBSplineSurface (provided by the package GeomConvert) to split the surface. Exceptions Standard_RangeError if UContinuityRange or VContinuityRange is less than zero.
        	:param BasisSurface:
        	:type BasisSurface: Geom_BSplineSurface
        	:param UContinuityRange:
        	:type UContinuityRange: int
        	:param VContinuityRange:
        	:type VContinuityRange: int
        	:rtype: None
        """
        _GeomConvert.GeomConvert_BSplineSurfaceKnotSplitting_swiginit(self, _GeomConvert.new_GeomConvert_BSplineSurfaceKnotSplitting(*args))
    NbUSplits = _swig_new_instance_method(_GeomConvert.GeomConvert_BSplineSurfaceKnotSplitting_NbUSplits)
    NbVSplits = _swig_new_instance_method(_GeomConvert.GeomConvert_BSplineSurfaceKnotSplitting_NbVSplits)
    Splitting = _swig_new_instance_method(_GeomConvert.GeomConvert_BSplineSurfaceKnotSplitting_Splitting)
    USplitValue = _swig_new_instance_method(_GeomConvert.GeomConvert_BSplineSurfaceKnotSplitting_USplitValue)
    VSplitValue = _swig_new_instance_method(_GeomConvert.GeomConvert_BSplineSurfaceKnotSplitting_VSplitValue)

    __repr__ = _dumps_object

    __swig_destroy__ = _GeomConvert.delete_GeomConvert_BSplineSurfaceKnotSplitting

# Register GeomConvert_BSplineSurfaceKnotSplitting in _GeomConvert:
_GeomConvert.GeomConvert_BSplineSurfaceKnotSplitting_swigregister(GeomConvert_BSplineSurfaceKnotSplitting)

class GeomConvert_BSplineSurfaceToBezierSurface(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Computes all the data needed to convert - the BSpline surface BasisSurface into a series of adjacent Bezier surfaces. The result consists of a grid of BasisSurface patches limited by isoparametric curves corresponding to knot values, both in the u and v parametric directions of the surface. A row in the grid corresponds to a series of adjacent patches, all limited by the same two u-isoparametric curves. A column in the grid corresponds to a series of adjacent patches, all limited by the same two v-isoparametric curves. Use the available interrogation functions to ascertain the number of computed Bezier patches, and then to construct each individual Bezier surface (or all Bezier surfaces). Note: ParametricTolerance is not used.
        	:param BasisSurface:
        	:type BasisSurface: Geom_BSplineSurface
        	:rtype: None* Computes all the data needed to convert the patch of the BSpline surface BasisSurface limited by the two parameter values U1 and U2 in the u parametric direction, and by the two parameter values V1 and V2 in the v parametric direction, into a series of adjacent Bezier surfaces. The result consists of a grid of BasisSurface patches limited by isoparametric curves corresponding to knot values, both in the u and v parametric directions of the surface. A row in the grid corresponds to a series of adjacent patches, all limited by the same two u-isoparametric curves. A column in the grid corresponds to a series of adjacent patches, all limited by the same two v-isoparametric curves. Use the available interrogation functions to ascertain the number of computed Bezier patches, and then to construct each individual Bezier surface (or all Bezier surfaces). Note: ParametricTolerance is not used. Raises DomainError if U1 or U2 or V1 or V2 are out of the parametric bounds of the basis surface [FirstUKnotIndex, LastUKnotIndex] , [FirstVKnotIndex, LastVKnotIndex] The tolerance criterion is ParametricTolerance. Raised if U2 - U1 <= ParametricTolerance or V2 - V1 <= ParametricTolerance.
        	:param BasisSurface:
        	:type BasisSurface: Geom_BSplineSurface
        	:param U1:
        	:type U1: float
        	:param U2:
        	:type U2: float
        	:param V1:
        	:type V1: float
        	:param V2:
        	:type V2: float
        	:param ParametricTolerance:
        	:type ParametricTolerance: float
        	:rtype: None
        """
        _GeomConvert.GeomConvert_BSplineSurfaceToBezierSurface_swiginit(self, _GeomConvert.new_GeomConvert_BSplineSurfaceToBezierSurface(*args))
    NbUPatches = _swig_new_instance_method(_GeomConvert.GeomConvert_BSplineSurfaceToBezierSurface_NbUPatches)
    NbVPatches = _swig_new_instance_method(_GeomConvert.GeomConvert_BSplineSurfaceToBezierSurface_NbVPatches)
    Patch = _swig_new_instance_method(_GeomConvert.GeomConvert_BSplineSurfaceToBezierSurface_Patch)
    Patches = _swig_new_instance_method(_GeomConvert.GeomConvert_BSplineSurfaceToBezierSurface_Patches)
    UKnots = _swig_new_instance_method(_GeomConvert.GeomConvert_BSplineSurfaceToBezierSurface_UKnots)
    VKnots = _swig_new_instance_method(_GeomConvert.GeomConvert_BSplineSurfaceToBezierSurface_VKnots)

    __repr__ = _dumps_object

    __swig_destroy__ = _GeomConvert.delete_GeomConvert_BSplineSurfaceToBezierSurface

# Register GeomConvert_BSplineSurfaceToBezierSurface in _GeomConvert:
_GeomConvert.GeomConvert_BSplineSurfaceToBezierSurface_swigregister(GeomConvert_BSplineSurfaceToBezierSurface)

class GeomConvert_CompBezierSurfacesToBSplineSurface(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Computes all the data needed to build a 'C0' continuous BSpline surface equivalent to the grid of adjacent non-rational Bezier surfaces Beziers. Each surface in the Beziers grid becomes a natural patch, limited by knots values, on the BSpline surface whose data is computed. Surfaces in the grid must satisfy the following conditions: - Coincident bounding curves between two consecutive surfaces in a row of the Beziers grid must be u-isoparametric bounding curves of these two surfaces. - Coincident bounding curves between two consecutive surfaces in a column of the Beziers grid must be v-isoparametric bounding curves of these two surfaces. The BSpline surface whose data is computed has the following characteristics: - Its degree in the u (respectively v) parametric direction is equal to that of the Bezier surface which has the highest degree in the u (respectively v) parametric direction in the Beziers grid. - It is a 'Piecewise Bezier' in both u and v parametric directions, i.e.: - the knots are regularly spaced in each parametric direction (i.e. the difference between two consecutive knots is a constant), and - all the multiplicities of the surface knots in a given parametric direction are equal to Degree, which is the degree of the BSpline surface in this parametric direction, except for the first and last knots for which the multiplicity is equal to Degree + 1. - Coincident bounding curves between two consecutive columns of Bezier surfaces in the Beziers grid become u-isoparametric curves, corresponding to knots values of the BSpline surface. - Coincident bounding curves between two consecutive rows of Bezier surfaces in the Beziers grid become v-isoparametric curves corresponding to knots values of the BSpline surface. Use the available consultation functions to access the computed data. This data may be used to construct the BSpline surface. Warning The surfaces in the Beziers grid must be adjacent, i.e. two consecutive Bezier surfaces in the grid (in a row or column) must have a coincident bounding curve. In addition, the location of the parameterization on each of these surfaces (i.e. the relative location of u and v isoparametric curves on the surface) is of importance with regard to the positioning of the surfaces in the Beziers grid. Care must be taken with respect to the above, as these properties are not checked and an error may occur if they are not satisfied. Exceptions Standard_NotImplemented if one of the Bezier surfaces of the Beziers grid is rational.
        	:param Beziers:
        	:type Beziers: TColGeom_Array2OfBezierSurface
        	:rtype: None* Build an Ci uniform (Rational) BSpline surface The higest Continuity Ci is imposed, like the maximal deformation is lower than <Tolerance>. Warning: The Continuity C0 is imposed without any check.
        	:param Beziers:
        	:type Beziers: TColGeom_Array2OfBezierSurface
        	:param Tolerance:
        	:type Tolerance: float
        	:param RemoveKnots: default value is Standard_True
        	:type RemoveKnots: bool
        	:rtype: None* Computes all the data needed to construct a BSpline surface equivalent to the adjacent non-rational Bezier surfaces Beziers grid. Each surface in the Beziers grid becomes a natural patch, limited by knots values, on the BSpline surface whose data is computed. Surfaces in the grid must satisfy the following conditions: - Coincident bounding curves between two consecutive surfaces in a row of the Beziers grid must be u-isoparametric bounding curves of these two surfaces. - Coincident bounding curves between two consecutive surfaces in a column of the Beziers grid must be v-isoparametric bounding curves of these two surfaces. The BSpline surface whose data is computed has the following characteristics: - Its degree in the u (respectively v) parametric direction is equal to that of the Bezier surface which has the highest degree in the u (respectively v) parametric direction in the Beziers grid. - Coincident bounding curves between two consecutive columns of Bezier surfaces in the Beziers grid become u-isoparametric curves corresponding to knots values of the BSpline surface. - Coincident bounding curves between two consecutive rows of Bezier surfaces in the Beziers grid become v-isoparametric curves corresponding to knots values of the BSpline surface. Knots values of the BSpline surface are given in the two tables: - UKnots for the u parametric direction (which corresponds to the order of Bezier surface columns in the Beziers grid), and - VKnots for the v parametric direction (which corresponds to the order of Bezier surface rows in the Beziers grid). The dimensions of UKnots (respectively VKnots) must be equal to the number of columns (respectively, rows) of the Beziers grid, plus 1 . UContinuity and VContinuity, which are both defaulted to GeomAbs_C0, specify the required continuity on the BSpline surface. If the required degree of continuity is greater than 0 in a given parametric direction, a deformation is applied locally on the initial surface (as defined by the Beziers grid) to satisfy this condition. This local deformation is not applied however, if it is greater than Tolerance (defaulted to 1.0 e-7). In such cases, the continuity condition is not satisfied, and the function IsDone will return false. A small tolerance value prevents any modification of the surface and a large tolerance value 'smoothes' the surface. Use the available consultation functions to access the computed data. This data may be used to construct the BSpline surface. Warning The surfaces in the Beziers grid must be adjacent, i.e. two consecutive Bezier surfaces in the grid (in a row or column) must have a coincident bounding curve. In addition, the location of the parameterization on each of these surfaces (i.e. the relative location of u and v isoparametric curves on the surface) is of importance with regard to the positioning of the surfaces in the Beziers grid. Care must be taken with respect to the above, as these properties are not checked and an error may occur if they are not satisfied. Exceptions Standard_DimensionMismatch: - if the number of knots in the UKnots table (i.e. the length of the UKnots array) is not equal to the number of columns of Bezier surfaces in the Beziers grid plus 1, or - if the number of knots in the VKnots table (i.e. the length of the VKnots array) is not equal to the number of rows of Bezier surfaces in the Beziers grid, plus 1. Standard_ConstructionError: - if UContinuity and VContinuity are not equal to one of the following values: GeomAbs_C0, GeomAbs_C1, GeomAbs_C2 and GeomAbs_C3; or - if the number of columns in the Beziers grid is greater than 1, and the required degree of continuity in the u parametric direction is greater than that of the Bezier surface with the highest degree in the u parametric direction (in the Beziers grid), minus 1; or - if the number of rows in the Beziers grid is greater than 1, and the required degree of continuity in the v parametric direction is greater than that of the Bezier surface with the highest degree in the v parametric direction (in the Beziers grid), minus 1 . Standard_NotImplemented if one of the Bezier surfaces in the Beziers grid is rational.
        	:param Beziers:
        	:type Beziers: TColGeom_Array2OfBezierSurface
        	:param UKnots:
        	:type UKnots: TColStd_Array1OfReal
        	:param VKnots:
        	:type VKnots: TColStd_Array1OfReal
        	:param UContinuity: default value is GeomAbs_C0
        	:type UContinuity: GeomAbs_Shape
        	:param VContinuity: default value is GeomAbs_C0
        	:type VContinuity: GeomAbs_Shape
        	:param Tolerance: default value is 1.0e-4
        	:type Tolerance: float
        	:rtype: None
        """
        _GeomConvert.GeomConvert_CompBezierSurfacesToBSplineSurface_swiginit(self, _GeomConvert.new_GeomConvert_CompBezierSurfacesToBSplineSurface(*args))
    IsDone = _swig_new_instance_method(_GeomConvert.GeomConvert_CompBezierSurfacesToBSplineSurface_IsDone)
    NbUKnots = _swig_new_instance_method(_GeomConvert.GeomConvert_CompBezierSurfacesToBSplineSurface_NbUKnots)
    NbUPoles = _swig_new_instance_method(_GeomConvert.GeomConvert_CompBezierSurfacesToBSplineSurface_NbUPoles)
    NbVKnots = _swig_new_instance_method(_GeomConvert.GeomConvert_CompBezierSurfacesToBSplineSurface_NbVKnots)
    NbVPoles = _swig_new_instance_method(_GeomConvert.GeomConvert_CompBezierSurfacesToBSplineSurface_NbVPoles)
    Poles = _swig_new_instance_method(_GeomConvert.GeomConvert_CompBezierSurfacesToBSplineSurface_Poles)
    UDegree = _swig_new_instance_method(_GeomConvert.GeomConvert_CompBezierSurfacesToBSplineSurface_UDegree)
    UKnots = _swig_new_instance_method(_GeomConvert.GeomConvert_CompBezierSurfacesToBSplineSurface_UKnots)
    UMultiplicities = _swig_new_instance_method(_GeomConvert.GeomConvert_CompBezierSurfacesToBSplineSurface_UMultiplicities)
    VDegree = _swig_new_instance_method(_GeomConvert.GeomConvert_CompBezierSurfacesToBSplineSurface_VDegree)
    VKnots = _swig_new_instance_method(_GeomConvert.GeomConvert_CompBezierSurfacesToBSplineSurface_VKnots)
    VMultiplicities = _swig_new_instance_method(_GeomConvert.GeomConvert_CompBezierSurfacesToBSplineSurface_VMultiplicities)

    __repr__ = _dumps_object

    __swig_destroy__ = _GeomConvert.delete_GeomConvert_CompBezierSurfacesToBSplineSurface

# Register GeomConvert_CompBezierSurfacesToBSplineSurface in _GeomConvert:
_GeomConvert.GeomConvert_CompBezierSurfacesToBSplineSurface_swigregister(GeomConvert_CompBezierSurfacesToBSplineSurface)

class GeomConvert_CompCurveToBSplineCurve(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Add = _swig_new_instance_method(_GeomConvert.GeomConvert_CompCurveToBSplineCurve_Add)
    BSplineCurve = _swig_new_instance_method(_GeomConvert.GeomConvert_CompCurveToBSplineCurve_BSplineCurve)

    def __init__(self, *args):
        r"""
        * Initialize the algorithme - Parameterisation is used to convert
        	:param Parameterisation: default value is Convert_TgtThetaOver2
        	:type Parameterisation: Convert_ParameterisationType
        	:rtype: None* Initialize the algorithme with one curve - Parameterisation is used to convert
        	:param BasisCurve:
        	:type BasisCurve: Geom_BoundedCurve
        	:param Parameterisation: default value is Convert_TgtThetaOver2
        	:type Parameterisation: Convert_ParameterisationType
        	:rtype: None
        """
        _GeomConvert.GeomConvert_CompCurveToBSplineCurve_swiginit(self, _GeomConvert.new_GeomConvert_CompCurveToBSplineCurve(*args))

    __repr__ = _dumps_object

    __swig_destroy__ = _GeomConvert.delete_GeomConvert_CompCurveToBSplineCurve

# Register GeomConvert_CompCurveToBSplineCurve in _GeomConvert:
_GeomConvert.GeomConvert_CompCurveToBSplineCurve_swigregister(GeomConvert_CompCurveToBSplineCurve)



