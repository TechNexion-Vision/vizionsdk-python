import pyvizionsdk
from pyvizionsdk import VX_UVC_IMAGE_PROPERTIES, VX_IMAGE_FORMAT
import sys


result, camera_list = pyvizionsdk.VxDiscoverCameraDevices()
if result == 0:
    print("No device detected. Please ensure the device is connected.")
    sys.exit()

print("Discovered cameras:")

# print camera_list
for camera in camera_list:
    print(camera)

print(f"Start initial device: {camera_list[0]}")

# initialize camera device
camera = pyvizionsdk.VxInitialCameraDevice(0)

# open camera
result = pyvizionsdk.VxOpen(camera)
print("Open camera return code:", result)

# get the camera device name 
result, name = pyvizionsdk.VxGetDeviceName(camera)
print("Device name:", name)

# get interface type
result, tyname = pyvizionsdk.VxGetDeviceInterfaceType(camera)
print("Device Interface type name:", tyname)

result, format_list = pyvizionsdk.VxGetFormatList(camera)
mjpg_format = None
min_resolution = float('inf')
for format in format_list:
    # get mjpg format and minimum resolution
    if format.format == VX_IMAGE_FORMAT.VX_IMAGE_FORMAT_MJPG:
        resolution = format.width * format.height
        if resolution < min_resolution:
            min_resolution = resolution
            mjpg_format = format
print("Get format List return code:", result)

result = pyvizionsdk.VxSetFormat(camera, mjpg_format)
print("Set format return code:", result)

# start streaming
result = pyvizionsdk.VxStartStreaming(camera)
print("Start streaming return code:", result)

# UVC Image Processing
result, brightness, flag = pyvizionsdk.VxGetUVCImageProcessing(camera, VX_UVC_IMAGE_PROPERTIES.UVC_IMAGE_BRIGHTNESS)
print("UVC brightness:", brightness)
print("Flag:", flag)
print("Return code:", result)

# set the brightness
result = pyvizionsdk.VxSetUVCImageProcessing(camera, VX_UVC_IMAGE_PROPERTIES.UVC_IMAGE_BRIGHTNESS, 12, 0)
print("Set UVC brightness return code:", result)

# stop streaming
result = pyvizionsdk.VxStopStreaming(camera)
print("Stop streaming return code:", result)

# close camera
pyvizionsdk.VxClose(camera)
