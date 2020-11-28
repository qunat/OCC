# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
BinMDataStd module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_binmdatastd.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _BinMDataStd
else:
    import _BinMDataStd

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _BinMDataStd.SWIG_PyInstanceMethod_New
_swig_new_static_method = _BinMDataStd.SWIG_PyStaticMethod_New

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
    __swig_destroy__ = _BinMDataStd.delete_SwigPyIterator
    value = _swig_new_instance_method(_BinMDataStd.SwigPyIterator_value)
    incr = _swig_new_instance_method(_BinMDataStd.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_BinMDataStd.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_BinMDataStd.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_BinMDataStd.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_BinMDataStd.SwigPyIterator_copy)
    next = _swig_new_instance_method(_BinMDataStd.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_BinMDataStd.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_BinMDataStd.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_BinMDataStd.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_BinMDataStd.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_BinMDataStd.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_BinMDataStd.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_BinMDataStd.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_BinMDataStd.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_BinMDataStd.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _BinMDataStd:
_BinMDataStd.SwigPyIterator_swigregister(SwigPyIterator)


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
import OCC.Core.BinMDF
import OCC.Core.TColStd
import OCC.Core.TCollection
import OCC.Core.Message
import OCC.Core.TDF
import OCC.Core.BinObjMgt
import OCC.Core.Storage
Handle_BinMDataStd_AsciiStringDriver_Create = _BinMDataStd.Handle_BinMDataStd_AsciiStringDriver_Create
Handle_BinMDataStd_AsciiStringDriver_DownCast = _BinMDataStd.Handle_BinMDataStd_AsciiStringDriver_DownCast
Handle_BinMDataStd_AsciiStringDriver_IsNull = _BinMDataStd.Handle_BinMDataStd_AsciiStringDriver_IsNull
Handle_BinMDataStd_BooleanArrayDriver_Create = _BinMDataStd.Handle_BinMDataStd_BooleanArrayDriver_Create
Handle_BinMDataStd_BooleanArrayDriver_DownCast = _BinMDataStd.Handle_BinMDataStd_BooleanArrayDriver_DownCast
Handle_BinMDataStd_BooleanArrayDriver_IsNull = _BinMDataStd.Handle_BinMDataStd_BooleanArrayDriver_IsNull
Handle_BinMDataStd_BooleanListDriver_Create = _BinMDataStd.Handle_BinMDataStd_BooleanListDriver_Create
Handle_BinMDataStd_BooleanListDriver_DownCast = _BinMDataStd.Handle_BinMDataStd_BooleanListDriver_DownCast
Handle_BinMDataStd_BooleanListDriver_IsNull = _BinMDataStd.Handle_BinMDataStd_BooleanListDriver_IsNull
Handle_BinMDataStd_ByteArrayDriver_Create = _BinMDataStd.Handle_BinMDataStd_ByteArrayDriver_Create
Handle_BinMDataStd_ByteArrayDriver_DownCast = _BinMDataStd.Handle_BinMDataStd_ByteArrayDriver_DownCast
Handle_BinMDataStd_ByteArrayDriver_IsNull = _BinMDataStd.Handle_BinMDataStd_ByteArrayDriver_IsNull
Handle_BinMDataStd_CommentDriver_Create = _BinMDataStd.Handle_BinMDataStd_CommentDriver_Create
Handle_BinMDataStd_CommentDriver_DownCast = _BinMDataStd.Handle_BinMDataStd_CommentDriver_DownCast
Handle_BinMDataStd_CommentDriver_IsNull = _BinMDataStd.Handle_BinMDataStd_CommentDriver_IsNull
Handle_BinMDataStd_DirectoryDriver_Create = _BinMDataStd.Handle_BinMDataStd_DirectoryDriver_Create
Handle_BinMDataStd_DirectoryDriver_DownCast = _BinMDataStd.Handle_BinMDataStd_DirectoryDriver_DownCast
Handle_BinMDataStd_DirectoryDriver_IsNull = _BinMDataStd.Handle_BinMDataStd_DirectoryDriver_IsNull
Handle_BinMDataStd_ExpressionDriver_Create = _BinMDataStd.Handle_BinMDataStd_ExpressionDriver_Create
Handle_BinMDataStd_ExpressionDriver_DownCast = _BinMDataStd.Handle_BinMDataStd_ExpressionDriver_DownCast
Handle_BinMDataStd_ExpressionDriver_IsNull = _BinMDataStd.Handle_BinMDataStd_ExpressionDriver_IsNull
Handle_BinMDataStd_ExtStringArrayDriver_Create = _BinMDataStd.Handle_BinMDataStd_ExtStringArrayDriver_Create
Handle_BinMDataStd_ExtStringArrayDriver_DownCast = _BinMDataStd.Handle_BinMDataStd_ExtStringArrayDriver_DownCast
Handle_BinMDataStd_ExtStringArrayDriver_IsNull = _BinMDataStd.Handle_BinMDataStd_ExtStringArrayDriver_IsNull
Handle_BinMDataStd_ExtStringListDriver_Create = _BinMDataStd.Handle_BinMDataStd_ExtStringListDriver_Create
Handle_BinMDataStd_ExtStringListDriver_DownCast = _BinMDataStd.Handle_BinMDataStd_ExtStringListDriver_DownCast
Handle_BinMDataStd_ExtStringListDriver_IsNull = _BinMDataStd.Handle_BinMDataStd_ExtStringListDriver_IsNull
Handle_BinMDataStd_IntPackedMapDriver_Create = _BinMDataStd.Handle_BinMDataStd_IntPackedMapDriver_Create
Handle_BinMDataStd_IntPackedMapDriver_DownCast = _BinMDataStd.Handle_BinMDataStd_IntPackedMapDriver_DownCast
Handle_BinMDataStd_IntPackedMapDriver_IsNull = _BinMDataStd.Handle_BinMDataStd_IntPackedMapDriver_IsNull
Handle_BinMDataStd_IntegerArrayDriver_Create = _BinMDataStd.Handle_BinMDataStd_IntegerArrayDriver_Create
Handle_BinMDataStd_IntegerArrayDriver_DownCast = _BinMDataStd.Handle_BinMDataStd_IntegerArrayDriver_DownCast
Handle_BinMDataStd_IntegerArrayDriver_IsNull = _BinMDataStd.Handle_BinMDataStd_IntegerArrayDriver_IsNull
Handle_BinMDataStd_IntegerDriver_Create = _BinMDataStd.Handle_BinMDataStd_IntegerDriver_Create
Handle_BinMDataStd_IntegerDriver_DownCast = _BinMDataStd.Handle_BinMDataStd_IntegerDriver_DownCast
Handle_BinMDataStd_IntegerDriver_IsNull = _BinMDataStd.Handle_BinMDataStd_IntegerDriver_IsNull
Handle_BinMDataStd_IntegerListDriver_Create = _BinMDataStd.Handle_BinMDataStd_IntegerListDriver_Create
Handle_BinMDataStd_IntegerListDriver_DownCast = _BinMDataStd.Handle_BinMDataStd_IntegerListDriver_DownCast
Handle_BinMDataStd_IntegerListDriver_IsNull = _BinMDataStd.Handle_BinMDataStd_IntegerListDriver_IsNull
Handle_BinMDataStd_NameDriver_Create = _BinMDataStd.Handle_BinMDataStd_NameDriver_Create
Handle_BinMDataStd_NameDriver_DownCast = _BinMDataStd.Handle_BinMDataStd_NameDriver_DownCast
Handle_BinMDataStd_NameDriver_IsNull = _BinMDataStd.Handle_BinMDataStd_NameDriver_IsNull
Handle_BinMDataStd_NamedDataDriver_Create = _BinMDataStd.Handle_BinMDataStd_NamedDataDriver_Create
Handle_BinMDataStd_NamedDataDriver_DownCast = _BinMDataStd.Handle_BinMDataStd_NamedDataDriver_DownCast
Handle_BinMDataStd_NamedDataDriver_IsNull = _BinMDataStd.Handle_BinMDataStd_NamedDataDriver_IsNull
Handle_BinMDataStd_NoteBookDriver_Create = _BinMDataStd.Handle_BinMDataStd_NoteBookDriver_Create
Handle_BinMDataStd_NoteBookDriver_DownCast = _BinMDataStd.Handle_BinMDataStd_NoteBookDriver_DownCast
Handle_BinMDataStd_NoteBookDriver_IsNull = _BinMDataStd.Handle_BinMDataStd_NoteBookDriver_IsNull
Handle_BinMDataStd_RealArrayDriver_Create = _BinMDataStd.Handle_BinMDataStd_RealArrayDriver_Create
Handle_BinMDataStd_RealArrayDriver_DownCast = _BinMDataStd.Handle_BinMDataStd_RealArrayDriver_DownCast
Handle_BinMDataStd_RealArrayDriver_IsNull = _BinMDataStd.Handle_BinMDataStd_RealArrayDriver_IsNull
Handle_BinMDataStd_RealDriver_Create = _BinMDataStd.Handle_BinMDataStd_RealDriver_Create
Handle_BinMDataStd_RealDriver_DownCast = _BinMDataStd.Handle_BinMDataStd_RealDriver_DownCast
Handle_BinMDataStd_RealDriver_IsNull = _BinMDataStd.Handle_BinMDataStd_RealDriver_IsNull
Handle_BinMDataStd_RealListDriver_Create = _BinMDataStd.Handle_BinMDataStd_RealListDriver_Create
Handle_BinMDataStd_RealListDriver_DownCast = _BinMDataStd.Handle_BinMDataStd_RealListDriver_DownCast
Handle_BinMDataStd_RealListDriver_IsNull = _BinMDataStd.Handle_BinMDataStd_RealListDriver_IsNull
Handle_BinMDataStd_ReferenceArrayDriver_Create = _BinMDataStd.Handle_BinMDataStd_ReferenceArrayDriver_Create
Handle_BinMDataStd_ReferenceArrayDriver_DownCast = _BinMDataStd.Handle_BinMDataStd_ReferenceArrayDriver_DownCast
Handle_BinMDataStd_ReferenceArrayDriver_IsNull = _BinMDataStd.Handle_BinMDataStd_ReferenceArrayDriver_IsNull
Handle_BinMDataStd_ReferenceListDriver_Create = _BinMDataStd.Handle_BinMDataStd_ReferenceListDriver_Create
Handle_BinMDataStd_ReferenceListDriver_DownCast = _BinMDataStd.Handle_BinMDataStd_ReferenceListDriver_DownCast
Handle_BinMDataStd_ReferenceListDriver_IsNull = _BinMDataStd.Handle_BinMDataStd_ReferenceListDriver_IsNull
Handle_BinMDataStd_RelationDriver_Create = _BinMDataStd.Handle_BinMDataStd_RelationDriver_Create
Handle_BinMDataStd_RelationDriver_DownCast = _BinMDataStd.Handle_BinMDataStd_RelationDriver_DownCast
Handle_BinMDataStd_RelationDriver_IsNull = _BinMDataStd.Handle_BinMDataStd_RelationDriver_IsNull
Handle_BinMDataStd_TickDriver_Create = _BinMDataStd.Handle_BinMDataStd_TickDriver_Create
Handle_BinMDataStd_TickDriver_DownCast = _BinMDataStd.Handle_BinMDataStd_TickDriver_DownCast
Handle_BinMDataStd_TickDriver_IsNull = _BinMDataStd.Handle_BinMDataStd_TickDriver_IsNull
Handle_BinMDataStd_TreeNodeDriver_Create = _BinMDataStd.Handle_BinMDataStd_TreeNodeDriver_Create
Handle_BinMDataStd_TreeNodeDriver_DownCast = _BinMDataStd.Handle_BinMDataStd_TreeNodeDriver_DownCast
Handle_BinMDataStd_TreeNodeDriver_IsNull = _BinMDataStd.Handle_BinMDataStd_TreeNodeDriver_IsNull
Handle_BinMDataStd_UAttributeDriver_Create = _BinMDataStd.Handle_BinMDataStd_UAttributeDriver_Create
Handle_BinMDataStd_UAttributeDriver_DownCast = _BinMDataStd.Handle_BinMDataStd_UAttributeDriver_DownCast
Handle_BinMDataStd_UAttributeDriver_IsNull = _BinMDataStd.Handle_BinMDataStd_UAttributeDriver_IsNull
Handle_BinMDataStd_VariableDriver_Create = _BinMDataStd.Handle_BinMDataStd_VariableDriver_Create
Handle_BinMDataStd_VariableDriver_DownCast = _BinMDataStd.Handle_BinMDataStd_VariableDriver_DownCast
Handle_BinMDataStd_VariableDriver_IsNull = _BinMDataStd.Handle_BinMDataStd_VariableDriver_IsNull
class binmdatastd(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    AddDrivers = _swig_new_static_method(_BinMDataStd.binmdatastd_AddDrivers)

    __repr__ = _dumps_object


    def __init__(self):
        _BinMDataStd.binmdatastd_swiginit(self, _BinMDataStd.new_binmdatastd())
    __swig_destroy__ = _BinMDataStd.delete_binmdatastd

# Register binmdatastd in _BinMDataStd:
_BinMDataStd.binmdatastd_swigregister(binmdatastd)
binmdatastd_AddDrivers = _BinMDataStd.binmdatastd_AddDrivers

class BinMDataStd_AsciiStringDriver(OCC.Core.BinMDF.BinMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :param theMessageDriver:
        	:type theMessageDriver: Message_Messenger
        	:rtype: None
        """
        _BinMDataStd.BinMDataStd_AsciiStringDriver_swiginit(self, _BinMDataStd.new_BinMDataStd_AsciiStringDriver(*args))
    Paste = _swig_new_instance_method(_BinMDataStd.BinMDataStd_AsciiStringDriver_Paste)


    @staticmethod
    def DownCast(t):
      return Handle_BinMDataStd_AsciiStringDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _BinMDataStd.delete_BinMDataStd_AsciiStringDriver

# Register BinMDataStd_AsciiStringDriver in _BinMDataStd:
_BinMDataStd.BinMDataStd_AsciiStringDriver_swigregister(BinMDataStd_AsciiStringDriver)

class BinMDataStd_BooleanArrayDriver(OCC.Core.BinMDF.BinMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :param theMessageDriver:
        	:type theMessageDriver: Message_Messenger
        	:rtype: None
        """
        _BinMDataStd.BinMDataStd_BooleanArrayDriver_swiginit(self, _BinMDataStd.new_BinMDataStd_BooleanArrayDriver(*args))
    Paste = _swig_new_instance_method(_BinMDataStd.BinMDataStd_BooleanArrayDriver_Paste)


    @staticmethod
    def DownCast(t):
      return Handle_BinMDataStd_BooleanArrayDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _BinMDataStd.delete_BinMDataStd_BooleanArrayDriver

# Register BinMDataStd_BooleanArrayDriver in _BinMDataStd:
_BinMDataStd.BinMDataStd_BooleanArrayDriver_swigregister(BinMDataStd_BooleanArrayDriver)

class BinMDataStd_BooleanListDriver(OCC.Core.BinMDF.BinMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :param theMessageDriver:
        	:type theMessageDriver: Message_Messenger
        	:rtype: None
        """
        _BinMDataStd.BinMDataStd_BooleanListDriver_swiginit(self, _BinMDataStd.new_BinMDataStd_BooleanListDriver(*args))
    Paste = _swig_new_instance_method(_BinMDataStd.BinMDataStd_BooleanListDriver_Paste)


    @staticmethod
    def DownCast(t):
      return Handle_BinMDataStd_BooleanListDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _BinMDataStd.delete_BinMDataStd_BooleanListDriver

# Register BinMDataStd_BooleanListDriver in _BinMDataStd:
_BinMDataStd.BinMDataStd_BooleanListDriver_swigregister(BinMDataStd_BooleanListDriver)

class BinMDataStd_ByteArrayDriver(OCC.Core.BinMDF.BinMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :param theMessageDriver:
        	:type theMessageDriver: Message_Messenger
        	:rtype: None
        """
        _BinMDataStd.BinMDataStd_ByteArrayDriver_swiginit(self, _BinMDataStd.new_BinMDataStd_ByteArrayDriver(*args))
    Paste = _swig_new_instance_method(_BinMDataStd.BinMDataStd_ByteArrayDriver_Paste)


    @staticmethod
    def DownCast(t):
      return Handle_BinMDataStd_ByteArrayDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _BinMDataStd.delete_BinMDataStd_ByteArrayDriver

# Register BinMDataStd_ByteArrayDriver in _BinMDataStd:
_BinMDataStd.BinMDataStd_ByteArrayDriver_swigregister(BinMDataStd_ByteArrayDriver)

class BinMDataStd_CommentDriver(OCC.Core.BinMDF.BinMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :param theMessageDriver:
        	:type theMessageDriver: Message_Messenger
        	:rtype: None
        """
        _BinMDataStd.BinMDataStd_CommentDriver_swiginit(self, _BinMDataStd.new_BinMDataStd_CommentDriver(*args))
    Paste = _swig_new_instance_method(_BinMDataStd.BinMDataStd_CommentDriver_Paste)


    @staticmethod
    def DownCast(t):
      return Handle_BinMDataStd_CommentDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _BinMDataStd.delete_BinMDataStd_CommentDriver

# Register BinMDataStd_CommentDriver in _BinMDataStd:
_BinMDataStd.BinMDataStd_CommentDriver_swigregister(BinMDataStd_CommentDriver)

class BinMDataStd_DirectoryDriver(OCC.Core.BinMDF.BinMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :param theMessageDriver:
        	:type theMessageDriver: Message_Messenger
        	:rtype: None
        """
        _BinMDataStd.BinMDataStd_DirectoryDriver_swiginit(self, _BinMDataStd.new_BinMDataStd_DirectoryDriver(*args))
    Paste = _swig_new_instance_method(_BinMDataStd.BinMDataStd_DirectoryDriver_Paste)


    @staticmethod
    def DownCast(t):
      return Handle_BinMDataStd_DirectoryDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _BinMDataStd.delete_BinMDataStd_DirectoryDriver

# Register BinMDataStd_DirectoryDriver in _BinMDataStd:
_BinMDataStd.BinMDataStd_DirectoryDriver_swigregister(BinMDataStd_DirectoryDriver)

class BinMDataStd_ExpressionDriver(OCC.Core.BinMDF.BinMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :param theMessageDriver:
        	:type theMessageDriver: Message_Messenger
        	:rtype: None
        """
        _BinMDataStd.BinMDataStd_ExpressionDriver_swiginit(self, _BinMDataStd.new_BinMDataStd_ExpressionDriver(*args))
    Paste = _swig_new_instance_method(_BinMDataStd.BinMDataStd_ExpressionDriver_Paste)


    @staticmethod
    def DownCast(t):
      return Handle_BinMDataStd_ExpressionDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _BinMDataStd.delete_BinMDataStd_ExpressionDriver

# Register BinMDataStd_ExpressionDriver in _BinMDataStd:
_BinMDataStd.BinMDataStd_ExpressionDriver_swigregister(BinMDataStd_ExpressionDriver)

class BinMDataStd_ExtStringArrayDriver(OCC.Core.BinMDF.BinMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :param theMessageDriver:
        	:type theMessageDriver: Message_Messenger
        	:rtype: None
        """
        _BinMDataStd.BinMDataStd_ExtStringArrayDriver_swiginit(self, _BinMDataStd.new_BinMDataStd_ExtStringArrayDriver(*args))
    Paste = _swig_new_instance_method(_BinMDataStd.BinMDataStd_ExtStringArrayDriver_Paste)


    @staticmethod
    def DownCast(t):
      return Handle_BinMDataStd_ExtStringArrayDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _BinMDataStd.delete_BinMDataStd_ExtStringArrayDriver

# Register BinMDataStd_ExtStringArrayDriver in _BinMDataStd:
_BinMDataStd.BinMDataStd_ExtStringArrayDriver_swigregister(BinMDataStd_ExtStringArrayDriver)

class BinMDataStd_ExtStringListDriver(OCC.Core.BinMDF.BinMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :param theMessageDriver:
        	:type theMessageDriver: Message_Messenger
        	:rtype: None
        """
        _BinMDataStd.BinMDataStd_ExtStringListDriver_swiginit(self, _BinMDataStd.new_BinMDataStd_ExtStringListDriver(*args))
    Paste = _swig_new_instance_method(_BinMDataStd.BinMDataStd_ExtStringListDriver_Paste)


    @staticmethod
    def DownCast(t):
      return Handle_BinMDataStd_ExtStringListDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _BinMDataStd.delete_BinMDataStd_ExtStringListDriver

# Register BinMDataStd_ExtStringListDriver in _BinMDataStd:
_BinMDataStd.BinMDataStd_ExtStringListDriver_swigregister(BinMDataStd_ExtStringListDriver)

class BinMDataStd_IntPackedMapDriver(OCC.Core.BinMDF.BinMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :param theMessageDriver:
        	:type theMessageDriver: Message_Messenger
        	:rtype: None
        """
        _BinMDataStd.BinMDataStd_IntPackedMapDriver_swiginit(self, _BinMDataStd.new_BinMDataStd_IntPackedMapDriver(*args))
    Paste = _swig_new_instance_method(_BinMDataStd.BinMDataStd_IntPackedMapDriver_Paste)


    @staticmethod
    def DownCast(t):
      return Handle_BinMDataStd_IntPackedMapDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _BinMDataStd.delete_BinMDataStd_IntPackedMapDriver

# Register BinMDataStd_IntPackedMapDriver in _BinMDataStd:
_BinMDataStd.BinMDataStd_IntPackedMapDriver_swigregister(BinMDataStd_IntPackedMapDriver)

class BinMDataStd_IntegerArrayDriver(OCC.Core.BinMDF.BinMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :param theMessageDriver:
        	:type theMessageDriver: Message_Messenger
        	:rtype: None
        """
        _BinMDataStd.BinMDataStd_IntegerArrayDriver_swiginit(self, _BinMDataStd.new_BinMDataStd_IntegerArrayDriver(*args))
    Paste = _swig_new_instance_method(_BinMDataStd.BinMDataStd_IntegerArrayDriver_Paste)


    @staticmethod
    def DownCast(t):
      return Handle_BinMDataStd_IntegerArrayDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _BinMDataStd.delete_BinMDataStd_IntegerArrayDriver

# Register BinMDataStd_IntegerArrayDriver in _BinMDataStd:
_BinMDataStd.BinMDataStd_IntegerArrayDriver_swigregister(BinMDataStd_IntegerArrayDriver)

class BinMDataStd_IntegerDriver(OCC.Core.BinMDF.BinMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :param theMessageDriver:
        	:type theMessageDriver: Message_Messenger
        	:rtype: None
        """
        _BinMDataStd.BinMDataStd_IntegerDriver_swiginit(self, _BinMDataStd.new_BinMDataStd_IntegerDriver(*args))
    Paste = _swig_new_instance_method(_BinMDataStd.BinMDataStd_IntegerDriver_Paste)


    @staticmethod
    def DownCast(t):
      return Handle_BinMDataStd_IntegerDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _BinMDataStd.delete_BinMDataStd_IntegerDriver

# Register BinMDataStd_IntegerDriver in _BinMDataStd:
_BinMDataStd.BinMDataStd_IntegerDriver_swigregister(BinMDataStd_IntegerDriver)

class BinMDataStd_IntegerListDriver(OCC.Core.BinMDF.BinMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :param theMessageDriver:
        	:type theMessageDriver: Message_Messenger
        	:rtype: None
        """
        _BinMDataStd.BinMDataStd_IntegerListDriver_swiginit(self, _BinMDataStd.new_BinMDataStd_IntegerListDriver(*args))
    Paste = _swig_new_instance_method(_BinMDataStd.BinMDataStd_IntegerListDriver_Paste)


    @staticmethod
    def DownCast(t):
      return Handle_BinMDataStd_IntegerListDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _BinMDataStd.delete_BinMDataStd_IntegerListDriver

# Register BinMDataStd_IntegerListDriver in _BinMDataStd:
_BinMDataStd.BinMDataStd_IntegerListDriver_swigregister(BinMDataStd_IntegerListDriver)

class BinMDataStd_NameDriver(OCC.Core.BinMDF.BinMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :param theMessageDriver:
        	:type theMessageDriver: Message_Messenger
        	:rtype: None
        """
        _BinMDataStd.BinMDataStd_NameDriver_swiginit(self, _BinMDataStd.new_BinMDataStd_NameDriver(*args))
    Paste = _swig_new_instance_method(_BinMDataStd.BinMDataStd_NameDriver_Paste)


    @staticmethod
    def DownCast(t):
      return Handle_BinMDataStd_NameDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _BinMDataStd.delete_BinMDataStd_NameDriver

# Register BinMDataStd_NameDriver in _BinMDataStd:
_BinMDataStd.BinMDataStd_NameDriver_swigregister(BinMDataStd_NameDriver)

class BinMDataStd_NamedDataDriver(OCC.Core.BinMDF.BinMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :param theMessageDriver:
        	:type theMessageDriver: Message_Messenger
        	:rtype: None
        """
        _BinMDataStd.BinMDataStd_NamedDataDriver_swiginit(self, _BinMDataStd.new_BinMDataStd_NamedDataDriver(*args))
    Paste = _swig_new_instance_method(_BinMDataStd.BinMDataStd_NamedDataDriver_Paste)


    @staticmethod
    def DownCast(t):
      return Handle_BinMDataStd_NamedDataDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _BinMDataStd.delete_BinMDataStd_NamedDataDriver

# Register BinMDataStd_NamedDataDriver in _BinMDataStd:
_BinMDataStd.BinMDataStd_NamedDataDriver_swigregister(BinMDataStd_NamedDataDriver)

class BinMDataStd_NoteBookDriver(OCC.Core.BinMDF.BinMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :param theMessageDriver:
        	:type theMessageDriver: Message_Messenger
        	:rtype: None
        """
        _BinMDataStd.BinMDataStd_NoteBookDriver_swiginit(self, _BinMDataStd.new_BinMDataStd_NoteBookDriver(*args))
    Paste = _swig_new_instance_method(_BinMDataStd.BinMDataStd_NoteBookDriver_Paste)


    @staticmethod
    def DownCast(t):
      return Handle_BinMDataStd_NoteBookDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _BinMDataStd.delete_BinMDataStd_NoteBookDriver

# Register BinMDataStd_NoteBookDriver in _BinMDataStd:
_BinMDataStd.BinMDataStd_NoteBookDriver_swigregister(BinMDataStd_NoteBookDriver)

class BinMDataStd_RealArrayDriver(OCC.Core.BinMDF.BinMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :param theMessageDriver:
        	:type theMessageDriver: Message_Messenger
        	:rtype: None
        """
        _BinMDataStd.BinMDataStd_RealArrayDriver_swiginit(self, _BinMDataStd.new_BinMDataStd_RealArrayDriver(*args))
    Paste = _swig_new_instance_method(_BinMDataStd.BinMDataStd_RealArrayDriver_Paste)


    @staticmethod
    def DownCast(t):
      return Handle_BinMDataStd_RealArrayDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _BinMDataStd.delete_BinMDataStd_RealArrayDriver

# Register BinMDataStd_RealArrayDriver in _BinMDataStd:
_BinMDataStd.BinMDataStd_RealArrayDriver_swigregister(BinMDataStd_RealArrayDriver)

class BinMDataStd_RealDriver(OCC.Core.BinMDF.BinMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :param theMessageDriver:
        	:type theMessageDriver: Message_Messenger
        	:rtype: None
        """
        _BinMDataStd.BinMDataStd_RealDriver_swiginit(self, _BinMDataStd.new_BinMDataStd_RealDriver(*args))
    Paste = _swig_new_instance_method(_BinMDataStd.BinMDataStd_RealDriver_Paste)


    @staticmethod
    def DownCast(t):
      return Handle_BinMDataStd_RealDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _BinMDataStd.delete_BinMDataStd_RealDriver

# Register BinMDataStd_RealDriver in _BinMDataStd:
_BinMDataStd.BinMDataStd_RealDriver_swigregister(BinMDataStd_RealDriver)

class BinMDataStd_RealListDriver(OCC.Core.BinMDF.BinMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :param theMessageDriver:
        	:type theMessageDriver: Message_Messenger
        	:rtype: None
        """
        _BinMDataStd.BinMDataStd_RealListDriver_swiginit(self, _BinMDataStd.new_BinMDataStd_RealListDriver(*args))
    Paste = _swig_new_instance_method(_BinMDataStd.BinMDataStd_RealListDriver_Paste)


    @staticmethod
    def DownCast(t):
      return Handle_BinMDataStd_RealListDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _BinMDataStd.delete_BinMDataStd_RealListDriver

# Register BinMDataStd_RealListDriver in _BinMDataStd:
_BinMDataStd.BinMDataStd_RealListDriver_swigregister(BinMDataStd_RealListDriver)

class BinMDataStd_ReferenceArrayDriver(OCC.Core.BinMDF.BinMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :param theMessageDriver:
        	:type theMessageDriver: Message_Messenger
        	:rtype: None
        """
        _BinMDataStd.BinMDataStd_ReferenceArrayDriver_swiginit(self, _BinMDataStd.new_BinMDataStd_ReferenceArrayDriver(*args))
    Paste = _swig_new_instance_method(_BinMDataStd.BinMDataStd_ReferenceArrayDriver_Paste)


    @staticmethod
    def DownCast(t):
      return Handle_BinMDataStd_ReferenceArrayDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _BinMDataStd.delete_BinMDataStd_ReferenceArrayDriver

# Register BinMDataStd_ReferenceArrayDriver in _BinMDataStd:
_BinMDataStd.BinMDataStd_ReferenceArrayDriver_swigregister(BinMDataStd_ReferenceArrayDriver)

class BinMDataStd_ReferenceListDriver(OCC.Core.BinMDF.BinMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :param theMessageDriver:
        	:type theMessageDriver: Message_Messenger
        	:rtype: None
        """
        _BinMDataStd.BinMDataStd_ReferenceListDriver_swiginit(self, _BinMDataStd.new_BinMDataStd_ReferenceListDriver(*args))
    Paste = _swig_new_instance_method(_BinMDataStd.BinMDataStd_ReferenceListDriver_Paste)


    @staticmethod
    def DownCast(t):
      return Handle_BinMDataStd_ReferenceListDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _BinMDataStd.delete_BinMDataStd_ReferenceListDriver

# Register BinMDataStd_ReferenceListDriver in _BinMDataStd:
_BinMDataStd.BinMDataStd_ReferenceListDriver_swigregister(BinMDataStd_ReferenceListDriver)

class BinMDataStd_RelationDriver(OCC.Core.BinMDF.BinMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :param theMessageDriver:
        	:type theMessageDriver: Message_Messenger
        	:rtype: None
        """
        _BinMDataStd.BinMDataStd_RelationDriver_swiginit(self, _BinMDataStd.new_BinMDataStd_RelationDriver(*args))
    Paste = _swig_new_instance_method(_BinMDataStd.BinMDataStd_RelationDriver_Paste)


    @staticmethod
    def DownCast(t):
      return Handle_BinMDataStd_RelationDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _BinMDataStd.delete_BinMDataStd_RelationDriver

# Register BinMDataStd_RelationDriver in _BinMDataStd:
_BinMDataStd.BinMDataStd_RelationDriver_swigregister(BinMDataStd_RelationDriver)

class BinMDataStd_TickDriver(OCC.Core.BinMDF.BinMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :param theMessageDriver:
        	:type theMessageDriver: Message_Messenger
        	:rtype: None
        """
        _BinMDataStd.BinMDataStd_TickDriver_swiginit(self, _BinMDataStd.new_BinMDataStd_TickDriver(*args))
    Paste = _swig_new_instance_method(_BinMDataStd.BinMDataStd_TickDriver_Paste)


    @staticmethod
    def DownCast(t):
      return Handle_BinMDataStd_TickDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _BinMDataStd.delete_BinMDataStd_TickDriver

# Register BinMDataStd_TickDriver in _BinMDataStd:
_BinMDataStd.BinMDataStd_TickDriver_swigregister(BinMDataStd_TickDriver)

class BinMDataStd_TreeNodeDriver(OCC.Core.BinMDF.BinMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :param theMessageDriver:
        	:type theMessageDriver: Message_Messenger
        	:rtype: None
        """
        _BinMDataStd.BinMDataStd_TreeNodeDriver_swiginit(self, _BinMDataStd.new_BinMDataStd_TreeNodeDriver(*args))
    Paste = _swig_new_instance_method(_BinMDataStd.BinMDataStd_TreeNodeDriver_Paste)


    @staticmethod
    def DownCast(t):
      return Handle_BinMDataStd_TreeNodeDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _BinMDataStd.delete_BinMDataStd_TreeNodeDriver

# Register BinMDataStd_TreeNodeDriver in _BinMDataStd:
_BinMDataStd.BinMDataStd_TreeNodeDriver_swigregister(BinMDataStd_TreeNodeDriver)

class BinMDataStd_UAttributeDriver(OCC.Core.BinMDF.BinMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :param theMessageDriver:
        	:type theMessageDriver: Message_Messenger
        	:rtype: None
        """
        _BinMDataStd.BinMDataStd_UAttributeDriver_swiginit(self, _BinMDataStd.new_BinMDataStd_UAttributeDriver(*args))
    Paste = _swig_new_instance_method(_BinMDataStd.BinMDataStd_UAttributeDriver_Paste)


    @staticmethod
    def DownCast(t):
      return Handle_BinMDataStd_UAttributeDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _BinMDataStd.delete_BinMDataStd_UAttributeDriver

# Register BinMDataStd_UAttributeDriver in _BinMDataStd:
_BinMDataStd.BinMDataStd_UAttributeDriver_swigregister(BinMDataStd_UAttributeDriver)

class BinMDataStd_VariableDriver(OCC.Core.BinMDF.BinMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :param theMessageDriver:
        	:type theMessageDriver: Message_Messenger
        	:rtype: None
        """
        _BinMDataStd.BinMDataStd_VariableDriver_swiginit(self, _BinMDataStd.new_BinMDataStd_VariableDriver(*args))
    Paste = _swig_new_instance_method(_BinMDataStd.BinMDataStd_VariableDriver_Paste)


    @staticmethod
    def DownCast(t):
      return Handle_BinMDataStd_VariableDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _BinMDataStd.delete_BinMDataStd_VariableDriver

# Register BinMDataStd_VariableDriver in _BinMDataStd:
_BinMDataStd.BinMDataStd_VariableDriver_swigregister(BinMDataStd_VariableDriver)



