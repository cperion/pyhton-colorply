# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 10:17:54 2019

@author: Cédric Perion | Arthur Dujardin
"""


import numpy as np
import plyfile

def readply(fname):
    """ Reads data from the ply file"""
    plydata = plyfile.PlyData.read(fname)
    return plydata

def writeply(data, fname):
    """
    Writes data to the plyfile
    @param data : the data to convert in ply
    @paramtype data : np.array
    """
    el = plyfile.PlyElement.describe(data, 'vertex')
    plyfile.PlyData([el], text=True).write(fname)
    return data

def convertPlyArray(plydata):
    """
    """
    data = np.array([plydata.elements[0].data['x']])

    return data


if __name__ == "__main__" :
    fname = "el.ply"
    plydata = readply(fname)
    print("The data from ", plydata, " is :\n", convertPlyArray(plydata))
    
    
    
    
    
    