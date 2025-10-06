#!/usr/bin/env python3
import sys
import pandas as pd
import numpy as np
from glob import glob
import matplotlib.pylab as plt
import os
import soundfile as sf
def main(argv):
    files = glob('input/*.jpg')
    audiofiles = glob('input/*.wav')
    if not files and not audiofiles:
        print("Input folder is empty, please try again")
        sys.exit()
    for i in files:
        imgmpl = plt.imread(i)
        data = imgmpl/255
        R = data[:,:,0].flatten()
        G = data[:,:,1].flatten()
        B = data[:,:,2].flatten()
        left = G + 0.5*B
        right = R + 0.5*B
        max_val = max(left.max(), right.max())
        left = (left / max_val) * 2 - 1
        right = (right / max_val) * 2 - 1
        stereo = np.column_stack((left, right))
        basename = os.path.splitext(os.path.basename(i))[0]
        outputfile = f"output/{basename}.wav"
        sf.write(outputfile, stereo, 44100)

    for i in audiofiles:
        data, samplerate = sf.read(i)
        outputdata = data.flatten()
        length = len(outputdata)
        width = int(np.sqrt(length))
        height = length // width
        outputdata = outputdata[:width*height]
        img_array = outputdata.reshape((height, width))
        img_array_uint8 = (img_array * 255).astype(np.uint8)
        basename = os.path.splitext(os.path.basename(i))[0]
        output = f"output/{basename}.jpg"
        plt.imsave(output, img_array_uint8, cmap='gray')
    print("Files converted. Have a nice day!")
if __name__ == '__main__':
    main(sys.argv[0:])