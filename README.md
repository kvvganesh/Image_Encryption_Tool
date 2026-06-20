🖼️ Image Encryption Tool — Pixel Manipulation

A Python command-line tool that encrypts and decrypts images using three different pixel-manipulation techniques: XOR, pixel swapping, and add/subtract key. Built as part of a Cybersecurity Internship task.



📋 Overview

Every digital image is just a grid of pixels, and every pixel is made of three numbers — Red, Green, and Blue, each ranging from 0–255. This tool scrambles those numbers using simple, reversible math, so the image becomes unreadable until decrypted with the correct key.

All three methods implemented here are fully reversible — encrypting and then decrypting with the same key restores the exact original image, pixel for pixel.


✨ Features

MethodHow it worksReversible byXOR Encryptionpixel ^ key on every R, G, B valueRunning the same XOR operation again with the same keyPixel SwappingSwaps every pair of adjacent pixels in the imageRunning the swap again — applying it twice restores original orderAdd Key(pixel + key) % 256 on every channel(pixel - key) % 256 — the subtract function

Other features:


Input validation for encryption keys (must be 1–255)
Output path validation (must end in a supported image extension)
Progress percentage shown during processing for larger images
Always saves output as lossless PNG, even if you type a different extension — this prevents JPEG's lossy compression from corrupting pixel data and breaking decryption
Clear error handling for missing files and invalid input



🛠️ Requirements

Python 3.8+
Pillow library

```
bashpip install pillow
```

▶️ Usage

bashpython task2_image_encryption.py

You'll see a menu:

=== ENCRYPTION OPTIONS ===
1. XOR Encrypt
2. Swap Pixels Encrypt
3. Add Key Encrypt

=== DECRYPTION OPTIONS ===
4. XOR Decrypt
5. Swap Pixels Decrypt
6. Subtract Key Decrypt

=== EXIT ===
7. Exit

Provide a full path to your input image, then a key (where required), then an output path. Example session:

Enter your choice: 1
Enter image path: sample_input_professional.png
Enter key (0-255): 77
Enter output path: encrypted.png

Image Size: 400x300 pixels
Before: (15, 23, 42)
After: (86, 102, 81)
Saved to encrypted.png

To reverse it, choose option 4 with the same key and the encrypted file as input — you'll get the original image back exactly.

📁 Project Structure

.
├── task2_image_encryption.py     # Main program
├
└── README.md                     # This file


⚠️ Note

This tool is for educational purposes — to understand basic encryption concepts through pixel manipulation. It is not a substitute for cryptographically secure encryption standards like AES, which should be used for any real-world data protection needs.

This project was built as part of a Cybersecurity Internship learning exercise.
