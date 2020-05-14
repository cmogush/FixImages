#!/usr/bin/env python3
from PIL import Image
import os
from pathlib import Path

src = r"C:\Users\Chris\Desktop\Python Scripts\FixImages\Images"
dest = r"C:\Users\Chris\Desktop\Python Scripts\FixImages\Icons"

def fixImage(file):
    # open image
    with Image.open(file) as img:
        # convert alpha channel
        if img.mode in ('RGBA', 'LA'):
            background = Image.new(img.mode[:-1], img.size, 'white')
            background.paste(img, img.split()[-1])
            img = background

        # rotate 90 deg
        out = img.rotate(90) # counter clockwise

        # resize to 128
        out = out.resize((128, 128))

        # save as jpg in new dest
        f, e = os.path.splitext(os.path.basename(file))
        outfile = dest + "\\" + f + ".jpg"
        out.save(outfile, "JPEG")

for file in os.listdir(src):
    f, e = os.path.splitext(file)
    if e == ".tiff":
        fixImage(src+"\\"+file)
