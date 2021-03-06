# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
Resource module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_resource.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _Resource
else:
    import _Resource

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _Resource.SWIG_PyInstanceMethod_New
_swig_new_static_method = _Resource.SWIG_PyStaticMethod_New

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
    __swig_destroy__ = _Resource.delete_SwigPyIterator
    value = _swig_new_instance_method(_Resource.SwigPyIterator_value)
    incr = _swig_new_instance_method(_Resource.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_Resource.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_Resource.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_Resource.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_Resource.SwigPyIterator_copy)
    next = _swig_new_instance_method(_Resource.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_Resource.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_Resource.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_Resource.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_Resource.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_Resource.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_Resource.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_Resource.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_Resource.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_Resource.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _Resource:
_Resource.SwigPyIterator_swigregister(SwigPyIterator)


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
import OCC.Core.TCollection
Resource_FormatType_SJIS = _Resource.Resource_FormatType_SJIS
Resource_FormatType_EUC = _Resource.Resource_FormatType_EUC
Resource_FormatType_ANSI = _Resource.Resource_FormatType_ANSI
Resource_FormatType_GB = _Resource.Resource_FormatType_GB
Resource_FormatType_UTF8 = _Resource.Resource_FormatType_UTF8
Resource_FormatType_SystemLocale = _Resource.Resource_FormatType_SystemLocale
Resource_SJIS = _Resource.Resource_SJIS
Resource_EUC = _Resource.Resource_EUC
Resource_ANSI = _Resource.Resource_ANSI
Resource_GB = _Resource.Resource_GB
Handle_Resource_Manager_Create = _Resource.Handle_Resource_Manager_Create
Handle_Resource_Manager_DownCast = _Resource.Handle_Resource_Manager_DownCast
Handle_Resource_Manager_IsNull = _Resource.Handle_Resource_Manager_IsNull
class Resource_DataMapOfAsciiStringAsciiString(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_Resource.Resource_DataMapOfAsciiStringAsciiString_begin)
    end = _swig_new_instance_method(_Resource.Resource_DataMapOfAsciiStringAsciiString_end)
    cbegin = _swig_new_instance_method(_Resource.Resource_DataMapOfAsciiStringAsciiString_cbegin)
    cend = _swig_new_instance_method(_Resource.Resource_DataMapOfAsciiStringAsciiString_cend)

    def __init__(self, *args):
        _Resource.Resource_DataMapOfAsciiStringAsciiString_swiginit(self, _Resource.new_Resource_DataMapOfAsciiStringAsciiString(*args))
    Exchange = _swig_new_instance_method(_Resource.Resource_DataMapOfAsciiStringAsciiString_Exchange)
    Assign = _swig_new_instance_method(_Resource.Resource_DataMapOfAsciiStringAsciiString_Assign)
    Set = _swig_new_instance_method(_Resource.Resource_DataMapOfAsciiStringAsciiString_Set)
    ReSize = _swig_new_instance_method(_Resource.Resource_DataMapOfAsciiStringAsciiString_ReSize)
    Bind = _swig_new_instance_method(_Resource.Resource_DataMapOfAsciiStringAsciiString_Bind)
    Bound = _swig_new_instance_method(_Resource.Resource_DataMapOfAsciiStringAsciiString_Bound)
    IsBound = _swig_new_instance_method(_Resource.Resource_DataMapOfAsciiStringAsciiString_IsBound)
    UnBind = _swig_new_instance_method(_Resource.Resource_DataMapOfAsciiStringAsciiString_UnBind)
    Seek = _swig_new_instance_method(_Resource.Resource_DataMapOfAsciiStringAsciiString_Seek)
    Find = _swig_new_instance_method(_Resource.Resource_DataMapOfAsciiStringAsciiString_Find)
    ChangeSeek = _swig_new_instance_method(_Resource.Resource_DataMapOfAsciiStringAsciiString_ChangeSeek)
    ChangeFind = _swig_new_instance_method(_Resource.Resource_DataMapOfAsciiStringAsciiString_ChangeFind)
    __call__ = _swig_new_instance_method(_Resource.Resource_DataMapOfAsciiStringAsciiString___call__)
    Clear = _swig_new_instance_method(_Resource.Resource_DataMapOfAsciiStringAsciiString_Clear)
    __swig_destroy__ = _Resource.delete_Resource_DataMapOfAsciiStringAsciiString
    Size = _swig_new_instance_method(_Resource.Resource_DataMapOfAsciiStringAsciiString_Size)

# Register Resource_DataMapOfAsciiStringAsciiString in _Resource:
_Resource.Resource_DataMapOfAsciiStringAsciiString_swigregister(Resource_DataMapOfAsciiStringAsciiString)

class Resource_DataMapOfAsciiStringExtendedString(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_Resource.Resource_DataMapOfAsciiStringExtendedString_begin)
    end = _swig_new_instance_method(_Resource.Resource_DataMapOfAsciiStringExtendedString_end)
    cbegin = _swig_new_instance_method(_Resource.Resource_DataMapOfAsciiStringExtendedString_cbegin)
    cend = _swig_new_instance_method(_Resource.Resource_DataMapOfAsciiStringExtendedString_cend)

    def __init__(self, *args):
        _Resource.Resource_DataMapOfAsciiStringExtendedString_swiginit(self, _Resource.new_Resource_DataMapOfAsciiStringExtendedString(*args))
    Exchange = _swig_new_instance_method(_Resource.Resource_DataMapOfAsciiStringExtendedString_Exchange)
    Assign = _swig_new_instance_method(_Resource.Resource_DataMapOfAsciiStringExtendedString_Assign)
    Set = _swig_new_instance_method(_Resource.Resource_DataMapOfAsciiStringExtendedString_Set)
    ReSize = _swig_new_instance_method(_Resource.Resource_DataMapOfAsciiStringExtendedString_ReSize)
    Bind = _swig_new_instance_method(_Resource.Resource_DataMapOfAsciiStringExtendedString_Bind)
    Bound = _swig_new_instance_method(_Resource.Resource_DataMapOfAsciiStringExtendedString_Bound)
    IsBound = _swig_new_instance_method(_Resource.Resource_DataMapOfAsciiStringExtendedString_IsBound)
    UnBind = _swig_new_instance_method(_Resource.Resource_DataMapOfAsciiStringExtendedString_UnBind)
    Seek = _swig_new_instance_method(_Resource.Resource_DataMapOfAsciiStringExtendedString_Seek)
    Find = _swig_new_instance_method(_Resource.Resource_DataMapOfAsciiStringExtendedString_Find)
    ChangeSeek = _swig_new_instance_method(_Resource.Resource_DataMapOfAsciiStringExtendedString_ChangeSeek)
    ChangeFind = _swig_new_instance_method(_Resource.Resource_DataMapOfAsciiStringExtendedString_ChangeFind)
    __call__ = _swig_new_instance_method(_Resource.Resource_DataMapOfAsciiStringExtendedString___call__)
    Clear = _swig_new_instance_method(_Resource.Resource_DataMapOfAsciiStringExtendedString_Clear)
    __swig_destroy__ = _Resource.delete_Resource_DataMapOfAsciiStringExtendedString
    Size = _swig_new_instance_method(_Resource.Resource_DataMapOfAsciiStringExtendedString_Size)

# Register Resource_DataMapOfAsciiStringExtendedString in _Resource:
_Resource.Resource_DataMapOfAsciiStringExtendedString_swigregister(Resource_DataMapOfAsciiStringExtendedString)

class Resource_LexicalCompare(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    IsLower = _swig_new_instance_method(_Resource.Resource_LexicalCompare_IsLower)

    def __init__(self, *args):
        r""":rtype: None"""
        _Resource.Resource_LexicalCompare_swiginit(self, _Resource.new_Resource_LexicalCompare(*args))

    __repr__ = _dumps_object

    __swig_destroy__ = _Resource.delete_Resource_LexicalCompare

# Register Resource_LexicalCompare in _Resource:
_Resource.Resource_LexicalCompare_swigregister(Resource_LexicalCompare)

class Resource_Manager(OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    ExtValue = _swig_new_instance_method(_Resource.Resource_Manager_ExtValue)
    Find = _swig_new_instance_method(_Resource.Resource_Manager_Find)
    GetResourcePath = _swig_new_static_method(_Resource.Resource_Manager_GetResourcePath)
    Integer = _swig_new_instance_method(_Resource.Resource_Manager_Integer)
    Real = _swig_new_instance_method(_Resource.Resource_Manager_Real)

    def __init__(self, *args):
        r"""
        * Create a Resource manager. Attempts to find the two following files: $CSF_`aName`Defaults/aName $CSF_`aName`UserDefaults/aName and load them respectively into a reference and a user resource structure. //! If CSF_ResourceVerbose defined, seeked files will be printed. //! FILE SYNTAX The syntax of a resource file is a sequence of resource lines terminated by newline characters or end of file. The syntax of an individual resource line is:
        	:param aName:
        	:type aName: char *
        	:param Verbose: default value is Standard_False
        	:type Verbose: bool
        	:rtype: None:param aName:
        	:type aName: char *
        	:param aDefaultsDirectory:
        	:type aDefaultsDirectory: TCollection_AsciiString
        	:param anUserDefaultsDirectory:
        	:type anUserDefaultsDirectory: TCollection_AsciiString
        	:param Verbose: default value is Standard_False
        	:type Verbose: bool
        	:rtype: None
        """
        _Resource.Resource_Manager_swiginit(self, _Resource.new_Resource_Manager(*args))
    Save = _swig_new_instance_method(_Resource.Resource_Manager_Save)
    SetResource = _swig_new_instance_method(_Resource.Resource_Manager_SetResource)
    Value = _swig_new_instance_method(_Resource.Resource_Manager_Value)


    @staticmethod
    def DownCast(t):
      return Handle_Resource_Manager_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _Resource.delete_Resource_Manager

# Register Resource_Manager in _Resource:
_Resource.Resource_Manager_swigregister(Resource_Manager)
Resource_Manager_GetResourcePath = _Resource.Resource_Manager_GetResourcePath

class Resource_Unicode(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    ConvertANSIToUnicode = _swig_new_static_method(_Resource.Resource_Unicode_ConvertANSIToUnicode)
    ConvertBig5ToUnicode = _swig_new_static_method(_Resource.Resource_Unicode_ConvertBig5ToUnicode)
    ConvertEUCToUnicode = _swig_new_static_method(_Resource.Resource_Unicode_ConvertEUCToUnicode)
    ConvertFormatToUnicode = _swig_new_static_method(_Resource.Resource_Unicode_ConvertFormatToUnicode)
    ConvertGBKToUnicode = _swig_new_static_method(_Resource.Resource_Unicode_ConvertGBKToUnicode)
    ConvertGBToUnicode = _swig_new_static_method(_Resource.Resource_Unicode_ConvertGBToUnicode)
    ConvertSJISToUnicode = _swig_new_static_method(_Resource.Resource_Unicode_ConvertSJISToUnicode)
    ConvertUnicodeToANSI = _swig_new_static_method(_Resource.Resource_Unicode_ConvertUnicodeToANSI)
    ConvertUnicodeToEUC = _swig_new_static_method(_Resource.Resource_Unicode_ConvertUnicodeToEUC)
    ConvertUnicodeToFormat = _swig_new_static_method(_Resource.Resource_Unicode_ConvertUnicodeToFormat)
    ConvertUnicodeToGB = _swig_new_static_method(_Resource.Resource_Unicode_ConvertUnicodeToGB)
    ConvertUnicodeToSJIS = _swig_new_static_method(_Resource.Resource_Unicode_ConvertUnicodeToSJIS)
    GetFormat = _swig_new_static_method(_Resource.Resource_Unicode_GetFormat)
    ReadFormat = _swig_new_static_method(_Resource.Resource_Unicode_ReadFormat)
    SetFormat = _swig_new_static_method(_Resource.Resource_Unicode_SetFormat)

    __repr__ = _dumps_object


    def __init__(self):
        _Resource.Resource_Unicode_swiginit(self, _Resource.new_Resource_Unicode())
    __swig_destroy__ = _Resource.delete_Resource_Unicode

# Register Resource_Unicode in _Resource:
_Resource.Resource_Unicode_swigregister(Resource_Unicode)
Resource_Unicode_ConvertANSIToUnicode = _Resource.Resource_Unicode_ConvertANSIToUnicode
Resource_Unicode_ConvertBig5ToUnicode = _Resource.Resource_Unicode_ConvertBig5ToUnicode
Resource_Unicode_ConvertEUCToUnicode = _Resource.Resource_Unicode_ConvertEUCToUnicode
Resource_Unicode_ConvertFormatToUnicode = _Resource.Resource_Unicode_ConvertFormatToUnicode
Resource_Unicode_ConvertGBKToUnicode = _Resource.Resource_Unicode_ConvertGBKToUnicode
Resource_Unicode_ConvertGBToUnicode = _Resource.Resource_Unicode_ConvertGBToUnicode
Resource_Unicode_ConvertSJISToUnicode = _Resource.Resource_Unicode_ConvertSJISToUnicode
Resource_Unicode_ConvertUnicodeToANSI = _Resource.Resource_Unicode_ConvertUnicodeToANSI
Resource_Unicode_ConvertUnicodeToEUC = _Resource.Resource_Unicode_ConvertUnicodeToEUC
Resource_Unicode_ConvertUnicodeToFormat = _Resource.Resource_Unicode_ConvertUnicodeToFormat
Resource_Unicode_ConvertUnicodeToGB = _Resource.Resource_Unicode_ConvertUnicodeToGB
Resource_Unicode_ConvertUnicodeToSJIS = _Resource.Resource_Unicode_ConvertUnicodeToSJIS
Resource_Unicode_GetFormat = _Resource.Resource_Unicode_GetFormat
Resource_Unicode_ReadFormat = _Resource.Resource_Unicode_ReadFormat
Resource_Unicode_SetFormat = _Resource.Resource_Unicode_SetFormat



