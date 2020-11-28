# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
Sweep module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_sweep.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _Sweep
else:
    import _Sweep

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _Sweep.SWIG_PyInstanceMethod_New
_swig_new_static_method = _Sweep.SWIG_PyStaticMethod_New

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
    __swig_destroy__ = _Sweep.delete_SwigPyIterator
    value = _swig_new_instance_method(_Sweep.SwigPyIterator_value)
    incr = _swig_new_instance_method(_Sweep.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_Sweep.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_Sweep.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_Sweep.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_Sweep.SwigPyIterator_copy)
    next = _swig_new_instance_method(_Sweep.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_Sweep.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_Sweep.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_Sweep.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_Sweep.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_Sweep.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_Sweep.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_Sweep.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_Sweep.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_Sweep.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _Sweep:
_Sweep.SwigPyIterator_swigregister(SwigPyIterator)


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
import OCC.Core.TopAbs
class Sweep_NumShape(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    BegInfinite = _swig_new_instance_method(_Sweep.Sweep_NumShape_BegInfinite)
    Closed = _swig_new_instance_method(_Sweep.Sweep_NumShape_Closed)
    EndInfinite = _swig_new_instance_method(_Sweep.Sweep_NumShape_EndInfinite)
    Index = _swig_new_instance_method(_Sweep.Sweep_NumShape_Index)
    Init = _swig_new_instance_method(_Sweep.Sweep_NumShape_Init)
    Orientation = _swig_new_instance_method(_Sweep.Sweep_NumShape_Orientation)

    def __init__(self, *args):
        r"""
        * Creates a dummy indexed edge.
        	:rtype: None* Creates a new simple indexed edge. //! For an Edge : Index is the number of vertices (0, 1 or 2),Type is TopAbs_EDGE, Closed is true if it is a closed edge, BegInf is true if the Edge is infinite at the begenning, EndInf is true if the edge is infinite at the end. //! For a Vertex : Index is the index of the vertex in the edge (1 or 2), Type is TopAbsVERTEX, all the other fields have no meanning.
        	:param Index:
        	:type Index: int
        	:param Type:
        	:type Type: TopAbs_ShapeEnum
        	:param Closed: default value is Standard_False
        	:type Closed: bool
        	:param BegInf: default value is Standard_False
        	:type BegInf: bool
        	:param EndInf: default value is Standard_False
        	:type EndInf: bool
        	:rtype: None
        """
        _Sweep.Sweep_NumShape_swiginit(self, _Sweep.new_Sweep_NumShape(*args))
    Type = _swig_new_instance_method(_Sweep.Sweep_NumShape_Type)

    __repr__ = _dumps_object

    __swig_destroy__ = _Sweep.delete_Sweep_NumShape

# Register Sweep_NumShape in _Sweep:
_Sweep.Sweep_NumShape_swigregister(Sweep_NumShape)

class Sweep_NumShapeIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Init = _swig_new_instance_method(_Sweep.Sweep_NumShapeIterator_Init)
    More = _swig_new_instance_method(_Sweep.Sweep_NumShapeIterator_More)
    Next = _swig_new_instance_method(_Sweep.Sweep_NumShapeIterator_Next)
    Orientation = _swig_new_instance_method(_Sweep.Sweep_NumShapeIterator_Orientation)

    def __init__(self, *args):
        r""":rtype: None"""
        _Sweep.Sweep_NumShapeIterator_swiginit(self, _Sweep.new_Sweep_NumShapeIterator(*args))
    Value = _swig_new_instance_method(_Sweep.Sweep_NumShapeIterator_Value)

    __repr__ = _dumps_object

    __swig_destroy__ = _Sweep.delete_Sweep_NumShapeIterator

# Register Sweep_NumShapeIterator in _Sweep:
_Sweep.Sweep_NumShapeIterator_swigregister(Sweep_NumShapeIterator)

class Sweep_NumShapeTool(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    FirstVertex = _swig_new_instance_method(_Sweep.Sweep_NumShapeTool_FirstVertex)
    HasFirstVertex = _swig_new_instance_method(_Sweep.Sweep_NumShapeTool_HasFirstVertex)
    HasLastVertex = _swig_new_instance_method(_Sweep.Sweep_NumShapeTool_HasLastVertex)
    Index = _swig_new_instance_method(_Sweep.Sweep_NumShapeTool_Index)
    LastVertex = _swig_new_instance_method(_Sweep.Sweep_NumShapeTool_LastVertex)
    NbShapes = _swig_new_instance_method(_Sweep.Sweep_NumShapeTool_NbShapes)
    Orientation = _swig_new_instance_method(_Sweep.Sweep_NumShapeTool_Orientation)
    Shape = _swig_new_instance_method(_Sweep.Sweep_NumShapeTool_Shape)

    def __init__(self, *args):
        r"""
        * Create a new NumShapeTool with <aShape>. The Tool must prepare an indexation for all the subshapes of this shape.
        	:param aShape:
        	:type aShape: Sweep_NumShape
        	:rtype: None
        """
        _Sweep.Sweep_NumShapeTool_swiginit(self, _Sweep.new_Sweep_NumShapeTool(*args))
    Type = _swig_new_instance_method(_Sweep.Sweep_NumShapeTool_Type)

    __repr__ = _dumps_object

    __swig_destroy__ = _Sweep.delete_Sweep_NumShapeTool

# Register Sweep_NumShapeTool in _Sweep:
_Sweep.Sweep_NumShapeTool_swigregister(Sweep_NumShapeTool)


