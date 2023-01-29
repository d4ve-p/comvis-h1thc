import cv2 as cv
import time
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from modules import file
from . import grayscale

reader_function = {
    "manual" : grayscale.generate_manual_grayscale,
    "cv" : grayscale.generate_cv_grayscale,
    "cv_equal" : grayscale.generate_cv_equalizer
}

def to_file(path:str, directory_path: str, option: str="manual"):
    fun = reader_function[option]
    image_array = fun(path)
    now = time.time()

    fname = f"{now}.png"
    user_storage = file.create_storage(directory_path)

    plt.hist(x=image_array.flatten(), bins=255)

    img_name = f"image-{option}-{fname}"
    plt_name = f"graph-{option}-{fname}"
    cv.imwrite(f"{user_storage}{img_name}", img=image_array)
    plt.savefig(fname=f"{user_storage}{plt_name}")
    plt.clf()

    return {
        "image": img_name,
        "plot": plt_name
    }