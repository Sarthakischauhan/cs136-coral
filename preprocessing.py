#! base/bin/python3
"""This will be used for implementing gaussian blur or smoothing functions"""

import cv2 as cv
import numpy as np

class PreProcessor:
    def __init__(self):
        print("Filtering block initialized")

    def apply_gaussian_filter(self, image, kernel_size=(5, 5), sigma=0):
        """
        Applies a Gaussian blur to the input image.
        """
        return cv.GaussianBlur(image, kernel_size, sigma)
    
    def apply_bilateral_filter(self, image, d, sigmaColor, sigmaSpace):
        """
        Applies a Bilateral blur to the input image.
        """
        return cv.bilateralFilter(image,d,sigmaColor,sigmaSpace)

    def apply_sobel_filter(self, image, direction='both', ksize=3):
        """
        Applies a Sobel filter in the x, y, or both directions.
        """
        sobel_x = cv.Sobel(image, cv.CV_64F, 1, 0, ksize=ksize)
        sobel_y = cv.Sobel(image, cv.CV_64F, 0, 1, ksize=ksize)

        if direction == 'x':
            return sobel_x
        elif direction == 'y':
            return sobel_y
        elif direction == 'both':
            sobel_combined = cv.magnitude(sobel_x, sobel_y)
            return sobel_combined

    def apply_canny_edge(self, image, threshold1=50, threshold2=150):
        """
        Applies the Canny edge detection algorithm.
        """
        return cv.Canny(image, threshold1, threshold2)

    def apply_laplacian_edge(self,image, depth=cv.CV_64f):
        """
        Applies the Laplacian edge detection algorithm.
        """ 
        return cv.Laplacian(image,depth)
