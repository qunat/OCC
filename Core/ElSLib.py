# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
ElSLib module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_elslib.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _ElSLib
else:
    import _ElSLib

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _ElSLib.SWIG_PyInstanceMethod_New
_swig_new_static_method = _ElSLib.SWIG_PyStaticMethod_New

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
    __swig_destroy__ = _ElSLib.delete_SwigPyIterator
    value = _swig_new_instance_method(_ElSLib.SwigPyIterator_value)
    incr = _swig_new_instance_method(_ElSLib.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_ElSLib.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_ElSLib.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_ElSLib.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_ElSLib.SwigPyIterator_copy)
    next = _swig_new_instance_method(_ElSLib.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_ElSLib.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_ElSLib.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_ElSLib.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_ElSLib.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_ElSLib.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_ElSLib.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_ElSLib.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_ElSLib.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_ElSLib.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _ElSLib:
_ElSLib.SwigPyIterator_swigregister(SwigPyIterator)


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
class elslib(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    ConeD0 = _swig_new_static_method(_ElSLib.elslib_ConeD0)
    ConeD1 = _swig_new_static_method(_ElSLib.elslib_ConeD1)
    ConeD2 = _swig_new_static_method(_ElSLib.elslib_ConeD2)
    ConeD3 = _swig_new_static_method(_ElSLib.elslib_ConeD3)
    ConeDN = _swig_new_static_method(_ElSLib.elslib_ConeDN)
    ConeParameters = _swig_new_static_method(_ElSLib.elslib_ConeParameters)
    ConeUIso = _swig_new_static_method(_ElSLib.elslib_ConeUIso)
    ConeVIso = _swig_new_static_method(_ElSLib.elslib_ConeVIso)
    ConeValue = _swig_new_static_method(_ElSLib.elslib_ConeValue)
    CylinderD0 = _swig_new_static_method(_ElSLib.elslib_CylinderD0)
    CylinderD1 = _swig_new_static_method(_ElSLib.elslib_CylinderD1)
    CylinderD2 = _swig_new_static_method(_ElSLib.elslib_CylinderD2)
    CylinderD3 = _swig_new_static_method(_ElSLib.elslib_CylinderD3)
    CylinderDN = _swig_new_static_method(_ElSLib.elslib_CylinderDN)
    CylinderParameters = _swig_new_static_method(_ElSLib.elslib_CylinderParameters)
    CylinderUIso = _swig_new_static_method(_ElSLib.elslib_CylinderUIso)
    CylinderVIso = _swig_new_static_method(_ElSLib.elslib_CylinderVIso)
    CylinderValue = _swig_new_static_method(_ElSLib.elslib_CylinderValue)
    D0 = _swig_new_static_method(_ElSLib.elslib_D0)
    D1 = _swig_new_static_method(_ElSLib.elslib_D1)
    D2 = _swig_new_static_method(_ElSLib.elslib_D2)
    D3 = _swig_new_static_method(_ElSLib.elslib_D3)
    DN = _swig_new_static_method(_ElSLib.elslib_DN)
    Parameters = _swig_new_static_method(_ElSLib.elslib_Parameters)
    PlaneD0 = _swig_new_static_method(_ElSLib.elslib_PlaneD0)
    PlaneD1 = _swig_new_static_method(_ElSLib.elslib_PlaneD1)
    PlaneDN = _swig_new_static_method(_ElSLib.elslib_PlaneDN)
    PlaneParameters = _swig_new_static_method(_ElSLib.elslib_PlaneParameters)
    PlaneUIso = _swig_new_static_method(_ElSLib.elslib_PlaneUIso)
    PlaneVIso = _swig_new_static_method(_ElSLib.elslib_PlaneVIso)
    PlaneValue = _swig_new_static_method(_ElSLib.elslib_PlaneValue)
    SphereD0 = _swig_new_static_method(_ElSLib.elslib_SphereD0)
    SphereD1 = _swig_new_static_method(_ElSLib.elslib_SphereD1)
    SphereD2 = _swig_new_static_method(_ElSLib.elslib_SphereD2)
    SphereD3 = _swig_new_static_method(_ElSLib.elslib_SphereD3)
    SphereDN = _swig_new_static_method(_ElSLib.elslib_SphereDN)
    SphereParameters = _swig_new_static_method(_ElSLib.elslib_SphereParameters)
    SphereUIso = _swig_new_static_method(_ElSLib.elslib_SphereUIso)
    SphereVIso = _swig_new_static_method(_ElSLib.elslib_SphereVIso)
    SphereValue = _swig_new_static_method(_ElSLib.elslib_SphereValue)
    TorusD0 = _swig_new_static_method(_ElSLib.elslib_TorusD0)
    TorusD1 = _swig_new_static_method(_ElSLib.elslib_TorusD1)
    TorusD2 = _swig_new_static_method(_ElSLib.elslib_TorusD2)
    TorusD3 = _swig_new_static_method(_ElSLib.elslib_TorusD3)
    TorusDN = _swig_new_static_method(_ElSLib.elslib_TorusDN)
    TorusParameters = _swig_new_static_method(_ElSLib.elslib_TorusParameters)
    TorusUIso = _swig_new_static_method(_ElSLib.elslib_TorusUIso)
    TorusVIso = _swig_new_static_method(_ElSLib.elslib_TorusVIso)
    TorusValue = _swig_new_static_method(_ElSLib.elslib_TorusValue)
    Value = _swig_new_static_method(_ElSLib.elslib_Value)

    __repr__ = _dumps_object


    def __init__(self):
        _ElSLib.elslib_swiginit(self, _ElSLib.new_elslib())
    __swig_destroy__ = _ElSLib.delete_elslib

# Register elslib in _ElSLib:
_ElSLib.elslib_swigregister(elslib)
elslib_ConeD0 = _ElSLib.elslib_ConeD0
elslib_ConeD1 = _ElSLib.elslib_ConeD1
elslib_ConeD2 = _ElSLib.elslib_ConeD2
elslib_ConeD3 = _ElSLib.elslib_ConeD3
elslib_ConeDN = _ElSLib.elslib_ConeDN
elslib_ConeParameters = _ElSLib.elslib_ConeParameters
elslib_ConeUIso = _ElSLib.elslib_ConeUIso
elslib_ConeVIso = _ElSLib.elslib_ConeVIso
elslib_ConeValue = _ElSLib.elslib_ConeValue
elslib_CylinderD0 = _ElSLib.elslib_CylinderD0
elslib_CylinderD1 = _ElSLib.elslib_CylinderD1
elslib_CylinderD2 = _ElSLib.elslib_CylinderD2
elslib_CylinderD3 = _ElSLib.elslib_CylinderD3
elslib_CylinderDN = _ElSLib.elslib_CylinderDN
elslib_CylinderParameters = _ElSLib.elslib_CylinderParameters
elslib_CylinderUIso = _ElSLib.elslib_CylinderUIso
elslib_CylinderVIso = _ElSLib.elslib_CylinderVIso
elslib_CylinderValue = _ElSLib.elslib_CylinderValue
elslib_D0 = _ElSLib.elslib_D0
elslib_D1 = _ElSLib.elslib_D1
elslib_D2 = _ElSLib.elslib_D2
elslib_D3 = _ElSLib.elslib_D3
elslib_DN = _ElSLib.elslib_DN
elslib_Parameters = _ElSLib.elslib_Parameters
elslib_PlaneD0 = _ElSLib.elslib_PlaneD0
elslib_PlaneD1 = _ElSLib.elslib_PlaneD1
elslib_PlaneDN = _ElSLib.elslib_PlaneDN
elslib_PlaneParameters = _ElSLib.elslib_PlaneParameters
elslib_PlaneUIso = _ElSLib.elslib_PlaneUIso
elslib_PlaneVIso = _ElSLib.elslib_PlaneVIso
elslib_PlaneValue = _ElSLib.elslib_PlaneValue
elslib_SphereD0 = _ElSLib.elslib_SphereD0
elslib_SphereD1 = _ElSLib.elslib_SphereD1
elslib_SphereD2 = _ElSLib.elslib_SphereD2
elslib_SphereD3 = _ElSLib.elslib_SphereD3
elslib_SphereDN = _ElSLib.elslib_SphereDN
elslib_SphereParameters = _ElSLib.elslib_SphereParameters
elslib_SphereUIso = _ElSLib.elslib_SphereUIso
elslib_SphereVIso = _ElSLib.elslib_SphereVIso
elslib_SphereValue = _ElSLib.elslib_SphereValue
elslib_TorusD0 = _ElSLib.elslib_TorusD0
elslib_TorusD1 = _ElSLib.elslib_TorusD1
elslib_TorusD2 = _ElSLib.elslib_TorusD2
elslib_TorusD3 = _ElSLib.elslib_TorusD3
elslib_TorusDN = _ElSLib.elslib_TorusDN
elslib_TorusParameters = _ElSLib.elslib_TorusParameters
elslib_TorusUIso = _ElSLib.elslib_TorusUIso
elslib_TorusVIso = _ElSLib.elslib_TorusVIso
elslib_TorusValue = _ElSLib.elslib_TorusValue
elslib_Value = _ElSLib.elslib_Value



