# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
IntAna module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_intana.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _IntAna
else:
    import _IntAna

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _IntAna.SWIG_PyInstanceMethod_New
_swig_new_static_method = _IntAna.SWIG_PyStaticMethod_New

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
    __swig_destroy__ = _IntAna.delete_SwigPyIterator
    value = _swig_new_instance_method(_IntAna.SwigPyIterator_value)
    incr = _swig_new_instance_method(_IntAna.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_IntAna.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_IntAna.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_IntAna.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_IntAna.SwigPyIterator_copy)
    next = _swig_new_instance_method(_IntAna.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_IntAna.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_IntAna.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_IntAna.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_IntAna.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_IntAna.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_IntAna.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_IntAna.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_IntAna.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_IntAna.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _IntAna:
_IntAna.SwigPyIterator_swigregister(SwigPyIterator)


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
import OCC.Core.gp
import OCC.Core.TColStd
import OCC.Core.TCollection
IntAna_Point = _IntAna.IntAna_Point
IntAna_Line = _IntAna.IntAna_Line
IntAna_Circle = _IntAna.IntAna_Circle
IntAna_PointAndCircle = _IntAna.IntAna_PointAndCircle
IntAna_Ellipse = _IntAna.IntAna_Ellipse
IntAna_Parabola = _IntAna.IntAna_Parabola
IntAna_Hyperbola = _IntAna.IntAna_Hyperbola
IntAna_Empty = _IntAna.IntAna_Empty
IntAna_Same = _IntAna.IntAna_Same
IntAna_NoGeometricSolution = _IntAna.IntAna_NoGeometricSolution
class IntAna_ListOfCurve(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_IntAna.IntAna_ListOfCurve_begin)
    end = _swig_new_instance_method(_IntAna.IntAna_ListOfCurve_end)
    cbegin = _swig_new_instance_method(_IntAna.IntAna_ListOfCurve_cbegin)
    cend = _swig_new_instance_method(_IntAna.IntAna_ListOfCurve_cend)

    def __init__(self, *args):
        _IntAna.IntAna_ListOfCurve_swiginit(self, _IntAna.new_IntAna_ListOfCurve(*args))
    Size = _swig_new_instance_method(_IntAna.IntAna_ListOfCurve_Size)
    Assign = _swig_new_instance_method(_IntAna.IntAna_ListOfCurve_Assign)
    Set = _swig_new_instance_method(_IntAna.IntAna_ListOfCurve_Set)
    Clear = _swig_new_instance_method(_IntAna.IntAna_ListOfCurve_Clear)
    First = _swig_new_instance_method(_IntAna.IntAna_ListOfCurve_First)
    Last = _swig_new_instance_method(_IntAna.IntAna_ListOfCurve_Last)
    Append = _swig_new_instance_method(_IntAna.IntAna_ListOfCurve_Append)
    Prepend = _swig_new_instance_method(_IntAna.IntAna_ListOfCurve_Prepend)
    RemoveFirst = _swig_new_instance_method(_IntAna.IntAna_ListOfCurve_RemoveFirst)
    Remove = _swig_new_instance_method(_IntAna.IntAna_ListOfCurve_Remove)
    InsertBefore = _swig_new_instance_method(_IntAna.IntAna_ListOfCurve_InsertBefore)
    InsertAfter = _swig_new_instance_method(_IntAna.IntAna_ListOfCurve_InsertAfter)
    Reverse = _swig_new_instance_method(_IntAna.IntAna_ListOfCurve_Reverse)
    __swig_destroy__ = _IntAna.delete_IntAna_ListOfCurve

# Register IntAna_ListOfCurve in _IntAna:
_IntAna.IntAna_ListOfCurve_swigregister(IntAna_ListOfCurve)

class IntAna_ListIteratorOfListOfCurve(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _IntAna.IntAna_ListIteratorOfListOfCurve_swiginit(self, _IntAna.new_IntAna_ListIteratorOfListOfCurve(*args))
    More = _swig_new_instance_method(_IntAna.IntAna_ListIteratorOfListOfCurve_More)
    Next = _swig_new_instance_method(_IntAna.IntAna_ListIteratorOfListOfCurve_Next)
    Value = _swig_new_instance_method(_IntAna.IntAna_ListIteratorOfListOfCurve_Value)
    ChangeValue = _swig_new_instance_method(_IntAna.IntAna_ListIteratorOfListOfCurve_ChangeValue)
    __swig_destroy__ = _IntAna.delete_IntAna_ListIteratorOfListOfCurve

# Register IntAna_ListIteratorOfListOfCurve in _IntAna:
_IntAna.IntAna_ListIteratorOfListOfCurve_swigregister(IntAna_ListIteratorOfListOfCurve)

class IntAna_Curve(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    D1u = _swig_new_instance_method(_IntAna.IntAna_Curve_D1u)
    Domain = _swig_new_instance_method(_IntAna.IntAna_Curve_Domain)
    FindParameter = _swig_new_instance_method(_IntAna.IntAna_Curve_FindParameter)

    def __init__(self, *args):
        r"""
        * Empty Constructor
        	:rtype: None
        """
        _IntAna.IntAna_Curve_swiginit(self, _IntAna.new_IntAna_Curve(*args))
    IsConstant = _swig_new_instance_method(_IntAna.IntAna_Curve_IsConstant)
    IsFirstOpen = _swig_new_instance_method(_IntAna.IntAna_Curve_IsFirstOpen)
    IsLastOpen = _swig_new_instance_method(_IntAna.IntAna_Curve_IsLastOpen)
    IsOpen = _swig_new_instance_method(_IntAna.IntAna_Curve_IsOpen)
    SetConeQuadValues = _swig_new_instance_method(_IntAna.IntAna_Curve_SetConeQuadValues)
    SetCylinderQuadValues = _swig_new_instance_method(_IntAna.IntAna_Curve_SetCylinderQuadValues)
    SetDomain = _swig_new_instance_method(_IntAna.IntAna_Curve_SetDomain)
    SetIsFirstOpen = _swig_new_instance_method(_IntAna.IntAna_Curve_SetIsFirstOpen)
    SetIsLastOpen = _swig_new_instance_method(_IntAna.IntAna_Curve_SetIsLastOpen)
    Value = _swig_new_instance_method(_IntAna.IntAna_Curve_Value)

    __repr__ = _dumps_object

    __swig_destroy__ = _IntAna.delete_IntAna_Curve

# Register IntAna_Curve in _IntAna:
_IntAna.IntAna_Curve_swigregister(IntAna_Curve)

class IntAna_Int3Pln(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :rtype: None* Determination of the intersection point between 3 planes.
        	:param P1:
        	:type P1: gp_Pln
        	:param P2:
        	:type P2: gp_Pln
        	:param P3:
        	:type P3: gp_Pln
        	:rtype: None
        """
        _IntAna.IntAna_Int3Pln_swiginit(self, _IntAna.new_IntAna_Int3Pln(*args))
    IsDone = _swig_new_instance_method(_IntAna.IntAna_Int3Pln_IsDone)
    IsEmpty = _swig_new_instance_method(_IntAna.IntAna_Int3Pln_IsEmpty)
    Perform = _swig_new_instance_method(_IntAna.IntAna_Int3Pln_Perform)
    Value = _swig_new_instance_method(_IntAna.IntAna_Int3Pln_Value)

    __repr__ = _dumps_object

    __swig_destroy__ = _IntAna.delete_IntAna_Int3Pln

# Register IntAna_Int3Pln in _IntAna:
_IntAna.IntAna_Int3Pln_swigregister(IntAna_Int3Pln)

class IntAna_IntConicQuad(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Empty constructor.
        	:rtype: None* Creates the intersection between a line and a quadric.
        	:param L:
        	:type L: gp_Lin
        	:param Q:
        	:type Q: IntAna_Quadric
        	:rtype: None* Creates the intersection between a circle and a quadric.
        	:param C:
        	:type C: gp_Circ
        	:param Q:
        	:type Q: IntAna_Quadric
        	:rtype: None* Creates the intersection between an ellipse and a quadric.
        	:param E:
        	:type E: gp_Elips
        	:param Q:
        	:type Q: IntAna_Quadric
        	:rtype: None* Creates the intersection between a parabola and a quadric.
        	:param P:
        	:type P: gp_Parab
        	:param Q:
        	:type Q: IntAna_Quadric
        	:rtype: None* Creates the intersection between an hyperbola and a quadric.
        	:param H:
        	:type H: gp_Hypr
        	:param Q:
        	:type Q: IntAna_Quadric
        	:rtype: None* Intersection between a line and a plane. Tolang is used to determine if the angle between two vectors is null. Tol is used to check the distance between line and plane on the distance <Len> from the origin of the line.
        	:param L:
        	:type L: gp_Lin
        	:param P:
        	:type P: gp_Pln
        	:param Tolang:
        	:type Tolang: float
        	:param Tol: default value is 0
        	:type Tol: float
        	:param Len: default value is 0
        	:type Len: float
        	:rtype: None* Intersection between a circle and a plane. Tolang is used to determine if the angle between two vectors is null. Tol is used to determine if a distance is null.
        	:param C:
        	:type C: gp_Circ
        	:param P:
        	:type P: gp_Pln
        	:param Tolang:
        	:type Tolang: float
        	:param Tol:
        	:type Tol: float
        	:rtype: None* Intersection between an ellipse and a plane. Tolang is used to determine if the angle between two vectors is null. Tol is used to determine if a distance is null.
        	:param E:
        	:type E: gp_Elips
        	:param P:
        	:type P: gp_Pln
        	:param Tolang:
        	:type Tolang: float
        	:param Tol:
        	:type Tol: float
        	:rtype: None* Intersection between a parabola and a plane. Tolang is used to determine if the angle between two vectors is null.
        	:param Pb:
        	:type Pb: gp_Parab
        	:param P:
        	:type P: gp_Pln
        	:param Tolang:
        	:type Tolang: float
        	:rtype: None* Intersection between an hyperbola and a plane. Tolang is used to determine if the angle between two vectors is null.
        	:param H:
        	:type H: gp_Hypr
        	:param P:
        	:type P: gp_Pln
        	:param Tolang:
        	:type Tolang: float
        	:rtype: None
        """
        _IntAna.IntAna_IntConicQuad_swiginit(self, _IntAna.new_IntAna_IntConicQuad(*args))
    IsDone = _swig_new_instance_method(_IntAna.IntAna_IntConicQuad_IsDone)
    IsInQuadric = _swig_new_instance_method(_IntAna.IntAna_IntConicQuad_IsInQuadric)
    IsParallel = _swig_new_instance_method(_IntAna.IntAna_IntConicQuad_IsParallel)
    NbPoints = _swig_new_instance_method(_IntAna.IntAna_IntConicQuad_NbPoints)
    ParamOnConic = _swig_new_instance_method(_IntAna.IntAna_IntConicQuad_ParamOnConic)
    Perform = _swig_new_instance_method(_IntAna.IntAna_IntConicQuad_Perform)
    Point = _swig_new_instance_method(_IntAna.IntAna_IntConicQuad_Point)

    __repr__ = _dumps_object

    __swig_destroy__ = _IntAna.delete_IntAna_IntConicQuad

# Register IntAna_IntConicQuad in _IntAna:
_IntAna.IntAna_IntConicQuad_swigregister(IntAna_IntConicQuad)

class IntAna_IntLinTorus(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :rtype: None* Creates the intersection between a line and a torus.
        	:param L:
        	:type L: gp_Lin
        	:param T:
        	:type T: gp_Torus
        	:rtype: None
        """
        _IntAna.IntAna_IntLinTorus_swiginit(self, _IntAna.new_IntAna_IntLinTorus(*args))
    IsDone = _swig_new_instance_method(_IntAna.IntAna_IntLinTorus_IsDone)
    NbPoints = _swig_new_instance_method(_IntAna.IntAna_IntLinTorus_NbPoints)
    ParamOnLine = _swig_new_instance_method(_IntAna.IntAna_IntLinTorus_ParamOnLine)
    ParamOnTorus = _swig_new_instance_method(_IntAna.IntAna_IntLinTorus_ParamOnTorus)
    Perform = _swig_new_instance_method(_IntAna.IntAna_IntLinTorus_Perform)
    Value = _swig_new_instance_method(_IntAna.IntAna_IntLinTorus_Value)

    __repr__ = _dumps_object

    __swig_destroy__ = _IntAna.delete_IntAna_IntLinTorus

# Register IntAna_IntLinTorus in _IntAna:
_IntAna.IntAna_IntLinTorus_swigregister(IntAna_IntLinTorus)

class IntAna_IntQuadQuad(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Curve = _swig_new_instance_method(_IntAna.IntAna_IntQuadQuad_Curve)
    HasNextCurve = _swig_new_instance_method(_IntAna.IntAna_IntQuadQuad_HasNextCurve)
    HasPreviousCurve = _swig_new_instance_method(_IntAna.IntAna_IntQuadQuad_HasPreviousCurve)
    IdenticalElements = _swig_new_instance_method(_IntAna.IntAna_IntQuadQuad_IdenticalElements)

    def __init__(self, *args):
        r"""
        * Empty Constructor
        	:rtype: None* Creates the intersection between a cylinder and a quadric . Tol est a definir plus precisemment.
        	:param C:
        	:type C: gp_Cylinder
        	:param Q:
        	:type Q: IntAna_Quadric
        	:param Tol:
        	:type Tol: float
        	:rtype: None* Creates the intersection between a cone and a quadric. Tol est a definir plus precisemment.
        	:param C:
        	:type C: gp_Cone
        	:param Q:
        	:type Q: IntAna_Quadric
        	:param Tol:
        	:type Tol: float
        	:rtype: None
        """
        _IntAna.IntAna_IntQuadQuad_swiginit(self, _IntAna.new_IntAna_IntQuadQuad(*args))
    IsDone = _swig_new_instance_method(_IntAna.IntAna_IntQuadQuad_IsDone)
    NbCurve = _swig_new_instance_method(_IntAna.IntAna_IntQuadQuad_NbCurve)
    NbPnt = _swig_new_instance_method(_IntAna.IntAna_IntQuadQuad_NbPnt)
    NextCurve = _swig_new_instance_method(_IntAna.IntAna_IntQuadQuad_NextCurve)
    Parameters = _swig_new_instance_method(_IntAna.IntAna_IntQuadQuad_Parameters)
    Perform = _swig_new_instance_method(_IntAna.IntAna_IntQuadQuad_Perform)
    Point = _swig_new_instance_method(_IntAna.IntAna_IntQuadQuad_Point)
    PreviousCurve = _swig_new_instance_method(_IntAna.IntAna_IntQuadQuad_PreviousCurve)

    __repr__ = _dumps_object

    __swig_destroy__ = _IntAna.delete_IntAna_IntQuadQuad

# Register IntAna_IntQuadQuad in _IntAna:
_IntAna.IntAna_IntQuadQuad_swigregister(IntAna_IntQuadQuad)

class IntAna_QuadQuadGeo(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Circle = _swig_new_instance_method(_IntAna.IntAna_QuadQuadGeo_Circle)
    Ellipse = _swig_new_instance_method(_IntAna.IntAna_QuadQuadGeo_Ellipse)
    HasCommonGen = _swig_new_instance_method(_IntAna.IntAna_QuadQuadGeo_HasCommonGen)
    Hyperbola = _swig_new_instance_method(_IntAna.IntAna_QuadQuadGeo_Hyperbola)

    def __init__(self, *args):
        r"""
        * Empty constructor.
        	:rtype: None* Creates the intersection between two planes. TolAng is the angular tolerance used to determine if the planes are parallel. Tol is the tolerance used to determine if the planes are identical (only when they are parallel).
        	:param P1:
        	:type P1: gp_Pln
        	:param P2:
        	:type P2: gp_Pln
        	:param TolAng:
        	:type TolAng: float
        	:param Tol:
        	:type Tol: float
        	:rtype: None* Creates the intersection between a plane and a cylinder. TolAng is the angular tolerance used to determine if the axis of the cylinder is parallel to the plane. Tol is the tolerance used to determine if the result is a circle or an ellipse. If the maximum distance between the ellipse solution and the circle centered at the ellipse center is less than Tol, the result will be the circle. H is the height of the cylinder <Cyl>. It is used to check whether the plane and cylinder are parallel.
        	:param P:
        	:type P: gp_Pln
        	:param C:
        	:type C: gp_Cylinder
        	:param Tolang:
        	:type Tolang: float
        	:param Tol:
        	:type Tol: float
        	:param H: default value is 0
        	:type H: float
        	:rtype: None* Creates the intersection between a plane and a sphere.
        	:param P:
        	:type P: gp_Pln
        	:param S:
        	:type S: gp_Sphere
        	:rtype: None* Creates the intersection between a plane and a cone. TolAng is the angular tolerance used to determine if the axis of the cone is parallel or perpendicular to the plane, and if the generating line of the cone is parallel to the plane. Tol is the tolerance used to determine if the apex of the cone is in the plane.
        	:param P:
        	:type P: gp_Pln
        	:param C:
        	:type C: gp_Cone
        	:param Tolang:
        	:type Tolang: float
        	:param Tol:
        	:type Tol: float
        	:rtype: None* Creates the intersection between two cylinders.
        	:param Cyl1:
        	:type Cyl1: gp_Cylinder
        	:param Cyl2:
        	:type Cyl2: gp_Cylinder
        	:param Tol:
        	:type Tol: float
        	:rtype: None* Creates the intersection between a Cylinder and a Sphere.
        	:param Cyl:
        	:type Cyl: gp_Cylinder
        	:param Sph:
        	:type Sph: gp_Sphere
        	:param Tol:
        	:type Tol: float
        	:rtype: None* Creates the intersection between a Cylinder and a Cone
        	:param Cyl:
        	:type Cyl: gp_Cylinder
        	:param Con:
        	:type Con: gp_Cone
        	:param Tol:
        	:type Tol: float
        	:rtype: None* Creates the intersection between two Spheres.
        	:param Sph1:
        	:type Sph1: gp_Sphere
        	:param Sph2:
        	:type Sph2: gp_Sphere
        	:param Tol:
        	:type Tol: float
        	:rtype: None* Creates the intersection beween a Sphere and a Cone.
        	:param Sph:
        	:type Sph: gp_Sphere
        	:param Con:
        	:type Con: gp_Cone
        	:param Tol:
        	:type Tol: float
        	:rtype: None* Creates the intersection beween two cones.
        	:param Con1:
        	:type Con1: gp_Cone
        	:param Con2:
        	:type Con2: gp_Cone
        	:param Tol:
        	:type Tol: float
        	:rtype: None* Creates the intersection beween plane and torus.
        	:param Pln:
        	:type Pln: gp_Pln
        	:param Tor:
        	:type Tor: gp_Torus
        	:param Tol:
        	:type Tol: float
        	:rtype: None* Creates the intersection beween cylinder and torus.
        	:param Cyl:
        	:type Cyl: gp_Cylinder
        	:param Tor:
        	:type Tor: gp_Torus
        	:param Tol:
        	:type Tol: float
        	:rtype: None* Creates the intersection beween cone and torus.
        	:param Con:
        	:type Con: gp_Cone
        	:param Tor:
        	:type Tor: gp_Torus
        	:param Tol:
        	:type Tol: float
        	:rtype: None* Creates the intersection beween sphere and torus.
        	:param Sph:
        	:type Sph: gp_Sphere
        	:param Tor:
        	:type Tor: gp_Torus
        	:param Tol:
        	:type Tol: float
        	:rtype: None* Creates the intersection beween two toruses.
        	:param Tor1:
        	:type Tor1: gp_Torus
        	:param Tor2:
        	:type Tor2: gp_Torus
        	:param Tol:
        	:type Tol: float
        	:rtype: None
        """
        _IntAna.IntAna_QuadQuadGeo_swiginit(self, _IntAna.new_IntAna_QuadQuadGeo(*args))
    IsDone = _swig_new_instance_method(_IntAna.IntAna_QuadQuadGeo_IsDone)
    Line = _swig_new_instance_method(_IntAna.IntAna_QuadQuadGeo_Line)
    NbSolutions = _swig_new_instance_method(_IntAna.IntAna_QuadQuadGeo_NbSolutions)
    PChar = _swig_new_instance_method(_IntAna.IntAna_QuadQuadGeo_PChar)
    Parabola = _swig_new_instance_method(_IntAna.IntAna_QuadQuadGeo_Parabola)
    Perform = _swig_new_instance_method(_IntAna.IntAna_QuadQuadGeo_Perform)
    Point = _swig_new_instance_method(_IntAna.IntAna_QuadQuadGeo_Point)
    TypeInter = _swig_new_instance_method(_IntAna.IntAna_QuadQuadGeo_TypeInter)

    __repr__ = _dumps_object

    __swig_destroy__ = _IntAna.delete_IntAna_QuadQuadGeo

# Register IntAna_QuadQuadGeo in _IntAna:
_IntAna.IntAna_QuadQuadGeo_swigregister(IntAna_QuadQuadGeo)

class IntAna_Quadric(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Coefficients = _swig_new_instance_method(_IntAna.IntAna_Quadric_Coefficients)

    def __init__(self, *args):
        r"""
        * Empty Constructor
        	:rtype: None* Creates a Quadric from a Pln
        	:param P:
        	:type P: gp_Pln
        	:rtype: None* Creates a Quadric from a Sphere
        	:param Sph:
        	:type Sph: gp_Sphere
        	:rtype: None* Creates a Quadric from a Cylinder
        	:param Cyl:
        	:type Cyl: gp_Cylinder
        	:rtype: None* Creates a Quadric from a Cone
        	:param Cone:
        	:type Cone: gp_Cone
        	:rtype: None
        """
        _IntAna.IntAna_Quadric_swiginit(self, _IntAna.new_IntAna_Quadric(*args))
    NewCoefficients = _swig_new_instance_method(_IntAna.IntAna_Quadric_NewCoefficients)
    SetQuadric = _swig_new_instance_method(_IntAna.IntAna_Quadric_SetQuadric)
    SpecialPoints = _swig_new_instance_method(_IntAna.IntAna_Quadric_SpecialPoints)

    __repr__ = _dumps_object

    __swig_destroy__ = _IntAna.delete_IntAna_Quadric

# Register IntAna_Quadric in _IntAna:
_IntAna.IntAna_Quadric_swigregister(IntAna_Quadric)



