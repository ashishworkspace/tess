import os
import sys
import pytesseract
# import cv2
import requests
from urllib.parse import unquote
from flask import request
from PIL import Image
import io


IMAGEPATH = "data"


def read_ocr():
    """
    """
    content = request.json
    image = content['image']
    lang = content['lang']
    config = content['config']
    response = requests.get(image)
    img = Image.open(io.BytesIO(response.content))
    text = pytesseract.image_to_string(img, lang=lang, config=config)
    return {"text": text}


def root():
    about = "https://github.com/ashishworkspace/tess#readme"
    return {"API Documentation": f"{about}"}
