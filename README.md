# Image Background Removal Project

## Overview

This project provides a simple and efficient way to automatically remove
the background from one or more images using Python. It leverages a
pre-trained machine learning model to segment the foreground from the
background, saving the result as a new image with a transparent
background.

## Features

-   Batch Processing: Process multiple images at once by placing them in
    a single folder.
-   Automatic Output: Automatically saves processed images to a
    designated output folder.
-   Simple to Use: Minimal setup required to get started.

# Project Structure
```
    project_background_remover/
    ├── images/                  # Place your input images here
    │   ├── image1.png
    │   ├── image2.jpg
    │   └── ...
    ├── output/                  # Processed images with transparent backgrounds are saved here
    │   ├── image1.png
    │   ├── image2.png
    │   └── ...
    ├── background_remover.py    # The main Python script
    ├── README.md                # This file
    └── requirements.txt         # Project dependencies
```
## Setup

1.  Install Dependencies

First, ensure you have Python installed. Then, navigate to the project
directory in your terminal and install the required libraries using pip:
```
    pip install -r requirements.txt
```
2.  Place Your Images

Place all the images you want to process inside the images/ folder. The
script is configured to look for files in this directory.

Usage

To run the background removal script, simply execute the
background_remover.py file from your terminal:
```
    python background_remover.py
```
The script will automatically create an output/ folder and save the new
images with their backgrounds removed inside it.

## Technical Details

This project utilizes the rembg library, which is built on a deep
learning model for image matting and background removal. It provides a
simple API to handle the complex segmentation process. The Pillow
library is used for basic image handling, and onnxruntime is the backend
for running the machine learning model.
