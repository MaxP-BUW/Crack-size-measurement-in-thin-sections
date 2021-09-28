# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 14:34:08 2021
Last update: Tue Sep 28 2021

@author: Patzelt
    Bauhaus University Weimar, Faculty of Civil Engineering
    F.A. Finger Institute for Bulding Material Science
    Professorship Building Material
    Coudraystraße 11C, Room 109, 99423 Weimar

Estimation of crack length and width via medial axis skeletonization
including pyplot for detailed workflow.
Scaling factor in test image used is 883,642 nm/Px.
"""
from skimage.morphology import medial_axis
from skimage.filters import threshold_otsu, gaussian
import numpy as np
import tifffile as tiff
import matplotlib.pyplot as plt
#-----------------------------------------------------------------------------
img_name = "detail_01_segmented_binary_measured_classified"
img_type = ".tif" #you can also import btf through the use of tifffile
###READ
img = tiff.imread(img_name+img_type)
img = np.array(img.astype(np.int))
##Previous steps to get the binary image. See readme for further details.
RGBimg = tiff.imread("detail_01_calibrated"+img_type)
Segimg = tiff.imread("detail_01_segmented_binary"+img_type)
Classimg = tiff.imread("detail_01_segmented_binary_measured"+img_type)
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
###COMPUTING WIDTH
dist_on_skel = distance * img_skeletonized
#Distance is doubled to compute crack width. To get the real width without the 
#shape, the shapes of the cracks are subtracted (-2 Px). But there are still
#cracks with just 2 Px width which would be zero. Their values have not been 
#changed.
width = dist_on_skel[dist_on_skel !=0]*2
for i in range(len(width)):
    if width[i] <= 2.0:
        width[i] = width[i]
    else:
        width[i] = width[i]-2   
###OUTPUT
length = np.count_nonzero(img_skeletonized) #Each pixel remaining after 
#skeletonization is interpreted as belonging to the crack and as crack length.
mean_width = np.mean(width)
max_width = np.max(width)
min_width = np.min(width)
print("Summarized Cracklength = "+str(length)+" Px")
print("Mean crack width = "+str(mean_width)+" Px")
print("Max crack width = "+str(max_width)+" Px")
print("Min crack width = "+str(min_width)+" Px")
###PLOT
fs_plot = 100
fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(60, 20), sharex=True, 
                         sharey=True)
ax = axes.ravel()
ax[0].imshow(RGBimg, cmap="CMRmap")
ax[0].axis('off')
ax[0].set_title("(1) Input", fontsize=fs_plot)
ax[1].imshow(Segimg, cmap="gray_r")
ax[1].axis('off')
ax[1].set_title("(2) Segmented", fontsize=fs_plot)
ax[2].imshow(Classimg, cmap="gray")
ax[2].axis('off')
ax[2].set_title("(3) Classified", fontsize=fs_plot)
ax[3].imshow(img, cmap="gray_r")
ax[3].axis('off')
ax[3].set_title("(4) Separated Crack", fontsize=fs_plot)
ax[4].imshow(gaussian_img, cmap="gray_r")
ax[4].axis('off')
ax[4].set_title("(5) Blurred", fontsize=fs_plot)
ax[5].imshow(binary, cmap="gray_r")
ax[5].axis('off')
ax[5].set_title("(6) Threshold Otsu", fontsize=fs_plot)
ax[6].imshow(img_skeletonized, cmap="gist_heat_r")
ax[6].contour(img, [0.1], colors="gray")
ax[6].axis('off')
ax[6].set_title("(7) Skeleton", fontsize=fs_plot)
ax[7].imshow(distance, cmap="hot_r")
ax[7].axis('off')
ax[7].set_title("(8) Distance Map", fontsize=fs_plot)
fig.tight_layout()
plt.show()
fig.savefig("workflow.tiff")