# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
TFunction module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_tfunction.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _TFunction
else:
    import _TFunction

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _TFunction.SWIG_PyInstanceMethod_New
_swig_new_static_method = _TFunction.SWIG_PyStaticMethod_New

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
    __swig_destroy__ = _TFunction.delete_SwigPyIterator
    value = _swig_new_instance_method(_TFunction.SwigPyIterator_value)
    incr = _swig_new_instance_method(_TFunction.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_TFunction.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_TFunction.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_TFunction.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_TFunction.SwigPyIterator_copy)
    next = _swig_new_instance_method(_TFunction.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_TFunction.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_TFunction.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_TFunction.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_TFunction.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_TFunction.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_TFunction.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_TFunction.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_TFunction.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_TFunction.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _TFunction:
_TFunction.SwigPyIterator_swigregister(SwigPyIterator)


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
import OCC.Core.TDF
import OCC.Core.TCollection
import OCC.Core.TColStd
TFunction_ES_WrongDefinition = _TFunction.TFunction_ES_WrongDefinition
TFunction_ES_NotExecuted = _TFunction.TFunction_ES_NotExecuted
TFunction_ES_Executing = _TFunction.TFunction_ES_Executing
TFunction_ES_Succeeded = _TFunction.TFunction_ES_Succeeded
TFunction_ES_Failed = _TFunction.TFunction_ES_Failed
Handle_TFunction_Driver_Create = _TFunction.Handle_TFunction_Driver_Create
Handle_TFunction_Driver_DownCast = _TFunction.Handle_TFunction_Driver_DownCast
Handle_TFunction_Driver_IsNull = _TFunction.Handle_TFunction_Driver_IsNull
Handle_TFunction_DriverTable_Create = _TFunction.Handle_TFunction_DriverTable_Create
Handle_TFunction_DriverTable_DownCast = _TFunction.Handle_TFunction_DriverTable_DownCast
Handle_TFunction_DriverTable_IsNull = _TFunction.Handle_TFunction_DriverTable_IsNull
Handle_TFunction_Function_Create = _TFunction.Handle_TFunction_Function_Create
Handle_TFunction_Function_DownCast = _TFunction.Handle_TFunction_Function_DownCast
Handle_TFunction_Function_IsNull = _TFunction.Handle_TFunction_Function_IsNull
Handle_TFunction_GraphNode_Create = _TFunction.Handle_TFunction_GraphNode_Create
Handle_TFunction_GraphNode_DownCast = _TFunction.Handle_TFunction_GraphNode_DownCast
Handle_TFunction_GraphNode_IsNull = _TFunction.Handle_TFunction_GraphNode_IsNull
Handle_TFunction_Logbook_Create = _TFunction.Handle_TFunction_Logbook_Create
Handle_TFunction_Logbook_DownCast = _TFunction.Handle_TFunction_Logbook_DownCast
Handle_TFunction_Logbook_IsNull = _TFunction.Handle_TFunction_Logbook_IsNull
Handle_TFunction_Scope_Create = _TFunction.Handle_TFunction_Scope_Create
Handle_TFunction_Scope_DownCast = _TFunction.Handle_TFunction_Scope_DownCast
Handle_TFunction_Scope_IsNull = _TFunction.Handle_TFunction_Scope_IsNull
Handle_TFunction_HArray1OfDataMapOfGUIDDriver_Create = _TFunction.Handle_TFunction_HArray1OfDataMapOfGUIDDriver_Create
Handle_TFunction_HArray1OfDataMapOfGUIDDriver_DownCast = _TFunction.Handle_TFunction_HArray1OfDataMapOfGUIDDriver_DownCast
Handle_TFunction_HArray1OfDataMapOfGUIDDriver_IsNull = _TFunction.Handle_TFunction_HArray1OfDataMapOfGUIDDriver_IsNull
class TFunction_Array1OfDataMapOfGUIDDriver(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_TFunction.TFunction_Array1OfDataMapOfGUIDDriver_begin)
    end = _swig_new_instance_method(_TFunction.TFunction_Array1OfDataMapOfGUIDDriver_end)
    cbegin = _swig_new_instance_method(_TFunction.TFunction_Array1OfDataMapOfGUIDDriver_cbegin)
    cend = _swig_new_instance_method(_TFunction.TFunction_Array1OfDataMapOfGUIDDriver_cend)

    def __init__(self, *args):
        _TFunction.TFunction_Array1OfDataMapOfGUIDDriver_swiginit(self, _TFunction.new_TFunction_Array1OfDataMapOfGUIDDriver(*args))
    Init = _swig_new_instance_method(_TFunction.TFunction_Array1OfDataMapOfGUIDDriver_Init)
    Size = _swig_new_instance_method(_TFunction.TFunction_Array1OfDataMapOfGUIDDriver_Size)
    Length = _swig_new_instance_method(_TFunction.TFunction_Array1OfDataMapOfGUIDDriver_Length)
    IsEmpty = _swig_new_instance_method(_TFunction.TFunction_Array1OfDataMapOfGUIDDriver_IsEmpty)
    Lower = _swig_new_instance_method(_TFunction.TFunction_Array1OfDataMapOfGUIDDriver_Lower)
    Upper = _swig_new_instance_method(_TFunction.TFunction_Array1OfDataMapOfGUIDDriver_Upper)
    IsDeletable = _swig_new_instance_method(_TFunction.TFunction_Array1OfDataMapOfGUIDDriver_IsDeletable)
    IsAllocated = _swig_new_instance_method(_TFunction.TFunction_Array1OfDataMapOfGUIDDriver_IsAllocated)
    Assign = _swig_new_instance_method(_TFunction.TFunction_Array1OfDataMapOfGUIDDriver_Assign)
    Move = _swig_new_instance_method(_TFunction.TFunction_Array1OfDataMapOfGUIDDriver_Move)
    Set = _swig_new_instance_method(_TFunction.TFunction_Array1OfDataMapOfGUIDDriver_Set)
    First = _swig_new_instance_method(_TFunction.TFunction_Array1OfDataMapOfGUIDDriver_First)
    ChangeFirst = _swig_new_instance_method(_TFunction.TFunction_Array1OfDataMapOfGUIDDriver_ChangeFirst)
    Last = _swig_new_instance_method(_TFunction.TFunction_Array1OfDataMapOfGUIDDriver_Last)
    ChangeLast = _swig_new_instance_method(_TFunction.TFunction_Array1OfDataMapOfGUIDDriver_ChangeLast)
    Value = _swig_new_instance_method(_TFunction.TFunction_Array1OfDataMapOfGUIDDriver_Value)
    ChangeValue = _swig_new_instance_method(_TFunction.TFunction_Array1OfDataMapOfGUIDDriver_ChangeValue)
    __call__ = _swig_new_instance_method(_TFunction.TFunction_Array1OfDataMapOfGUIDDriver___call__)
    SetValue = _swig_new_instance_method(_TFunction.TFunction_Array1OfDataMapOfGUIDDriver_SetValue)
    Resize = _swig_new_instance_method(_TFunction.TFunction_Array1OfDataMapOfGUIDDriver_Resize)
    __swig_destroy__ = _TFunction.delete_TFunction_Array1OfDataMapOfGUIDDriver

    def __getitem__(self, index):
        if index + self.Lower() > self.Upper():
            raise IndexError("index out of range")
        else:
            return self.Value(index + self.Lower())

    def __setitem__(self, index, value):
        if index + self.Lower() > self.Upper():
            raise IndexError("index out of range")
        else:
            self.SetValue(index + self.Lower(), value)

    def __len__(self):
        return self.Length()

    def __iter__(self):
        self.low = self.Lower()
        self.up = self.Upper()
        self.current = self.Lower() - 1
        return self

    def next(self):
        if self.current >= self.Upper():
            raise StopIteration
        else:
            self.current += 1
        return self.Value(self.current)

    __next__ = next


# Register TFunction_Array1OfDataMapOfGUIDDriver in _TFunction:
_TFunction.TFunction_Array1OfDataMapOfGUIDDriver_swigregister(TFunction_Array1OfDataMapOfGUIDDriver)

class TFunction_DataMapOfGUIDDriver(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_TFunction.TFunction_DataMapOfGUIDDriver_begin)
    end = _swig_new_instance_method(_TFunction.TFunction_DataMapOfGUIDDriver_end)
    cbegin = _swig_new_instance_method(_TFunction.TFunction_DataMapOfGUIDDriver_cbegin)
    cend = _swig_new_instance_method(_TFunction.TFunction_DataMapOfGUIDDriver_cend)

    def __init__(self, *args):
        _TFunction.TFunction_DataMapOfGUIDDriver_swiginit(self, _TFunction.new_TFunction_DataMapOfGUIDDriver(*args))
    Exchange = _swig_new_instance_method(_TFunction.TFunction_DataMapOfGUIDDriver_Exchange)
    Assign = _swig_new_instance_method(_TFunction.TFunction_DataMapOfGUIDDriver_Assign)
    Set = _swig_new_instance_method(_TFunction.TFunction_DataMapOfGUIDDriver_Set)
    ReSize = _swig_new_instance_method(_TFunction.TFunction_DataMapOfGUIDDriver_ReSize)
    Bind = _swig_new_instance_method(_TFunction.TFunction_DataMapOfGUIDDriver_Bind)
    Bound = _swig_new_instance_method(_TFunction.TFunction_DataMapOfGUIDDriver_Bound)
    IsBound = _swig_new_instance_method(_TFunction.TFunction_DataMapOfGUIDDriver_IsBound)
    UnBind = _swig_new_instance_method(_TFunction.TFunction_DataMapOfGUIDDriver_UnBind)
    Seek = _swig_new_instance_method(_TFunction.TFunction_DataMapOfGUIDDriver_Seek)
    Find = _swig_new_instance_method(_TFunction.TFunction_DataMapOfGUIDDriver_Find)
    ChangeSeek = _swig_new_instance_method(_TFunction.TFunction_DataMapOfGUIDDriver_ChangeSeek)
    ChangeFind = _swig_new_instance_method(_TFunction.TFunction_DataMapOfGUIDDriver_ChangeFind)
    __call__ = _swig_new_instance_method(_TFunction.TFunction_DataMapOfGUIDDriver___call__)
    Clear = _swig_new_instance_method(_TFunction.TFunction_DataMapOfGUIDDriver_Clear)
    __swig_destroy__ = _TFunction.delete_TFunction_DataMapOfGUIDDriver
    Size = _swig_new_instance_method(_TFunction.TFunction_DataMapOfGUIDDriver_Size)

# Register TFunction_DataMapOfGUIDDriver in _TFunction:
_TFunction.TFunction_DataMapOfGUIDDriver_swigregister(TFunction_DataMapOfGUIDDriver)

class TFunction_DoubleMapOfIntegerLabel(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _TFunction.TFunction_DoubleMapOfIntegerLabel_swiginit(self, _TFunction.new_TFunction_DoubleMapOfIntegerLabel(*args))
    Exchange = _swig_new_instance_method(_TFunction.TFunction_DoubleMapOfIntegerLabel_Exchange)
    Assign = _swig_new_instance_method(_TFunction.TFunction_DoubleMapOfIntegerLabel_Assign)
    Set = _swig_new_instance_method(_TFunction.TFunction_DoubleMapOfIntegerLabel_Set)
    ReSize = _swig_new_instance_method(_TFunction.TFunction_DoubleMapOfIntegerLabel_ReSize)
    Bind = _swig_new_instance_method(_TFunction.TFunction_DoubleMapOfIntegerLabel_Bind)
    AreBound = _swig_new_instance_method(_TFunction.TFunction_DoubleMapOfIntegerLabel_AreBound)
    IsBound1 = _swig_new_instance_method(_TFunction.TFunction_DoubleMapOfIntegerLabel_IsBound1)
    IsBound2 = _swig_new_instance_method(_TFunction.TFunction_DoubleMapOfIntegerLabel_IsBound2)
    UnBind1 = _swig_new_instance_method(_TFunction.TFunction_DoubleMapOfIntegerLabel_UnBind1)
    UnBind2 = _swig_new_instance_method(_TFunction.TFunction_DoubleMapOfIntegerLabel_UnBind2)
    Find1 = _swig_new_instance_method(_TFunction.TFunction_DoubleMapOfIntegerLabel_Find1)
    Seek1 = _swig_new_instance_method(_TFunction.TFunction_DoubleMapOfIntegerLabel_Seek1)
    Find2 = _swig_new_instance_method(_TFunction.TFunction_DoubleMapOfIntegerLabel_Find2)
    Seek2 = _swig_new_instance_method(_TFunction.TFunction_DoubleMapOfIntegerLabel_Seek2)
    Clear = _swig_new_instance_method(_TFunction.TFunction_DoubleMapOfIntegerLabel_Clear)
    __swig_destroy__ = _TFunction.delete_TFunction_DoubleMapOfIntegerLabel
    Size = _swig_new_instance_method(_TFunction.TFunction_DoubleMapOfIntegerLabel_Size)

# Register TFunction_DoubleMapOfIntegerLabel in _TFunction:
_TFunction.TFunction_DoubleMapOfIntegerLabel_swigregister(TFunction_DoubleMapOfIntegerLabel)

class TFunction_DataMapOfLabelListOfLabel(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_TFunction.TFunction_DataMapOfLabelListOfLabel_begin)
    end = _swig_new_instance_method(_TFunction.TFunction_DataMapOfLabelListOfLabel_end)
    cbegin = _swig_new_instance_method(_TFunction.TFunction_DataMapOfLabelListOfLabel_cbegin)
    cend = _swig_new_instance_method(_TFunction.TFunction_DataMapOfLabelListOfLabel_cend)

    def __init__(self, *args):
        _TFunction.TFunction_DataMapOfLabelListOfLabel_swiginit(self, _TFunction.new_TFunction_DataMapOfLabelListOfLabel(*args))
    Exchange = _swig_new_instance_method(_TFunction.TFunction_DataMapOfLabelListOfLabel_Exchange)
    Assign = _swig_new_instance_method(_TFunction.TFunction_DataMapOfLabelListOfLabel_Assign)
    Set = _swig_new_instance_method(_TFunction.TFunction_DataMapOfLabelListOfLabel_Set)
    ReSize = _swig_new_instance_method(_TFunction.TFunction_DataMapOfLabelListOfLabel_ReSize)
    Bind = _swig_new_instance_method(_TFunction.TFunction_DataMapOfLabelListOfLabel_Bind)
    Bound = _swig_new_instance_method(_TFunction.TFunction_DataMapOfLabelListOfLabel_Bound)
    IsBound = _swig_new_instance_method(_TFunction.TFunction_DataMapOfLabelListOfLabel_IsBound)
    UnBind = _swig_new_instance_method(_TFunction.TFunction_DataMapOfLabelListOfLabel_UnBind)
    Seek = _swig_new_instance_method(_TFunction.TFunction_DataMapOfLabelListOfLabel_Seek)
    Find = _swig_new_instance_method(_TFunction.TFunction_DataMapOfLabelListOfLabel_Find)
    ChangeSeek = _swig_new_instance_method(_TFunction.TFunction_DataMapOfLabelListOfLabel_ChangeSeek)
    ChangeFind = _swig_new_instance_method(_TFunction.TFunction_DataMapOfLabelListOfLabel_ChangeFind)
    __call__ = _swig_new_instance_method(_TFunction.TFunction_DataMapOfLabelListOfLabel___call__)
    Clear = _swig_new_instance_method(_TFunction.TFunction_DataMapOfLabelListOfLabel_Clear)
    __swig_destroy__ = _TFunction.delete_TFunction_DataMapOfLabelListOfLabel
    Size = _swig_new_instance_method(_TFunction.TFunction_DataMapOfLabelListOfLabel_Size)

# Register TFunction_DataMapOfLabelListOfLabel in _TFunction:
_TFunction.TFunction_DataMapOfLabelListOfLabel_swigregister(TFunction_DataMapOfLabelListOfLabel)

class TFunction_Driver(OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    Arguments = _swig_new_instance_method(_TFunction.TFunction_Driver_Arguments)
    Execute = _swig_new_instance_method(_TFunction.TFunction_Driver_Execute)
    Init = _swig_new_instance_method(_TFunction.TFunction_Driver_Init)
    Label = _swig_new_instance_method(_TFunction.TFunction_Driver_Label)
    MustExecute = _swig_new_instance_method(_TFunction.TFunction_Driver_MustExecute)
    Results = _swig_new_instance_method(_TFunction.TFunction_Driver_Results)
    Validate = _swig_new_instance_method(_TFunction.TFunction_Driver_Validate)


    @staticmethod
    def DownCast(t):
      return Handle_TFunction_Driver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _TFunction.delete_TFunction_Driver

# Register TFunction_Driver in _TFunction:
_TFunction.TFunction_Driver_swigregister(TFunction_Driver)

class TFunction_DriverTable(OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    AddDriver = _swig_new_instance_method(_TFunction.TFunction_DriverTable_AddDriver)
    Clear = _swig_new_instance_method(_TFunction.TFunction_DriverTable_Clear)
    DumpToString = _swig_new_instance_method(_TFunction.TFunction_DriverTable_DumpToString)
    FindDriver = _swig_new_instance_method(_TFunction.TFunction_DriverTable_FindDriver)
    Get = _swig_new_static_method(_TFunction.TFunction_DriverTable_Get)
    HasDriver = _swig_new_instance_method(_TFunction.TFunction_DriverTable_HasDriver)
    RemoveDriver = _swig_new_instance_method(_TFunction.TFunction_DriverTable_RemoveDriver)

    def __init__(self, *args):
        r"""
        * Default constructor
        	:rtype: None
        """
        _TFunction.TFunction_DriverTable_swiginit(self, _TFunction.new_TFunction_DriverTable(*args))


    @staticmethod
    def DownCast(t):
      return Handle_TFunction_DriverTable_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _TFunction.delete_TFunction_DriverTable

# Register TFunction_DriverTable in _TFunction:
_TFunction.TFunction_DriverTable_swigregister(TFunction_DriverTable)
TFunction_DriverTable_Get = _TFunction.TFunction_DriverTable_Get

class TFunction_Function(OCC.Core.TDF.TDF_Attribute):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    DumpToString = _swig_new_instance_method(_TFunction.TFunction_Function_DumpToString)
    Failed = _swig_new_instance_method(_TFunction.TFunction_Function_Failed)
    GetDriverGUID = _swig_new_instance_method(_TFunction.TFunction_Function_GetDriverGUID)
    GetFailure = _swig_new_instance_method(_TFunction.TFunction_Function_GetFailure)
    GetID = _swig_new_static_method(_TFunction.TFunction_Function_GetID)
    Set = _swig_new_static_method(_TFunction.TFunction_Function_Set)
    SetDriverGUID = _swig_new_instance_method(_TFunction.TFunction_Function_SetDriverGUID)
    SetFailure = _swig_new_instance_method(_TFunction.TFunction_Function_SetFailure)

    def __init__(self, *args):
        r""":rtype: None"""
        _TFunction.TFunction_Function_swiginit(self, _TFunction.new_TFunction_Function(*args))


    @staticmethod
    def DownCast(t):
      return Handle_TFunction_Function_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _TFunction.delete_TFunction_Function

# Register TFunction_Function in _TFunction:
_TFunction.TFunction_Function_swigregister(TFunction_Function)
TFunction_Function_GetID = _TFunction.TFunction_Function_GetID
TFunction_Function_Set = _TFunction.TFunction_Function_Set

class TFunction_GraphNode(OCC.Core.TDF.TDF_Attribute):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    AddNext = _swig_new_instance_method(_TFunction.TFunction_GraphNode_AddNext)
    AddPrevious = _swig_new_instance_method(_TFunction.TFunction_GraphNode_AddPrevious)
    DumpToString = _swig_new_instance_method(_TFunction.TFunction_GraphNode_DumpToString)
    GetID = _swig_new_static_method(_TFunction.TFunction_GraphNode_GetID)
    GetNext = _swig_new_instance_method(_TFunction.TFunction_GraphNode_GetNext)
    GetPrevious = _swig_new_instance_method(_TFunction.TFunction_GraphNode_GetPrevious)
    GetStatus = _swig_new_instance_method(_TFunction.TFunction_GraphNode_GetStatus)
    RemoveAllNext = _swig_new_instance_method(_TFunction.TFunction_GraphNode_RemoveAllNext)
    RemoveAllPrevious = _swig_new_instance_method(_TFunction.TFunction_GraphNode_RemoveAllPrevious)
    RemoveNext = _swig_new_instance_method(_TFunction.TFunction_GraphNode_RemoveNext)
    RemovePrevious = _swig_new_instance_method(_TFunction.TFunction_GraphNode_RemovePrevious)
    Set = _swig_new_static_method(_TFunction.TFunction_GraphNode_Set)
    SetStatus = _swig_new_instance_method(_TFunction.TFunction_GraphNode_SetStatus)

    def __init__(self, *args):
        r""":rtype: None"""
        _TFunction.TFunction_GraphNode_swiginit(self, _TFunction.new_TFunction_GraphNode(*args))


    @staticmethod
    def DownCast(t):
      return Handle_TFunction_GraphNode_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _TFunction.delete_TFunction_GraphNode

# Register TFunction_GraphNode in _TFunction:
_TFunction.TFunction_GraphNode_swigregister(TFunction_GraphNode)
TFunction_GraphNode_GetID = _TFunction.TFunction_GraphNode_GetID
TFunction_GraphNode_Set = _TFunction.TFunction_GraphNode_Set

class TFunction_IFunction(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Arguments = _swig_new_instance_method(_TFunction.TFunction_IFunction_Arguments)
    DeleteFunction = _swig_new_static_method(_TFunction.TFunction_IFunction_DeleteFunction)
    GetAllFunctions = _swig_new_instance_method(_TFunction.TFunction_IFunction_GetAllFunctions)
    GetDriver = _swig_new_instance_method(_TFunction.TFunction_IFunction_GetDriver)
    GetGraphNode = _swig_new_instance_method(_TFunction.TFunction_IFunction_GetGraphNode)
    GetLogbook = _swig_new_instance_method(_TFunction.TFunction_IFunction_GetLogbook)
    GetNext = _swig_new_instance_method(_TFunction.TFunction_IFunction_GetNext)
    GetPrevious = _swig_new_instance_method(_TFunction.TFunction_IFunction_GetPrevious)
    GetStatus = _swig_new_instance_method(_TFunction.TFunction_IFunction_GetStatus)
    Init = _swig_new_instance_method(_TFunction.TFunction_IFunction_Init)
    Label = _swig_new_instance_method(_TFunction.TFunction_IFunction_Label)
    NewFunction = _swig_new_static_method(_TFunction.TFunction_IFunction_NewFunction)
    Results = _swig_new_instance_method(_TFunction.TFunction_IFunction_Results)
    SetStatus = _swig_new_instance_method(_TFunction.TFunction_IFunction_SetStatus)

    def __init__(self, *args):
        r"""
        :rtype: None* A constructor. Initializes the interface by the label of function.
        	:param L:
        	:type L: TDF_Label
        	:rtype: None
        """
        _TFunction.TFunction_IFunction_swiginit(self, _TFunction.new_TFunction_IFunction(*args))
    UpdateDependencies = _swig_new_instance_method(_TFunction.TFunction_IFunction_UpdateDependencies)

    __repr__ = _dumps_object

    __swig_destroy__ = _TFunction.delete_TFunction_IFunction

# Register TFunction_IFunction in _TFunction:
_TFunction.TFunction_IFunction_swigregister(TFunction_IFunction)
TFunction_IFunction_DeleteFunction = _TFunction.TFunction_IFunction_DeleteFunction
TFunction_IFunction_NewFunction = _TFunction.TFunction_IFunction_NewFunction

class TFunction_Iterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Current = _swig_new_instance_method(_TFunction.TFunction_Iterator_Current)
    DumpToString = _swig_new_instance_method(_TFunction.TFunction_Iterator_DumpToString)
    GetMaxNbThreads = _swig_new_instance_method(_TFunction.TFunction_Iterator_GetMaxNbThreads)
    GetStatus = _swig_new_instance_method(_TFunction.TFunction_Iterator_GetStatus)
    GetUsageOfExecutionStatus = _swig_new_instance_method(_TFunction.TFunction_Iterator_GetUsageOfExecutionStatus)
    Init = _swig_new_instance_method(_TFunction.TFunction_Iterator_Init)
    More = _swig_new_instance_method(_TFunction.TFunction_Iterator_More)
    Next = _swig_new_instance_method(_TFunction.TFunction_Iterator_Next)
    SetStatus = _swig_new_instance_method(_TFunction.TFunction_Iterator_SetStatus)
    SetUsageOfExecutionStatus = _swig_new_instance_method(_TFunction.TFunction_Iterator_SetUsageOfExecutionStatus)

    def __init__(self, *args):
        r"""
        * An empty constructor.
        	:rtype: None* A constructor. Initializes the iterator.
        	:param Access:
        	:type Access: TDF_Label
        	:rtype: None
        """
        _TFunction.TFunction_Iterator_swiginit(self, _TFunction.new_TFunction_Iterator(*args))

    __repr__ = _dumps_object

    __swig_destroy__ = _TFunction.delete_TFunction_Iterator

# Register TFunction_Iterator in _TFunction:
_TFunction.TFunction_Iterator_swigregister(TFunction_Iterator)

class TFunction_Logbook(OCC.Core.TDF.TDF_Attribute):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Clear = _swig_new_instance_method(_TFunction.TFunction_Logbook_Clear)
    Done = _swig_new_instance_method(_TFunction.TFunction_Logbook_Done)
    DumpToString = _swig_new_instance_method(_TFunction.TFunction_Logbook_DumpToString)
    GetID = _swig_new_static_method(_TFunction.TFunction_Logbook_GetID)
    GetImpacted = _swig_new_instance_method(_TFunction.TFunction_Logbook_GetImpacted)
    GetTouched = _swig_new_instance_method(_TFunction.TFunction_Logbook_GetTouched)
    GetValid = _swig_new_instance_method(_TFunction.TFunction_Logbook_GetValid)
    IsDone = _swig_new_instance_method(_TFunction.TFunction_Logbook_IsDone)
    IsEmpty = _swig_new_instance_method(_TFunction.TFunction_Logbook_IsEmpty)
    IsModified = _swig_new_instance_method(_TFunction.TFunction_Logbook_IsModified)
    Set = _swig_new_static_method(_TFunction.TFunction_Logbook_Set)
    SetImpacted = _swig_new_instance_method(_TFunction.TFunction_Logbook_SetImpacted)
    SetTouched = _swig_new_instance_method(_TFunction.TFunction_Logbook_SetTouched)
    SetValid = _swig_new_instance_method(_TFunction.TFunction_Logbook_SetValid)

    def __init__(self, *args):
        r"""
        * The methods manipulating the data (touched, impacted and valid labels) Constructor (empty).
        	:rtype: None
        """
        _TFunction.TFunction_Logbook_swiginit(self, _TFunction.new_TFunction_Logbook(*args))


    @staticmethod
    def DownCast(t):
      return Handle_TFunction_Logbook_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _TFunction.delete_TFunction_Logbook

# Register TFunction_Logbook in _TFunction:
_TFunction.TFunction_Logbook_swigregister(TFunction_Logbook)
TFunction_Logbook_GetID = _TFunction.TFunction_Logbook_GetID
TFunction_Logbook_Set = _TFunction.TFunction_Logbook_Set

class TFunction_Scope(OCC.Core.TDF.TDF_Attribute):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    AddFunction = _swig_new_instance_method(_TFunction.TFunction_Scope_AddFunction)
    ChangeFunctions = _swig_new_instance_method(_TFunction.TFunction_Scope_ChangeFunctions)
    DumpToString = _swig_new_instance_method(_TFunction.TFunction_Scope_DumpToString)
    GetFreeID = _swig_new_instance_method(_TFunction.TFunction_Scope_GetFreeID)
    GetFunction = _swig_new_instance_method(_TFunction.TFunction_Scope_GetFunction)
    GetFunctions = _swig_new_instance_method(_TFunction.TFunction_Scope_GetFunctions)
    GetID = _swig_new_static_method(_TFunction.TFunction_Scope_GetID)
    GetLogbook = _swig_new_instance_method(_TFunction.TFunction_Scope_GetLogbook)
    HasFunction = _swig_new_instance_method(_TFunction.TFunction_Scope_HasFunction)
    RemoveAllFunctions = _swig_new_instance_method(_TFunction.TFunction_Scope_RemoveAllFunctions)
    RemoveFunction = _swig_new_instance_method(_TFunction.TFunction_Scope_RemoveFunction)
    Set = _swig_new_static_method(_TFunction.TFunction_Scope_Set)
    SetFreeID = _swig_new_instance_method(_TFunction.TFunction_Scope_SetFreeID)

    def __init__(self, *args):
        r""":rtype: None"""
        _TFunction.TFunction_Scope_swiginit(self, _TFunction.new_TFunction_Scope(*args))


    @staticmethod
    def DownCast(t):
      return Handle_TFunction_Scope_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _TFunction.delete_TFunction_Scope

# Register TFunction_Scope in _TFunction:
_TFunction.TFunction_Scope_swigregister(TFunction_Scope)
TFunction_Scope_GetID = _TFunction.TFunction_Scope_GetID
TFunction_Scope_Set = _TFunction.TFunction_Scope_Set

class TFunction_HArray1OfDataMapOfGUIDDriver(TFunction_Array1OfDataMapOfGUIDDriver, OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _TFunction.TFunction_HArray1OfDataMapOfGUIDDriver_swiginit(self, _TFunction.new_TFunction_HArray1OfDataMapOfGUIDDriver(*args))
    Array1 = _swig_new_instance_method(_TFunction.TFunction_HArray1OfDataMapOfGUIDDriver_Array1)
    ChangeArray1 = _swig_new_instance_method(_TFunction.TFunction_HArray1OfDataMapOfGUIDDriver_ChangeArray1)


    @staticmethod
    def DownCast(t):
      return Handle_TFunction_HArray1OfDataMapOfGUIDDriver_DownCast(t)

    __swig_destroy__ = _TFunction.delete_TFunction_HArray1OfDataMapOfGUIDDriver

# Register TFunction_HArray1OfDataMapOfGUIDDriver in _TFunction:
_TFunction.TFunction_HArray1OfDataMapOfGUIDDriver_swigregister(TFunction_HArray1OfDataMapOfGUIDDriver)



