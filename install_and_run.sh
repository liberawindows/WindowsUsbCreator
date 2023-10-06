#!/bin/bash

# Variables
REPO_URL="https://github.com/mathisen99/windows-usb-creator.git"
DIRECTORY_NAME="windows-usb-creator"

# Function to check if a command exists
command_exists() {
    command -v "$1" &> /dev/null
}

# Install git, python3, pip3 if they don't exist
if ! command_exists git; then
    echo "Git is not installed. Installing git..."
    sudo apt update
    sudo apt install -y git
fi

if ! command_exists python3; then
    echo "Python3 is not installed. Installing Python3..."
    sudo apt update
    sudo apt install -y python3
fi

if ! command_exists pip3; then
    echo "pip3 is not installed. Installing pip3..."
    sudo apt update
    sudo apt install -y python3-pip
fi

# Clone the repository
git clone $REPO_URL $DIRECTORY_NAME
cd $DIRECTORY_NAME

# Install required packages
echo "Installing additional required packages..."
sudo apt update
sudo apt install -y python3-tk policykit-1

# Run the application
python3 main.py
