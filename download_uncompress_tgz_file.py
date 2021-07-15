# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 21:10:21 2021

@author: goka
"""

import urllib # This is URL handling module required for downloading files from the Internet

import tarfile # This is used for decompressing .tgz file

def fetch_housing_data(url, filename, extract_to):
    
    urllib.request.urlretrieve(url+filename, filename)
    housing_tgz = tarfile.open(filename)
    housing_tgz.extractall(extract_to)
    housing_tgz.close()