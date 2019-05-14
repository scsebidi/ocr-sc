import socket
import requests
from env import  DROPFOLDER, SENTIMENTPATH, LOG_FILE, IMAGEPATH
import json 
import sys
import os
import logging
import datetime
from time import gmtime, strftime 

from PIL import Image
import pytesseract
from io import BytesIO

offset = -1

logging.basicConfig(filename=LOG_FILE + f"{strftime('%d-%m-%Y', gmtime())}.log", level=logging.DEBUG)

def run():
    logging.info(f"Starting ocr.....")
    text = ocr(IMAGEPATH)
    createTextFile(text,IMAGEPATH)

def createTextFile(text,IMAGEPATH):
    path = f'{DROPFOLDER}/test.txt'
    f = open(path, "w")
    f.write(text)
    f.close()

def ocr(path):
    try:
        response = requests.get(path)
        img = Image.open(BytesIO(response.content))
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        logging.error(f"******************************Something went wrong {e} - {path}*********************")
        return None


if __name__ == '__main__':
    run()
