# pyvizionsdk
pyvizionsdk is a software development kit for Python bindings wrapped from the original VizionSDK C++ implementation. It supports various versions of Python on different types of platforms.

## What is included in the repository
- Samples : Python samples project source code.
- config : A config file of TechNexion Camera series for pyvizionsdk to recognize the devices.

## Supported TechNexion Cameras

### MIPI Cameras
- TEVS-AR0144
- TEVS-AR0145
- TEVS-AR0234
- TEVS-AR0521
- TEVS-AR0522
- TEVS-AR0522
- TEVS-AR0821
- TEVS-AR0822
- TEVS-AR1335

### FPD-LinkIII Cameras

- VLS3-AR0144
- VLS3-AR0145
- VLS3-AR0234
- VLS3-AR0521
- VLS3-AR0522
- VLS3-AR0522
- VLS3-AR0821
- VLS3-AR0822
- VLS3-AR1335

### UVC Cameras

- VCI-AR0144
- VCI-AR0234
- VCI-AR0521
- VCI-AR0522
- VCI-AR0522
- VCI-AR0821
- VCI-AR0822
- VCI-AR1335

## Supported Platforms
- Windows 10/11
- Ubuntu
- NXP i.MX93
- NXP i.MX95
- NXP i.MX8MP
- NXP i.MX8MM
- Jetson Orin Nano (JetPack 5.x/6.x)
- UP Squared Pro 7000
  
## Supported Versions

- Python 3.8
- Python 3.9
- Python 3.10
- Python 3.11
- Python 3.12
- Python 3.13

### How to Install pyvizionsdk

#### `pip install` from the website directly
```
pip install pyvizionsdk -i https://pypi.vizionsdk.com/root/pyvizionsdk/+simple/
```
⚠️ **Note for Linux and embedded systems:**  
If you intend to use the `pyvizion-ctl` tool, please ensure that `~/.local/bin` is included in your `PATH` environment variable.

#### X86 Platforms
- [Windows 10 and 11 (64-bit)](https://developer.technexion.com/docs/python-installation#windows)
- [Linux (Debian): Ubuntu Desktop 20.04 and 22.04 (64-bit)](https://developer.technexion.com/docs/python-installation#linux)

#### Embedded Platforms
- [NXP-iMX93, NXP-iMX95, NXP-iMX8MP, NXP-iMX8MM](https://developer.technexion.com/docs/python-installation#arm)
- [NVIDIA-Jetpack5 and Later](https://developer.technexion.com/docs/python-installation#arm)
  
## Documents
- Github Pages：https://github.com/TechNexion
- Overview Document：https://developer.technexion.com/docs/product-category-overview
- API User Guide: https://developer.technexion.com/docs/log-file-setting-1

## Related links
- [Technexion Main Page](https://www.technexion.com/)
