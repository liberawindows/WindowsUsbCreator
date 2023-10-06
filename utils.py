import subprocess
import json

def check_woeusb_installed():
    """Check if WoeUSB is installed on the system."""
    try:
        subprocess.check_output(["woeusb", "--version"])
        return True
    except:
        return False

def get_usb_devices():
    """Use lsblk to get a list of block devices and parse the JSON output for USB devices."""
    result = subprocess.check_output(["lsblk", "-J"]).decode("utf-8")
    devices = json.loads(result)["blockdevices"]

    usb_devices = []
    for device in devices:
        if device["rm"] == 1:  # if the device is removable
            usb_devices.append(f"/dev/{device['name']} ({device['size']})")

    return usb_devices
