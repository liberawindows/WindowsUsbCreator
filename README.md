# Mathisen's Windows USB Creator

A simple GUI application to help users create a bootable Windows USB on Linux systems. The application is built using Python's `tkinter` module.

## Screenshot
![Screenshot of the application](https://imgur.com/R439Ow5.png)

## Quick Installation and Run

For a quick installation and run, execute the following command:

```bash
curl -sL https://raw.githubusercontent.com/mathisen99/windows-usb-creator/main/install_and_run.sh | bash
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
```git clone foobar ```
2. Run the application:
```python3 main.py```
3. Follow the on-screen instructions to select an ISO file and a USB drive.
4. Install WoeUSB if not already installed.
5. Click on "Create Bootable USB" to start the process.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)