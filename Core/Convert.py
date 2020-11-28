# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
Convert module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_convert.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _Convert
else:
    import _Convert

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _Convert.SWIG_PyInstanceMethod_New
_swig_new_static_method = _Convert.SWIG_PyStaticMethod_New

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
    __swig_destroy__ = _Convert.delete_SwigPyIterator
    value = _swig_new_instance_method(_Convert.SwigPyIterator_value)
    incr = _swig_new_instance_method(_Convert.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_Convert.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_Convert.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_Convert.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_Convert.SwigPyIterator_copy)
    next = _swig_new_instance_method(_Convert.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_Convert.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_Convert.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_Convert.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_Convert.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_Convert.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_Convert.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_Convert.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_Convert.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_Convert.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _Convert:
_Convert.SwigPyIterator_swigregister(SwigPyIterator)


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
import OCC.Core.TColgp
import OCC.Core.TColStd
import OCC.Core.TCollection
import OCC.Core.gp
Convert_TgtThetaOver2 = _Convert.Convert_TgtThetaOver2
Convert_TgtThetaOver2_1 = _Convert.Convert_TgtThetaOver2_1
Convert_TgtThetaOver2_2 = _Convert.Convert_TgtThetaOver2_2
Convert_TgtThetaOver2_3 = _Convert.Convert_TgtThetaOver2_3
Convert_TgtThetaOver2_4 = _Convert.Convert_TgtThetaOver2_4
Convert_QuasiAngular = _Convert.Convert_QuasiAngular
Convert_RationalC1 = _Convert.Convert_RationalC1
Convert_Polynomial = _Convert.Convert_Polynomial
class Convert_SequenceOfArray1OfPoles(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_Convert.Convert_SequenceOfArray1OfPoles_begin)
    end = _swig_new_instance_method(_Convert.Convert_SequenceOfArray1OfPoles_end)
    cbegin = _swig_new_instance_method(_Convert.Convert_SequenceOfArray1OfPoles_cbegin)
    cend = _swig_new_instance_method(_Convert.Convert_SequenceOfArray1OfPoles_cend)

    def __init__(self, *args):
        _Convert.Convert_SequenceOfArray1OfPoles_swiginit(self, _Convert.new_Convert_SequenceOfArray1OfPoles(*args))
    Size = _swig_new_instance_method(_Convert.Convert_SequenceOfArray1OfPoles_Size)
    Length = _swig_new_instance_method(_Convert.Convert_SequenceOfArray1OfPoles_Length)
    Lower = _swig_new_instance_method(_Convert.Convert_SequenceOfArray1OfPoles_Lower)
    Upper = _swig_new_instance_method(_Convert.Convert_SequenceOfArray1OfPoles_Upper)
    IsEmpty = _swig_new_instance_method(_Convert.Convert_SequenceOfArray1OfPoles_IsEmpty)
    Reverse = _swig_new_instance_method(_Convert.Convert_SequenceOfArray1OfPoles_Reverse)
    Exchange = _swig_new_instance_method(_Convert.Convert_SequenceOfArray1OfPoles_Exchange)
    delNode = _swig_new_static_method(_Convert.Convert_SequenceOfArray1OfPoles_delNode)
    Clear = _swig_new_instance_method(_Convert.Convert_SequenceOfArray1OfPoles_Clear)
    Assign = _swig_new_instance_method(_Convert.Convert_SequenceOfArray1OfPoles_Assign)
    Set = _swig_new_instance_method(_Convert.Convert_SequenceOfArray1OfPoles_Set)
    Remove = _swig_new_instance_method(_Convert.Convert_SequenceOfArray1OfPoles_Remove)
    Append = _swig_new_instance_method(_Convert.Convert_SequenceOfArray1OfPoles_Append)
    Prepend = _swig_new_instance_method(_Convert.Convert_SequenceOfArray1OfPoles_Prepend)
    InsertBefore = _swig_new_instance_method(_Convert.Convert_SequenceOfArray1OfPoles_InsertBefore)
    InsertAfter = _swig_new_instance_method(_Convert.Convert_SequenceOfArray1OfPoles_InsertAfter)
    Split = _swig_new_instance_method(_Convert.Convert_SequenceOfArray1OfPoles_Split)
    First = _swig_new_instance_method(_Convert.Convert_SequenceOfArray1OfPoles_First)
    ChangeFirst = _swig_new_instance_method(_Convert.Convert_SequenceOfArray1OfPoles_ChangeFirst)
    Last = _swig_new_instance_method(_Convert.Convert_SequenceOfArray1OfPoles_Last)
    ChangeLast = _swig_new_instance_method(_Convert.Convert_SequenceOfArray1OfPoles_ChangeLast)
    Value = _swig_new_instance_method(_Convert.Convert_SequenceOfArray1OfPoles_Value)
    ChangeValue = _swig_new_instance_method(_Convert.Convert_SequenceOfArray1OfPoles_ChangeValue)
    __call__ = _swig_new_instance_method(_Convert.Convert_SequenceOfArray1OfPoles___call__)
    SetValue = _swig_new_instance_method(_Convert.Convert_SequenceOfArray1OfPoles_SetValue)
    __swig_destroy__ = _Convert.delete_Convert_SequenceOfArray1OfPoles

# Register Convert_SequenceOfArray1OfPoles in _Convert:
_Convert.Convert_SequenceOfArray1OfPoles_swigregister(Convert_SequenceOfArray1OfPoles)
Convert_SequenceOfArray1OfPoles_delNode = _Convert.Convert_SequenceOfArray1OfPoles_delNode

class Convert_CompBezierCurves2dToBSplineCurve2d(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    AddCurve = _swig_new_instance_method(_Convert.Convert_CompBezierCurves2dToBSplineCurve2d_AddCurve)

    def __init__(self, *args):
        r"""
        * Constructs a framework for converting a sequence of adjacent non-rational Bezier curves into a BSpline curve. Knots will be created on the computed BSpline curve at each junction point of two consecutive Bezier curves. The degree of continuity of the BSpline curve will be increased at the junction point of two consecutive Bezier curves if their tangent vectors at this point are parallel. AngularTolerance (given in radians, and defaulted to 1.0 e-4) will be used to check the parallelism of the two tangent vectors. Use the following functions: - AddCurve to define in sequence the adjacent Bezier curves to be converted, - Perform to compute the data needed to build the BSpline curve, - and the available consultation functions to access the computed data. This data may be used to construct the BSpline curve.
        	:param AngularTolerance: default value is 1.0e-4
        	:type AngularTolerance: float
        	:rtype: None
        """
        _Convert.Convert_CompBezierCurves2dToBSplineCurve2d_swiginit(self, _Convert.new_Convert_CompBezierCurves2dToBSplineCurve2d(*args))
    Degree = _swig_new_instance_method(_Convert.Convert_CompBezierCurves2dToBSplineCurve2d_Degree)
    KnotsAndMults = _swig_new_instance_method(_Convert.Convert_CompBezierCurves2dToBSplineCurve2d_KnotsAndMults)
    NbKnots = _swig_new_instance_method(_Convert.Convert_CompBezierCurves2dToBSplineCurve2d_NbKnots)
    NbPoles = _swig_new_instance_method(_Convert.Convert_CompBezierCurves2dToBSplineCurve2d_NbPoles)
    Perform = _swig_new_instance_method(_Convert.Convert_CompBezierCurves2dToBSplineCurve2d_Perform)
    Poles = _swig_new_instance_method(_Convert.Convert_CompBezierCurves2dToBSplineCurve2d_Poles)

    __repr__ = _dumps_object

    __swig_destroy__ = _Convert.delete_Convert_CompBezierCurves2dToBSplineCurve2d

# Register Convert_CompBezierCurves2dToBSplineCurve2d in _Convert:
_Convert.Convert_CompBezierCurves2dToBSplineCurve2d_swigregister(Convert_CompBezierCurves2dToBSplineCurve2d)

class Convert_CompBezierCurvesToBSplineCurve(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    AddCurve = _swig_new_instance_method(_Convert.Convert_CompBezierCurvesToBSplineCurve_AddCurve)

    def __init__(self, *args):
        r"""
        * Constructs a framework for converting a sequence of adjacent non-rational Bezier curves into a BSpline curve. Knots will be created on the computed BSpline curve at each junction point of two consecutive Bezier curves. The degree of continuity of the BSpline curve will be increased at the junction point of two consecutive Bezier curves if their tangent vectors at this point are parallel. AngularTolerance (given in radians, and defaulted to 1.0 e-4) will be used to check the parallelism of the two tangent vectors. Use the following functions: - AddCurve to define in sequence the adjacent Bezier curves to be converted, - Perform to compute the data needed to build the BSpline curve, - and the available consultation functions to access the computed data. This data may be used to construct the BSpline curve.
        	:param AngularTolerance: default value is 1.0e-4
        	:type AngularTolerance: float
        	:rtype: None
        """
        _Convert.Convert_CompBezierCurvesToBSplineCurve_swiginit(self, _Convert.new_Convert_CompBezierCurvesToBSplineCurve(*args))
    Degree = _swig_new_instance_method(_Convert.Convert_CompBezierCurvesToBSplineCurve_Degree)
    KnotsAndMults = _swig_new_instance_method(_Convert.Convert_CompBezierCurvesToBSplineCurve_KnotsAndMults)
    NbKnots = _swig_new_instance_method(_Convert.Convert_CompBezierCurvesToBSplineCurve_NbKnots)
    NbPoles = _swig_new_instance_method(_Convert.Convert_CompBezierCurvesToBSplineCurve_NbPoles)
    Perform = _swig_new_instance_method(_Convert.Convert_CompBezierCurvesToBSplineCurve_Perform)
    Poles = _swig_new_instance_method(_Convert.Convert_CompBezierCurvesToBSplineCurve_Poles)

    __repr__ = _dumps_object

    __swig_destroy__ = _Convert.delete_Convert_CompBezierCurvesToBSplineCurve

# Register Convert_CompBezierCurvesToBSplineCurve in _Convert:
_Convert.Convert_CompBezierCurvesToBSplineCurve_swigregister(Convert_CompBezierCurvesToBSplineCurve)

class Convert_CompPolynomialToPoles(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Warning! Continuity can be at MOST the maximum degree of the polynomial functions TrueIntervals : this is the true parameterisation for the composite curve that is : the curve has myContinuity if the nth curve is parameterized between myTrueIntervals(n) and myTrueIntervals(n+1) //! Coefficients have to be the implicit 'c form': Coefficients[Numcurves][MaxDegree+1][Dimension] //! Warning! The NumberOfCoefficient of an polynome is his degree + 1 Example: To convert the linear function f(x) = 2*x + 1 on the domaine [2,5] to BSpline with the bound [-1,1]. Arguments are : NumCurves = 1; Continuity = 1; Dimension = 1; MaxDegree = 1; NumCoeffPerCurve [1] = {2}; Coefficients[2] = {1, 2}; PolynomialIntervals[1,2] = {{2,5}} TrueIntervals[2] = {-1, 1}
        	:param NumCurves:
        	:type NumCurves: int
        	:param Continuity:
        	:type Continuity: int
        	:param Dimension:
        	:type Dimension: int
        	:param MaxDegree:
        	:type MaxDegree: int
        	:param NumCoeffPerCurve:
        	:type NumCoeffPerCurve: TColStd_HArray1OfInteger
        	:param Coefficients:
        	:type Coefficients: TColStd_HArray1OfReal
        	:param PolynomialIntervals:
        	:type PolynomialIntervals: TColStd_HArray2OfReal
        	:param TrueIntervals:
        	:type TrueIntervals: TColStd_HArray1OfReal
        	:rtype: None* To Convert sevral span with different order of Continuity. Warning: The Length of Continuity have to be NumCurves-1
        	:param NumCurves:
        	:type NumCurves: int
        	:param Dimension:
        	:type Dimension: int
        	:param MaxDegree:
        	:type MaxDegree: int
        	:param Continuity:
        	:type Continuity: TColStd_Array1OfInteger
        	:param NumCoeffPerCurve:
        	:type NumCoeffPerCurve: TColStd_Array1OfInteger
        	:param Coefficients:
        	:type Coefficients: TColStd_Array1OfReal
        	:param PolynomialIntervals:
        	:type PolynomialIntervals: TColStd_Array2OfReal
        	:param TrueIntervals:
        	:type TrueIntervals: TColStd_Array1OfReal
        	:rtype: None* To Convert only one span.
        	:param Dimension:
        	:type Dimension: int
        	:param MaxDegree:
        	:type MaxDegree: int
        	:param Degree:
        	:type Degree: int
        	:param Coefficients:
        	:type Coefficients: TColStd_Array1OfReal
        	:param PolynomialIntervals:
        	:type PolynomialIntervals: TColStd_Array1OfReal
        	:param TrueIntervals:
        	:type TrueIntervals: TColStd_Array1OfReal
        	:rtype: None
        """
        _Convert.Convert_CompPolynomialToPoles_swiginit(self, _Convert.new_Convert_CompPolynomialToPoles(*args))
    Degree = _swig_new_instance_method(_Convert.Convert_CompPolynomialToPoles_Degree)
    IsDone = _swig_new_instance_method(_Convert.Convert_CompPolynomialToPoles_IsDone)
    Knots = _swig_new_instance_method(_Convert.Convert_CompPolynomialToPoles_Knots)
    Multiplicities = _swig_new_instance_method(_Convert.Convert_CompPolynomialToPoles_Multiplicities)
    NbKnots = _swig_new_instance_method(_Convert.Convert_CompPolynomialToPoles_NbKnots)
    NbPoles = _swig_new_instance_method(_Convert.Convert_CompPolynomialToPoles_NbPoles)
    Poles = _swig_new_instance_method(_Convert.Convert_CompPolynomialToPoles_Poles)

    __repr__ = _dumps_object

    __swig_destroy__ = _Convert.delete_Convert_CompPolynomialToPoles

# Register Convert_CompPolynomialToPoles in _Convert:
_Convert.Convert_CompPolynomialToPoles_swigregister(Convert_CompPolynomialToPoles)

class Convert_ConicToBSplineCurve(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    BuildCosAndSin = _swig_new_instance_method(_Convert.Convert_ConicToBSplineCurve_BuildCosAndSin)
    Degree = _swig_new_instance_method(_Convert.Convert_ConicToBSplineCurve_Degree)
    IsPeriodic = _swig_new_instance_method(_Convert.Convert_ConicToBSplineCurve_IsPeriodic)
    Knot = _swig_new_instance_method(_Convert.Convert_ConicToBSplineCurve_Knot)
    Multiplicity = _swig_new_instance_method(_Convert.Convert_ConicToBSplineCurve_Multiplicity)
    NbKnots = _swig_new_instance_method(_Convert.Convert_ConicToBSplineCurve_NbKnots)
    NbPoles = _swig_new_instance_method(_Convert.Convert_ConicToBSplineCurve_NbPoles)
    Pole = _swig_new_instance_method(_Convert.Convert_ConicToBSplineCurve_Pole)
    Weight = _swig_new_instance_method(_Convert.Convert_ConicToBSplineCurve_Weight)

    __repr__ = _dumps_object

    __swig_destroy__ = _Convert.delete_Convert_ConicToBSplineCurve

# Register Convert_ConicToBSplineCurve in _Convert:
_Convert.Convert_ConicToBSplineCurve_swigregister(Convert_ConicToBSplineCurve)

class Convert_ElementarySurfaceToBSplineSurface(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    IsUPeriodic = _swig_new_instance_method(_Convert.Convert_ElementarySurfaceToBSplineSurface_IsUPeriodic)
    IsVPeriodic = _swig_new_instance_method(_Convert.Convert_ElementarySurfaceToBSplineSurface_IsVPeriodic)
    NbUKnots = _swig_new_instance_method(_Convert.Convert_ElementarySurfaceToBSplineSurface_NbUKnots)
    NbUPoles = _swig_new_instance_method(_Convert.Convert_ElementarySurfaceToBSplineSurface_NbUPoles)
    NbVKnots = _swig_new_instance_method(_Convert.Convert_ElementarySurfaceToBSplineSurface_NbVKnots)
    NbVPoles = _swig_new_instance_method(_Convert.Convert_ElementarySurfaceToBSplineSurface_NbVPoles)
    Pole = _swig_new_instance_method(_Convert.Convert_ElementarySurfaceToBSplineSurface_Pole)
    UDegree = _swig_new_instance_method(_Convert.Convert_ElementarySurfaceToBSplineSurface_UDegree)
    UKnot = _swig_new_instance_method(_Convert.Convert_ElementarySurfaceToBSplineSurface_UKnot)
    UMultiplicity = _swig_new_instance_method(_Convert.Convert_ElementarySurfaceToBSplineSurface_UMultiplicity)
    VDegree = _swig_new_instance_method(_Convert.Convert_ElementarySurfaceToBSplineSurface_VDegree)
    VKnot = _swig_new_instance_method(_Convert.Convert_ElementarySurfaceToBSplineSurface_VKnot)
    VMultiplicity = _swig_new_instance_method(_Convert.Convert_ElementarySurfaceToBSplineSurface_VMultiplicity)
    Weight = _swig_new_instance_method(_Convert.Convert_ElementarySurfaceToBSplineSurface_Weight)

    __repr__ = _dumps_object

    __swig_destroy__ = _Convert.delete_Convert_ElementarySurfaceToBSplineSurface

# Register Convert_ElementarySurfaceToBSplineSurface in _Convert:
_Convert.Convert_ElementarySurfaceToBSplineSurface_swigregister(Convert_ElementarySurfaceToBSplineSurface)

class Convert_GridPolynomialToPoles(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * To only one polynomial Surface. The Length of <PolynomialUIntervals> and <PolynomialVIntervals> have to be 2. This values defined the parametric domain of the Polynomial Equation. //! Coefficients : The <Coefficients> have to be formated than an 'C array' [MaxUDegree+1] [MaxVDegree+1] [3]
        	:param MaxUDegree:
        	:type MaxUDegree: int
        	:param MaxVDegree:
        	:type MaxVDegree: int
        	:param NumCoeff:
        	:type NumCoeff: TColStd_HArray1OfInteger
        	:param Coefficients:
        	:type Coefficients: TColStd_HArray1OfReal
        	:param PolynomialUIntervals:
        	:type PolynomialUIntervals: TColStd_HArray1OfReal
        	:param PolynomialVIntervals:
        	:type PolynomialVIntervals: TColStd_HArray1OfReal
        	:rtype: None* To one grid of polynomial Surface. Warning! Continuity in each parametric direction can be at MOST the maximum degree of the polynomial functions. //! <TrueUIntervals>, <TrueVIntervals> : this is the true parameterisation for the composite surface //! Coefficients : The Coefficients have to be formated than an 'C array' [NbVSurfaces] [NBUSurfaces] [MaxUDegree+1] [MaxVDegree+1] [3] raises DomainError if <NumCoeffPerSurface> is not a [1, NbVSurfaces*NbUSurfaces, 1,2] array. if <Coefficients> is not a
        	:param NbUSurfaces:
        	:type NbUSurfaces: int
        	:param NBVSurfaces:
        	:type NBVSurfaces: int
        	:param UContinuity:
        	:type UContinuity: int
        	:param VContinuity:
        	:type VContinuity: int
        	:param MaxUDegree:
        	:type MaxUDegree: int
        	:param MaxVDegree:
        	:type MaxVDegree: int
        	:param NumCoeffPerSurface:
        	:type NumCoeffPerSurface: TColStd_HArray2OfInteger
        	:param Coefficients:
        	:type Coefficients: TColStd_HArray1OfReal
        	:param PolynomialUIntervals:
        	:type PolynomialUIntervals: TColStd_HArray1OfReal
        	:param PolynomialVIntervals:
        	:type PolynomialVIntervals: TColStd_HArray1OfReal
        	:param TrueUIntervals:
        	:type TrueUIntervals: TColStd_HArray1OfReal
        	:param TrueVIntervals:
        	:type TrueVIntervals: TColStd_HArray1OfReal
        	:rtype: None
        """
        _Convert.Convert_GridPolynomialToPoles_swiginit(self, _Convert.new_Convert_GridPolynomialToPoles(*args))
    IsDone = _swig_new_instance_method(_Convert.Convert_GridPolynomialToPoles_IsDone)
    NbUKnots = _swig_new_instance_method(_Convert.Convert_GridPolynomialToPoles_NbUKnots)
    NbUPoles = _swig_new_instance_method(_Convert.Convert_GridPolynomialToPoles_NbUPoles)
    NbVKnots = _swig_new_instance_method(_Convert.Convert_GridPolynomialToPoles_NbVKnots)
    NbVPoles = _swig_new_instance_method(_Convert.Convert_GridPolynomialToPoles_NbVPoles)
    Perform = _swig_new_instance_method(_Convert.Convert_GridPolynomialToPoles_Perform)
    Poles = _swig_new_instance_method(_Convert.Convert_GridPolynomialToPoles_Poles)
    UDegree = _swig_new_instance_method(_Convert.Convert_GridPolynomialToPoles_UDegree)
    UKnots = _swig_new_instance_method(_Convert.Convert_GridPolynomialToPoles_UKnots)
    UMultiplicities = _swig_new_instance_method(_Convert.Convert_GridPolynomialToPoles_UMultiplicities)
    VDegree = _swig_new_instance_method(_Convert.Convert_GridPolynomialToPoles_VDegree)
    VKnots = _swig_new_instance_method(_Convert.Convert_GridPolynomialToPoles_VKnots)
    VMultiplicities = _swig_new_instance_method(_Convert.Convert_GridPolynomialToPoles_VMultiplicities)

    __repr__ = _dumps_object

    __swig_destroy__ = _Convert.delete_Convert_GridPolynomialToPoles

# Register Convert_GridPolynomialToPoles in _Convert:
_Convert.Convert_GridPolynomialToPoles_swigregister(Convert_GridPolynomialToPoles)

class Convert_CircleToBSplineCurve(Convert_ConicToBSplineCurve):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * The equivalent B-spline curve has the same orientation as the circle C.
        	:param C:
        	:type C: gp_Circ2d
        	:param Parameterisation: default value is Convert_TgtThetaOver2
        	:type Parameterisation: Convert_ParameterisationType
        	:rtype: None* The circle C is limited between the parametric values U1, U2 in radians. U1 and U2 [0.0, 2*Pi] . The equivalent B-spline curve is oriented from U1 to U2 and has the same orientation as the circle C. //! Raised if U1 = U2 or U1 = U2 + 2.0 * Pi
        	:param C:
        	:type C: gp_Circ2d
        	:param U1:
        	:type U1: float
        	:param U2:
        	:type U2: float
        	:param Parameterisation: default value is Convert_TgtThetaOver2
        	:type Parameterisation: Convert_ParameterisationType
        	:rtype: None
        """
        _Convert.Convert_CircleToBSplineCurve_swiginit(self, _Convert.new_Convert_CircleToBSplineCurve(*args))

    __repr__ = _dumps_object

    __swig_destroy__ = _Convert.delete_Convert_CircleToBSplineCurve

# Register Convert_CircleToBSplineCurve in _Convert:
_Convert.Convert_CircleToBSplineCurve_swigregister(Convert_CircleToBSplineCurve)

class Convert_ConeToBSplineSurface(Convert_ElementarySurfaceToBSplineSurface):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * The equivalent B-spline surface as the same orientation as the Cone in the U and V parametric directions. //! Raised if U1 = U2 or U1 = U2 + 2.0 * Pi Raised if V1 = V2.
        	:param C:
        	:type C: gp_Cone
        	:param U1:
        	:type U1: float
        	:param U2:
        	:type U2: float
        	:param V1:
        	:type V1: float
        	:param V2:
        	:type V2: float
        	:rtype: None* The equivalent B-spline surface as the same orientation as the Cone in the U and V parametric directions. //! Raised if V1 = V2.
        	:param C:
        	:type C: gp_Cone
        	:param V1:
        	:type V1: float
        	:param V2:
        	:type V2: float
        	:rtype: None
        """
        _Convert.Convert_ConeToBSplineSurface_swiginit(self, _Convert.new_Convert_ConeToBSplineSurface(*args))

    __repr__ = _dumps_object

    __swig_destroy__ = _Convert.delete_Convert_ConeToBSplineSurface

# Register Convert_ConeToBSplineSurface in _Convert:
_Convert.Convert_ConeToBSplineSurface_swigregister(Convert_ConeToBSplineSurface)

class Convert_CylinderToBSplineSurface(Convert_ElementarySurfaceToBSplineSurface):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * The equivalent B-splineSurface as the same orientation as the cylinder in the U and V parametric directions. //! Raised if U1 = U2 or U1 = U2 + 2.0 * Pi Raised if V1 = V2.
        	:param Cyl:
        	:type Cyl: gp_Cylinder
        	:param U1:
        	:type U1: float
        	:param U2:
        	:type U2: float
        	:param V1:
        	:type V1: float
        	:param V2:
        	:type V2: float
        	:rtype: None* The equivalent B-splineSurface as the same orientation as the cylinder in the U and V parametric directions. //! Raised if V1 = V2.
        	:param Cyl:
        	:type Cyl: gp_Cylinder
        	:param V1:
        	:type V1: float
        	:param V2:
        	:type V2: float
        	:rtype: None
        """
        _Convert.Convert_CylinderToBSplineSurface_swiginit(self, _Convert.new_Convert_CylinderToBSplineSurface(*args))

    __repr__ = _dumps_object

    __swig_destroy__ = _Convert.delete_Convert_CylinderToBSplineSurface

# Register Convert_CylinderToBSplineSurface in _Convert:
_Convert.Convert_CylinderToBSplineSurface_swigregister(Convert_CylinderToBSplineSurface)

class Convert_EllipseToBSplineCurve(Convert_ConicToBSplineCurve):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * The equivalent B-spline curve has the same orientation as the ellipse E.
        	:param E:
        	:type E: gp_Elips2d
        	:param Parameterisation: default value is Convert_TgtThetaOver2
        	:type Parameterisation: Convert_ParameterisationType
        	:rtype: None* The ellipse E is limited between the parametric values U1, U2. The equivalent B-spline curve is oriented from U1 to U2 and has the same orientation as E. //! Raised if U1 = U2 or U1 = U2 + 2.0 * Pi
        	:param E:
        	:type E: gp_Elips2d
        	:param U1:
        	:type U1: float
        	:param U2:
        	:type U2: float
        	:param Parameterisation: default value is Convert_TgtThetaOver2
        	:type Parameterisation: Convert_ParameterisationType
        	:rtype: None
        """
        _Convert.Convert_EllipseToBSplineCurve_swiginit(self, _Convert.new_Convert_EllipseToBSplineCurve(*args))

    __repr__ = _dumps_object

    __swig_destroy__ = _Convert.delete_Convert_EllipseToBSplineCurve

# Register Convert_EllipseToBSplineCurve in _Convert:
_Convert.Convert_EllipseToBSplineCurve_swigregister(Convert_EllipseToBSplineCurve)

class Convert_HyperbolaToBSplineCurve(Convert_ConicToBSplineCurve):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * The hyperbola H is limited between the parametric values U1, U2 and the equivalent B-spline curve has the same orientation as the hyperbola.
        	:param H:
        	:type H: gp_Hypr2d
        	:param U1:
        	:type U1: float
        	:param U2:
        	:type U2: float
        	:rtype: None
        """
        _Convert.Convert_HyperbolaToBSplineCurve_swiginit(self, _Convert.new_Convert_HyperbolaToBSplineCurve(*args))

    __repr__ = _dumps_object

    __swig_destroy__ = _Convert.delete_Convert_HyperbolaToBSplineCurve

# Register Convert_HyperbolaToBSplineCurve in _Convert:
_Convert.Convert_HyperbolaToBSplineCurve_swigregister(Convert_HyperbolaToBSplineCurve)

class Convert_ParabolaToBSplineCurve(Convert_ConicToBSplineCurve):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * The parabola Prb is limited between the parametric values U1, U2 and the equivalent B-spline curve as the same orientation as the parabola Prb.
        	:param Prb:
        	:type Prb: gp_Parab2d
        	:param U1:
        	:type U1: float
        	:param U2:
        	:type U2: float
        	:rtype: None
        """
        _Convert.Convert_ParabolaToBSplineCurve_swiginit(self, _Convert.new_Convert_ParabolaToBSplineCurve(*args))

    __repr__ = _dumps_object

    __swig_destroy__ = _Convert.delete_Convert_ParabolaToBSplineCurve

# Register Convert_ParabolaToBSplineCurve in _Convert:
_Convert.Convert_ParabolaToBSplineCurve_swigregister(Convert_ParabolaToBSplineCurve)

class Convert_SphereToBSplineSurface(Convert_ElementarySurfaceToBSplineSurface):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * The equivalent B-spline surface as the same orientation as the sphere in the U and V parametric directions. //! Raised if U1 = U2 or U1 = U2 + 2.0 * Pi Raised if V1 = V2.
        	:param Sph:
        	:type Sph: gp_Sphere
        	:param U1:
        	:type U1: float
        	:param U2:
        	:type U2: float
        	:param V1:
        	:type V1: float
        	:param V2:
        	:type V2: float
        	:rtype: None* The equivalent B-spline surface as the same orientation as the sphere in the U and V parametric directions. //! Raised if UTrim = True and Param1 = Param2 or Param1 = Param2 + 2.0 * Pi Raised if UTrim = False and Param1 = Param2
        	:param Sph:
        	:type Sph: gp_Sphere
        	:param Param1:
        	:type Param1: float
        	:param Param2:
        	:type Param2: float
        	:param UTrim: default value is Standard_True
        	:type UTrim: bool
        	:rtype: None* The equivalent B-spline surface as the same orientation as the sphere in the U and V parametric directions.
        	:param Sph:
        	:type Sph: gp_Sphere
        	:rtype: None
        """
        _Convert.Convert_SphereToBSplineSurface_swiginit(self, _Convert.new_Convert_SphereToBSplineSurface(*args))

    __repr__ = _dumps_object

    __swig_destroy__ = _Convert.delete_Convert_SphereToBSplineSurface

# Register Convert_SphereToBSplineSurface in _Convert:
_Convert.Convert_SphereToBSplineSurface_swigregister(Convert_SphereToBSplineSurface)

class Convert_TorusToBSplineSurface(Convert_ElementarySurfaceToBSplineSurface):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * The equivalent B-spline surface as the same orientation as the torus in the U and V parametric directions. //! Raised if U1 = U2 or U1 = U2 + 2.0 * Pi Raised if V1 = V2 or V1 = V2 + 2.0 * Pi
        	:param T:
        	:type T: gp_Torus
        	:param U1:
        	:type U1: float
        	:param U2:
        	:type U2: float
        	:param V1:
        	:type V1: float
        	:param V2:
        	:type V2: float
        	:rtype: None* The equivalent B-spline surface as the same orientation as the torus in the U and V parametric directions. //! Raised if Param1 = Param2 or Param1 = Param2 + 2.0 * Pi
        	:param T:
        	:type T: gp_Torus
        	:param Param1:
        	:type Param1: float
        	:param Param2:
        	:type Param2: float
        	:param UTrim: default value is Standard_True
        	:type UTrim: bool
        	:rtype: None* The equivalent B-spline surface as the same orientation as the torus in the U and V parametric directions.
        	:param T:
        	:type T: gp_Torus
        	:rtype: None
        """
        _Convert.Convert_TorusToBSplineSurface_swiginit(self, _Convert.new_Convert_TorusToBSplineSurface(*args))

    __repr__ = _dumps_object

    __swig_destroy__ = _Convert.delete_Convert_TorusToBSplineSurface

# Register Convert_TorusToBSplineSurface in _Convert:
_Convert.Convert_TorusToBSplineSurface_swigregister(Convert_TorusToBSplineSurface)



