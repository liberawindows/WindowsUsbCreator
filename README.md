# \#Windows @ Libera USB Creator

# Windows USB Creator for Linux

A user-friendly GUI application designed specifically to address a common challenge encountered by users in the #windows channel on the Libera IRC network: creating a bootable Windows USB from a Linux system.

## Connecting to Libera IRC Network

1. **Using an IRC Client**:
   - Server: `irc.libera.chat`
   - Port: `6667` (or `6697` for SSL)
   - Channel: `#windows`
   
2. **Using a Web Client**:
   - Visit [Libera Chat's web client](https://web.libera.chat/)
   - Choose a nickname and enter `#windows` as the channel to join.

**Note**: To join the `#windows` channel, users must be registered with `NickServ` on the Libera IRC network.


## Screenshot
<p align="center">
  <img src="https://imgur.com/SoLDhSN.png" alt="Screenshot of the application">
</p>


## Quick Installation and Run

For a quick installation and run, execute the following command:

```bash
curl -sL https://raw.githubusercontent.com/liberawindows/windowsusbcreator/main/install_and_run.sh | bash
```

**Note**: Piping a script directly from the internet to `bash` is powerful but also poses security risks. Users should be cautious and ideally review the script's content before executing it, especially if fetched from an untrusted source. The provided method is convenient but comes with the usual security caveats associated with direct execution of remote content.

## Features

- Intuitive GUI to select a Windows ISO file.
- Display and selection of attached USB drives.
- Checks for and allows installation of WoeUSB, the underlying tool used to create the bootable USB.
- Informative status updates and prompts.

## Prerequisites

- Python 3.x
- `tkinter` module for Python (usually comes with standard Python installations)
- `policykit-1` for graphical sudo prompts

## Usage

1. Clone the repository:
```git clone https://github.com/liberawindows/WindowsUsbCreator.git ```
2. Run the application:
```python3 main.py```
3. Follow the on-screen instructions to select an ISO file and a USB drive.
4. Install WoeUSB if not already installed.
5. Click on "Create Bootable USB" to start the process.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)