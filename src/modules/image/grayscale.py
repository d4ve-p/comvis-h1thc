import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

def generate_manual_grayscale(image_path: str):
    image_array = plt.imread(image_path)
    copy = image_array.copy()
    for col in range(0, len(image_array)):
        for row in range(0, len(image_array[col])):
            copy[col,row] = np.clip(0.21 * copy[col,row, 0] + 0.72 * copy[col,row,1] + 0.07 * copy[col,row,2], 0, 255)

    return copy

def generate_cv_grayscale(image_path: str):
    return cv.imread(image_path, cv.IMREAD_GRAYSCALE)

def generate_cv_equalizer(image_path):
    temp = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    return cv.equalizeHist(temp)
