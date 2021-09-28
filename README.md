# Crack-size-measurement-in-thin-sections
Measuring crack length and width in binary images
The aim of this script is to measure lenght and width of cracks in binary images. 
Used libraries: skimage, numpy, tifffile, matplotlib
Used image: transmitted light microscopy image of a concrete thin section 
Used microscope: Olympus BX43, SC50 camera
Used Software:
- Stream Motion Software (Olympus-SIS) for capturing image, object measurements and classification
- Trainable Weka Segmentation included in fiji (ImageJ) with trained classifier for segmentation

The Gaussian filter was used to reduce heterogeneous morphology of the cracks and to avoid skeleton branches.
Each Pixel remaning after the iterativ skeletoniazation is interpreted the median line of a crack and thus as crack length.
The results of the distance function multiplied by the skeleton are doubled to compute the crack width. To get the real width the shapes of the cracks are subtracted (by 2 Px). There are still cracks with just 2 Px width which would be zero. Their values have not been changed.
The single steps in the script start at point (4) in the shown workflow (see image), which can be plotted with the 2nd extended script.
