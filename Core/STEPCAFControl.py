# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
STEPCAFControl module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_stepcafcontrol.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _STEPCAFControl
else:
    import _STEPCAFControl

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _STEPCAFControl.SWIG_PyInstanceMethod_New
_swig_new_static_method = _STEPCAFControl.SWIG_PyStaticMethod_New

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
    __swig_destroy__ = _STEPCAFControl.delete_SwigPyIterator
    value = _swig_new_instance_method(_STEPCAFControl.SwigPyIterator_value)
    incr = _swig_new_instance_method(_STEPCAFControl.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_STEPCAFControl.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_STEPCAFControl.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_STEPCAFControl.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_STEPCAFControl.SwigPyIterator_copy)
    next = _swig_new_instance_method(_STEPCAFControl.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_STEPCAFControl.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_STEPCAFControl.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_STEPCAFControl.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_STEPCAFControl.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_STEPCAFControl.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_STEPCAFControl.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_STEPCAFControl.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_STEPCAFControl.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_STEPCAFControl.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _STEPCAFControl:
_STEPCAFControl.SwigPyIterator_swigregister(SwigPyIterator)


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
import OCC.Core.StepShape
import OCC.Core.StepGeom
import OCC.Core.StepData
import OCC.Core.Interface
import OCC.Core.TCollection
import OCC.Core.TColStd
import OCC.Core.Message
import OCC.Core.MoniTool
import OCC.Core.TopoDS
import OCC.Core.TopAbs
import OCC.Core.TopLoc
import OCC.Core.gp
import OCC.Core.OSD
import OCC.Core.StepRepr
import OCC.Core.StepBasic
import OCC.Core.STEPControl
import OCC.Core.Transfer
import OCC.Core.TopTools
import OCC.Core.XSControl
import OCC.Core.IFSelect
import OCC.Core.Geom
import OCC.Core.GeomAbs
import OCC.Core.TColgp
import OCC.Core.Geom2d
import OCC.Core.TDF
import OCC.Core.XCAFDimTolObjects
import OCC.Core.TDocStd
import OCC.Core.CDF
import OCC.Core.CDM
import OCC.Core.Resource
import OCC.Core.PCDM
import OCC.Core.Storage
import OCC.Core.StepDimTol
import OCC.Core.StepVisual
import OCC.Core.XCAFDoc
import OCC.Core.Quantity
import OCC.Core.XCAFNoteObjects
import OCC.Core.TDataStd
import OCC.Core.XCAFView
import OCC.Core.STEPConstruct
import OCC.Core.StepAP203
Handle_STEPCAFControl_ActorWrite_Create = _STEPCAFControl.Handle_STEPCAFControl_ActorWrite_Create
Handle_STEPCAFControl_ActorWrite_DownCast = _STEPCAFControl.Handle_STEPCAFControl_ActorWrite_DownCast
Handle_STEPCAFControl_ActorWrite_IsNull = _STEPCAFControl.Handle_STEPCAFControl_ActorWrite_IsNull
Handle_STEPCAFControl_Controller_Create = _STEPCAFControl.Handle_STEPCAFControl_Controller_Create
Handle_STEPCAFControl_Controller_DownCast = _STEPCAFControl.Handle_STEPCAFControl_Controller_DownCast
Handle_STEPCAFControl_Controller_IsNull = _STEPCAFControl.Handle_STEPCAFControl_Controller_IsNull
Handle_STEPCAFControl_ExternFile_Create = _STEPCAFControl.Handle_STEPCAFControl_ExternFile_Create
Handle_STEPCAFControl_ExternFile_DownCast = _STEPCAFControl.Handle_STEPCAFControl_ExternFile_DownCast
Handle_STEPCAFControl_ExternFile_IsNull = _STEPCAFControl.Handle_STEPCAFControl_ExternFile_IsNull
class STEPCAFControl_DataMapOfPDExternFile(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfPDExternFile_begin)
    end = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfPDExternFile_end)
    cbegin = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfPDExternFile_cbegin)
    cend = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfPDExternFile_cend)

    def __init__(self, *args):
        _STEPCAFControl.STEPCAFControl_DataMapOfPDExternFile_swiginit(self, _STEPCAFControl.new_STEPCAFControl_DataMapOfPDExternFile(*args))
    Exchange = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfPDExternFile_Exchange)
    Assign = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfPDExternFile_Assign)
    Set = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfPDExternFile_Set)
    ReSize = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfPDExternFile_ReSize)
    Bind = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfPDExternFile_Bind)
    Bound = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfPDExternFile_Bound)
    IsBound = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfPDExternFile_IsBound)
    UnBind = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfPDExternFile_UnBind)
    Seek = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfPDExternFile_Seek)
    Find = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfPDExternFile_Find)
    ChangeSeek = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfPDExternFile_ChangeSeek)
    ChangeFind = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfPDExternFile_ChangeFind)
    __call__ = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfPDExternFile___call__)
    Clear = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfPDExternFile_Clear)
    __swig_destroy__ = _STEPCAFControl.delete_STEPCAFControl_DataMapOfPDExternFile
    Size = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfPDExternFile_Size)

# Register STEPCAFControl_DataMapOfPDExternFile in _STEPCAFControl:
_STEPCAFControl.STEPCAFControl_DataMapOfPDExternFile_swigregister(STEPCAFControl_DataMapOfPDExternFile)

class STEPCAFControl_DataMapOfShapeSDR(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfShapeSDR_begin)
    end = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfShapeSDR_end)
    cbegin = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfShapeSDR_cbegin)
    cend = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfShapeSDR_cend)

    def __init__(self, *args):
        _STEPCAFControl.STEPCAFControl_DataMapOfShapeSDR_swiginit(self, _STEPCAFControl.new_STEPCAFControl_DataMapOfShapeSDR(*args))
    Exchange = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfShapeSDR_Exchange)
    Assign = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfShapeSDR_Assign)
    Set = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfShapeSDR_Set)
    ReSize = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfShapeSDR_ReSize)
    Bind = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfShapeSDR_Bind)
    Bound = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfShapeSDR_Bound)
    IsBound = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfShapeSDR_IsBound)
    UnBind = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfShapeSDR_UnBind)
    Seek = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfShapeSDR_Seek)
    Find = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfShapeSDR_Find)
    ChangeSeek = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfShapeSDR_ChangeSeek)
    ChangeFind = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfShapeSDR_ChangeFind)
    __call__ = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfShapeSDR___call__)
    Clear = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfShapeSDR_Clear)
    __swig_destroy__ = _STEPCAFControl.delete_STEPCAFControl_DataMapOfShapeSDR
    Size = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfShapeSDR_Size)

# Register STEPCAFControl_DataMapOfShapeSDR in _STEPCAFControl:
_STEPCAFControl.STEPCAFControl_DataMapOfShapeSDR_swigregister(STEPCAFControl_DataMapOfShapeSDR)

class STEPCAFControl_DataMapOfShapePD(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfShapePD_begin)
    end = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfShapePD_end)
    cbegin = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfShapePD_cbegin)
    cend = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfShapePD_cend)

    def __init__(self, *args):
        _STEPCAFControl.STEPCAFControl_DataMapOfShapePD_swiginit(self, _STEPCAFControl.new_STEPCAFControl_DataMapOfShapePD(*args))
    Exchange = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfShapePD_Exchange)
    Assign = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfShapePD_Assign)
    Set = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfShapePD_Set)
    ReSize = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfShapePD_ReSize)
    Bind = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfShapePD_Bind)
    Bound = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfShapePD_Bound)
    IsBound = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfShapePD_IsBound)
    UnBind = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfShapePD_UnBind)
    Seek = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfShapePD_Seek)
    Find = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfShapePD_Find)
    ChangeSeek = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfShapePD_ChangeSeek)
    ChangeFind = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfShapePD_ChangeFind)
    __call__ = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfShapePD___call__)
    Clear = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfShapePD_Clear)
    __swig_destroy__ = _STEPCAFControl.delete_STEPCAFControl_DataMapOfShapePD
    Size = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfShapePD_Size)

# Register STEPCAFControl_DataMapOfShapePD in _STEPCAFControl:
_STEPCAFControl.STEPCAFControl_DataMapOfShapePD_swigregister(STEPCAFControl_DataMapOfShapePD)

class STEPCAFControl_DataMapOfLabelExternFile(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfLabelExternFile_begin)
    end = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfLabelExternFile_end)
    cbegin = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfLabelExternFile_cbegin)
    cend = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfLabelExternFile_cend)

    def __init__(self, *args):
        _STEPCAFControl.STEPCAFControl_DataMapOfLabelExternFile_swiginit(self, _STEPCAFControl.new_STEPCAFControl_DataMapOfLabelExternFile(*args))
    Exchange = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfLabelExternFile_Exchange)
    Assign = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfLabelExternFile_Assign)
    Set = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfLabelExternFile_Set)
    ReSize = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfLabelExternFile_ReSize)
    Bind = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfLabelExternFile_Bind)
    Bound = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfLabelExternFile_Bound)
    IsBound = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfLabelExternFile_IsBound)
    UnBind = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfLabelExternFile_UnBind)
    Seek = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfLabelExternFile_Seek)
    Find = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfLabelExternFile_Find)
    ChangeSeek = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfLabelExternFile_ChangeSeek)
    ChangeFind = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfLabelExternFile_ChangeFind)
    __call__ = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfLabelExternFile___call__)
    Clear = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfLabelExternFile_Clear)
    __swig_destroy__ = _STEPCAFControl.delete_STEPCAFControl_DataMapOfLabelExternFile
    Size = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfLabelExternFile_Size)

# Register STEPCAFControl_DataMapOfLabelExternFile in _STEPCAFControl:
_STEPCAFControl.STEPCAFControl_DataMapOfLabelExternFile_swigregister(STEPCAFControl_DataMapOfLabelExternFile)

class STEPCAFControl_DataMapOfSDRExternFile(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfSDRExternFile_begin)
    end = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfSDRExternFile_end)
    cbegin = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfSDRExternFile_cbegin)
    cend = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfSDRExternFile_cend)

    def __init__(self, *args):
        _STEPCAFControl.STEPCAFControl_DataMapOfSDRExternFile_swiginit(self, _STEPCAFControl.new_STEPCAFControl_DataMapOfSDRExternFile(*args))
    Exchange = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfSDRExternFile_Exchange)
    Assign = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfSDRExternFile_Assign)
    Set = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfSDRExternFile_Set)
    ReSize = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfSDRExternFile_ReSize)
    Bind = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfSDRExternFile_Bind)
    Bound = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfSDRExternFile_Bound)
    IsBound = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfSDRExternFile_IsBound)
    UnBind = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfSDRExternFile_UnBind)
    Seek = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfSDRExternFile_Seek)
    Find = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfSDRExternFile_Find)
    ChangeSeek = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfSDRExternFile_ChangeSeek)
    ChangeFind = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfSDRExternFile_ChangeFind)
    __call__ = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfSDRExternFile___call__)
    Clear = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfSDRExternFile_Clear)
    __swig_destroy__ = _STEPCAFControl.delete_STEPCAFControl_DataMapOfSDRExternFile
    Size = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfSDRExternFile_Size)

# Register STEPCAFControl_DataMapOfSDRExternFile in _STEPCAFControl:
_STEPCAFControl.STEPCAFControl_DataMapOfSDRExternFile_swigregister(STEPCAFControl_DataMapOfSDRExternFile)

class STEPCAFControl_DataMapOfLabelShape(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfLabelShape_begin)
    end = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfLabelShape_end)
    cbegin = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfLabelShape_cbegin)
    cend = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfLabelShape_cend)

    def __init__(self, *args):
        _STEPCAFControl.STEPCAFControl_DataMapOfLabelShape_swiginit(self, _STEPCAFControl.new_STEPCAFControl_DataMapOfLabelShape(*args))
    Exchange = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfLabelShape_Exchange)
    Assign = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfLabelShape_Assign)
    Set = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfLabelShape_Set)
    ReSize = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfLabelShape_ReSize)
    Bind = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfLabelShape_Bind)
    Bound = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfLabelShape_Bound)
    IsBound = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfLabelShape_IsBound)
    UnBind = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfLabelShape_UnBind)
    Seek = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfLabelShape_Seek)
    Find = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfLabelShape_Find)
    ChangeSeek = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfLabelShape_ChangeSeek)
    ChangeFind = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfLabelShape_ChangeFind)
    __call__ = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfLabelShape___call__)
    Clear = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfLabelShape_Clear)
    __swig_destroy__ = _STEPCAFControl.delete_STEPCAFControl_DataMapOfLabelShape
    Size = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_DataMapOfLabelShape_Size)

# Register STEPCAFControl_DataMapOfLabelShape in _STEPCAFControl:
_STEPCAFControl.STEPCAFControl_DataMapOfLabelShape_swigregister(STEPCAFControl_DataMapOfLabelShape)

class STEPCAFControl_ActorWrite(OCC.Core.STEPControl.STEPControl_ActorWrite):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    ClearMap = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_ActorWrite_ClearMap)
    RegisterAssembly = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_ActorWrite_RegisterAssembly)

    def __init__(self, *args):
        r""":rtype: None"""
        _STEPCAFControl.STEPCAFControl_ActorWrite_swiginit(self, _STEPCAFControl.new_STEPCAFControl_ActorWrite(*args))
    SetStdMode = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_ActorWrite_SetStdMode)


    @staticmethod
    def DownCast(t):
      return Handle_STEPCAFControl_ActorWrite_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _STEPCAFControl.delete_STEPCAFControl_ActorWrite

# Register STEPCAFControl_ActorWrite in _STEPCAFControl:
_STEPCAFControl.STEPCAFControl_ActorWrite_swigregister(STEPCAFControl_ActorWrite)

class STEPCAFControl_Controller(OCC.Core.STEPControl.STEPControl_Controller):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Init = _swig_new_static_method(_STEPCAFControl.STEPCAFControl_Controller_Init)

    def __init__(self, *args):
        r"""
        * Initializes the use of STEP Norm (the first time)
        	:rtype: None
        """
        _STEPCAFControl.STEPCAFControl_Controller_swiginit(self, _STEPCAFControl.new_STEPCAFControl_Controller(*args))


    @staticmethod
    def DownCast(t):
      return Handle_STEPCAFControl_Controller_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _STEPCAFControl.delete_STEPCAFControl_Controller

# Register STEPCAFControl_Controller in _STEPCAFControl:
_STEPCAFControl.STEPCAFControl_Controller_swigregister(STEPCAFControl_Controller)
STEPCAFControl_Controller_Init = _STEPCAFControl.STEPCAFControl_Controller_Init

class STEPCAFControl_ExternFile(OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    GetLabel = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_ExternFile_GetLabel)
    GetLoadStatus = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_ExternFile_GetLoadStatus)
    GetName = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_ExternFile_GetName)
    GetTransferStatus = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_ExternFile_GetTransferStatus)
    GetWS = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_ExternFile_GetWS)
    GetWriteStatus = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_ExternFile_GetWriteStatus)

    def __init__(self, *args):
        r"""
        * Creates an empty structure
        	:rtype: None
        """
        _STEPCAFControl.STEPCAFControl_ExternFile_swiginit(self, _STEPCAFControl.new_STEPCAFControl_ExternFile(*args))
    SetLabel = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_ExternFile_SetLabel)
    SetLoadStatus = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_ExternFile_SetLoadStatus)
    SetName = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_ExternFile_SetName)
    SetTransferStatus = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_ExternFile_SetTransferStatus)
    SetWS = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_ExternFile_SetWS)
    SetWriteStatus = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_ExternFile_SetWriteStatus)


    @staticmethod
    def DownCast(t):
      return Handle_STEPCAFControl_ExternFile_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _STEPCAFControl.delete_STEPCAFControl_ExternFile

# Register STEPCAFControl_ExternFile in _STEPCAFControl:
_STEPCAFControl.STEPCAFControl_ExternFile_swigregister(STEPCAFControl_ExternFile)

class STEPCAFControl_GDTProperty(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    GetDatumRefModifiers = _swig_new_static_method(_STEPCAFControl.STEPCAFControl_GDTProperty_GetDatumRefModifiers)
    GetDatumTargetName = _swig_new_static_method(_STEPCAFControl.STEPCAFControl_GDTProperty_GetDatumTargetName)
    GetDatumTargetType = _swig_new_static_method(_STEPCAFControl.STEPCAFControl_GDTProperty_GetDatumTargetType)
    GetDimClassOfTolerance = _swig_new_static_method(_STEPCAFControl.STEPCAFControl_GDTProperty_GetDimClassOfTolerance)
    GetDimModifierName = _swig_new_static_method(_STEPCAFControl.STEPCAFControl_GDTProperty_GetDimModifierName)
    GetDimModifiers = _swig_new_static_method(_STEPCAFControl.STEPCAFControl_GDTProperty_GetDimModifiers)
    GetDimQualifierName = _swig_new_static_method(_STEPCAFControl.STEPCAFControl_GDTProperty_GetDimQualifierName)
    GetDimQualifierType = _swig_new_static_method(_STEPCAFControl.STEPCAFControl_GDTProperty_GetDimQualifierType)
    GetDimType = _swig_new_static_method(_STEPCAFControl.STEPCAFControl_GDTProperty_GetDimType)
    GetDimTypeName = _swig_new_static_method(_STEPCAFControl.STEPCAFControl_GDTProperty_GetDimTypeName)
    GetGeomTolerance = _swig_new_static_method(_STEPCAFControl.STEPCAFControl_GDTProperty_GetGeomTolerance)
    GetGeomToleranceModifier = _swig_new_static_method(_STEPCAFControl.STEPCAFControl_GDTProperty_GetGeomToleranceModifier)
    GetGeomToleranceType = _swig_new_static_method(_STEPCAFControl.STEPCAFControl_GDTProperty_GetGeomToleranceType)
    GetLimitsAndFits = _swig_new_static_method(_STEPCAFControl.STEPCAFControl_GDTProperty_GetLimitsAndFits)
    GetTessellation = _swig_new_static_method(_STEPCAFControl.STEPCAFControl_GDTProperty_GetTessellation)
    GetTolValueType = _swig_new_static_method(_STEPCAFControl.STEPCAFControl_GDTProperty_GetTolValueType)
    IsDimensionalLocation = _swig_new_static_method(_STEPCAFControl.STEPCAFControl_GDTProperty_IsDimensionalLocation)
    IsDimensionalSize = _swig_new_static_method(_STEPCAFControl.STEPCAFControl_GDTProperty_IsDimensionalSize)

    def __init__(self, *args):
        r""":rtype: None"""
        _STEPCAFControl.STEPCAFControl_GDTProperty_swiginit(self, _STEPCAFControl.new_STEPCAFControl_GDTProperty(*args))

    __repr__ = _dumps_object

    __swig_destroy__ = _STEPCAFControl.delete_STEPCAFControl_GDTProperty

# Register STEPCAFControl_GDTProperty in _STEPCAFControl:
_STEPCAFControl.STEPCAFControl_GDTProperty_swigregister(STEPCAFControl_GDTProperty)
STEPCAFControl_GDTProperty_GetDatumRefModifiers = _STEPCAFControl.STEPCAFControl_GDTProperty_GetDatumRefModifiers
STEPCAFControl_GDTProperty_GetDatumTargetName = _STEPCAFControl.STEPCAFControl_GDTProperty_GetDatumTargetName
STEPCAFControl_GDTProperty_GetDatumTargetType = _STEPCAFControl.STEPCAFControl_GDTProperty_GetDatumTargetType
STEPCAFControl_GDTProperty_GetDimClassOfTolerance = _STEPCAFControl.STEPCAFControl_GDTProperty_GetDimClassOfTolerance
STEPCAFControl_GDTProperty_GetDimModifierName = _STEPCAFControl.STEPCAFControl_GDTProperty_GetDimModifierName
STEPCAFControl_GDTProperty_GetDimModifiers = _STEPCAFControl.STEPCAFControl_GDTProperty_GetDimModifiers
STEPCAFControl_GDTProperty_GetDimQualifierName = _STEPCAFControl.STEPCAFControl_GDTProperty_GetDimQualifierName
STEPCAFControl_GDTProperty_GetDimQualifierType = _STEPCAFControl.STEPCAFControl_GDTProperty_GetDimQualifierType
STEPCAFControl_GDTProperty_GetDimType = _STEPCAFControl.STEPCAFControl_GDTProperty_GetDimType
STEPCAFControl_GDTProperty_GetDimTypeName = _STEPCAFControl.STEPCAFControl_GDTProperty_GetDimTypeName
STEPCAFControl_GDTProperty_GetGeomTolerance = _STEPCAFControl.STEPCAFControl_GDTProperty_GetGeomTolerance
STEPCAFControl_GDTProperty_GetGeomToleranceModifier = _STEPCAFControl.STEPCAFControl_GDTProperty_GetGeomToleranceModifier
STEPCAFControl_GDTProperty_GetGeomToleranceType = _STEPCAFControl.STEPCAFControl_GDTProperty_GetGeomToleranceType
STEPCAFControl_GDTProperty_GetLimitsAndFits = _STEPCAFControl.STEPCAFControl_GDTProperty_GetLimitsAndFits
STEPCAFControl_GDTProperty_GetTessellation = _STEPCAFControl.STEPCAFControl_GDTProperty_GetTessellation
STEPCAFControl_GDTProperty_GetTolValueType = _STEPCAFControl.STEPCAFControl_GDTProperty_GetTolValueType
STEPCAFControl_GDTProperty_IsDimensionalLocation = _STEPCAFControl.STEPCAFControl_GDTProperty_IsDimensionalLocation
STEPCAFControl_GDTProperty_IsDimensionalSize = _STEPCAFControl.STEPCAFControl_GDTProperty_IsDimensionalSize

class STEPCAFControl_Reader(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    ChangeReader = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Reader_ChangeReader)
    ExternFile = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Reader_ExternFile)
    ExternFiles = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Reader_ExternFiles)
    FindInstance = _swig_new_static_method(_STEPCAFControl.STEPCAFControl_Reader_FindInstance)
    GetColorMode = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Reader_GetColorMode)
    GetGDTMode = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Reader_GetGDTMode)
    GetLayerMode = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Reader_GetLayerMode)
    GetMatMode = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Reader_GetMatMode)
    GetNameMode = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Reader_GetNameMode)
    GetPropsMode = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Reader_GetPropsMode)
    GetSHUOMode = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Reader_GetSHUOMode)
    GetViewMode = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Reader_GetViewMode)
    Init = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Reader_Init)
    NbRootsForTransfer = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Reader_NbRootsForTransfer)
    Perform = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Reader_Perform)
    ReadFile = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Reader_ReadFile)
    Reader = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Reader_Reader)

    def __init__(self, *args):
        r"""
        * Creates a reader with an empty STEP model and sets ColorMode, LayerMode, NameMode and PropsMode to Standard_True.
        	:rtype: None* Creates a reader tool and attaches it to an already existing Session Clears the session if it was not yet set for STEP
        	:param WS:
        	:type WS: XSControl_WorkSession
        	:param scratch: default value is Standard_True
        	:type scratch: bool
        	:rtype: None
        """
        _STEPCAFControl.STEPCAFControl_Reader_swiginit(self, _STEPCAFControl.new_STEPCAFControl_Reader(*args))
    SetColorMode = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Reader_SetColorMode)
    SetGDTMode = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Reader_SetGDTMode)
    SetLayerMode = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Reader_SetLayerMode)
    SetMatMode = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Reader_SetMatMode)
    SetNameMode = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Reader_SetNameMode)
    SetPropsMode = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Reader_SetPropsMode)
    SetSHUOMode = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Reader_SetSHUOMode)
    SetSourceCodePage = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Reader_SetSourceCodePage)
    SetViewMode = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Reader_SetViewMode)
    SourceCodePage = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Reader_SourceCodePage)
    Transfer = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Reader_Transfer)
    TransferOneRoot = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Reader_TransferOneRoot)

    __repr__ = _dumps_object

    __swig_destroy__ = _STEPCAFControl.delete_STEPCAFControl_Reader

# Register STEPCAFControl_Reader in _STEPCAFControl:
_STEPCAFControl.STEPCAFControl_Reader_swigregister(STEPCAFControl_Reader)
STEPCAFControl_Reader_FindInstance = _STEPCAFControl.STEPCAFControl_Reader_FindInstance

class STEPCAFControl_Writer(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    ChangeWriter = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Writer_ChangeWriter)
    ExternFile = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Writer_ExternFile)
    ExternFiles = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Writer_ExternFiles)
    GetColorMode = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Writer_GetColorMode)
    GetDimTolMode = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Writer_GetDimTolMode)
    GetLayerMode = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Writer_GetLayerMode)
    GetMaterialMode = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Writer_GetMaterialMode)
    GetNameMode = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Writer_GetNameMode)
    GetPropsMode = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Writer_GetPropsMode)
    GetSHUOMode = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Writer_GetSHUOMode)
    Init = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Writer_Init)
    Perform = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Writer_Perform)

    def __init__(self, *args):
        r"""
        * Creates a writer with an empty STEP model and sets ColorMode, LayerMode, NameMode and PropsMode to Standard_True.
        	:rtype: None* Creates a reader tool and attaches it to an already existing Session Clears the session if it was not yet set for STEP Clears the internal data structures
        	:param WS:
        	:type WS: XSControl_WorkSession
        	:param scratch: default value is Standard_True
        	:type scratch: bool
        	:rtype: None
        """
        _STEPCAFControl.STEPCAFControl_Writer_swiginit(self, _STEPCAFControl.new_STEPCAFControl_Writer(*args))
    SetColorMode = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Writer_SetColorMode)
    SetDimTolMode = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Writer_SetDimTolMode)
    SetLayerMode = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Writer_SetLayerMode)
    SetMaterialMode = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Writer_SetMaterialMode)
    SetNameMode = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Writer_SetNameMode)
    SetPropsMode = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Writer_SetPropsMode)
    SetSHUOMode = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Writer_SetSHUOMode)
    Transfer = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Writer_Transfer)
    Write = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Writer_Write)
    Writer = _swig_new_instance_method(_STEPCAFControl.STEPCAFControl_Writer_Writer)

    __repr__ = _dumps_object

    __swig_destroy__ = _STEPCAFControl.delete_STEPCAFControl_Writer

# Register STEPCAFControl_Writer in _STEPCAFControl:
_STEPCAFControl.STEPCAFControl_Writer_swigregister(STEPCAFControl_Writer)



