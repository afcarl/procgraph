from procgraph.core.registrar_other import simple_block
# import numpy as np
# from . import cv as cv2
# from procgraph_cv.conversions import numpy_to_cv
# from reprep.graphics.zoom import rgb_zoom
from contracts import contract
from procgraph_images.filters import torgb

@simple_block
@contract(gray='array[HxW]')
def simple_detector_demo(gray):
    import cv2

#     print gray[10, :]


    gray = torgb(gray)

#     print gray[10, :, 0]
#     img = numpy_to_cv(rgb)

    # Initiate STAR detector
#     star = cv2.FeatureDetector_create("STAR")  # @UndefinedVariable

    # Initiate BRIEF extractor

#     brief = cv2.DescriptorExtractor_create("BRIEF")  # @UndefinedVariable

    surf = cv2.SIFT()

    # find the keypoints with STAR
#     gray = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)

    kps = surf.detect(gray)  # , None, useProvidedKeypoints=False)

#     print kps
    res = cv2.drawKeypoints(gray, kps)
#     print res[10, :, 0]
#
#     for kp in kps:
#         x = kp.x
#         y = kp.y
#         img[y, x, 0] = 255

#     kp = star.detect(imgg, None)

    # compute the descriptors with BRIEF
#     kp, des = brief.compute(rgb, kp)

#     print kp
#     print brief.getInt('bytes')
#     print des


    return res
