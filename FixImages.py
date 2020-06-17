#!/usr/bin/env python3
from PIL import Image
import os
from pathlib import Path

src = r"/home/student-03-fac5da9edff2/images"
dest = r"/opt/icons"

def fixImage(file):
    # open image
    with Image.open(file) as img:

        # rotate 90 deg
        out = img.rotate(90) # counter clockwise
        # resize to 128
        out = out.resize((128, 128))

        # save as jpg in new dest
        f, e = os.path.splitext(os.path.basename(file))
    outfile = dest + "/" + f
    out.save(outfile, "JPEG")

for file in os.listdir(src):
     try:
         print("fixing {}".format(file))
         fixImage(src+"/"+file)
     except:
         print("{} not image".format(file))
