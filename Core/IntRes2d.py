# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
IntRes2d module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_intres2d.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _IntRes2d
else:
    import _IntRes2d

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _IntRes2d.SWIG_PyInstanceMethod_New
_swig_new_static_method = _IntRes2d.SWIG_PyStaticMethod_New

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
    __swig_destroy__ = _IntRes2d.delete_SwigPyIterator
    value = _swig_new_instance_method(_IntRes2d.SwigPyIterator_value)
    incr = _swig_new_instance_method(_IntRes2d.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_IntRes2d.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_IntRes2d.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_IntRes2d.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_IntRes2d.SwigPyIterator_copy)
    next = _swig_new_instance_method(_IntRes2d.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_IntRes2d.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_IntRes2d.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_IntRes2d.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_IntRes2d.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_IntRes2d.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_IntRes2d.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_IntRes2d.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_IntRes2d.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_IntRes2d.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _IntRes2d:
_IntRes2d.SwigPyIterator_swigregister(SwigPyIterator)


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
IntRes2d_Head = _IntRes2d.IntRes2d_Head
IntRes2d_Middle = _IntRes2d.IntRes2d_Middle
IntRes2d_End = _IntRes2d.IntRes2d_End
IntRes2d_Inside = _IntRes2d.IntRes2d_Inside
IntRes2d_Outside = _IntRes2d.IntRes2d_Outside
IntRes2d_Unknown = _IntRes2d.IntRes2d_Unknown
IntRes2d_In = _IntRes2d.IntRes2d_In
IntRes2d_Out = _IntRes2d.IntRes2d_Out
IntRes2d_Touch = _IntRes2d.IntRes2d_Touch
IntRes2d_Undecided = _IntRes2d.IntRes2d_Undecided
class IntRes2d_SequenceOfIntersectionSegment(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionSegment_begin)
    end = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionSegment_end)
    cbegin = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionSegment_cbegin)
    cend = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionSegment_cend)

    def __init__(self, *args):
        _IntRes2d.IntRes2d_SequenceOfIntersectionSegment_swiginit(self, _IntRes2d.new_IntRes2d_SequenceOfIntersectionSegment(*args))
    Size = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionSegment_Size)
    Length = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionSegment_Length)
    Lower = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionSegment_Lower)
    Upper = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionSegment_Upper)
    IsEmpty = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionSegment_IsEmpty)
    Reverse = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionSegment_Reverse)
    Exchange = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionSegment_Exchange)
    delNode = _swig_new_static_method(_IntRes2d.IntRes2d_SequenceOfIntersectionSegment_delNode)
    Clear = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionSegment_Clear)
    Assign = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionSegment_Assign)
    Set = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionSegment_Set)
    Remove = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionSegment_Remove)
    Append = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionSegment_Append)
    Prepend = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionSegment_Prepend)
    InsertBefore = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionSegment_InsertBefore)
    InsertAfter = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionSegment_InsertAfter)
    Split = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionSegment_Split)
    First = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionSegment_First)
    ChangeFirst = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionSegment_ChangeFirst)
    Last = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionSegment_Last)
    ChangeLast = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionSegment_ChangeLast)
    Value = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionSegment_Value)
    ChangeValue = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionSegment_ChangeValue)
    __call__ = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionSegment___call__)
    SetValue = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionSegment_SetValue)
    __swig_destroy__ = _IntRes2d.delete_IntRes2d_SequenceOfIntersectionSegment

# Register IntRes2d_SequenceOfIntersectionSegment in _IntRes2d:
_IntRes2d.IntRes2d_SequenceOfIntersectionSegment_swigregister(IntRes2d_SequenceOfIntersectionSegment)
IntRes2d_SequenceOfIntersectionSegment_delNode = _IntRes2d.IntRes2d_SequenceOfIntersectionSegment_delNode

class IntRes2d_SequenceOfIntersectionPoint(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionPoint_begin)
    end = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionPoint_end)
    cbegin = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionPoint_cbegin)
    cend = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionPoint_cend)

    def __init__(self, *args):
        _IntRes2d.IntRes2d_SequenceOfIntersectionPoint_swiginit(self, _IntRes2d.new_IntRes2d_SequenceOfIntersectionPoint(*args))
    Size = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionPoint_Size)
    Length = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionPoint_Length)
    Lower = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionPoint_Lower)
    Upper = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionPoint_Upper)
    IsEmpty = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionPoint_IsEmpty)
    Reverse = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionPoint_Reverse)
    Exchange = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionPoint_Exchange)
    delNode = _swig_new_static_method(_IntRes2d.IntRes2d_SequenceOfIntersectionPoint_delNode)
    Clear = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionPoint_Clear)
    Assign = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionPoint_Assign)
    Set = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionPoint_Set)
    Remove = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionPoint_Remove)
    Append = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionPoint_Append)
    Prepend = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionPoint_Prepend)
    InsertBefore = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionPoint_InsertBefore)
    InsertAfter = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionPoint_InsertAfter)
    Split = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionPoint_Split)
    First = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionPoint_First)
    ChangeFirst = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionPoint_ChangeFirst)
    Last = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionPoint_Last)
    ChangeLast = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionPoint_ChangeLast)
    Value = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionPoint_Value)
    ChangeValue = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionPoint_ChangeValue)
    __call__ = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionPoint___call__)
    SetValue = _swig_new_instance_method(_IntRes2d.IntRes2d_SequenceOfIntersectionPoint_SetValue)
    __swig_destroy__ = _IntRes2d.delete_IntRes2d_SequenceOfIntersectionPoint

# Register IntRes2d_SequenceOfIntersectionPoint in _IntRes2d:
_IntRes2d.IntRes2d_SequenceOfIntersectionPoint_swigregister(IntRes2d_SequenceOfIntersectionPoint)
IntRes2d_SequenceOfIntersectionPoint_delNode = _IntRes2d.IntRes2d_SequenceOfIntersectionPoint_delNode

class IntRes2d_Domain(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    EquivalentParameters = _swig_new_instance_method(_IntRes2d.IntRes2d_Domain_EquivalentParameters)
    FirstParameter = _swig_new_instance_method(_IntRes2d.IntRes2d_Domain_FirstParameter)
    FirstPoint = _swig_new_instance_method(_IntRes2d.IntRes2d_Domain_FirstPoint)
    FirstTolerance = _swig_new_instance_method(_IntRes2d.IntRes2d_Domain_FirstTolerance)
    HasFirstPoint = _swig_new_instance_method(_IntRes2d.IntRes2d_Domain_HasFirstPoint)
    HasLastPoint = _swig_new_instance_method(_IntRes2d.IntRes2d_Domain_HasLastPoint)

    def __init__(self, *args):
        r"""
        * Creates an infinite Domain (HasFirstPoint = False and HasLastPoint = False).
        	:rtype: None* Creates a bounded Domain.
        	:param Pnt1:
        	:type Pnt1: gp_Pnt2d
        	:param Par1:
        	:type Par1: float
        	:param Tol1:
        	:type Tol1: float
        	:param Pnt2:
        	:type Pnt2: gp_Pnt2d
        	:param Par2:
        	:type Par2: float
        	:param Tol2:
        	:type Tol2: float
        	:rtype: None* Creates a semi-infinite Domain. If First is set to True, the given point is the first point of the domain, otherwise it is the last point.
        	:param Pnt:
        	:type Pnt: gp_Pnt2d
        	:param Par:
        	:type Par: float
        	:param Tol:
        	:type Tol: float
        	:param First:
        	:type First: bool
        	:rtype: None
        """
        _IntRes2d.IntRes2d_Domain_swiginit(self, _IntRes2d.new_IntRes2d_Domain(*args))
    IsClosed = _swig_new_instance_method(_IntRes2d.IntRes2d_Domain_IsClosed)
    LastParameter = _swig_new_instance_method(_IntRes2d.IntRes2d_Domain_LastParameter)
    LastPoint = _swig_new_instance_method(_IntRes2d.IntRes2d_Domain_LastPoint)
    LastTolerance = _swig_new_instance_method(_IntRes2d.IntRes2d_Domain_LastTolerance)
    SetEquivalentParameters = _swig_new_instance_method(_IntRes2d.IntRes2d_Domain_SetEquivalentParameters)
    SetValues = _swig_new_instance_method(_IntRes2d.IntRes2d_Domain_SetValues)

    __repr__ = _dumps_object

    __swig_destroy__ = _IntRes2d.delete_IntRes2d_Domain

# Register IntRes2d_Domain in _IntRes2d:
_IntRes2d.IntRes2d_Domain_swigregister(IntRes2d_Domain)

class IntRes2d_Intersection(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    IsDone = _swig_new_instance_method(_IntRes2d.IntRes2d_Intersection_IsDone)
    IsEmpty = _swig_new_instance_method(_IntRes2d.IntRes2d_Intersection_IsEmpty)
    NbPoints = _swig_new_instance_method(_IntRes2d.IntRes2d_Intersection_NbPoints)
    NbSegments = _swig_new_instance_method(_IntRes2d.IntRes2d_Intersection_NbSegments)
    Point = _swig_new_instance_method(_IntRes2d.IntRes2d_Intersection_Point)
    Segment = _swig_new_instance_method(_IntRes2d.IntRes2d_Intersection_Segment)
    SetReversedParameters = _swig_new_instance_method(_IntRes2d.IntRes2d_Intersection_SetReversedParameters)

    __repr__ = _dumps_object


# Register IntRes2d_Intersection in _IntRes2d:
_IntRes2d.IntRes2d_Intersection_swigregister(IntRes2d_Intersection)

class IntRes2d_IntersectionPoint(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Empty constructor.
        	:rtype: None* Creates an IntersectionPoint. if ReversedFlag is False, the parameter Uc1(resp. Uc2) and the Transition Trans1 (resp. Trans2) refer to the first curve (resp. second curve) otherwise Uc1 and Trans1 (resp. Uc2 and Trans2) refer to the second curve (resp. the first curve).
        	:param P:
        	:type P: gp_Pnt2d
        	:param Uc1:
        	:type Uc1: float
        	:param Uc2:
        	:type Uc2: float
        	:param Trans1:
        	:type Trans1: IntRes2d_Transition
        	:param Trans2:
        	:type Trans2: IntRes2d_Transition
        	:param ReversedFlag:
        	:type ReversedFlag: bool
        	:rtype: None
        """
        _IntRes2d.IntRes2d_IntersectionPoint_swiginit(self, _IntRes2d.new_IntRes2d_IntersectionPoint(*args))
    ParamOnFirst = _swig_new_instance_method(_IntRes2d.IntRes2d_IntersectionPoint_ParamOnFirst)
    ParamOnSecond = _swig_new_instance_method(_IntRes2d.IntRes2d_IntersectionPoint_ParamOnSecond)
    SetValues = _swig_new_instance_method(_IntRes2d.IntRes2d_IntersectionPoint_SetValues)
    TransitionOfFirst = _swig_new_instance_method(_IntRes2d.IntRes2d_IntersectionPoint_TransitionOfFirst)
    TransitionOfSecond = _swig_new_instance_method(_IntRes2d.IntRes2d_IntersectionPoint_TransitionOfSecond)
    Value = _swig_new_instance_method(_IntRes2d.IntRes2d_IntersectionPoint_Value)

    __repr__ = _dumps_object

    __swig_destroy__ = _IntRes2d.delete_IntRes2d_IntersectionPoint

# Register IntRes2d_IntersectionPoint in _IntRes2d:
_IntRes2d.IntRes2d_IntersectionPoint_swigregister(IntRes2d_IntersectionPoint)

class IntRes2d_IntersectionSegment(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    FirstPoint = _swig_new_instance_method(_IntRes2d.IntRes2d_IntersectionSegment_FirstPoint)
    HasFirstPoint = _swig_new_instance_method(_IntRes2d.IntRes2d_IntersectionSegment_HasFirstPoint)
    HasLastPoint = _swig_new_instance_method(_IntRes2d.IntRes2d_IntersectionSegment_HasLastPoint)

    def __init__(self, *args):
        r"""
        * Empty constructor.
        	:rtype: None:param P1:
        	:type P1: IntRes2d_IntersectionPoint
        	:param P2:
        	:type P2: IntRes2d_IntersectionPoint
        	:param Oppos:
        	:type Oppos: bool
        	:param ReverseFlag:
        	:type ReverseFlag: bool
        	:rtype: None:param P:
        	:type P: IntRes2d_IntersectionPoint
        	:param First:
        	:type First: bool
        	:param Oppos:
        	:type Oppos: bool
        	:param ReverseFlag:
        	:type ReverseFlag: bool
        	:rtype: None* Creates an infinite segment of intersection.
        	:param Oppos:
        	:type Oppos: bool
        	:rtype: None
        """
        _IntRes2d.IntRes2d_IntersectionSegment_swiginit(self, _IntRes2d.new_IntRes2d_IntersectionSegment(*args))
    IsOpposite = _swig_new_instance_method(_IntRes2d.IntRes2d_IntersectionSegment_IsOpposite)
    LastPoint = _swig_new_instance_method(_IntRes2d.IntRes2d_IntersectionSegment_LastPoint)

    __repr__ = _dumps_object

    __swig_destroy__ = _IntRes2d.delete_IntRes2d_IntersectionSegment

# Register IntRes2d_IntersectionSegment in _IntRes2d:
_IntRes2d.IntRes2d_IntersectionSegment_swigregister(IntRes2d_IntersectionSegment)

class IntRes2d_Transition(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Empty constructor.
        	:rtype: None* Creates an IN or OUT transition.
        	:param Tangent:
        	:type Tangent: bool
        	:param Pos:
        	:type Pos: IntRes2d_Position
        	:param Type:
        	:type Type: IntRes2d_TypeTrans
        	:rtype: None* Creates a TOUCH transition.
        	:param Tangent:
        	:type Tangent: bool
        	:param Pos:
        	:type Pos: IntRes2d_Position
        	:param Situ:
        	:type Situ: IntRes2d_Situation
        	:param Oppos:
        	:type Oppos: bool
        	:rtype: None* Creates an UNDECIDED transition.
        	:param Pos:
        	:type Pos: IntRes2d_Position
        	:rtype: None
        """
        _IntRes2d.IntRes2d_Transition_swiginit(self, _IntRes2d.new_IntRes2d_Transition(*args))
    IsOpposite = _swig_new_instance_method(_IntRes2d.IntRes2d_Transition_IsOpposite)
    IsTangent = _swig_new_instance_method(_IntRes2d.IntRes2d_Transition_IsTangent)
    PositionOnCurve = _swig_new_instance_method(_IntRes2d.IntRes2d_Transition_PositionOnCurve)
    SetPosition = _swig_new_instance_method(_IntRes2d.IntRes2d_Transition_SetPosition)
    SetValue = _swig_new_instance_method(_IntRes2d.IntRes2d_Transition_SetValue)
    Situation = _swig_new_instance_method(_IntRes2d.IntRes2d_Transition_Situation)
    TransitionType = _swig_new_instance_method(_IntRes2d.IntRes2d_Transition_TransitionType)

    __repr__ = _dumps_object

    __swig_destroy__ = _IntRes2d.delete_IntRes2d_Transition

# Register IntRes2d_Transition in _IntRes2d:
_IntRes2d.IntRes2d_Transition_swigregister(IntRes2d_Transition)


