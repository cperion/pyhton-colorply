# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 10:17:54 2019

@author: Cédric Perion | Arthur Dujardin
"""


import  numpy as np

def fimage(F, M, R, S) :
    k = np.ndarray([0,0,1])
    R_inv = np.linalg.inv(R)
    top = k.dot(F).dot(R).dot(M - S)
    bottom = k.transpose.dot(R).dot(M -S)
    return F - top/bottom


















