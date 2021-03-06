# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
GeomLProp module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_geomlprop.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _GeomLProp
else:
    import _GeomLProp

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _GeomLProp.SWIG_PyInstanceMethod_New
_swig_new_static_method = _GeomLProp.SWIG_PyStaticMethod_New

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
    __swig_destroy__ = _GeomLProp.delete_SwigPyIterator
    value = _swig_new_instance_method(_GeomLProp.SwigPyIterator_value)
    incr = _swig_new_instance_method(_GeomLProp.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_GeomLProp.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_GeomLProp.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_GeomLProp.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_GeomLProp.SwigPyIterator_copy)
    next = _swig_new_instance_method(_GeomLProp.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_GeomLProp.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_GeomLProp.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_GeomLProp.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_GeomLProp.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_GeomLProp.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_GeomLProp.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_GeomLProp.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_GeomLProp.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_GeomLProp.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _GeomLProp:
_GeomLProp.SwigPyIterator_swigregister(SwigPyIterator)


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
class geomlprop(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Continuity = _swig_new_static_method(_GeomLProp.geomlprop_Continuity)

    __repr__ = _dumps_object


    def __init__(self):
        _GeomLProp.geomlprop_swiginit(self, _GeomLProp.new_geomlprop())
    __swig_destroy__ = _GeomLProp.delete_geomlprop

# Register geomlprop in _GeomLProp:
_GeomLProp.geomlprop_swigregister(geomlprop)
geomlprop_Continuity = _GeomLProp.geomlprop_Continuity

class GeomLProp_CLProps(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    CentreOfCurvature = _swig_new_instance_method(_GeomLProp.GeomLProp_CLProps_CentreOfCurvature)
    Curvature = _swig_new_instance_method(_GeomLProp.GeomLProp_CLProps_Curvature)
    D1 = _swig_new_instance_method(_GeomLProp.GeomLProp_CLProps_D1)
    D2 = _swig_new_instance_method(_GeomLProp.GeomLProp_CLProps_D2)
    D3 = _swig_new_instance_method(_GeomLProp.GeomLProp_CLProps_D3)

    def __init__(self, *args):
        r"""
        * Initializes the local properties of the curve <C> The current point and the derivatives are computed at the same time, which allows an optimization of the computation time. <N> indicates the maximum number of derivations to be done (0, 1, 2 or 3). For example, to compute only the tangent, N should be equal to 1. <Resolution> is the linear tolerance (it is used to test if a vector is null).
        	:param C:
        	:type C: Geom_Curve
        	:param N:
        	:type N: int
        	:param Resolution:
        	:type Resolution: float
        	:rtype: None* Same as previous constructor but here the parameter is set to the value <U>. All the computations done will be related to <C> and <U>.
        	:param C:
        	:type C: Geom_Curve
        	:param U:
        	:type U: float
        	:param N:
        	:type N: int
        	:param Resolution:
        	:type Resolution: float
        	:rtype: None* Same as previous constructor but here the parameter is set to the value <U> and the curve is set with SetCurve. the curve can have a empty constructor All the computations done will be related to <C> and <U> when the functions 'set' will be done.
        	:param N:
        	:type N: int
        	:param Resolution:
        	:type Resolution: float
        	:rtype: None
        """
        _GeomLProp.GeomLProp_CLProps_swiginit(self, _GeomLProp.new_GeomLProp_CLProps(*args))
    IsTangentDefined = _swig_new_instance_method(_GeomLProp.GeomLProp_CLProps_IsTangentDefined)
    Normal = _swig_new_instance_method(_GeomLProp.GeomLProp_CLProps_Normal)
    SetCurve = _swig_new_instance_method(_GeomLProp.GeomLProp_CLProps_SetCurve)
    SetParameter = _swig_new_instance_method(_GeomLProp.GeomLProp_CLProps_SetParameter)
    Tangent = _swig_new_instance_method(_GeomLProp.GeomLProp_CLProps_Tangent)
    Value = _swig_new_instance_method(_GeomLProp.GeomLProp_CLProps_Value)

    __repr__ = _dumps_object

    __swig_destroy__ = _GeomLProp.delete_GeomLProp_CLProps

# Register GeomLProp_CLProps in _GeomLProp:
_GeomLProp.GeomLProp_CLProps_swigregister(GeomLProp_CLProps)

class GeomLProp_CurveTool(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Continuity = _swig_new_static_method(_GeomLProp.GeomLProp_CurveTool_Continuity)
    D1 = _swig_new_static_method(_GeomLProp.GeomLProp_CurveTool_D1)
    D2 = _swig_new_static_method(_GeomLProp.GeomLProp_CurveTool_D2)
    D3 = _swig_new_static_method(_GeomLProp.GeomLProp_CurveTool_D3)
    FirstParameter = _swig_new_static_method(_GeomLProp.GeomLProp_CurveTool_FirstParameter)
    LastParameter = _swig_new_static_method(_GeomLProp.GeomLProp_CurveTool_LastParameter)
    Value = _swig_new_static_method(_GeomLProp.GeomLProp_CurveTool_Value)

    __repr__ = _dumps_object


    def __init__(self):
        _GeomLProp.GeomLProp_CurveTool_swiginit(self, _GeomLProp.new_GeomLProp_CurveTool())
    __swig_destroy__ = _GeomLProp.delete_GeomLProp_CurveTool

# Register GeomLProp_CurveTool in _GeomLProp:
_GeomLProp.GeomLProp_CurveTool_swigregister(GeomLProp_CurveTool)
GeomLProp_CurveTool_Continuity = _GeomLProp.GeomLProp_CurveTool_Continuity
GeomLProp_CurveTool_D1 = _GeomLProp.GeomLProp_CurveTool_D1
GeomLProp_CurveTool_D2 = _GeomLProp.GeomLProp_CurveTool_D2
GeomLProp_CurveTool_D3 = _GeomLProp.GeomLProp_CurveTool_D3
GeomLProp_CurveTool_FirstParameter = _GeomLProp.GeomLProp_CurveTool_FirstParameter
GeomLProp_CurveTool_LastParameter = _GeomLProp.GeomLProp_CurveTool_LastParameter
GeomLProp_CurveTool_Value = _GeomLProp.GeomLProp_CurveTool_Value

class GeomLProp_SLProps(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    CurvatureDirections = _swig_new_instance_method(_GeomLProp.GeomLProp_SLProps_CurvatureDirections)
    D1U = _swig_new_instance_method(_GeomLProp.GeomLProp_SLProps_D1U)
    D1V = _swig_new_instance_method(_GeomLProp.GeomLProp_SLProps_D1V)
    D2U = _swig_new_instance_method(_GeomLProp.GeomLProp_SLProps_D2U)
    D2V = _swig_new_instance_method(_GeomLProp.GeomLProp_SLProps_D2V)
    DUV = _swig_new_instance_method(_GeomLProp.GeomLProp_SLProps_DUV)
    GaussianCurvature = _swig_new_instance_method(_GeomLProp.GeomLProp_SLProps_GaussianCurvature)

    def __init__(self, *args):
        r"""
        * Initializes the local properties of the surface <S> for the parameter values (<U>, <V>). The current point and the derivatives are computed at the same time, which allows an optimization of the computation time. <N> indicates the maximum number of derivations to be done (0, 1, or 2). For example, to compute only the tangent, N should be equal to 1. <Resolution> is the linear tolerance (it is used to test if a vector is null).
        	:param S:
        	:type S: Geom_Surface
        	:param U:
        	:type U: float
        	:param V:
        	:type V: float
        	:param N:
        	:type N: int
        	:param Resolution:
        	:type Resolution: float
        	:rtype: None* idem as previous constructor but without setting the value of parameters <U> and <V>.
        	:param S:
        	:type S: Geom_Surface
        	:param N:
        	:type N: int
        	:param Resolution:
        	:type Resolution: float
        	:rtype: None* idem as previous constructor but without setting the value of parameters <U> and <V> and the surface. the surface can have an empty constructor.
        	:param N:
        	:type N: int
        	:param Resolution:
        	:type Resolution: float
        	:rtype: None
        """
        _GeomLProp.GeomLProp_SLProps_swiginit(self, _GeomLProp.new_GeomLProp_SLProps(*args))
    IsCurvatureDefined = _swig_new_instance_method(_GeomLProp.GeomLProp_SLProps_IsCurvatureDefined)
    IsNormalDefined = _swig_new_instance_method(_GeomLProp.GeomLProp_SLProps_IsNormalDefined)
    IsTangentUDefined = _swig_new_instance_method(_GeomLProp.GeomLProp_SLProps_IsTangentUDefined)
    IsTangentVDefined = _swig_new_instance_method(_GeomLProp.GeomLProp_SLProps_IsTangentVDefined)
    IsUmbilic = _swig_new_instance_method(_GeomLProp.GeomLProp_SLProps_IsUmbilic)
    MaxCurvature = _swig_new_instance_method(_GeomLProp.GeomLProp_SLProps_MaxCurvature)
    MeanCurvature = _swig_new_instance_method(_GeomLProp.GeomLProp_SLProps_MeanCurvature)
    MinCurvature = _swig_new_instance_method(_GeomLProp.GeomLProp_SLProps_MinCurvature)
    Normal = _swig_new_instance_method(_GeomLProp.GeomLProp_SLProps_Normal)
    SetParameters = _swig_new_instance_method(_GeomLProp.GeomLProp_SLProps_SetParameters)
    SetSurface = _swig_new_instance_method(_GeomLProp.GeomLProp_SLProps_SetSurface)
    TangentU = _swig_new_instance_method(_GeomLProp.GeomLProp_SLProps_TangentU)
    TangentV = _swig_new_instance_method(_GeomLProp.GeomLProp_SLProps_TangentV)
    Value = _swig_new_instance_method(_GeomLProp.GeomLProp_SLProps_Value)

    __repr__ = _dumps_object

    __swig_destroy__ = _GeomLProp.delete_GeomLProp_SLProps

# Register GeomLProp_SLProps in _GeomLProp:
_GeomLProp.GeomLProp_SLProps_swigregister(GeomLProp_SLProps)

class GeomLProp_SurfaceTool(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Bounds = _swig_new_static_method(_GeomLProp.GeomLProp_SurfaceTool_Bounds)
    Continuity = _swig_new_static_method(_GeomLProp.GeomLProp_SurfaceTool_Continuity)
    D1 = _swig_new_static_method(_GeomLProp.GeomLProp_SurfaceTool_D1)
    D2 = _swig_new_static_method(_GeomLProp.GeomLProp_SurfaceTool_D2)
    DN = _swig_new_static_method(_GeomLProp.GeomLProp_SurfaceTool_DN)
    Value = _swig_new_static_method(_GeomLProp.GeomLProp_SurfaceTool_Value)

    __repr__ = _dumps_object


    def __init__(self):
        _GeomLProp.GeomLProp_SurfaceTool_swiginit(self, _GeomLProp.new_GeomLProp_SurfaceTool())
    __swig_destroy__ = _GeomLProp.delete_GeomLProp_SurfaceTool

# Register GeomLProp_SurfaceTool in _GeomLProp:
_GeomLProp.GeomLProp_SurfaceTool_swigregister(GeomLProp_SurfaceTool)
GeomLProp_SurfaceTool_Bounds = _GeomLProp.GeomLProp_SurfaceTool_Bounds
GeomLProp_SurfaceTool_Continuity = _GeomLProp.GeomLProp_SurfaceTool_Continuity
GeomLProp_SurfaceTool_D1 = _GeomLProp.GeomLProp_SurfaceTool_D1
GeomLProp_SurfaceTool_D2 = _GeomLProp.GeomLProp_SurfaceTool_D2
GeomLProp_SurfaceTool_DN = _GeomLProp.GeomLProp_SurfaceTool_DN
GeomLProp_SurfaceTool_Value = _GeomLProp.GeomLProp_SurfaceTool_Value



