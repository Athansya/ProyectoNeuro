# Import packages
import numpy as np
import matplotlib.pyplot as plt
import SimpleITK as itk
import mahotas as mh
import os
from glob import glob


# Explore images
path = "/home/atoriz98/Datasets/BrainGliomas/GliomasImages/"
files = {}

for dir1 in glob(path+"*/"):
    files[dir1] = {}
    for dir2 in glob(dir1+"*/"):
        files[dir1][dir2] = {}
        for dir3 in glob(dir2+"*/"):
            files[dir1][dir2][dir3] = {}
            for dir4 in glob(dir3+"*/"):
                files[dir1][dir2][dir3][dir4] = {}
    #for key2 in files[key].keys():
    #    for dir3 in glob(key2+"*/"):
    #        print(dir3)
            #for key in files.keys():
            #    files[key][dir2][dir3] = {}
            #print(dir3)
        #for dir3 in glob(key2+"*/"):
        #    files[key][key2][dir3] = {}    
        
#print(files) 