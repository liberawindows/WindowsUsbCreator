#!/bin/bash

# Variables
REPO_URL="https://github.com/mathisen99/windows-usb-creator.git"
DIRECTORY_NAME="windows-creator"

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "Git is not installed. Please install git first."
    exit 1
fi

# Clone the repository
git clone $REPO_URL $DIRECTORY_NAME
cd $DIRECTORY_NAME

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python3 is not installed. Please install Python3 first."
    exit 1
fi

# Install required packages
echo "Installing required packages..."
sudo apt update
sudo apt install -y python3-tk policykit-1

# Run the application
python3 main.py