# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
ExprIntrp module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_exprintrp.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _ExprIntrp
else:
    import _ExprIntrp

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _ExprIntrp.SWIG_PyInstanceMethod_New
_swig_new_static_method = _ExprIntrp.SWIG_PyStaticMethod_New

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
    __swig_destroy__ = _ExprIntrp.delete_SwigPyIterator
    value = _swig_new_instance_method(_ExprIntrp.SwigPyIterator_value)
    incr = _swig_new_instance_method(_ExprIntrp.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_ExprIntrp.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_ExprIntrp.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_ExprIntrp.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_ExprIntrp.SwigPyIterator_copy)
    next = _swig_new_instance_method(_ExprIntrp.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_ExprIntrp.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_ExprIntrp.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_ExprIntrp.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_ExprIntrp.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_ExprIntrp.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_ExprIntrp.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_ExprIntrp.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_ExprIntrp.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_ExprIntrp.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _ExprIntrp:
_ExprIntrp.SwigPyIterator_swigregister(SwigPyIterator)


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
import OCC.Core.Expr
import OCC.Core.TColStd
import OCC.Core.TCollection
Handle_ExprIntrp_Generator_Create = _ExprIntrp.Handle_ExprIntrp_Generator_Create
Handle_ExprIntrp_Generator_DownCast = _ExprIntrp.Handle_ExprIntrp_Generator_DownCast
Handle_ExprIntrp_Generator_IsNull = _ExprIntrp.Handle_ExprIntrp_Generator_IsNull
Handle_ExprIntrp_GenExp_Create = _ExprIntrp.Handle_ExprIntrp_GenExp_Create
Handle_ExprIntrp_GenExp_DownCast = _ExprIntrp.Handle_ExprIntrp_GenExp_DownCast
Handle_ExprIntrp_GenExp_IsNull = _ExprIntrp.Handle_ExprIntrp_GenExp_IsNull
Handle_ExprIntrp_GenFct_Create = _ExprIntrp.Handle_ExprIntrp_GenFct_Create
Handle_ExprIntrp_GenFct_DownCast = _ExprIntrp.Handle_ExprIntrp_GenFct_DownCast
Handle_ExprIntrp_GenFct_IsNull = _ExprIntrp.Handle_ExprIntrp_GenFct_IsNull
Handle_ExprIntrp_GenRel_Create = _ExprIntrp.Handle_ExprIntrp_GenRel_Create
Handle_ExprIntrp_GenRel_DownCast = _ExprIntrp.Handle_ExprIntrp_GenRel_DownCast
Handle_ExprIntrp_GenRel_IsNull = _ExprIntrp.Handle_ExprIntrp_GenRel_IsNull
class ExprIntrp_StackOfGeneralRelation(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralRelation_begin)
    end = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralRelation_end)
    cbegin = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralRelation_cbegin)
    cend = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralRelation_cend)

    def __init__(self, *args):
        _ExprIntrp.ExprIntrp_StackOfGeneralRelation_swiginit(self, _ExprIntrp.new_ExprIntrp_StackOfGeneralRelation(*args))
    Size = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralRelation_Size)
    Assign = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralRelation_Assign)
    Set = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralRelation_Set)
    Clear = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralRelation_Clear)
    First = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralRelation_First)
    Last = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralRelation_Last)
    Append = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralRelation_Append)
    Prepend = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralRelation_Prepend)
    RemoveFirst = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralRelation_RemoveFirst)
    Remove = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralRelation_Remove)
    InsertBefore = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralRelation_InsertBefore)
    InsertAfter = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralRelation_InsertAfter)
    Reverse = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralRelation_Reverse)
    __swig_destroy__ = _ExprIntrp.delete_ExprIntrp_StackOfGeneralRelation

# Register ExprIntrp_StackOfGeneralRelation in _ExprIntrp:
_ExprIntrp.ExprIntrp_StackOfGeneralRelation_swigregister(ExprIntrp_StackOfGeneralRelation)

class ExprIntrp_ListIteratorOfStackOfGeneralRelation(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _ExprIntrp.ExprIntrp_ListIteratorOfStackOfGeneralRelation_swiginit(self, _ExprIntrp.new_ExprIntrp_ListIteratorOfStackOfGeneralRelation(*args))
    More = _swig_new_instance_method(_ExprIntrp.ExprIntrp_ListIteratorOfStackOfGeneralRelation_More)
    Next = _swig_new_instance_method(_ExprIntrp.ExprIntrp_ListIteratorOfStackOfGeneralRelation_Next)
    Value = _swig_new_instance_method(_ExprIntrp.ExprIntrp_ListIteratorOfStackOfGeneralRelation_Value)
    ChangeValue = _swig_new_instance_method(_ExprIntrp.ExprIntrp_ListIteratorOfStackOfGeneralRelation_ChangeValue)
    __swig_destroy__ = _ExprIntrp.delete_ExprIntrp_ListIteratorOfStackOfGeneralRelation

# Register ExprIntrp_ListIteratorOfStackOfGeneralRelation in _ExprIntrp:
_ExprIntrp.ExprIntrp_ListIteratorOfStackOfGeneralRelation_swigregister(ExprIntrp_ListIteratorOfStackOfGeneralRelation)

class ExprIntrp_SequenceOfNamedFunction(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedFunction_begin)
    end = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedFunction_end)
    cbegin = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedFunction_cbegin)
    cend = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedFunction_cend)

    def __init__(self, *args):
        _ExprIntrp.ExprIntrp_SequenceOfNamedFunction_swiginit(self, _ExprIntrp.new_ExprIntrp_SequenceOfNamedFunction(*args))
    Size = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedFunction_Size)
    Length = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedFunction_Length)
    Lower = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedFunction_Lower)
    Upper = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedFunction_Upper)
    IsEmpty = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedFunction_IsEmpty)
    Reverse = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedFunction_Reverse)
    Exchange = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedFunction_Exchange)
    delNode = _swig_new_static_method(_ExprIntrp.ExprIntrp_SequenceOfNamedFunction_delNode)
    Clear = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedFunction_Clear)
    Assign = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedFunction_Assign)
    Set = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedFunction_Set)
    Remove = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedFunction_Remove)
    Append = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedFunction_Append)
    Prepend = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedFunction_Prepend)
    InsertBefore = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedFunction_InsertBefore)
    InsertAfter = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedFunction_InsertAfter)
    Split = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedFunction_Split)
    First = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedFunction_First)
    ChangeFirst = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedFunction_ChangeFirst)
    Last = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedFunction_Last)
    ChangeLast = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedFunction_ChangeLast)
    Value = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedFunction_Value)
    ChangeValue = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedFunction_ChangeValue)
    __call__ = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedFunction___call__)
    SetValue = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedFunction_SetValue)
    __swig_destroy__ = _ExprIntrp.delete_ExprIntrp_SequenceOfNamedFunction

# Register ExprIntrp_SequenceOfNamedFunction in _ExprIntrp:
_ExprIntrp.ExprIntrp_SequenceOfNamedFunction_swigregister(ExprIntrp_SequenceOfNamedFunction)
ExprIntrp_SequenceOfNamedFunction_delNode = _ExprIntrp.ExprIntrp_SequenceOfNamedFunction_delNode

class ExprIntrp_StackOfGeneralFunction(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralFunction_begin)
    end = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralFunction_end)
    cbegin = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralFunction_cbegin)
    cend = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralFunction_cend)

    def __init__(self, *args):
        _ExprIntrp.ExprIntrp_StackOfGeneralFunction_swiginit(self, _ExprIntrp.new_ExprIntrp_StackOfGeneralFunction(*args))
    Size = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralFunction_Size)
    Assign = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralFunction_Assign)
    Set = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralFunction_Set)
    Clear = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralFunction_Clear)
    First = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralFunction_First)
    Last = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralFunction_Last)
    Append = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralFunction_Append)
    Prepend = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralFunction_Prepend)
    RemoveFirst = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralFunction_RemoveFirst)
    Remove = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralFunction_Remove)
    InsertBefore = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralFunction_InsertBefore)
    InsertAfter = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralFunction_InsertAfter)
    Reverse = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralFunction_Reverse)
    __swig_destroy__ = _ExprIntrp.delete_ExprIntrp_StackOfGeneralFunction

# Register ExprIntrp_StackOfGeneralFunction in _ExprIntrp:
_ExprIntrp.ExprIntrp_StackOfGeneralFunction_swigregister(ExprIntrp_StackOfGeneralFunction)

class ExprIntrp_ListIteratorOfStackOfGeneralFunction(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _ExprIntrp.ExprIntrp_ListIteratorOfStackOfGeneralFunction_swiginit(self, _ExprIntrp.new_ExprIntrp_ListIteratorOfStackOfGeneralFunction(*args))
    More = _swig_new_instance_method(_ExprIntrp.ExprIntrp_ListIteratorOfStackOfGeneralFunction_More)
    Next = _swig_new_instance_method(_ExprIntrp.ExprIntrp_ListIteratorOfStackOfGeneralFunction_Next)
    Value = _swig_new_instance_method(_ExprIntrp.ExprIntrp_ListIteratorOfStackOfGeneralFunction_Value)
    ChangeValue = _swig_new_instance_method(_ExprIntrp.ExprIntrp_ListIteratorOfStackOfGeneralFunction_ChangeValue)
    __swig_destroy__ = _ExprIntrp.delete_ExprIntrp_ListIteratorOfStackOfGeneralFunction

# Register ExprIntrp_ListIteratorOfStackOfGeneralFunction in _ExprIntrp:
_ExprIntrp.ExprIntrp_ListIteratorOfStackOfGeneralFunction_swigregister(ExprIntrp_ListIteratorOfStackOfGeneralFunction)

class ExprIntrp_SequenceOfNamedExpression(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedExpression_begin)
    end = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedExpression_end)
    cbegin = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedExpression_cbegin)
    cend = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedExpression_cend)

    def __init__(self, *args):
        _ExprIntrp.ExprIntrp_SequenceOfNamedExpression_swiginit(self, _ExprIntrp.new_ExprIntrp_SequenceOfNamedExpression(*args))
    Size = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedExpression_Size)
    Length = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedExpression_Length)
    Lower = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedExpression_Lower)
    Upper = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedExpression_Upper)
    IsEmpty = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedExpression_IsEmpty)
    Reverse = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedExpression_Reverse)
    Exchange = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedExpression_Exchange)
    delNode = _swig_new_static_method(_ExprIntrp.ExprIntrp_SequenceOfNamedExpression_delNode)
    Clear = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedExpression_Clear)
    Assign = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedExpression_Assign)
    Set = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedExpression_Set)
    Remove = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedExpression_Remove)
    Append = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedExpression_Append)
    Prepend = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedExpression_Prepend)
    InsertBefore = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedExpression_InsertBefore)
    InsertAfter = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedExpression_InsertAfter)
    Split = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedExpression_Split)
    First = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedExpression_First)
    ChangeFirst = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedExpression_ChangeFirst)
    Last = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedExpression_Last)
    ChangeLast = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedExpression_ChangeLast)
    Value = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedExpression_Value)
    ChangeValue = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedExpression_ChangeValue)
    __call__ = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedExpression___call__)
    SetValue = _swig_new_instance_method(_ExprIntrp.ExprIntrp_SequenceOfNamedExpression_SetValue)
    __swig_destroy__ = _ExprIntrp.delete_ExprIntrp_SequenceOfNamedExpression

# Register ExprIntrp_SequenceOfNamedExpression in _ExprIntrp:
_ExprIntrp.ExprIntrp_SequenceOfNamedExpression_swigregister(ExprIntrp_SequenceOfNamedExpression)
ExprIntrp_SequenceOfNamedExpression_delNode = _ExprIntrp.ExprIntrp_SequenceOfNamedExpression_delNode

class ExprIntrp_StackOfGeneralExpression(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralExpression_begin)
    end = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralExpression_end)
    cbegin = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralExpression_cbegin)
    cend = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralExpression_cend)

    def __init__(self, *args):
        _ExprIntrp.ExprIntrp_StackOfGeneralExpression_swiginit(self, _ExprIntrp.new_ExprIntrp_StackOfGeneralExpression(*args))
    Size = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralExpression_Size)
    Assign = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralExpression_Assign)
    Set = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralExpression_Set)
    Clear = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralExpression_Clear)
    First = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralExpression_First)
    Last = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralExpression_Last)
    Append = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralExpression_Append)
    Prepend = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralExpression_Prepend)
    RemoveFirst = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralExpression_RemoveFirst)
    Remove = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralExpression_Remove)
    InsertBefore = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralExpression_InsertBefore)
    InsertAfter = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralExpression_InsertAfter)
    Reverse = _swig_new_instance_method(_ExprIntrp.ExprIntrp_StackOfGeneralExpression_Reverse)
    __swig_destroy__ = _ExprIntrp.delete_ExprIntrp_StackOfGeneralExpression

# Register ExprIntrp_StackOfGeneralExpression in _ExprIntrp:
_ExprIntrp.ExprIntrp_StackOfGeneralExpression_swigregister(ExprIntrp_StackOfGeneralExpression)

class ExprIntrp_ListIteratorOfStackOfGeneralExpression(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _ExprIntrp.ExprIntrp_ListIteratorOfStackOfGeneralExpression_swiginit(self, _ExprIntrp.new_ExprIntrp_ListIteratorOfStackOfGeneralExpression(*args))
    More = _swig_new_instance_method(_ExprIntrp.ExprIntrp_ListIteratorOfStackOfGeneralExpression_More)
    Next = _swig_new_instance_method(_ExprIntrp.ExprIntrp_ListIteratorOfStackOfGeneralExpression_Next)
    Value = _swig_new_instance_method(_ExprIntrp.ExprIntrp_ListIteratorOfStackOfGeneralExpression_Value)
    ChangeValue = _swig_new_instance_method(_ExprIntrp.ExprIntrp_ListIteratorOfStackOfGeneralExpression_ChangeValue)
    __swig_destroy__ = _ExprIntrp.delete_ExprIntrp_ListIteratorOfStackOfGeneralExpression

# Register ExprIntrp_ListIteratorOfStackOfGeneralExpression in _ExprIntrp:
_ExprIntrp.ExprIntrp_ListIteratorOfStackOfGeneralExpression_swigregister(ExprIntrp_ListIteratorOfStackOfGeneralExpression)

class exprintrp(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    __repr__ = _dumps_object


    def __init__(self):
        _ExprIntrp.exprintrp_swiginit(self, _ExprIntrp.new_exprintrp())
    __swig_destroy__ = _ExprIntrp.delete_exprintrp

# Register exprintrp in _ExprIntrp:
_ExprIntrp.exprintrp_swigregister(exprintrp)

class ExprIntrp_Analysis(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r""":rtype: None"""
        _ExprIntrp.ExprIntrp_Analysis_swiginit(self, _ExprIntrp.new_ExprIntrp_Analysis(*args))
    GetFunction = _swig_new_instance_method(_ExprIntrp.ExprIntrp_Analysis_GetFunction)
    GetNamed = _swig_new_instance_method(_ExprIntrp.ExprIntrp_Analysis_GetNamed)
    IsExpStackEmpty = _swig_new_instance_method(_ExprIntrp.ExprIntrp_Analysis_IsExpStackEmpty)
    IsRelStackEmpty = _swig_new_instance_method(_ExprIntrp.ExprIntrp_Analysis_IsRelStackEmpty)
    Pop = _swig_new_instance_method(_ExprIntrp.ExprIntrp_Analysis_Pop)
    PopFunction = _swig_new_instance_method(_ExprIntrp.ExprIntrp_Analysis_PopFunction)
    PopName = _swig_new_instance_method(_ExprIntrp.ExprIntrp_Analysis_PopName)
    PopRelation = _swig_new_instance_method(_ExprIntrp.ExprIntrp_Analysis_PopRelation)
    PopValue = _swig_new_instance_method(_ExprIntrp.ExprIntrp_Analysis_PopValue)
    Push = _swig_new_instance_method(_ExprIntrp.ExprIntrp_Analysis_Push)
    PushFunction = _swig_new_instance_method(_ExprIntrp.ExprIntrp_Analysis_PushFunction)
    PushName = _swig_new_instance_method(_ExprIntrp.ExprIntrp_Analysis_PushName)
    PushRelation = _swig_new_instance_method(_ExprIntrp.ExprIntrp_Analysis_PushRelation)
    PushValue = _swig_new_instance_method(_ExprIntrp.ExprIntrp_Analysis_PushValue)
    ResetAll = _swig_new_instance_method(_ExprIntrp.ExprIntrp_Analysis_ResetAll)
    SetMaster = _swig_new_instance_method(_ExprIntrp.ExprIntrp_Analysis_SetMaster)
    Use = _swig_new_instance_method(_ExprIntrp.ExprIntrp_Analysis_Use)

    __repr__ = _dumps_object

    __swig_destroy__ = _ExprIntrp.delete_ExprIntrp_Analysis

# Register ExprIntrp_Analysis in _ExprIntrp:
_ExprIntrp.ExprIntrp_Analysis_swigregister(ExprIntrp_Analysis)

class ExprIntrp_Generator(OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    GetFunction = _swig_new_instance_method(_ExprIntrp.ExprIntrp_Generator_GetFunction)
    GetFunctions = _swig_new_instance_method(_ExprIntrp.ExprIntrp_Generator_GetFunctions)
    GetNamed = _swig_new_instance_method(_ExprIntrp.ExprIntrp_Generator_GetNamed)
    Use = _swig_new_instance_method(_ExprIntrp.ExprIntrp_Generator_Use)


    @staticmethod
    def DownCast(t):
      return Handle_ExprIntrp_Generator_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _ExprIntrp.delete_ExprIntrp_Generator

# Register ExprIntrp_Generator in _ExprIntrp:
_ExprIntrp.ExprIntrp_Generator_swigregister(ExprIntrp_Generator)

class ExprIntrp_GenExp(ExprIntrp_Generator):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    Create = _swig_new_static_method(_ExprIntrp.ExprIntrp_GenExp_Create)
    Expression = _swig_new_instance_method(_ExprIntrp.ExprIntrp_GenExp_Expression)
    IsDone = _swig_new_instance_method(_ExprIntrp.ExprIntrp_GenExp_IsDone)
    Process = _swig_new_instance_method(_ExprIntrp.ExprIntrp_GenExp_Process)


    @staticmethod
    def DownCast(t):
      return Handle_ExprIntrp_GenExp_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _ExprIntrp.delete_ExprIntrp_GenExp

# Register ExprIntrp_GenExp in _ExprIntrp:
_ExprIntrp.ExprIntrp_GenExp_swigregister(ExprIntrp_GenExp)
ExprIntrp_GenExp_Create = _ExprIntrp.ExprIntrp_GenExp_Create

class ExprIntrp_GenFct(ExprIntrp_Generator):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    Create = _swig_new_static_method(_ExprIntrp.ExprIntrp_GenFct_Create)
    IsDone = _swig_new_instance_method(_ExprIntrp.ExprIntrp_GenFct_IsDone)
    Process = _swig_new_instance_method(_ExprIntrp.ExprIntrp_GenFct_Process)


    @staticmethod
    def DownCast(t):
      return Handle_ExprIntrp_GenFct_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _ExprIntrp.delete_ExprIntrp_GenFct

# Register ExprIntrp_GenFct in _ExprIntrp:
_ExprIntrp.ExprIntrp_GenFct_swigregister(ExprIntrp_GenFct)
ExprIntrp_GenFct_Create = _ExprIntrp.ExprIntrp_GenFct_Create

class ExprIntrp_GenRel(ExprIntrp_Generator):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    Create = _swig_new_static_method(_ExprIntrp.ExprIntrp_GenRel_Create)
    IsDone = _swig_new_instance_method(_ExprIntrp.ExprIntrp_GenRel_IsDone)
    Process = _swig_new_instance_method(_ExprIntrp.ExprIntrp_GenRel_Process)
    Relation = _swig_new_instance_method(_ExprIntrp.ExprIntrp_GenRel_Relation)


    @staticmethod
    def DownCast(t):
      return Handle_ExprIntrp_GenRel_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _ExprIntrp.delete_ExprIntrp_GenRel

# Register ExprIntrp_GenRel in _ExprIntrp:
_ExprIntrp.ExprIntrp_GenRel_swigregister(ExprIntrp_GenRel)
ExprIntrp_GenRel_Create = _ExprIntrp.ExprIntrp_GenRel_Create



