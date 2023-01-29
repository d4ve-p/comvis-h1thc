import modules
from modules import app
from modules import image

import os
import sys

MODULES_PATH = f"{os.getcwd()}\\src\\modules"
if(MODULES_PATH not in sys.path):
    sys.path.append(MODULES_PATH)

if(__name__ == '__main__'):
    # Test generate image
    # Hasil di simpan ke storage/test
    # image.to_file("bocchi.jpg", "test", "manual")
    # image.to_file("bocchi.jpg", "test", "cv")
    # image.to_file("bocchi.jpg", "test", "cv_equal")
    app.run(debug=False) # object asli untuk app.run ada di app/__init__.py