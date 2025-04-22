# pyvizionsdk
pyvizionsdk is a software development kit for Python bindings wrapped from the original VizionSDK C++ implementation. It supports various versions of Python on different types of platforms.

## What is included in the repository
- Samples : Python samples project source code.
- config : A config file of TechNexion Camera series for pyvizionsdk to recognize the devices.

## Supported TechNexion Cameras

| Sensor | MIPI           | FPD-LinkIII      | UVC            |
|--------|----------------|------------------|----------------|
| AR0144 | ✓ TEVS-AR0144  | ✓ VLS3-AR0144    | ✓ VCI-AR0144   |
| AR0145 | ✓ TEVS-AR0145  | ✓ VLS3-AR0145    |                |
| AR0234 | ✓ TEVS-AR0234  | ✓ VLS3-AR0234    | ✓ VCI-AR0234   |
| AR0521 | ✓ TEVS-AR0521  | ✓ VLS3-AR0521    | ✓ VCI-AR0521   |
| AR0522 | ✓ TEVS-AR0522  | ✓ VLS3-AR0522    | ✓ VCI-AR0522   |
| AR0821 | ✓ TEVS-AR0821  | ✓ VLS3-AR0821    | ✓ VCI-AR0821   |
| AR0822 | ✓ TEVS-AR0822  | ✓ VLS3-AR0822    | ✓ VCI-AR0822   |
| AR1335 | ✓ TEVS-AR1335  | ✓ VLS3-AR1335    | ✓ VCI-AR1335   |
  
## Supported Versions

- Python 3.8
- Python 3.9
- Python 3.10
- Python 3.11
- Python 3.12
- Python 3.13

## How to Install pyvizionsdk

#### `pip install` from the website directly
```
pip install pyvizionsdk -i https://pypi.vizionsdk.com/root/pyvizionsdk/+simple/
```
⚠️ **Note for Linux and embedded systems:**  
If you intend to use the `pyvizion-ctl` tool, please ensure that `~/.local/bin` is included in your `PATH` environment variable.

#### [Windows x64](https://developer.technexion.com/docs/vizionsdk-python-installation#windowsx64)
- Windows 10 and 11 (64-bit)
#### [Linux x64](https://developer.technexion.com/docs/vizionsdk-python-installation#linuxx64)
- Ubuntu Desktop 20.04 and 22.04 (64-bit)
- UP Squared Pro 7000
#### [Linux ARM64](https://developer.technexion.com/docs/vizionsdk-python-installation#linuxarm64)
- NVIDIA Jetson (JetPack5 or later)
- NXP-i.MX8MM, NXP-i.MX8MQ, NXP-i.MX8MP, NXP-i.MX93, NXP-i.MX95
- TI-TDA4VM
  
## Documents
- Github Pages: https://github.com/TechNexion
- VizionSDK Overview: https://developer.technexion.com/docs/vizionsdk-overview
- VizionSDK Python Installation: https://developer.technexion.com/docs/vizionsdk-python-installation
- VizionSDK API User Guide: https://developer.technexion.com/docs/vizionsdk-api-log-file-setting

## Related links
- [Technexion Main Page](https://www.technexion.com/)
