# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 09:04:23 2023

@author: Patzelt

"""
from skimage.morphology import medial_axis
from skimage.filters import threshold_otsu, gaussian
import numpy as np
import tifffile as tiff

def crack_quantification(img_name, img_type):
    # Import
    img = tiff.imread(img_name+img_type)
    img = np.array(img.astype(np.int32))
    
    # Gaussian
    gaussian_img = gaussian(img, sigma=7)
    
    # Segmentation
    thresh = threshold_otsu(gaussian_img)
    binary = np.array(gaussian_img > thresh, dtype=int)
    
    # Invert image, if needed
    # image0 = 1-binary ###Schleife ergänzen
    image0 = binary
    
    # Sekeletonization
    img_skeletonized, distance = medial_axis(image0, return_distance=True)
    img_skeletonized = np.array(img_skeletonized.astype(np.int32))
    dist_on_skel = distance * img_skeletonized
    
    # Quantification of cracks
    width = dist_on_skel[dist_on_skel !=0]*2
    for i in range(len(width)):
        if width[i] <= 2.0:
            width[i] = width[i]
        else:
            width[i] = width[i]-2
    length = np.count_nonzero(img_skeletonized)
    mean_width = np.mean(width)
    max_width = np.max(width)
    min_width = np.min(width)
    
    # Save skeletonized image and return output
    tiff.imsave(img_name+"_blurred-skeletonized"+img_type, img_skeletonized, shape=None, dtype=int)  
    return length, mean_width, max_width, min_width, width