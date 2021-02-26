# Import packages
import numpy as np
import matplotlib.pyplot as plt
import SimpleITK as itk
import mahotas as mh
import os
from glob import glob


# Explore files
path = "/home/atoriz98/Datasets/BrainGliomas/GliomasImages"

files = glob(path + "/**/*.mha", recursive = True)

# Dictionaries and list to organize files
Dataset = {'HG': {}, 'LG': {}}
id_HG = np.asarray([])
id_LG = np.asarray([])

# Image types
types = ['Flair', 'T1', 'T1c', 'T2', 'OT']

for file in files:
    if 'HG' in file:
        id_HG = np.append(id_HG, file.split('/')[7])
    else:
        id_LG = np.append(id_LG, file.split('/')[7])

for unique in np.unique(id_HG):
    Dataset['HG'][unique] = {}
    for img in types:
        Dataset['HG'][unique][img] = {}
for unique in np.unique(id_LG):
    Dataset['LG'][unique] = {}
    for img in types:
        Dataset['LG'][unique][img] = {}
    
for grade in Dataset.keys(): # HG LG
    for case in Dataset[grade].keys(): # Num
        for img in types: # Flair, Tc1, Tc2 ...
            for file in files:
                route = file.split('/')
                if route[6] == grade and route[7] == case and route[8].endswith(img):
                    Dataset[grade][case][img] = file
        
        