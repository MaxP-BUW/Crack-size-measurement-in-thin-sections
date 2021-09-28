# Crack-size-measurement-in-thin-sections
_Measuring crack length and width in binary images_
## Estimate_crack_width_and_length_of_binary_images.py



The aim of this script is to measure lenght and width of cracks in binary images using median axis skeletonization and gaussian blur.

Used libraries: skimage, numpy, tifffile, matplotlib

Used image: transmitted light microscopy image of a concrete thin section 

Used microscope: Olympus BX43, SC50 camera

Used Software:
- Stream Motion Software (Olympus-SIS) for capturing image, object measurements and classification
- Trainable Weka Segmentation included in fiji (ImageJ) with trained classifier for segmentation

To get started change the variable img_name in line 20 regarding to the name of your image analysed. Then adjust your image format in line 21. The input image must be binary, 
e.g. through segmentation. You can use either tif or btf images. After that run the script. You will get the output in the console for the summarized crack length, mean crack 
width, max. crack width and min. crack width. Additionally the skeletonized image will be saved. 

The Gaussian filter was used to reduce heterogeneous morphology of the cracks and to avoid skeleton branches.
Each Pixel remaning after the iterativ skeletoniazation is interpreted the median line of a crack and thus as crack length.
The results of the distance function multiplied by the skeleton are doubled to compute the crack width. To get the real width the shapes of the cracks are subtracted (by 2 Px). 
There are still cracks with just 2 Px width which would be zero. Their values have not been changed.

## Estimate_crack_width_and_length_of_binary_images-workflowplot.py
The single steps in the script start at point (4) in the shown workflow (see image), which can be plotted with the 2nd extended script.

## Corresponding Paper
- in review

## Requirements
This script was tested in Python 3.7.

## Written by 
Max Patzelt

Bauhaus University Weimar, Faculty of Civil Engineering;
F. A. Finger Institute for Bulding Material Science;
Professorship Building Materials;
Coudraystraße 11C, Room 109, 99423 Weimar;
max.patzelt@uni-weimar.de
