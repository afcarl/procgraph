'''
--- example_architecture
input odometry  Odometry signal
input FRONTAL
input OMNI 
input SVS_R
input SVS_T
input SVS_L

# Extract linear, angular velocity from odometry log 
odometry -> |estimate_commands_unicycle| -> commands -> |split| -> linear, angular 

# Do some camera preprocessing
FRONTAL -> |camera_preprocessing| -> y1
OMNI    -> |camera_preprocessing| -> y2 
SVS_R   -> |camera_preprocessing| -> y3
SVS_T   -> |camera_preprocessing| -> y4 
SVS_L   -> |camera_preprocessing| -> y5 
 
# Learn control tensors

y1, commands -> |bds1:BDS_analysis| 
    bds1.surprise ->  


----- BDS_analysis
input image
input commands
output image_surprise
output commands_surprise
output T

# remove the mean from the image
image -> |expectation min_samples=10| -> image_n

# compute the derivative
image -> |derivative| -> image_dot

# whiten the commands
commands -> |whitening| -> commands_w

# the tensor T is the expectation of the tensor product 
image, image_dot, commands_w -> |outer| -> |expectation min_samples=100| -> T  

# compute the error
T, image, image_dot, commands_w -> |surprise| ->  


----- camera_preprocessing
description      Standard pipeline for extracting contrast from images.  
input  y  type=image
output contrast type=image 

y -> |grayscale| -> gray -> |gradient| -> gx, gy

gx -> |op f=square| -> gx_square
gy -> |op f=square| -> gy_square

gx_square, gy_square -> |+| -> contrast

'''
