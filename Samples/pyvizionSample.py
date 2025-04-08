import pyvizionsdk
from pyvizionsdk import VX_UVC_IMAGE_PROPERTIES


result, camera_list = pyvizionsdk.VxDiscoverCameraDevices()
print("Discovered cameras:", camera_list)

# print camera_list
for camera in camera_list:
    print(camera)

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
