# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.9
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ultimateCreditCardSdk', [dirname(__file__)])
        except ImportError:
            import _ultimateCreditCardSdk
            return _ultimateCreditCardSdk
        if fp is not None:
            try:
                _mod = imp.load_module('_ultimateCreditCardSdk', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _ultimateCreditCardSdk = swig_import_helper()
    del swig_import_helper
else:
    import _ultimateCreditCardSdk
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


try:
    import weakref
    weakref_proxy = weakref.proxy
except:
    weakref_proxy = lambda x: x


ULTCCARD_SDK_VERSION_MAJOR = _ultimateCreditCardSdk.ULTCCARD_SDK_VERSION_MAJOR
ULTCCARD_SDK_VERSION_MINOR = _ultimateCreditCardSdk.ULTCCARD_SDK_VERSION_MINOR
ULTCCARD_SDK_VERSION_MICRO = _ultimateCreditCardSdk.ULTCCARD_SDK_VERSION_MICRO
ULTCCARD_SDK_IMAGE_TYPE_RGB24 = _ultimateCreditCardSdk.ULTCCARD_SDK_IMAGE_TYPE_RGB24
ULTCCARD_SDK_IMAGE_TYPE_RGBA32 = _ultimateCreditCardSdk.ULTCCARD_SDK_IMAGE_TYPE_RGBA32
ULTCCARD_SDK_IMAGE_TYPE_BGRA32 = _ultimateCreditCardSdk.ULTCCARD_SDK_IMAGE_TYPE_BGRA32
ULTCCARD_SDK_IMAGE_TYPE_NV12 = _ultimateCreditCardSdk.ULTCCARD_SDK_IMAGE_TYPE_NV12
ULTCCARD_SDK_IMAGE_TYPE_NV21 = _ultimateCreditCardSdk.ULTCCARD_SDK_IMAGE_TYPE_NV21
ULTCCARD_SDK_IMAGE_TYPE_YUV420P = _ultimateCreditCardSdk.ULTCCARD_SDK_IMAGE_TYPE_YUV420P
ULTCCARD_SDK_IMAGE_TYPE_YVU420P = _ultimateCreditCardSdk.ULTCCARD_SDK_IMAGE_TYPE_YVU420P
ULTCCARD_SDK_IMAGE_TYPE_YUV422P = _ultimateCreditCardSdk.ULTCCARD_SDK_IMAGE_TYPE_YUV422P
ULTCCARD_SDK_IMAGE_TYPE_YUV444P = _ultimateCreditCardSdk.ULTCCARD_SDK_IMAGE_TYPE_YUV444P
class UltCreditCardSdkResult(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, UltCreditCardSdkResult, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, UltCreditCardSdkResult, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _ultimateCreditCardSdk.new_UltCreditCardSdkResult(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ultimateCreditCardSdk.delete_UltCreditCardSdkResult
    __del__ = lambda self : None;
    def code(self): return _ultimateCreditCardSdk.UltCreditCardSdkResult_code(self)
    def phrase(self): return _ultimateCreditCardSdk.UltCreditCardSdkResult_phrase(self)
    def json(self): return _ultimateCreditCardSdk.UltCreditCardSdkResult_json(self)
    def numCards(self): return _ultimateCreditCardSdk.UltCreditCardSdkResult_numCards(self)
    def isOK(self): return _ultimateCreditCardSdk.UltCreditCardSdkResult_isOK(self)
UltCreditCardSdkResult_swigregister = _ultimateCreditCardSdk.UltCreditCardSdkResult_swigregister
UltCreditCardSdkResult_swigregister(UltCreditCardSdkResult)

class UltCreditCardSdkParallelDeliveryCallback(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, UltCreditCardSdkParallelDeliveryCallback, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, UltCreditCardSdkParallelDeliveryCallback, name)
    __repr__ = _swig_repr
    def __init__(self): 
        if self.__class__ == UltCreditCardSdkParallelDeliveryCallback:
            _self = None
        else:
            _self = self
        this = _ultimateCreditCardSdk.new_UltCreditCardSdkParallelDeliveryCallback(_self, )
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ultimateCreditCardSdk.delete_UltCreditCardSdkParallelDeliveryCallback
    __del__ = lambda self : None;
    def onNewResult(self, *args): return _ultimateCreditCardSdk.UltCreditCardSdkParallelDeliveryCallback_onNewResult(self, *args)
    def __disown__(self):
        self.this.disown()
        _ultimateCreditCardSdk.disown_UltCreditCardSdkParallelDeliveryCallback(self)
        return weakref_proxy(self)
UltCreditCardSdkParallelDeliveryCallback_swigregister = _ultimateCreditCardSdk.UltCreditCardSdkParallelDeliveryCallback_swigregister
UltCreditCardSdkParallelDeliveryCallback_swigregister(UltCreditCardSdkParallelDeliveryCallback)

class UltCreditCardSdkEngine(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, UltCreditCardSdkEngine, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, UltCreditCardSdkEngine, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_getmethods__["init"] = lambda x: _ultimateCreditCardSdk.UltCreditCardSdkEngine_init
    if _newclass:init = staticmethod(_ultimateCreditCardSdk.UltCreditCardSdkEngine_init)
    __swig_getmethods__["deInit"] = lambda x: _ultimateCreditCardSdk.UltCreditCardSdkEngine_deInit
    if _newclass:deInit = staticmethod(_ultimateCreditCardSdk.UltCreditCardSdkEngine_deInit)
    __swig_getmethods__["process"] = lambda x: _ultimateCreditCardSdk.UltCreditCardSdkEngine_process
    if _newclass:process = staticmethod(_ultimateCreditCardSdk.UltCreditCardSdkEngine_process)
    __swig_getmethods__["requestRuntimeLicenseKey"] = lambda x: _ultimateCreditCardSdk.UltCreditCardSdkEngine_requestRuntimeLicenseKey
    if _newclass:requestRuntimeLicenseKey = staticmethod(_ultimateCreditCardSdk.UltCreditCardSdkEngine_requestRuntimeLicenseKey)
    __swig_getmethods__["warmUp"] = lambda x: _ultimateCreditCardSdk.UltCreditCardSdkEngine_warmUp
    if _newclass:warmUp = staticmethod(_ultimateCreditCardSdk.UltCreditCardSdkEngine_warmUp)
    __swig_destroy__ = _ultimateCreditCardSdk.delete_UltCreditCardSdkEngine
    __del__ = lambda self : None;
UltCreditCardSdkEngine_swigregister = _ultimateCreditCardSdk.UltCreditCardSdkEngine_swigregister
UltCreditCardSdkEngine_swigregister(UltCreditCardSdkEngine)

def UltCreditCardSdkEngine_init(*args):
  return _ultimateCreditCardSdk.UltCreditCardSdkEngine_init(*args)
UltCreditCardSdkEngine_init = _ultimateCreditCardSdk.UltCreditCardSdkEngine_init

def UltCreditCardSdkEngine_deInit():
  return _ultimateCreditCardSdk.UltCreditCardSdkEngine_deInit()
UltCreditCardSdkEngine_deInit = _ultimateCreditCardSdk.UltCreditCardSdkEngine_deInit

def UltCreditCardSdkEngine_process(*args):
  return _ultimateCreditCardSdk.UltCreditCardSdkEngine_process(*args)
UltCreditCardSdkEngine_process = _ultimateCreditCardSdk.UltCreditCardSdkEngine_process

def UltCreditCardSdkEngine_requestRuntimeLicenseKey(rawInsteadOfJSON=False):
  return _ultimateCreditCardSdk.UltCreditCardSdkEngine_requestRuntimeLicenseKey(rawInsteadOfJSON)
UltCreditCardSdkEngine_requestRuntimeLicenseKey = _ultimateCreditCardSdk.UltCreditCardSdkEngine_requestRuntimeLicenseKey

def UltCreditCardSdkEngine_warmUp(*args):
  return _ultimateCreditCardSdk.UltCreditCardSdkEngine_warmUp(*args)
UltCreditCardSdkEngine_warmUp = _ultimateCreditCardSdk.UltCreditCardSdkEngine_warmUp

# This file is compatible with both classic and new-style classes.


