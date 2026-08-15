# CS50P - Shirt

A Python program that overlays a shirt design onto a user-provided image.

This project was completed as part of **CS50's Introduction to Programming with Python (CS50P)**.

## What it does

The program:

- Takes an input image and an output filename through command-line arguments.
- Checks that the correct number of arguments is provided.
- Validates the input and output image extensions.
- Resizes and crops the input image to 600 × 600 pixels using `ImageOps.fit`.
- Opens the provided `shirt.png` overlay.
- Applies the shirt overlay to the resized image using its transparency mask.
- Saves the resulting image using the requested output filename.

## Technologies

- Python
- Pillow (`PIL`)
- Command-line arguments
- Image processing

## How to run

Install Pillow if it is not already installed:
pip install pillow
Then run-
python shirt.py input.jpg output.jpg
The input and output files must use the same image extension.

## What I practiced

This project helped me practice:

Command-line arguments with sys.argv
Conditional statements
String methods such as endswith() and lower()
File handling with with
Image manipulation using Pillow
Image resizing and cropping
Applying an image overlay using a mask
Handling invalid user input with sys.exit()
