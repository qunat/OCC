# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
UnitsAPI module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_unitsapi.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _UnitsAPI
else:
    import _UnitsAPI

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _UnitsAPI.SWIG_PyInstanceMethod_New
_swig_new_static_method = _UnitsAPI.SWIG_PyStaticMethod_New

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
    __swig_destroy__ = _UnitsAPI.delete_SwigPyIterator
    value = _swig_new_instance_method(_UnitsAPI.SwigPyIterator_value)
    incr = _swig_new_instance_method(_UnitsAPI.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_UnitsAPI.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_UnitsAPI.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_UnitsAPI.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_UnitsAPI.SwigPyIterator_copy)
    next = _swig_new_instance_method(_UnitsAPI.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_UnitsAPI.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_UnitsAPI.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_UnitsAPI.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_UnitsAPI.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_UnitsAPI.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_UnitsAPI.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_UnitsAPI.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_UnitsAPI.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_UnitsAPI.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _UnitsAPI:
_UnitsAPI.SwigPyIterator_swigregister(SwigPyIterator)


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
import OCC.Core.Units
import OCC.Core.TCollection
import OCC.Core.TColStd
UnitsAPI_DEFAULT = _UnitsAPI.UnitsAPI_DEFAULT
UnitsAPI_SI = _UnitsAPI.UnitsAPI_SI
UnitsAPI_MDTV = _UnitsAPI.UnitsAPI_MDTV
class unitsapi(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    AnyFromLS = _swig_new_static_method(_UnitsAPI.unitsapi_AnyFromLS)
    AnyFromSI = _swig_new_static_method(_UnitsAPI.unitsapi_AnyFromSI)
    AnyToAny = _swig_new_static_method(_UnitsAPI.unitsapi_AnyToAny)
    AnyToLS = _swig_new_static_method(_UnitsAPI.unitsapi_AnyToLS)
    AnyToSI = _swig_new_static_method(_UnitsAPI.unitsapi_AnyToSI)
    Check = _swig_new_static_method(_UnitsAPI.unitsapi_Check)
    CurrentFromAny = _swig_new_static_method(_UnitsAPI.unitsapi_CurrentFromAny)
    CurrentFromLS = _swig_new_static_method(_UnitsAPI.unitsapi_CurrentFromLS)
    CurrentFromSI = _swig_new_static_method(_UnitsAPI.unitsapi_CurrentFromSI)
    CurrentToAny = _swig_new_static_method(_UnitsAPI.unitsapi_CurrentToAny)
    CurrentToLS = _swig_new_static_method(_UnitsAPI.unitsapi_CurrentToLS)
    CurrentToSI = _swig_new_static_method(_UnitsAPI.unitsapi_CurrentToSI)
    CurrentUnit = _swig_new_static_method(_UnitsAPI.unitsapi_CurrentUnit)
    DimensionAmountOfSubstance = _swig_new_static_method(_UnitsAPI.unitsapi_DimensionAmountOfSubstance)
    DimensionElectricCurrent = _swig_new_static_method(_UnitsAPI.unitsapi_DimensionElectricCurrent)
    DimensionLength = _swig_new_static_method(_UnitsAPI.unitsapi_DimensionLength)
    DimensionLess = _swig_new_static_method(_UnitsAPI.unitsapi_DimensionLess)
    DimensionLuminousIntensity = _swig_new_static_method(_UnitsAPI.unitsapi_DimensionLuminousIntensity)
    DimensionMass = _swig_new_static_method(_UnitsAPI.unitsapi_DimensionMass)
    DimensionPlaneAngle = _swig_new_static_method(_UnitsAPI.unitsapi_DimensionPlaneAngle)
    DimensionSolidAngle = _swig_new_static_method(_UnitsAPI.unitsapi_DimensionSolidAngle)
    DimensionThermodynamicTemperature = _swig_new_static_method(_UnitsAPI.unitsapi_DimensionThermodynamicTemperature)
    DimensionTime = _swig_new_static_method(_UnitsAPI.unitsapi_DimensionTime)
    Dimensions = _swig_new_static_method(_UnitsAPI.unitsapi_Dimensions)
    LSToSI = _swig_new_static_method(_UnitsAPI.unitsapi_LSToSI)
    LocalSystem = _swig_new_static_method(_UnitsAPI.unitsapi_LocalSystem)
    Reload = _swig_new_static_method(_UnitsAPI.unitsapi_Reload)
    SIToLS = _swig_new_static_method(_UnitsAPI.unitsapi_SIToLS)
    Save = _swig_new_static_method(_UnitsAPI.unitsapi_Save)
    SetCurrentUnit = _swig_new_static_method(_UnitsAPI.unitsapi_SetCurrentUnit)
    SetLocalSystem = _swig_new_static_method(_UnitsAPI.unitsapi_SetLocalSystem)

    __repr__ = _dumps_object


    def __init__(self):
        _UnitsAPI.unitsapi_swiginit(self, _UnitsAPI.new_unitsapi())
    __swig_destroy__ = _UnitsAPI.delete_unitsapi

# Register unitsapi in _UnitsAPI:
_UnitsAPI.unitsapi_swigregister(unitsapi)
unitsapi_AnyFromLS = _UnitsAPI.unitsapi_AnyFromLS
unitsapi_AnyFromSI = _UnitsAPI.unitsapi_AnyFromSI
unitsapi_AnyToAny = _UnitsAPI.unitsapi_AnyToAny
unitsapi_AnyToLS = _UnitsAPI.unitsapi_AnyToLS
unitsapi_AnyToSI = _UnitsAPI.unitsapi_AnyToSI
unitsapi_Check = _UnitsAPI.unitsapi_Check
unitsapi_CurrentFromAny = _UnitsAPI.unitsapi_CurrentFromAny
unitsapi_CurrentFromLS = _UnitsAPI.unitsapi_CurrentFromLS
unitsapi_CurrentFromSI = _UnitsAPI.unitsapi_CurrentFromSI
unitsapi_CurrentToAny = _UnitsAPI.unitsapi_CurrentToAny
unitsapi_CurrentToLS = _UnitsAPI.unitsapi_CurrentToLS
unitsapi_CurrentToSI = _UnitsAPI.unitsapi_CurrentToSI
unitsapi_CurrentUnit = _UnitsAPI.unitsapi_CurrentUnit
unitsapi_DimensionAmountOfSubstance = _UnitsAPI.unitsapi_DimensionAmountOfSubstance
unitsapi_DimensionElectricCurrent = _UnitsAPI.unitsapi_DimensionElectricCurrent
unitsapi_DimensionLength = _UnitsAPI.unitsapi_DimensionLength
unitsapi_DimensionLess = _UnitsAPI.unitsapi_DimensionLess
unitsapi_DimensionLuminousIntensity = _UnitsAPI.unitsapi_DimensionLuminousIntensity
unitsapi_DimensionMass = _UnitsAPI.unitsapi_DimensionMass
unitsapi_DimensionPlaneAngle = _UnitsAPI.unitsapi_DimensionPlaneAngle
unitsapi_DimensionSolidAngle = _UnitsAPI.unitsapi_DimensionSolidAngle
unitsapi_DimensionThermodynamicTemperature = _UnitsAPI.unitsapi_DimensionThermodynamicTemperature
unitsapi_DimensionTime = _UnitsAPI.unitsapi_DimensionTime
unitsapi_Dimensions = _UnitsAPI.unitsapi_Dimensions
unitsapi_LSToSI = _UnitsAPI.unitsapi_LSToSI
unitsapi_LocalSystem = _UnitsAPI.unitsapi_LocalSystem
unitsapi_Reload = _UnitsAPI.unitsapi_Reload
unitsapi_SIToLS = _UnitsAPI.unitsapi_SIToLS
unitsapi_Save = _UnitsAPI.unitsapi_Save
unitsapi_SetCurrentUnit = _UnitsAPI.unitsapi_SetCurrentUnit
unitsapi_SetLocalSystem = _UnitsAPI.unitsapi_SetLocalSystem



