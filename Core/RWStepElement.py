# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
RWStepElement module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_rwstepelement.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _RWStepElement
else:
    import _RWStepElement

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _RWStepElement.SWIG_PyInstanceMethod_New
_swig_new_static_method = _RWStepElement.SWIG_PyStaticMethod_New

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
    __swig_destroy__ = _RWStepElement.delete_SwigPyIterator
    value = _swig_new_instance_method(_RWStepElement.SwigPyIterator_value)
    incr = _swig_new_instance_method(_RWStepElement.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_RWStepElement.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_RWStepElement.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_RWStepElement.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_RWStepElement.SwigPyIterator_copy)
    next = _swig_new_instance_method(_RWStepElement.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_RWStepElement.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_RWStepElement.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_RWStepElement.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_RWStepElement.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_RWStepElement.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_RWStepElement.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_RWStepElement.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_RWStepElement.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_RWStepElement.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _RWStepElement:
_RWStepElement.SwigPyIterator_swigregister(SwigPyIterator)


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
import OCC.Core.StepElement
import OCC.Core.StepRepr
import OCC.Core.StepBasic
class RWStepElement_RWAnalysisItemWithinRepresentation(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Empty constructor
        	:rtype: None
        """
        _RWStepElement.RWStepElement_RWAnalysisItemWithinRepresentation_swiginit(self, _RWStepElement.new_RWStepElement_RWAnalysisItemWithinRepresentation(*args))
    ReadStep = _swig_new_instance_method(_RWStepElement.RWStepElement_RWAnalysisItemWithinRepresentation_ReadStep)
    Share = _swig_new_instance_method(_RWStepElement.RWStepElement_RWAnalysisItemWithinRepresentation_Share)
    WriteStep = _swig_new_instance_method(_RWStepElement.RWStepElement_RWAnalysisItemWithinRepresentation_WriteStep)

    __repr__ = _dumps_object

    __swig_destroy__ = _RWStepElement.delete_RWStepElement_RWAnalysisItemWithinRepresentation

# Register RWStepElement_RWAnalysisItemWithinRepresentation in _RWStepElement:
_RWStepElement.RWStepElement_RWAnalysisItemWithinRepresentation_swigregister(RWStepElement_RWAnalysisItemWithinRepresentation)

class RWStepElement_RWCurve3dElementDescriptor(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Empty constructor
        	:rtype: None
        """
        _RWStepElement.RWStepElement_RWCurve3dElementDescriptor_swiginit(self, _RWStepElement.new_RWStepElement_RWCurve3dElementDescriptor(*args))
    ReadStep = _swig_new_instance_method(_RWStepElement.RWStepElement_RWCurve3dElementDescriptor_ReadStep)
    Share = _swig_new_instance_method(_RWStepElement.RWStepElement_RWCurve3dElementDescriptor_Share)
    WriteStep = _swig_new_instance_method(_RWStepElement.RWStepElement_RWCurve3dElementDescriptor_WriteStep)

    __repr__ = _dumps_object

    __swig_destroy__ = _RWStepElement.delete_RWStepElement_RWCurve3dElementDescriptor

# Register RWStepElement_RWCurve3dElementDescriptor in _RWStepElement:
_RWStepElement.RWStepElement_RWCurve3dElementDescriptor_swigregister(RWStepElement_RWCurve3dElementDescriptor)

class RWStepElement_RWCurveElementEndReleasePacket(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Empty constructor
        	:rtype: None
        """
        _RWStepElement.RWStepElement_RWCurveElementEndReleasePacket_swiginit(self, _RWStepElement.new_RWStepElement_RWCurveElementEndReleasePacket(*args))
    ReadStep = _swig_new_instance_method(_RWStepElement.RWStepElement_RWCurveElementEndReleasePacket_ReadStep)
    Share = _swig_new_instance_method(_RWStepElement.RWStepElement_RWCurveElementEndReleasePacket_Share)
    WriteStep = _swig_new_instance_method(_RWStepElement.RWStepElement_RWCurveElementEndReleasePacket_WriteStep)

    __repr__ = _dumps_object

    __swig_destroy__ = _RWStepElement.delete_RWStepElement_RWCurveElementEndReleasePacket

# Register RWStepElement_RWCurveElementEndReleasePacket in _RWStepElement:
_RWStepElement.RWStepElement_RWCurveElementEndReleasePacket_swigregister(RWStepElement_RWCurveElementEndReleasePacket)

class RWStepElement_RWCurveElementSectionDefinition(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Empty constructor
        	:rtype: None
        """
        _RWStepElement.RWStepElement_RWCurveElementSectionDefinition_swiginit(self, _RWStepElement.new_RWStepElement_RWCurveElementSectionDefinition(*args))
    ReadStep = _swig_new_instance_method(_RWStepElement.RWStepElement_RWCurveElementSectionDefinition_ReadStep)
    Share = _swig_new_instance_method(_RWStepElement.RWStepElement_RWCurveElementSectionDefinition_Share)
    WriteStep = _swig_new_instance_method(_RWStepElement.RWStepElement_RWCurveElementSectionDefinition_WriteStep)

    __repr__ = _dumps_object

    __swig_destroy__ = _RWStepElement.delete_RWStepElement_RWCurveElementSectionDefinition

# Register RWStepElement_RWCurveElementSectionDefinition in _RWStepElement:
_RWStepElement.RWStepElement_RWCurveElementSectionDefinition_swigregister(RWStepElement_RWCurveElementSectionDefinition)

class RWStepElement_RWCurveElementSectionDerivedDefinitions(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Empty constructor
        	:rtype: None
        """
        _RWStepElement.RWStepElement_RWCurveElementSectionDerivedDefinitions_swiginit(self, _RWStepElement.new_RWStepElement_RWCurveElementSectionDerivedDefinitions(*args))
    ReadStep = _swig_new_instance_method(_RWStepElement.RWStepElement_RWCurveElementSectionDerivedDefinitions_ReadStep)
    Share = _swig_new_instance_method(_RWStepElement.RWStepElement_RWCurveElementSectionDerivedDefinitions_Share)
    WriteStep = _swig_new_instance_method(_RWStepElement.RWStepElement_RWCurveElementSectionDerivedDefinitions_WriteStep)

    __repr__ = _dumps_object

    __swig_destroy__ = _RWStepElement.delete_RWStepElement_RWCurveElementSectionDerivedDefinitions

# Register RWStepElement_RWCurveElementSectionDerivedDefinitions in _RWStepElement:
_RWStepElement.RWStepElement_RWCurveElementSectionDerivedDefinitions_swigregister(RWStepElement_RWCurveElementSectionDerivedDefinitions)

class RWStepElement_RWElementDescriptor(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Empty constructor
        	:rtype: None
        """
        _RWStepElement.RWStepElement_RWElementDescriptor_swiginit(self, _RWStepElement.new_RWStepElement_RWElementDescriptor(*args))
    ReadStep = _swig_new_instance_method(_RWStepElement.RWStepElement_RWElementDescriptor_ReadStep)
    Share = _swig_new_instance_method(_RWStepElement.RWStepElement_RWElementDescriptor_Share)
    WriteStep = _swig_new_instance_method(_RWStepElement.RWStepElement_RWElementDescriptor_WriteStep)

    __repr__ = _dumps_object

    __swig_destroy__ = _RWStepElement.delete_RWStepElement_RWElementDescriptor

# Register RWStepElement_RWElementDescriptor in _RWStepElement:
_RWStepElement.RWStepElement_RWElementDescriptor_swigregister(RWStepElement_RWElementDescriptor)

class RWStepElement_RWElementMaterial(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Empty constructor
        	:rtype: None
        """
        _RWStepElement.RWStepElement_RWElementMaterial_swiginit(self, _RWStepElement.new_RWStepElement_RWElementMaterial(*args))
    ReadStep = _swig_new_instance_method(_RWStepElement.RWStepElement_RWElementMaterial_ReadStep)
    Share = _swig_new_instance_method(_RWStepElement.RWStepElement_RWElementMaterial_Share)
    WriteStep = _swig_new_instance_method(_RWStepElement.RWStepElement_RWElementMaterial_WriteStep)

    __repr__ = _dumps_object

    __swig_destroy__ = _RWStepElement.delete_RWStepElement_RWElementMaterial

# Register RWStepElement_RWElementMaterial in _RWStepElement:
_RWStepElement.RWStepElement_RWElementMaterial_swigregister(RWStepElement_RWElementMaterial)

class RWStepElement_RWSurface3dElementDescriptor(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Empty constructor
        	:rtype: None
        """
        _RWStepElement.RWStepElement_RWSurface3dElementDescriptor_swiginit(self, _RWStepElement.new_RWStepElement_RWSurface3dElementDescriptor(*args))
    ReadStep = _swig_new_instance_method(_RWStepElement.RWStepElement_RWSurface3dElementDescriptor_ReadStep)
    Share = _swig_new_instance_method(_RWStepElement.RWStepElement_RWSurface3dElementDescriptor_Share)
    WriteStep = _swig_new_instance_method(_RWStepElement.RWStepElement_RWSurface3dElementDescriptor_WriteStep)

    __repr__ = _dumps_object

    __swig_destroy__ = _RWStepElement.delete_RWStepElement_RWSurface3dElementDescriptor

# Register RWStepElement_RWSurface3dElementDescriptor in _RWStepElement:
_RWStepElement.RWStepElement_RWSurface3dElementDescriptor_swigregister(RWStepElement_RWSurface3dElementDescriptor)

class RWStepElement_RWSurfaceElementProperty(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Empty constructor
        	:rtype: None
        """
        _RWStepElement.RWStepElement_RWSurfaceElementProperty_swiginit(self, _RWStepElement.new_RWStepElement_RWSurfaceElementProperty(*args))
    ReadStep = _swig_new_instance_method(_RWStepElement.RWStepElement_RWSurfaceElementProperty_ReadStep)
    Share = _swig_new_instance_method(_RWStepElement.RWStepElement_RWSurfaceElementProperty_Share)
    WriteStep = _swig_new_instance_method(_RWStepElement.RWStepElement_RWSurfaceElementProperty_WriteStep)

    __repr__ = _dumps_object

    __swig_destroy__ = _RWStepElement.delete_RWStepElement_RWSurfaceElementProperty

# Register RWStepElement_RWSurfaceElementProperty in _RWStepElement:
_RWStepElement.RWStepElement_RWSurfaceElementProperty_swigregister(RWStepElement_RWSurfaceElementProperty)

class RWStepElement_RWSurfaceSection(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Empty constructor
        	:rtype: None
        """
        _RWStepElement.RWStepElement_RWSurfaceSection_swiginit(self, _RWStepElement.new_RWStepElement_RWSurfaceSection(*args))
    ReadStep = _swig_new_instance_method(_RWStepElement.RWStepElement_RWSurfaceSection_ReadStep)
    Share = _swig_new_instance_method(_RWStepElement.RWStepElement_RWSurfaceSection_Share)
    WriteStep = _swig_new_instance_method(_RWStepElement.RWStepElement_RWSurfaceSection_WriteStep)

    __repr__ = _dumps_object

    __swig_destroy__ = _RWStepElement.delete_RWStepElement_RWSurfaceSection

# Register RWStepElement_RWSurfaceSection in _RWStepElement:
_RWStepElement.RWStepElement_RWSurfaceSection_swigregister(RWStepElement_RWSurfaceSection)

class RWStepElement_RWSurfaceSectionField(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Empty constructor
        	:rtype: None
        """
        _RWStepElement.RWStepElement_RWSurfaceSectionField_swiginit(self, _RWStepElement.new_RWStepElement_RWSurfaceSectionField(*args))
    ReadStep = _swig_new_instance_method(_RWStepElement.RWStepElement_RWSurfaceSectionField_ReadStep)
    Share = _swig_new_instance_method(_RWStepElement.RWStepElement_RWSurfaceSectionField_Share)
    WriteStep = _swig_new_instance_method(_RWStepElement.RWStepElement_RWSurfaceSectionField_WriteStep)

    __repr__ = _dumps_object

    __swig_destroy__ = _RWStepElement.delete_RWStepElement_RWSurfaceSectionField

# Register RWStepElement_RWSurfaceSectionField in _RWStepElement:
_RWStepElement.RWStepElement_RWSurfaceSectionField_swigregister(RWStepElement_RWSurfaceSectionField)

class RWStepElement_RWSurfaceSectionFieldConstant(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Empty constructor
        	:rtype: None
        """
        _RWStepElement.RWStepElement_RWSurfaceSectionFieldConstant_swiginit(self, _RWStepElement.new_RWStepElement_RWSurfaceSectionFieldConstant(*args))
    ReadStep = _swig_new_instance_method(_RWStepElement.RWStepElement_RWSurfaceSectionFieldConstant_ReadStep)
    Share = _swig_new_instance_method(_RWStepElement.RWStepElement_RWSurfaceSectionFieldConstant_Share)
    WriteStep = _swig_new_instance_method(_RWStepElement.RWStepElement_RWSurfaceSectionFieldConstant_WriteStep)

    __repr__ = _dumps_object

    __swig_destroy__ = _RWStepElement.delete_RWStepElement_RWSurfaceSectionFieldConstant

# Register RWStepElement_RWSurfaceSectionFieldConstant in _RWStepElement:
_RWStepElement.RWStepElement_RWSurfaceSectionFieldConstant_swigregister(RWStepElement_RWSurfaceSectionFieldConstant)

class RWStepElement_RWSurfaceSectionFieldVarying(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Empty constructor
        	:rtype: None
        """
        _RWStepElement.RWStepElement_RWSurfaceSectionFieldVarying_swiginit(self, _RWStepElement.new_RWStepElement_RWSurfaceSectionFieldVarying(*args))
    ReadStep = _swig_new_instance_method(_RWStepElement.RWStepElement_RWSurfaceSectionFieldVarying_ReadStep)
    Share = _swig_new_instance_method(_RWStepElement.RWStepElement_RWSurfaceSectionFieldVarying_Share)
    WriteStep = _swig_new_instance_method(_RWStepElement.RWStepElement_RWSurfaceSectionFieldVarying_WriteStep)

    __repr__ = _dumps_object

    __swig_destroy__ = _RWStepElement.delete_RWStepElement_RWSurfaceSectionFieldVarying

# Register RWStepElement_RWSurfaceSectionFieldVarying in _RWStepElement:
_RWStepElement.RWStepElement_RWSurfaceSectionFieldVarying_swigregister(RWStepElement_RWSurfaceSectionFieldVarying)

class RWStepElement_RWUniformSurfaceSection(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Empty constructor
        	:rtype: None
        """
        _RWStepElement.RWStepElement_RWUniformSurfaceSection_swiginit(self, _RWStepElement.new_RWStepElement_RWUniformSurfaceSection(*args))
    ReadStep = _swig_new_instance_method(_RWStepElement.RWStepElement_RWUniformSurfaceSection_ReadStep)
    Share = _swig_new_instance_method(_RWStepElement.RWStepElement_RWUniformSurfaceSection_Share)
    WriteStep = _swig_new_instance_method(_RWStepElement.RWStepElement_RWUniformSurfaceSection_WriteStep)

    __repr__ = _dumps_object

    __swig_destroy__ = _RWStepElement.delete_RWStepElement_RWUniformSurfaceSection

# Register RWStepElement_RWUniformSurfaceSection in _RWStepElement:
_RWStepElement.RWStepElement_RWUniformSurfaceSection_swigregister(RWStepElement_RWUniformSurfaceSection)

class RWStepElement_RWVolume3dElementDescriptor(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Empty constructor
        	:rtype: None
        """
        _RWStepElement.RWStepElement_RWVolume3dElementDescriptor_swiginit(self, _RWStepElement.new_RWStepElement_RWVolume3dElementDescriptor(*args))
    ReadStep = _swig_new_instance_method(_RWStepElement.RWStepElement_RWVolume3dElementDescriptor_ReadStep)
    Share = _swig_new_instance_method(_RWStepElement.RWStepElement_RWVolume3dElementDescriptor_Share)
    WriteStep = _swig_new_instance_method(_RWStepElement.RWStepElement_RWVolume3dElementDescriptor_WriteStep)

    __repr__ = _dumps_object

    __swig_destroy__ = _RWStepElement.delete_RWStepElement_RWVolume3dElementDescriptor

# Register RWStepElement_RWVolume3dElementDescriptor in _RWStepElement:
_RWStepElement.RWStepElement_RWVolume3dElementDescriptor_swigregister(RWStepElement_RWVolume3dElementDescriptor)



