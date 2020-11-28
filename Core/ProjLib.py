# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
ProjLib module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_projlib.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _ProjLib
else:
    import _ProjLib

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _ProjLib.SWIG_PyInstanceMethod_New
_swig_new_static_method = _ProjLib.SWIG_PyStaticMethod_New

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
    __swig_destroy__ = _ProjLib.delete_SwigPyIterator
    value = _swig_new_instance_method(_ProjLib.SwigPyIterator_value)
    incr = _swig_new_instance_method(_ProjLib.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_ProjLib.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_ProjLib.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_ProjLib.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_ProjLib.SwigPyIterator_copy)
    next = _swig_new_instance_method(_ProjLib.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_ProjLib.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_ProjLib.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_ProjLib.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_ProjLib.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_ProjLib.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_ProjLib.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_ProjLib.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_ProjLib.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_ProjLib.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _ProjLib:
_ProjLib.SwigPyIterator_swigregister(SwigPyIterator)


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
import OCC.Core.Adaptor3d
import OCC.Core.Geom
import OCC.Core.gp
import OCC.Core.GeomAbs
import OCC.Core.TColStd
import OCC.Core.TCollection
import OCC.Core.TopAbs
import OCC.Core.Adaptor2d
import OCC.Core.Geom2d
import OCC.Core.math
import OCC.Core.Message
import OCC.Core.AppParCurves
import OCC.Core.GeomAdaptor
Handle_ProjLib_HCompProjectedCurve_Create = _ProjLib.Handle_ProjLib_HCompProjectedCurve_Create
Handle_ProjLib_HCompProjectedCurve_DownCast = _ProjLib.Handle_ProjLib_HCompProjectedCurve_DownCast
Handle_ProjLib_HCompProjectedCurve_IsNull = _ProjLib.Handle_ProjLib_HCompProjectedCurve_IsNull
Handle_ProjLib_HProjectedCurve_Create = _ProjLib.Handle_ProjLib_HProjectedCurve_Create
Handle_ProjLib_HProjectedCurve_DownCast = _ProjLib.Handle_ProjLib_HProjectedCurve_DownCast
Handle_ProjLib_HProjectedCurve_IsNull = _ProjLib.Handle_ProjLib_HProjectedCurve_IsNull
Handle_ProjLib_HSequenceOfHSequenceOfPnt_Create = _ProjLib.Handle_ProjLib_HSequenceOfHSequenceOfPnt_Create
Handle_ProjLib_HSequenceOfHSequenceOfPnt_DownCast = _ProjLib.Handle_ProjLib_HSequenceOfHSequenceOfPnt_DownCast
Handle_ProjLib_HSequenceOfHSequenceOfPnt_IsNull = _ProjLib.Handle_ProjLib_HSequenceOfHSequenceOfPnt_IsNull
class ProjLib_SequenceOfHSequenceOfPnt(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_ProjLib.ProjLib_SequenceOfHSequenceOfPnt_begin)
    end = _swig_new_instance_method(_ProjLib.ProjLib_SequenceOfHSequenceOfPnt_end)
    cbegin = _swig_new_instance_method(_ProjLib.ProjLib_SequenceOfHSequenceOfPnt_cbegin)
    cend = _swig_new_instance_method(_ProjLib.ProjLib_SequenceOfHSequenceOfPnt_cend)

    def __init__(self, *args):
        _ProjLib.ProjLib_SequenceOfHSequenceOfPnt_swiginit(self, _ProjLib.new_ProjLib_SequenceOfHSequenceOfPnt(*args))
    Size = _swig_new_instance_method(_ProjLib.ProjLib_SequenceOfHSequenceOfPnt_Size)
    Length = _swig_new_instance_method(_ProjLib.ProjLib_SequenceOfHSequenceOfPnt_Length)
    Lower = _swig_new_instance_method(_ProjLib.ProjLib_SequenceOfHSequenceOfPnt_Lower)
    Upper = _swig_new_instance_method(_ProjLib.ProjLib_SequenceOfHSequenceOfPnt_Upper)
    IsEmpty = _swig_new_instance_method(_ProjLib.ProjLib_SequenceOfHSequenceOfPnt_IsEmpty)
    Reverse = _swig_new_instance_method(_ProjLib.ProjLib_SequenceOfHSequenceOfPnt_Reverse)
    Exchange = _swig_new_instance_method(_ProjLib.ProjLib_SequenceOfHSequenceOfPnt_Exchange)
    delNode = _swig_new_static_method(_ProjLib.ProjLib_SequenceOfHSequenceOfPnt_delNode)
    Clear = _swig_new_instance_method(_ProjLib.ProjLib_SequenceOfHSequenceOfPnt_Clear)
    Assign = _swig_new_instance_method(_ProjLib.ProjLib_SequenceOfHSequenceOfPnt_Assign)
    Set = _swig_new_instance_method(_ProjLib.ProjLib_SequenceOfHSequenceOfPnt_Set)
    Remove = _swig_new_instance_method(_ProjLib.ProjLib_SequenceOfHSequenceOfPnt_Remove)
    Append = _swig_new_instance_method(_ProjLib.ProjLib_SequenceOfHSequenceOfPnt_Append)
    Prepend = _swig_new_instance_method(_ProjLib.ProjLib_SequenceOfHSequenceOfPnt_Prepend)
    InsertBefore = _swig_new_instance_method(_ProjLib.ProjLib_SequenceOfHSequenceOfPnt_InsertBefore)
    InsertAfter = _swig_new_instance_method(_ProjLib.ProjLib_SequenceOfHSequenceOfPnt_InsertAfter)
    Split = _swig_new_instance_method(_ProjLib.ProjLib_SequenceOfHSequenceOfPnt_Split)
    First = _swig_new_instance_method(_ProjLib.ProjLib_SequenceOfHSequenceOfPnt_First)
    ChangeFirst = _swig_new_instance_method(_ProjLib.ProjLib_SequenceOfHSequenceOfPnt_ChangeFirst)
    Last = _swig_new_instance_method(_ProjLib.ProjLib_SequenceOfHSequenceOfPnt_Last)
    ChangeLast = _swig_new_instance_method(_ProjLib.ProjLib_SequenceOfHSequenceOfPnt_ChangeLast)
    Value = _swig_new_instance_method(_ProjLib.ProjLib_SequenceOfHSequenceOfPnt_Value)
    ChangeValue = _swig_new_instance_method(_ProjLib.ProjLib_SequenceOfHSequenceOfPnt_ChangeValue)
    __call__ = _swig_new_instance_method(_ProjLib.ProjLib_SequenceOfHSequenceOfPnt___call__)
    SetValue = _swig_new_instance_method(_ProjLib.ProjLib_SequenceOfHSequenceOfPnt_SetValue)
    __swig_destroy__ = _ProjLib.delete_ProjLib_SequenceOfHSequenceOfPnt

# Register ProjLib_SequenceOfHSequenceOfPnt in _ProjLib:
_ProjLib.ProjLib_SequenceOfHSequenceOfPnt_swigregister(ProjLib_SequenceOfHSequenceOfPnt)
ProjLib_SequenceOfHSequenceOfPnt_delNode = _ProjLib.ProjLib_SequenceOfHSequenceOfPnt_delNode

class projlib(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    IsAnaSurf = _swig_new_static_method(_ProjLib.projlib_IsAnaSurf)
    MakePCurveOfType = _swig_new_static_method(_ProjLib.projlib_MakePCurveOfType)
    Project = _swig_new_static_method(_ProjLib.projlib_Project)

    __repr__ = _dumps_object


    def __init__(self):
        _ProjLib.projlib_swiginit(self, _ProjLib.new_projlib())
    __swig_destroy__ = _ProjLib.delete_projlib

# Register projlib in _ProjLib:
_ProjLib.projlib_swigregister(projlib)
projlib_IsAnaSurf = _ProjLib.projlib_IsAnaSurf
projlib_MakePCurveOfType = _ProjLib.projlib_MakePCurveOfType
projlib_Project = _ProjLib.projlib_Project

class ProjLib_CompProjectedCurve(OCC.Core.Adaptor2d.Adaptor2d_Curve2d):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Bounds = _swig_new_instance_method(_ProjLib.ProjLib_CompProjectedCurve_Bounds)
    GetCurve = _swig_new_instance_method(_ProjLib.ProjLib_CompProjectedCurve_GetCurve)
    GetSequence = _swig_new_instance_method(_ProjLib.ProjLib_CompProjectedCurve_GetSequence)
    GetSurface = _swig_new_instance_method(_ProjLib.ProjLib_CompProjectedCurve_GetSurface)
    GetTolerance = _swig_new_instance_method(_ProjLib.ProjLib_CompProjectedCurve_GetTolerance)
    Init = _swig_new_instance_method(_ProjLib.ProjLib_CompProjectedCurve_Init)
    IsSinglePnt = _swig_new_instance_method(_ProjLib.ProjLib_CompProjectedCurve_IsSinglePnt)
    IsUIso = _swig_new_instance_method(_ProjLib.ProjLib_CompProjectedCurve_IsUIso)
    IsVIso = _swig_new_instance_method(_ProjLib.ProjLib_CompProjectedCurve_IsVIso)
    Load = _swig_new_instance_method(_ProjLib.ProjLib_CompProjectedCurve_Load)
    MaxDistance = _swig_new_instance_method(_ProjLib.ProjLib_CompProjectedCurve_MaxDistance)
    NbCurves = _swig_new_instance_method(_ProjLib.ProjLib_CompProjectedCurve_NbCurves)

    def __init__(self, *args):
        r"""
        :rtype: None* try to find all solutions
        	:param S:
        	:type S: Adaptor3d_HSurface
        	:param C:
        	:type C: Adaptor3d_HCurve
        	:param TolU:
        	:type TolU: float
        	:param TolV:
        	:type TolV: float
        	:rtype: None* this constructor tries to optimize the search using the assumption that maximum distance between surface and curve less or equal then MaxDist. if MaxDist < 0 then algorithm works as above.
        	:param S:
        	:type S: Adaptor3d_HSurface
        	:param C:
        	:type C: Adaptor3d_HCurve
        	:param TolU:
        	:type TolU: float
        	:param TolV:
        	:type TolV: float
        	:param MaxDist:
        	:type MaxDist: float
        	:rtype: None
        """
        _ProjLib.ProjLib_CompProjectedCurve_swiginit(self, _ProjLib.new_ProjLib_CompProjectedCurve(*args))

    __repr__ = _dumps_object

    __swig_destroy__ = _ProjLib.delete_ProjLib_CompProjectedCurve

# Register ProjLib_CompProjectedCurve in _ProjLib:
_ProjLib.ProjLib_CompProjectedCurve_swigregister(ProjLib_CompProjectedCurve)

class ProjLib_ComputeApprox(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    BSpline = _swig_new_instance_method(_ProjLib.ProjLib_ComputeApprox_BSpline)
    Bezier = _swig_new_instance_method(_ProjLib.ProjLib_ComputeApprox_Bezier)
    Perform = _swig_new_instance_method(_ProjLib.ProjLib_ComputeApprox_Perform)

    def __init__(self, *args):
        r"""
        * Empty constructor, it only sets some initial values for class fields.
        	:rtype: None* <Tol> is the tolerance with which the approximation is performed. Other parameters for approximation have default values.
        	:param C:
        	:type C: Adaptor3d_HCurve
        	:param S:
        	:type S: Adaptor3d_HSurface
        	:param Tol:
        	:type Tol: float
        	:rtype: None
        """
        _ProjLib.ProjLib_ComputeApprox_swiginit(self, _ProjLib.new_ProjLib_ComputeApprox(*args))
    SetBndPnt = _swig_new_instance_method(_ProjLib.ProjLib_ComputeApprox_SetBndPnt)
    SetDegree = _swig_new_instance_method(_ProjLib.ProjLib_ComputeApprox_SetDegree)
    SetMaxSegments = _swig_new_instance_method(_ProjLib.ProjLib_ComputeApprox_SetMaxSegments)
    SetTolerance = _swig_new_instance_method(_ProjLib.ProjLib_ComputeApprox_SetTolerance)
    Tolerance = _swig_new_instance_method(_ProjLib.ProjLib_ComputeApprox_Tolerance)

    __repr__ = _dumps_object

    __swig_destroy__ = _ProjLib.delete_ProjLib_ComputeApprox

# Register ProjLib_ComputeApprox in _ProjLib:
_ProjLib.ProjLib_ComputeApprox_swigregister(ProjLib_ComputeApprox)

class ProjLib_ComputeApproxOnPolarSurface(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    BSpline = _swig_new_instance_method(_ProjLib.ProjLib_ComputeApproxOnPolarSurface_BSpline)
    BuildInitialCurve2d = _swig_new_instance_method(_ProjLib.ProjLib_ComputeApproxOnPolarSurface_BuildInitialCurve2d)
    Curve2d = _swig_new_instance_method(_ProjLib.ProjLib_ComputeApproxOnPolarSurface_Curve2d)
    IsDone = _swig_new_instance_method(_ProjLib.ProjLib_ComputeApproxOnPolarSurface_IsDone)
    Perform = _swig_new_instance_method(_ProjLib.ProjLib_ComputeApproxOnPolarSurface_Perform)

    def __init__(self, *args):
        r"""
        * Empty constructor, it only sets some initial values for class fields.
        	:rtype: None* Constructor, which performs projecting.
        	:param C:
        	:type C: Adaptor3d_HCurve
        	:param S:
        	:type S: Adaptor3d_HSurface
        	:param Tol: default value is 1.0e-4
        	:type Tol: float
        	:rtype: None* Constructor, which performs projecting, using initial curve 2d InitCurve2d, which is any rough approximation of result curve. Parameter Tol is 3d tolerance of approximation.
        	:param InitCurve2d:
        	:type InitCurve2d: Adaptor2d_HCurve2d
        	:param C:
        	:type C: Adaptor3d_HCurve
        	:param S:
        	:type S: Adaptor3d_HSurface
        	:param Tol:
        	:type Tol: float
        	:rtype: None* Constructor, which performs projecting, using two initial curves 2d: InitCurve2d and InitCurve2dBis that are any rough approximations of result curves. This constructor is used to get two pcurves for seem edge. Parameter Tol is 3d tolerance of approximation.
        	:param InitCurve2d:
        	:type InitCurve2d: Adaptor2d_HCurve2d
        	:param InitCurve2dBis:
        	:type InitCurve2dBis: Adaptor2d_HCurve2d
        	:param C:
        	:type C: Adaptor3d_HCurve
        	:param S:
        	:type S: Adaptor3d_HSurface
        	:param Tol:
        	:type Tol: float
        	:rtype: None
        """
        _ProjLib.ProjLib_ComputeApproxOnPolarSurface_swiginit(self, _ProjLib.new_ProjLib_ComputeApproxOnPolarSurface(*args))
    ProjectUsingInitialCurve2d = _swig_new_instance_method(_ProjLib.ProjLib_ComputeApproxOnPolarSurface_ProjectUsingInitialCurve2d)
    SetBndPnt = _swig_new_instance_method(_ProjLib.ProjLib_ComputeApproxOnPolarSurface_SetBndPnt)
    SetDegree = _swig_new_instance_method(_ProjLib.ProjLib_ComputeApproxOnPolarSurface_SetDegree)
    SetMaxDist = _swig_new_instance_method(_ProjLib.ProjLib_ComputeApproxOnPolarSurface_SetMaxDist)
    SetMaxSegments = _swig_new_instance_method(_ProjLib.ProjLib_ComputeApproxOnPolarSurface_SetMaxSegments)
    SetTolerance = _swig_new_instance_method(_ProjLib.ProjLib_ComputeApproxOnPolarSurface_SetTolerance)
    Tolerance = _swig_new_instance_method(_ProjLib.ProjLib_ComputeApproxOnPolarSurface_Tolerance)

    __repr__ = _dumps_object

    __swig_destroy__ = _ProjLib.delete_ProjLib_ComputeApproxOnPolarSurface

# Register ProjLib_ComputeApproxOnPolarSurface in _ProjLib:
_ProjLib.ProjLib_ComputeApproxOnPolarSurface_swigregister(ProjLib_ComputeApproxOnPolarSurface)

class ProjLib_HCompProjectedCurve(OCC.Core.Adaptor2d.Adaptor2d_HCurve2d):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    ChangeCurve2d = _swig_new_instance_method(_ProjLib.ProjLib_HCompProjectedCurve_ChangeCurve2d)

    def __init__(self, *args):
        r"""
        * Creates an empty GenHCurve2d.
        	:rtype: None* Creates a GenHCurve2d from a Curve
        	:param C:
        	:type C: ProjLib_CompProjectedCurve
        	:rtype: None
        """
        _ProjLib.ProjLib_HCompProjectedCurve_swiginit(self, _ProjLib.new_ProjLib_HCompProjectedCurve(*args))
    Set = _swig_new_instance_method(_ProjLib.ProjLib_HCompProjectedCurve_Set)


    @staticmethod
    def DownCast(t):
      return Handle_ProjLib_HCompProjectedCurve_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _ProjLib.delete_ProjLib_HCompProjectedCurve

# Register ProjLib_HCompProjectedCurve in _ProjLib:
_ProjLib.ProjLib_HCompProjectedCurve_swigregister(ProjLib_HCompProjectedCurve)

class ProjLib_HProjectedCurve(OCC.Core.Adaptor2d.Adaptor2d_HCurve2d):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    ChangeCurve2d = _swig_new_instance_method(_ProjLib.ProjLib_HProjectedCurve_ChangeCurve2d)

    def __init__(self, *args):
        r"""
        * Creates an empty GenHCurve2d.
        	:rtype: None* Creates a GenHCurve2d from a Curve
        	:param C:
        	:type C: ProjLib_ProjectedCurve
        	:rtype: None
        """
        _ProjLib.ProjLib_HProjectedCurve_swiginit(self, _ProjLib.new_ProjLib_HProjectedCurve(*args))
    Set = _swig_new_instance_method(_ProjLib.ProjLib_HProjectedCurve_Set)


    @staticmethod
    def DownCast(t):
      return Handle_ProjLib_HProjectedCurve_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _ProjLib.delete_ProjLib_HProjectedCurve

# Register ProjLib_HProjectedCurve in _ProjLib:
_ProjLib.ProjLib_HProjectedCurve_swigregister(ProjLib_HProjectedCurve)

class ProjLib_PrjFunc(OCC.Core.math.math_FunctionSetWithDerivatives):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :param C:
        	:type C: Adaptor3d_CurvePtr
        	:param FixVal:
        	:type FixVal: float
        	:param S:
        	:type S: Adaptor3d_SurfacePtr
        	:param Fix:
        	:type Fix: int
        	:rtype: None
        """
        _ProjLib.ProjLib_PrjFunc_swiginit(self, _ProjLib.new_ProjLib_PrjFunc(*args))
    Solution = _swig_new_instance_method(_ProjLib.ProjLib_PrjFunc_Solution)

    __repr__ = _dumps_object

    __swig_destroy__ = _ProjLib.delete_ProjLib_PrjFunc

# Register ProjLib_PrjFunc in _ProjLib:
_ProjLib.ProjLib_PrjFunc_swigregister(ProjLib_PrjFunc)

class ProjLib_PrjResolve(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    IsDone = _swig_new_instance_method(_ProjLib.ProjLib_PrjResolve_IsDone)
    Perform = _swig_new_instance_method(_ProjLib.ProjLib_PrjResolve_Perform)

    def __init__(self, *args):
        r"""
        :param C:
        	:type C: Adaptor3d_Curve
        	:param S:
        	:type S: Adaptor3d_Surface
        	:param Fix:
        	:type Fix: int
        	:rtype: None
        """
        _ProjLib.ProjLib_PrjResolve_swiginit(self, _ProjLib.new_ProjLib_PrjResolve(*args))
    Solution = _swig_new_instance_method(_ProjLib.ProjLib_PrjResolve_Solution)

    __repr__ = _dumps_object

    __swig_destroy__ = _ProjLib.delete_ProjLib_PrjResolve

# Register ProjLib_PrjResolve in _ProjLib:
_ProjLib.ProjLib_PrjResolve_swigregister(ProjLib_PrjResolve)

class ProjLib_ProjectOnPlane(OCC.Core.Adaptor3d.Adaptor3d_Curve):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    GetCurve = _swig_new_instance_method(_ProjLib.ProjLib_ProjectOnPlane_GetCurve)
    GetDirection = _swig_new_instance_method(_ProjLib.ProjLib_ProjectOnPlane_GetDirection)
    GetPlane = _swig_new_instance_method(_ProjLib.ProjLib_ProjectOnPlane_GetPlane)
    GetResult = _swig_new_instance_method(_ProjLib.ProjLib_ProjectOnPlane_GetResult)
    Load = _swig_new_instance_method(_ProjLib.ProjLib_ProjectOnPlane_Load)

    def __init__(self, *args):
        r"""
        * Empty constructor.
        	:rtype: None* The projection will be normal to the Plane defined by the Ax3 <Pl>.
        	:param Pl:
        	:type Pl: gp_Ax3
        	:rtype: None* The projection will be along the direction <D> on the plane defined by the Ax3 <Pl>. raises if the direction <D> is parallel to the plane <Pl>.
        	:param Pl:
        	:type Pl: gp_Ax3
        	:param D:
        	:type D: gp_Dir
        	:rtype: None
        """
        _ProjLib.ProjLib_ProjectOnPlane_swiginit(self, _ProjLib.new_ProjLib_ProjectOnPlane(*args))

    __repr__ = _dumps_object

    __swig_destroy__ = _ProjLib.delete_ProjLib_ProjectOnPlane

# Register ProjLib_ProjectOnPlane in _ProjLib:
_ProjLib.ProjLib_ProjectOnPlane_swigregister(ProjLib_ProjectOnPlane)

class ProjLib_ProjectOnSurface(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    BSpline = _swig_new_instance_method(_ProjLib.ProjLib_ProjectOnSurface_BSpline)
    IsDone = _swig_new_instance_method(_ProjLib.ProjLib_ProjectOnSurface_IsDone)

    def __init__(self, *args):
        r"""
        * Create an empty projector.
        	:rtype: None* Create a projector normaly to the surface <S>.
        	:param S:
        	:type S: Adaptor3d_HSurface
        	:rtype: None
        """
        _ProjLib.ProjLib_ProjectOnSurface_swiginit(self, _ProjLib.new_ProjLib_ProjectOnSurface(*args))

    __repr__ = _dumps_object

    __swig_destroy__ = _ProjLib.delete_ProjLib_ProjectOnSurface

# Register ProjLib_ProjectOnSurface in _ProjLib:
_ProjLib.ProjLib_ProjectOnSurface_swigregister(ProjLib_ProjectOnSurface)

class ProjLib_ProjectedCurve(OCC.Core.Adaptor2d.Adaptor2d_Curve2d):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    GetCurve = _swig_new_instance_method(_ProjLib.ProjLib_ProjectedCurve_GetCurve)
    GetSurface = _swig_new_instance_method(_ProjLib.ProjLib_ProjectedCurve_GetSurface)
    GetTolerance = _swig_new_instance_method(_ProjLib.ProjLib_ProjectedCurve_GetTolerance)
    Perform = _swig_new_instance_method(_ProjLib.ProjLib_ProjectedCurve_Perform)

    def __init__(self, *args):
        r"""
        * Empty constructor, it only sets some initial values for class fields.
        	:rtype: None* Constructor with initialisation field mySurface
        	:param S:
        	:type S: Adaptor3d_HSurface
        	:rtype: None* Constructor, which performs projecting. If projecting uses approximation, default parameters are used, in particular, 3d tolerance of approximation is Precision::Confusion()
        	:param S:
        	:type S: Adaptor3d_HSurface
        	:param C:
        	:type C: Adaptor3d_HCurve
        	:rtype: None* Constructor, which performs projecting. If projecting uses approximation, 3d tolerance is Tol, default parameters are used,
        	:param S:
        	:type S: Adaptor3d_HSurface
        	:param C:
        	:type C: Adaptor3d_HCurve
        	:param Tol:
        	:type Tol: float
        	:rtype: None
        """
        _ProjLib.ProjLib_ProjectedCurve_swiginit(self, _ProjLib.new_ProjLib_ProjectedCurve(*args))
    SetBndPnt = _swig_new_instance_method(_ProjLib.ProjLib_ProjectedCurve_SetBndPnt)
    SetDegree = _swig_new_instance_method(_ProjLib.ProjLib_ProjectedCurve_SetDegree)
    SetMaxDist = _swig_new_instance_method(_ProjLib.ProjLib_ProjectedCurve_SetMaxDist)
    SetMaxSegments = _swig_new_instance_method(_ProjLib.ProjLib_ProjectedCurve_SetMaxSegments)

    __repr__ = _dumps_object

    __swig_destroy__ = _ProjLib.delete_ProjLib_ProjectedCurve

# Register ProjLib_ProjectedCurve in _ProjLib:
_ProjLib.ProjLib_ProjectedCurve_swigregister(ProjLib_ProjectedCurve)

class ProjLib_Projector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    BSpline = _swig_new_instance_method(_ProjLib.ProjLib_Projector_BSpline)
    Bezier = _swig_new_instance_method(_ProjLib.ProjLib_Projector_Bezier)
    Circle = _swig_new_instance_method(_ProjLib.ProjLib_Projector_Circle)
    Done = _swig_new_instance_method(_ProjLib.ProjLib_Projector_Done)
    Ellipse = _swig_new_instance_method(_ProjLib.ProjLib_Projector_Ellipse)
    GetType = _swig_new_instance_method(_ProjLib.ProjLib_Projector_GetType)
    Hyperbola = _swig_new_instance_method(_ProjLib.ProjLib_Projector_Hyperbola)
    IsDone = _swig_new_instance_method(_ProjLib.ProjLib_Projector_IsDone)
    IsPeriodic = _swig_new_instance_method(_ProjLib.ProjLib_Projector_IsPeriodic)
    Line = _swig_new_instance_method(_ProjLib.ProjLib_Projector_Line)
    Parabola = _swig_new_instance_method(_ProjLib.ProjLib_Projector_Parabola)

    def __init__(self, *args):
        r"""
        * Sets the type to OtherCurve
        	:rtype: None
        """
        _ProjLib.ProjLib_Projector_swiginit(self, _ProjLib.new_ProjLib_Projector(*args))
    Project = _swig_new_instance_method(_ProjLib.ProjLib_Projector_Project)
    SetBSpline = _swig_new_instance_method(_ProjLib.ProjLib_Projector_SetBSpline)
    SetBezier = _swig_new_instance_method(_ProjLib.ProjLib_Projector_SetBezier)
    SetPeriodic = _swig_new_instance_method(_ProjLib.ProjLib_Projector_SetPeriodic)
    SetType = _swig_new_instance_method(_ProjLib.ProjLib_Projector_SetType)
    UFrame = _swig_new_instance_method(_ProjLib.ProjLib_Projector_UFrame)
    VFrame = _swig_new_instance_method(_ProjLib.ProjLib_Projector_VFrame)

    __repr__ = _dumps_object

    __swig_destroy__ = _ProjLib.delete_ProjLib_Projector

# Register ProjLib_Projector in _ProjLib:
_ProjLib.ProjLib_Projector_swigregister(ProjLib_Projector)

class ProjLib_Cone(ProjLib_Projector):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Init = _swig_new_instance_method(_ProjLib.ProjLib_Cone_Init)

    def __init__(self, *args):
        r"""
        * Undefined projection.
        	:rtype: None* Projection on the cone <Co>.
        	:param Co:
        	:type Co: gp_Cone
        	:rtype: None* Projection of the line <L> on the cone <Co>.
        	:param Co:
        	:type Co: gp_Cone
        	:param L:
        	:type L: gp_Lin
        	:rtype: None* Projection of the circle <C> on the cone <Co>.
        	:param Co:
        	:type Co: gp_Cone
        	:param C:
        	:type C: gp_Circ
        	:rtype: None
        """
        _ProjLib.ProjLib_Cone_swiginit(self, _ProjLib.new_ProjLib_Cone(*args))
    Project = _swig_new_instance_method(_ProjLib.ProjLib_Cone_Project)

    __repr__ = _dumps_object

    __swig_destroy__ = _ProjLib.delete_ProjLib_Cone

# Register ProjLib_Cone in _ProjLib:
_ProjLib.ProjLib_Cone_swigregister(ProjLib_Cone)

class ProjLib_Cylinder(ProjLib_Projector):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Init = _swig_new_instance_method(_ProjLib.ProjLib_Cylinder_Init)

    def __init__(self, *args):
        r"""
        * Undefined projection.
        	:rtype: None* Projection on the cylinder <Cyl>.
        	:param Cyl:
        	:type Cyl: gp_Cylinder
        	:rtype: None* Projection of the line <L> on the cylinder <Cyl>.
        	:param Cyl:
        	:type Cyl: gp_Cylinder
        	:param L:
        	:type L: gp_Lin
        	:rtype: None* Projection of the circle <C> on the cylinder <Cyl>.
        	:param Cyl:
        	:type Cyl: gp_Cylinder
        	:param C:
        	:type C: gp_Circ
        	:rtype: None* Projection of the ellipse <E> on the cylinder <Cyl>.
        	:param Cyl:
        	:type Cyl: gp_Cylinder
        	:param E:
        	:type E: gp_Elips
        	:rtype: None
        """
        _ProjLib.ProjLib_Cylinder_swiginit(self, _ProjLib.new_ProjLib_Cylinder(*args))
    Project = _swig_new_instance_method(_ProjLib.ProjLib_Cylinder_Project)

    __repr__ = _dumps_object

    __swig_destroy__ = _ProjLib.delete_ProjLib_Cylinder

# Register ProjLib_Cylinder in _ProjLib:
_ProjLib.ProjLib_Cylinder_swigregister(ProjLib_Cylinder)

class ProjLib_Plane(ProjLib_Projector):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Init = _swig_new_instance_method(_ProjLib.ProjLib_Plane_Init)

    def __init__(self, *args):
        r"""
        * Undefined projection.
        	:rtype: None* Projection on the plane <Pl>.
        	:param Pl:
        	:type Pl: gp_Pln
        	:rtype: None* Projection of the line <L> on the plane <Pl>.
        	:param Pl:
        	:type Pl: gp_Pln
        	:param L:
        	:type L: gp_Lin
        	:rtype: None* Projection of the circle <C> on the plane <Pl>.
        	:param Pl:
        	:type Pl: gp_Pln
        	:param C:
        	:type C: gp_Circ
        	:rtype: None* Projection of the ellipse <E> on the plane <Pl>.
        	:param Pl:
        	:type Pl: gp_Pln
        	:param E:
        	:type E: gp_Elips
        	:rtype: None* Projection of the parabola <P> on the plane <Pl>.
        	:param Pl:
        	:type Pl: gp_Pln
        	:param P:
        	:type P: gp_Parab
        	:rtype: None* Projection of the hyperbola <H> on the plane <Pl>.
        	:param Pl:
        	:type Pl: gp_Pln
        	:param H:
        	:type H: gp_Hypr
        	:rtype: None
        """
        _ProjLib.ProjLib_Plane_swiginit(self, _ProjLib.new_ProjLib_Plane(*args))
    Project = _swig_new_instance_method(_ProjLib.ProjLib_Plane_Project)

    __repr__ = _dumps_object

    __swig_destroy__ = _ProjLib.delete_ProjLib_Plane

# Register ProjLib_Plane in _ProjLib:
_ProjLib.ProjLib_Plane_swigregister(ProjLib_Plane)

class ProjLib_Sphere(ProjLib_Projector):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Init = _swig_new_instance_method(_ProjLib.ProjLib_Sphere_Init)

    def __init__(self, *args):
        r"""
        * Undefined projection.
        	:rtype: None* Projection on the sphere <Sp>.
        	:param Sp:
        	:type Sp: gp_Sphere
        	:rtype: None* Projection of the circle <C> on the sphere <Sp>.
        	:param Sp:
        	:type Sp: gp_Sphere
        	:param C:
        	:type C: gp_Circ
        	:rtype: None
        """
        _ProjLib.ProjLib_Sphere_swiginit(self, _ProjLib.new_ProjLib_Sphere(*args))
    Project = _swig_new_instance_method(_ProjLib.ProjLib_Sphere_Project)
    SetInBounds = _swig_new_instance_method(_ProjLib.ProjLib_Sphere_SetInBounds)

    __repr__ = _dumps_object

    __swig_destroy__ = _ProjLib.delete_ProjLib_Sphere

# Register ProjLib_Sphere in _ProjLib:
_ProjLib.ProjLib_Sphere_swigregister(ProjLib_Sphere)

class ProjLib_Torus(ProjLib_Projector):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Init = _swig_new_instance_method(_ProjLib.ProjLib_Torus_Init)

    def __init__(self, *args):
        r"""
        * Undefined projection.
        	:rtype: None* Projection on the torus <To>.
        	:param To:
        	:type To: gp_Torus
        	:rtype: None* Projection of the circle <C> on the torus <To>.
        	:param To:
        	:type To: gp_Torus
        	:param C:
        	:type C: gp_Circ
        	:rtype: None
        """
        _ProjLib.ProjLib_Torus_swiginit(self, _ProjLib.new_ProjLib_Torus(*args))
    Project = _swig_new_instance_method(_ProjLib.ProjLib_Torus_Project)

    __repr__ = _dumps_object

    __swig_destroy__ = _ProjLib.delete_ProjLib_Torus

# Register ProjLib_Torus in _ProjLib:
_ProjLib.ProjLib_Torus_swigregister(ProjLib_Torus)

class ProjLib_HSequenceOfHSequenceOfPnt(ProjLib_SequenceOfHSequenceOfPnt, OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _ProjLib.ProjLib_HSequenceOfHSequenceOfPnt_swiginit(self, _ProjLib.new_ProjLib_HSequenceOfHSequenceOfPnt(*args))
    Sequence = _swig_new_instance_method(_ProjLib.ProjLib_HSequenceOfHSequenceOfPnt_Sequence)
    Append = _swig_new_instance_method(_ProjLib.ProjLib_HSequenceOfHSequenceOfPnt_Append)
    ChangeSequence = _swig_new_instance_method(_ProjLib.ProjLib_HSequenceOfHSequenceOfPnt_ChangeSequence)


    @staticmethod
    def DownCast(t):
      return Handle_ProjLib_HSequenceOfHSequenceOfPnt_DownCast(t)

    __swig_destroy__ = _ProjLib.delete_ProjLib_HSequenceOfHSequenceOfPnt

# Register ProjLib_HSequenceOfHSequenceOfPnt in _ProjLib:
_ProjLib.ProjLib_HSequenceOfHSequenceOfPnt_swigregister(ProjLib_HSequenceOfHSequenceOfPnt)



