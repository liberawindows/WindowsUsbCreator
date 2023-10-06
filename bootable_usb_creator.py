import tkinter as tk
from tkinter import filedialog
import os
import subprocess
import json
from utils import check_woeusb_installed, get_usb_devices

class BootableUSBCreator(tk.Tk):
    """Main GUI class for the Bootable USB Creator."""
    
    def __init__(self):
        super().__init__()

        self.title("Mathisen's Windows USB Creator")
        self.geometry("600x400")

        self.iso_path = tk.StringVar()
        self.woeusb_installed = check_woeusb_installed()

        # Labels and buttons
        self.label = tk.Label(self, text="Select ISO and USB Drive to create bootable USB")
        self.label.pack(pady=20)

        self.status_label = tk.Label(self, text=self.get_status_text())
        self.status_label.pack(pady=10)

        self.iso_button = tk.Button(self, text="Choose ISO File", command=self.choose_iso, bg='white')
        self.iso_button.pack(pady=10)

        self.usb_label = tk.Label(self, text="Choose a USB drive from the list below:")
        self.usb_label.pack(pady=5)

        self.usb_listbox = tk.Listbox(self, height=5)
        self.usb_listbox.bind("<<ListboxSelect>>", self.on_usb_select)
        self.usb_listbox.pack(pady=10, padx=10, fill=tk.BOTH)
        self.refresh_usb_list()

        if not self.woeusb_installed:
            self.install_button = tk.Button(self, text="Install WoeUSB", command=self.install_woeusb, bg='red')
            self.install_button.pack(pady=10)
        else:
            self.install_button = tk.Button(self, text="WoeUSB Installed", bg='green')
            self.install_button.pack(pady=10)

        self.create_button = tk.Button(self, text="Create Bootable USB", command=self.create_usb, state=tk.DISABLED if not self.woeusb_installed else tk.NORMAL)
        self.create_button.pack(pady=10)

    def get_status_text(self):
        """Return the status text based on WoeUSB installation."""
        return "WoeUSB is installed!" if self.woeusb_installed else "WoeUSB is not installed. Please install it first."

    def choose_iso(self):
        """Open file dialog to let the user choose an ISO file."""
        file_path = filedialog.askopenfilename(title="Choose Windows ISO", filetypes=[("ISO files", "*.iso")])
        if file_path:
            self.iso_path.set(file_path)
            self.iso_button.config(text=os.path.basename(file_path), bg='green')

    def refresh_usb_list(self):
        """Refresh the list of USB drives shown in the listbox."""
        self.usb_listbox.delete(0, tk.END)
        devices = get_usb_devices()
        for device in devices:
            self.usb_listbox.insert(tk.END, device)

    def on_usb_select(self, event):
        """Highlight the listbox when a USB drive is selected."""
        if self.usb_listbox.curselection():
            self.usb_listbox.config(bg="green")

    def install_woeusb(self):
        """Install WoeUSB using the package manager."""
        # For simplicity, Debian/Ubuntu/mint installation steps are provided. (will add more distros later)
        commands = [
            ["pkexec", "apt", "install", "git", "p7zip-full", "grub2-common", "grub-pc-bin", "parted", "dosfstools", "ntfs-3g"],
            ["pkexec", "pip3", "install", "wxPython"],
            ["pkexec", "pip3", "install", "WoeUSB-ng"]
        ]
        for cmd in commands:
            subprocess.Popen(cmd).wait()

        # Refresh the status after installation attempt
        self.woeusb_installed = check_woeusb_installed()
        self.status_label.config(text=self.get_status_text())
        if self.woeusb_installed:
            self.install_button.config(text="WoeUSB Installed", bg='green')
            self.create_button.config(state=tk.NORMAL)

    def create_usb(self):
        """Create the bootable USB using the selected ISO and USB drive."""
        if self.iso_path.get() and self.usb_listbox.curselection():
            selected_usb = self.usb_listbox.get(self.usb_listbox.curselection())
            usb_path = selected_usb.split(" ")[0]
            cmd = ["woeusb", "--target-filesystem", "NTFS", "--device", self.iso_path.get(), usb_path]
            subprocess.Popen(cmd)
