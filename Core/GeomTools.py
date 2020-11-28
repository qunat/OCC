# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
GeomTools module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_geomtools.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _GeomTools
else:
    import _GeomTools

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _GeomTools.SWIG_PyInstanceMethod_New
_swig_new_static_method = _GeomTools.SWIG_PyStaticMethod_New

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
    __swig_destroy__ = _GeomTools.delete_SwigPyIterator
    value = _swig_new_instance_method(_GeomTools.SwigPyIterator_value)
    incr = _swig_new_instance_method(_GeomTools.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_GeomTools.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_GeomTools.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_GeomTools.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_GeomTools.SwigPyIterator_copy)
    next = _swig_new_instance_method(_GeomTools.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_GeomTools.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_GeomTools.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_GeomTools.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_GeomTools.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_GeomTools.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_GeomTools.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_GeomTools.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_GeomTools.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_GeomTools.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _GeomTools:
_GeomTools.SwigPyIterator_swigregister(SwigPyIterator)


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
import OCC.Core.Geom2d
import OCC.Core.Message
Handle_GeomTools_UndefinedTypeHandler_Create = _GeomTools.Handle_GeomTools_UndefinedTypeHandler_Create
Handle_GeomTools_UndefinedTypeHandler_DownCast = _GeomTools.Handle_GeomTools_UndefinedTypeHandler_DownCast
Handle_GeomTools_UndefinedTypeHandler_IsNull = _GeomTools.Handle_GeomTools_UndefinedTypeHandler_IsNull
class geomtools(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Dump = _swig_new_static_method(_GeomTools.geomtools_Dump)
    GetReal = _swig_new_static_method(_GeomTools.geomtools_GetReal)
    GetUndefinedTypeHandler = _swig_new_static_method(_GeomTools.geomtools_GetUndefinedTypeHandler)
    Read = _swig_new_static_method(_GeomTools.geomtools_Read)
    SetUndefinedTypeHandler = _swig_new_static_method(_GeomTools.geomtools_SetUndefinedTypeHandler)
    Write = _swig_new_static_method(_GeomTools.geomtools_Write)

    __repr__ = _dumps_object


    def __init__(self):
        _GeomTools.geomtools_swiginit(self, _GeomTools.new_geomtools())
    __swig_destroy__ = _GeomTools.delete_geomtools

# Register geomtools in _GeomTools:
_GeomTools.geomtools_swigregister(geomtools)
geomtools_Dump = _GeomTools.geomtools_Dump
geomtools_GetReal = _GeomTools.geomtools_GetReal
geomtools_GetUndefinedTypeHandler = _GeomTools.geomtools_GetUndefinedTypeHandler
geomtools_Read = _GeomTools.geomtools_Read
geomtools_SetUndefinedTypeHandler = _GeomTools.geomtools_SetUndefinedTypeHandler
geomtools_Write = _GeomTools.geomtools_Write

class GeomTools_Curve2dSet(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Add = _swig_new_instance_method(_GeomTools.GeomTools_Curve2dSet_Add)
    Clear = _swig_new_instance_method(_GeomTools.GeomTools_Curve2dSet_Clear)
    Curve2d = _swig_new_instance_method(_GeomTools.GeomTools_Curve2dSet_Curve2d)
    DumpToString = _swig_new_instance_method(_GeomTools.GeomTools_Curve2dSet_DumpToString)

    def __init__(self, *args):
        r"""
        * Returns an empty set of Curves.
        	:rtype: None
        """
        _GeomTools.GeomTools_Curve2dSet_swiginit(self, _GeomTools.new_GeomTools_Curve2dSet(*args))
    GetProgress = _swig_new_instance_method(_GeomTools.GeomTools_Curve2dSet_GetProgress)
    Index = _swig_new_instance_method(_GeomTools.GeomTools_Curve2dSet_Index)
    PrintCurve2d = _swig_new_static_method(_GeomTools.GeomTools_Curve2dSet_PrintCurve2d)
    ReadFromString = _swig_new_instance_method(_GeomTools.GeomTools_Curve2dSet_ReadFromString)
    ReadCurve2dFromString = _swig_new_instance_method(_GeomTools.GeomTools_Curve2dSet_ReadCurve2dFromString)
    SetProgress = _swig_new_instance_method(_GeomTools.GeomTools_Curve2dSet_SetProgress)
    WriteToString = _swig_new_instance_method(_GeomTools.GeomTools_Curve2dSet_WriteToString)

    __repr__ = _dumps_object

    __swig_destroy__ = _GeomTools.delete_GeomTools_Curve2dSet

# Register GeomTools_Curve2dSet in _GeomTools:
_GeomTools.GeomTools_Curve2dSet_swigregister(GeomTools_Curve2dSet)
GeomTools_Curve2dSet_PrintCurve2d = _GeomTools.GeomTools_Curve2dSet_PrintCurve2d

class GeomTools_CurveSet(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Add = _swig_new_instance_method(_GeomTools.GeomTools_CurveSet_Add)
    Clear = _swig_new_instance_method(_GeomTools.GeomTools_CurveSet_Clear)
    Curve = _swig_new_instance_method(_GeomTools.GeomTools_CurveSet_Curve)
    DumpToString = _swig_new_instance_method(_GeomTools.GeomTools_CurveSet_DumpToString)

    def __init__(self, *args):
        r"""
        * Returns an empty set of Curves.
        	:rtype: None
        """
        _GeomTools.GeomTools_CurveSet_swiginit(self, _GeomTools.new_GeomTools_CurveSet(*args))
    GetProgress = _swig_new_instance_method(_GeomTools.GeomTools_CurveSet_GetProgress)
    Index = _swig_new_instance_method(_GeomTools.GeomTools_CurveSet_Index)
    PrintCurve = _swig_new_static_method(_GeomTools.GeomTools_CurveSet_PrintCurve)
    ReadFromString = _swig_new_instance_method(_GeomTools.GeomTools_CurveSet_ReadFromString)
    ReadCurveFromString = _swig_new_instance_method(_GeomTools.GeomTools_CurveSet_ReadCurveFromString)
    SetProgress = _swig_new_instance_method(_GeomTools.GeomTools_CurveSet_SetProgress)
    WriteToString = _swig_new_instance_method(_GeomTools.GeomTools_CurveSet_WriteToString)

    __repr__ = _dumps_object

    __swig_destroy__ = _GeomTools.delete_GeomTools_CurveSet

# Register GeomTools_CurveSet in _GeomTools:
_GeomTools.GeomTools_CurveSet_swigregister(GeomTools_CurveSet)
GeomTools_CurveSet_PrintCurve = _GeomTools.GeomTools_CurveSet_PrintCurve

class GeomTools_SurfaceSet(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Add = _swig_new_instance_method(_GeomTools.GeomTools_SurfaceSet_Add)
    Clear = _swig_new_instance_method(_GeomTools.GeomTools_SurfaceSet_Clear)
    DumpToString = _swig_new_instance_method(_GeomTools.GeomTools_SurfaceSet_DumpToString)

    def __init__(self, *args):
        r"""
        * Returns an empty set of Surfaces.
        	:rtype: None
        """
        _GeomTools.GeomTools_SurfaceSet_swiginit(self, _GeomTools.new_GeomTools_SurfaceSet(*args))
    GetProgress = _swig_new_instance_method(_GeomTools.GeomTools_SurfaceSet_GetProgress)
    Index = _swig_new_instance_method(_GeomTools.GeomTools_SurfaceSet_Index)
    PrintSurface = _swig_new_static_method(_GeomTools.GeomTools_SurfaceSet_PrintSurface)
    ReadFromString = _swig_new_instance_method(_GeomTools.GeomTools_SurfaceSet_ReadFromString)
    ReadSurfaceFromString = _swig_new_instance_method(_GeomTools.GeomTools_SurfaceSet_ReadSurfaceFromString)
    SetProgress = _swig_new_instance_method(_GeomTools.GeomTools_SurfaceSet_SetProgress)
    Surface = _swig_new_instance_method(_GeomTools.GeomTools_SurfaceSet_Surface)
    WriteToString = _swig_new_instance_method(_GeomTools.GeomTools_SurfaceSet_WriteToString)

    __repr__ = _dumps_object

    __swig_destroy__ = _GeomTools.delete_GeomTools_SurfaceSet

# Register GeomTools_SurfaceSet in _GeomTools:
_GeomTools.GeomTools_SurfaceSet_swigregister(GeomTools_SurfaceSet)
GeomTools_SurfaceSet_PrintSurface = _GeomTools.GeomTools_SurfaceSet_PrintSurface

class GeomTools_UndefinedTypeHandler(OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r""":rtype: None"""
        _GeomTools.GeomTools_UndefinedTypeHandler_swiginit(self, _GeomTools.new_GeomTools_UndefinedTypeHandler(*args))
    PrintCurve = _swig_new_instance_method(_GeomTools.GeomTools_UndefinedTypeHandler_PrintCurve)
    PrintCurve2d = _swig_new_instance_method(_GeomTools.GeomTools_UndefinedTypeHandler_PrintCurve2d)
    PrintSurface = _swig_new_instance_method(_GeomTools.GeomTools_UndefinedTypeHandler_PrintSurface)
    ReadCurve = _swig_new_instance_method(_GeomTools.GeomTools_UndefinedTypeHandler_ReadCurve)
    ReadCurve2d = _swig_new_instance_method(_GeomTools.GeomTools_UndefinedTypeHandler_ReadCurve2d)
    ReadSurface = _swig_new_instance_method(_GeomTools.GeomTools_UndefinedTypeHandler_ReadSurface)


    @staticmethod
    def DownCast(t):
      return Handle_GeomTools_UndefinedTypeHandler_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _GeomTools.delete_GeomTools_UndefinedTypeHandler

# Register GeomTools_UndefinedTypeHandler in _GeomTools:
_GeomTools.GeomTools_UndefinedTypeHandler_swigregister(GeomTools_UndefinedTypeHandler)



