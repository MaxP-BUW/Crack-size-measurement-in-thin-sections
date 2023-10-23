# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 09:12:30 2023

@author: Patzelt

Scaling factor 883,642 nm/Px
"""
import pandas as pd
import os
import tifffile as tiff
import numpy as np
from crack_quantification import crack_quantification

# Folder path with the images to be analysed
folder_path = r"C:\Users\Patzelt\Documents\Python_scripts"

# Image type to be analysed
img_type = ".tif"

# List of all image files in the folder
file_list = os.listdir(folder_path)

# Empty list for saving the results for average crack sizes and crack widths
results = []
results_width = []

# Loop for images to be analysed
for file_name in file_list:
    if file_name.endswith(img_type):  # only tif-images!
    
        # Import image
        img = tiff.imread(folder_path +"\\"+ file_name)
        img = np.array(img.astype(np.int32))
        img_name = file_name.replace(img_type,"")
        
        # Call up the function for calculating crack sizes
        length, mean_width, max_width, min_width, width = crack_quantification(img_name, img_type)
        
        # Save results in lists
        results.append([file_name, length, mean_width, max_width, min_width])
        results_width.append([file_name, width])
        
# Save results in tables
df = pd.DataFrame(results, columns=["File Name", "Summarized Cracklength (px)", "Mean crack width (px)", "Max crack width (px)", "Min crack width (px)"])
df_width = pd.DataFrame(results_width, columns=["File Name", "Crack widths (px)"])
df.to_csv("results.csv", index=False)
df_width.to_csv("results_width.csv", index=False)

#df_exc = pd.DataFrame.to_excel(results, )

#Plot crack density deviation
#Plot crack width deviation
#Plot average crack sizes per specimen