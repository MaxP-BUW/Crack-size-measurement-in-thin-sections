# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 14:34:08 2021
Last update: Tue Sep 28 2021

@author: Patzelt
    Bauhaus University Weimar, Faculty of Civil Engineering
    F.A. Finger Institute for Bulding Material Science
    Professorship Building Material
    Coudraystraße 11C, Room 109, 99423 Weimar

Estimation of crack length and width via medial axis skeletonization.
Scaling factor in test image used is 883,642 nm/Px.
"""
from skimage.morphology import medial_axis
from skimage.filters import threshold_otsu, gaussian
import numpy as np
import tifffile as tiff
#-----------------------------------------------------------------------------
img_name = "detail_01_segmented_binary_measured_classified"
img_type = ".tif" #you can also import btf through the use of tifffile
###READ
img = tiff.imread(img_name+img_type)
img = np.array(img.astype(np.int))
###GAUSSIAN
gaussian_img = gaussian(img, sigma=7)
###SEGMENTATION
thresh = threshold_otsu(gaussian_img)
binary = np.array(gaussian_img > thresh, dtype=int)
###INVERT if needed
#image0 = 1-binary
image0 = binary
###SKELETONIZATION
img_skeletonized, distance = medial_axis(image0, return_distance=True)
img_skeletonized = np.array(img_skeletonized.astype(np.int))
dist_on_skel = distance * img_skeletonized
width = dist_on_skel[dist_on_skel !=0]*2
for i in range(len(width)):
    if width[i] <= 2.0:
        width[i] = width[i]
    else:
        width[i] = width[i]-2   
###SAVE SKELETON
tiff.imsave(img_name+"_blurred-skeletonized"+img_type, img_skeletonized, shape=None, dtype=int)
###OUTPUT
length = np.count_nonzero(img_skeletonized)
mean_width = np.mean(width)
max_width = np.max(width)
min_width = np.min(width)
print("Summarized Cracklength = "+str(length)+" Px")
print("Mean crack width = "+str(mean_width)+" Px")
print("Max crack width = "+str(max_width)+" Px")
print("Min crack width = "+str(min_width)+" Px")