# This program was written by Tommy Mathisen
# This was written for the purpose of creating a bootable USB drive in an easy way on Linux
# The reason for this is that I have seen uers struggle with the terminal and the commands needed to create a bootable USB drive
from bootable_usb_creator import BootableUSBCreator

if __name__ == "__main__":
    app = BootableUSBCreator()
    app.mainloop()
