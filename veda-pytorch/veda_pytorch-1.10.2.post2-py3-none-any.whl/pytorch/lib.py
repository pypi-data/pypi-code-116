__all__ = []

import ctypes
import os
import collections
import torch # make sure pytorch was loaded before

if not "1.10.2" in torch.__version__:
	raise sol.Exception("The NEC SX-Aurora TSUBASA can only be used with PyTorch v1.10.2 but you are using {}".format(torch.__version__))

cwd				= os.path.dirname(__file__)
libvedapytorch	= ctypes.cdll.LoadLibrary(os.path.join(cwd, 'lib64/libveda-pytorch.so'))
libveda			= ctypes.cdll.LoadLibrary(os.path.join(cwd, '../lib64/libveda.so.1'))

# Prevent Huggingface-BERT to load TF! -----------------------------------------
os.environ["USE_TORCH"] = "ON"

libveda.vedaCtxGetDevice.argtypes				= [ctypes.c_void_p]
libveda.vedaCtxGetDevice.restype				= ctypes.c_int
libveda.vedaCtxPushCurrent.argtypes				= [ctypes.c_void_p]
libveda.vedaCtxPushCurrent.restype				= ctypes.c_int
libveda.vedaCtxPopCurrent.argtypes				= [ctypes.c_void_p]
libveda.vedaCtxPopCurrent.restype				= ctypes.c_int
libveda.vedaDevicePrimaryCtxRetain.argtypes		= [ctypes.c_void_p, ctypes.c_int]
libveda.vedaDevicePrimaryCtxRetain.restype		= ctypes.c_int
libveda.vedaCtxSynchronize.argtypes				= []
libveda.vedaCtxSynchronize.restype				= ctypes.c_int
libveda.vedaDeviceGetCount.argtypes				= [ctypes.c_void_p]
libveda.vedaDeviceGetCount.restype				= ctypes.c_int
libveda.vedaDevicePrimaryCtxGetState.argtypes	= [ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]
libveda.vedaDevicePrimaryCtxGetState.restype	= ctypes.c_int
libveda.vedaMemGetInfo.argtypes					= [ctypes.c_void_p, ctypes.c_void_p]
libveda.vedaMemGetInfo.restype					= ctypes.c_int

def is_available():
	return True

def current_device():
	device = ctypes.c_int()
	libveda.vedaCtxGetDevice(ctypes.byref(device))
	return device.value

def set_device(idx):
	ctx = ctypes.c_void_p()
	libveda.vedaDevicePrimaryCtxRetain(ctypes.byref(ctx), idx)
	libveda.vedaCtxPushCurrent(ctx)

def device_count():
	cnt = ctypes.c_int()
	libveda.vedaDeviceGetCount(ctypes.byref(cnt))
	return cnt.value

def get_device_idx(device):
	if device is None:						return -1
	elif isinstance(device, torch.device):	return device.index
	elif isinstance(device, int):			return device
	raise Exception("Invalid type, expected None, torch.device or int but is {}".format(type(device)))

def memory_allocated(device=None):
	device	= get_device_idx(device)
	total	= ctypes.c_long()
	free	= ctypes.c_long()
	libveda.vedaMemGetInfo(ctypes.byref(free), ctypes.byref(total))
	return total.value - free.value

def to_ve(self, device=None, non_blocking=False, memory_format=torch.preserve_format):
	assert device == None or isinstance(device, int)
	return self.to(device=torch.device('ve', device), non_blocking=non_blocking, memory_format=memory_format)

def to_model_ve(self, device=None):
	assert device == None or isinstance(device, int)
	return self.to(device=torch.device('ve', device))

class Device:
	def __init__(self, device):
		if isinstance(device, str):
			device = torch.device(device)
			assert device.type == 've'
		assert isinstance(device, torch.device) or isinstance(device, int)
		self.m_previous = None
		self.m_device   = device.index if isinstance(device, torch.device) else device

	def __enter__(self):
		assert isinstance(self.m_device, int)
		self.m_previous = current_device()
		set_device(self.m_device)
		return self

	def __exit__(self, type, value, traceback):
		assert isinstance(self.m_previous, int)
		ctx = ctypes.c_void_p()
		libveda.vedaCtxPopCurrent(ctypes.byref(ctx))
		
class DeviceOf(Device):
	def __init__(self, tensor):
		super().__init__(tensor.device)

def synchronize(device=None):
	device	= get_device_idx(device)

	flags	= ctypes.c_int()
	active	= ctypes.c_int()

	def sync(device):
		libveda.vedaDevicePrimaryCtxGetState(device, ctypes.byref(flags), ctypes.byref(active))
		if active.value:
			with Device(device):
				libveda.vedaCtxSynchronize()

	if device == -1:
		for i in range(device_count()):
			sync(i)
	else:
		sync(device)

torch.ve			= collections.namedtuple('VE', ['synchronize', 'is_available', 'current_device', 'set_device', 'device_count', 'device', 'device_of', 'memory_allocated'])(synchronize, is_available, current_device, set_device, device_count, Device, DeviceOf, memory_allocated)
torch.Tensor.ve		= to_ve
torch.nn.Module.ve	= to_model_ve
