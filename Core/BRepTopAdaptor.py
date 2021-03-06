# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
BRepTopAdaptor module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_breptopadaptor.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _BRepTopAdaptor
else:
    import _BRepTopAdaptor

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _BRepTopAdaptor.SWIG_PyInstanceMethod_New
_swig_new_static_method = _BRepTopAdaptor.SWIG_PyStaticMethod_New

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
    __swig_destroy__ = _BRepTopAdaptor.delete_SwigPyIterator
    value = _swig_new_instance_method(_BRepTopAdaptor.SwigPyIterator_value)
    incr = _swig_new_instance_method(_BRepTopAdaptor.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_BRepTopAdaptor.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_BRepTopAdaptor.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_BRepTopAdaptor.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_BRepTopAdaptor.SwigPyIterator_copy)
    next = _swig_new_instance_method(_BRepTopAdaptor.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_BRepTopAdaptor.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_BRepTopAdaptor.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_BRepTopAdaptor.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_BRepTopAdaptor.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_BRepTopAdaptor.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_BRepTopAdaptor.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_BRepTopAdaptor.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_BRepTopAdaptor.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_BRepTopAdaptor.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _BRepTopAdaptor:
_BRepTopAdaptor.SwigPyIterator_swigregister(SwigPyIterator)


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
import OCC.Core.TColStd
import OCC.Core.TCollection
import OCC.Core.TopoDS
import OCC.Core.Message
import OCC.Core.TopAbs
import OCC.Core.TopLoc
import OCC.Core.gp
import OCC.Core.Adaptor3d
import OCC.Core.Geom
import OCC.Core.GeomAbs
import OCC.Core.TColgp
import OCC.Core.Adaptor2d
import OCC.Core.Geom2d
import OCC.Core.math
import OCC.Core.BRepAdaptor
import OCC.Core.GeomAdaptor
import OCC.Core.Geom2dAdaptor
Handle_BRepTopAdaptor_HVertex_Create = _BRepTopAdaptor.Handle_BRepTopAdaptor_HVertex_Create
Handle_BRepTopAdaptor_HVertex_DownCast = _BRepTopAdaptor.Handle_BRepTopAdaptor_HVertex_DownCast
Handle_BRepTopAdaptor_HVertex_IsNull = _BRepTopAdaptor.Handle_BRepTopAdaptor_HVertex_IsNull
Handle_BRepTopAdaptor_TopolTool_Create = _BRepTopAdaptor.Handle_BRepTopAdaptor_TopolTool_Create
Handle_BRepTopAdaptor_TopolTool_DownCast = _BRepTopAdaptor.Handle_BRepTopAdaptor_TopolTool_DownCast
Handle_BRepTopAdaptor_TopolTool_IsNull = _BRepTopAdaptor.Handle_BRepTopAdaptor_TopolTool_IsNull
class BRepTopAdaptor_MapOfShapeTool(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool_begin)
    end = _swig_new_instance_method(_BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool_end)
    cbegin = _swig_new_instance_method(_BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool_cbegin)
    cend = _swig_new_instance_method(_BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool_cend)

    def __init__(self, *args):
        _BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool_swiginit(self, _BRepTopAdaptor.new_BRepTopAdaptor_MapOfShapeTool(*args))
    Exchange = _swig_new_instance_method(_BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool_Exchange)
    Assign = _swig_new_instance_method(_BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool_Assign)
    Set = _swig_new_instance_method(_BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool_Set)
    ReSize = _swig_new_instance_method(_BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool_ReSize)
    Bind = _swig_new_instance_method(_BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool_Bind)
    Bound = _swig_new_instance_method(_BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool_Bound)
    IsBound = _swig_new_instance_method(_BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool_IsBound)
    UnBind = _swig_new_instance_method(_BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool_UnBind)
    Seek = _swig_new_instance_method(_BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool_Seek)
    Find = _swig_new_instance_method(_BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool_Find)
    ChangeSeek = _swig_new_instance_method(_BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool_ChangeSeek)
    ChangeFind = _swig_new_instance_method(_BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool_ChangeFind)
    __call__ = _swig_new_instance_method(_BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool___call__)
    Clear = _swig_new_instance_method(_BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool_Clear)
    __swig_destroy__ = _BRepTopAdaptor.delete_BRepTopAdaptor_MapOfShapeTool
    Size = _swig_new_instance_method(_BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool_Size)

# Register BRepTopAdaptor_MapOfShapeTool in _BRepTopAdaptor:
_BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool_swigregister(BRepTopAdaptor_MapOfShapeTool)

class BRepTopAdaptor_FClass2d(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :param F:
        	:type F: TopoDS_Face
        	:param Tol:
        	:type Tol: float
        	:rtype: None
        """
        _BRepTopAdaptor.BRepTopAdaptor_FClass2d_swiginit(self, _BRepTopAdaptor.new_BRepTopAdaptor_FClass2d(*args))
    Copy = _swig_new_instance_method(_BRepTopAdaptor.BRepTopAdaptor_FClass2d_Copy)
    Destroy = _swig_new_instance_method(_BRepTopAdaptor.BRepTopAdaptor_FClass2d_Destroy)
    Perform = _swig_new_instance_method(_BRepTopAdaptor.BRepTopAdaptor_FClass2d_Perform)
    PerformInfinitePoint = _swig_new_instance_method(_BRepTopAdaptor.BRepTopAdaptor_FClass2d_PerformInfinitePoint)
    TestOnRestriction = _swig_new_instance_method(_BRepTopAdaptor.BRepTopAdaptor_FClass2d_TestOnRestriction)
    Set = _swig_new_instance_method(_BRepTopAdaptor.BRepTopAdaptor_FClass2d_Set)

    __repr__ = _dumps_object

    __swig_destroy__ = _BRepTopAdaptor.delete_BRepTopAdaptor_FClass2d

# Register BRepTopAdaptor_FClass2d in _BRepTopAdaptor:
_BRepTopAdaptor.BRepTopAdaptor_FClass2d_swigregister(BRepTopAdaptor_FClass2d)

class BRepTopAdaptor_HVertex(OCC.Core.Adaptor3d.Adaptor3d_HVertex):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :param Vtx:
        	:type Vtx: TopoDS_Vertex
        	:param Curve:
        	:type Curve: BRepAdaptor_HCurve2d
        	:rtype: None
        """
        _BRepTopAdaptor.BRepTopAdaptor_HVertex_swiginit(self, _BRepTopAdaptor.new_BRepTopAdaptor_HVertex(*args))
    ChangeVertex = _swig_new_instance_method(_BRepTopAdaptor.BRepTopAdaptor_HVertex_ChangeVertex)
    Vertex = _swig_new_instance_method(_BRepTopAdaptor.BRepTopAdaptor_HVertex_Vertex)


    @staticmethod
    def DownCast(t):
      return Handle_BRepTopAdaptor_HVertex_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _BRepTopAdaptor.delete_BRepTopAdaptor_HVertex

# Register BRepTopAdaptor_HVertex in _BRepTopAdaptor:
_BRepTopAdaptor.BRepTopAdaptor_HVertex_swigregister(BRepTopAdaptor_HVertex)

class BRepTopAdaptor_Tool(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :rtype: None:param F:
        	:type F: TopoDS_Face
        	:param Tol2d:
        	:type Tol2d: float
        	:rtype: None:param Surface:
        	:type Surface: Adaptor3d_HSurface
        	:param Tol2d:
        	:type Tol2d: float
        	:rtype: None
        """
        _BRepTopAdaptor.BRepTopAdaptor_Tool_swiginit(self, _BRepTopAdaptor.new_BRepTopAdaptor_Tool(*args))
    Destroy = _swig_new_instance_method(_BRepTopAdaptor.BRepTopAdaptor_Tool_Destroy)
    GetSurface = _swig_new_instance_method(_BRepTopAdaptor.BRepTopAdaptor_Tool_GetSurface)
    GetTopolTool = _swig_new_instance_method(_BRepTopAdaptor.BRepTopAdaptor_Tool_GetTopolTool)
    Init = _swig_new_instance_method(_BRepTopAdaptor.BRepTopAdaptor_Tool_Init)
    SetTopolTool = _swig_new_instance_method(_BRepTopAdaptor.BRepTopAdaptor_Tool_SetTopolTool)

    __repr__ = _dumps_object

    __swig_destroy__ = _BRepTopAdaptor.delete_BRepTopAdaptor_Tool

# Register BRepTopAdaptor_Tool in _BRepTopAdaptor:
_BRepTopAdaptor.BRepTopAdaptor_Tool_swigregister(BRepTopAdaptor_Tool)

class BRepTopAdaptor_TopolTool(OCC.Core.Adaptor3d.Adaptor3d_TopolTool):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :rtype: None:param Surface:
        	:type Surface: Adaptor3d_HSurface
        	:rtype: None
        """
        _BRepTopAdaptor.BRepTopAdaptor_TopolTool_swiginit(self, _BRepTopAdaptor.new_BRepTopAdaptor_TopolTool(*args))
    Destroy = _swig_new_instance_method(_BRepTopAdaptor.BRepTopAdaptor_TopolTool_Destroy)
    Initialize = _swig_new_instance_method(_BRepTopAdaptor.BRepTopAdaptor_TopolTool_Initialize)
    Orientation = _swig_new_instance_method(_BRepTopAdaptor.BRepTopAdaptor_TopolTool_Orientation)
    Tol3d = _swig_new_instance_method(_BRepTopAdaptor.BRepTopAdaptor_TopolTool_Tol3d)


    @staticmethod
    def DownCast(t):
      return Handle_BRepTopAdaptor_TopolTool_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _BRepTopAdaptor.delete_BRepTopAdaptor_TopolTool

# Register BRepTopAdaptor_TopolTool in _BRepTopAdaptor:
_BRepTopAdaptor.BRepTopAdaptor_TopolTool_swigregister(BRepTopAdaptor_TopolTool)



