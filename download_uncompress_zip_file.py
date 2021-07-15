# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 21:11:31 2021

@author: goka
"""


###############################################################
### Download and unzip .zip files
###################################################################
from urllib.request import urlopen
from io import BytesIO
from zipfile import ZipFile


def download_and_unzip(url, extract_to='.'):
    http_response = urlopen(url)
    zipfile = ZipFile(BytesIO(http_response.read()))
    zipfile.extractall(path=extract_to)
    
