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
    @param fname : the name of the ply file
    @paramtype fname : string
    :return : ply data
    :rtype : plydata
    """
    el = plyfile.PlyElement.describe(data, 'vertex')
    plyfile.PlyData([el], text=True).write(fname)
    return data

def convertCoordinatesPlyArray(plydata):
    """
    Convert a plydata to a numpy array. The user can choose how many colors to add to each point (R, V, B)
    @plydata : the .ply element
    @plydatatype : plydata
    :return : the coordinates of every points from the cloud
    :rtype : np.array    
    """
    data = np.array([plydata.elements[0].data['x'], 
             plydata.elements[0].data['y'], 
             plydata.elements[0].data['z']])
    #print(len(plydata.elements[0].data['x']))
    #print(len(plydata.elements[0].data['y']))
    #print(len(plydata.elements[0].data['z']))

    return np.transpose(data)

def addCanalFromPly(plydata, coord, canal):
    """
    Add the canal to the numpy data (converted by the function convertCoordinatePlyArray)
    @plydata : the .ply element
    @plydatatype : plydata
    @coord : the data which contains the coordinates of every points
    @coordtype :np.array
    @canal : the name of the canal to add
    @canaltype : string
    :return : data + the colors to the coord data
    :rtype : np.array
    """
    #print(len(np.transpose(plydata.elements[0].data[canal])))
    data = np.column_stack((coord, plydata.elements[0].data[canal]))
    return data

def addCanalGenrated(coord, canal_data, canal_name):
    """
    Add a canal (usually generated by a projection into other images) to the numpy data
    @coord : the data which contains the coordinates of every points
    @coordtype :np.array
    @canal_data : a list of every values of the canal
    @paramtype canal_data : np.array
    @canal_name : the name of the canal to add
    @canaltype : string
    :return : data + the colors to the coord data
    :rtype : np.array
    """
    if len(canal_data != len(plydata.elements[0].data['x'])):
        print("\nERROR : different size between the canal added and the matrix of coordinates points\n\n")
    else:
        coord = np.column_stack((coord, canal_data))
    return coord


if __name__ == "__main__" :
    fname = "nuageGREEN.ply"
    plydata = readply(fname)
    
    #1/ Converting the plydata to an array
    data = convertCoordinatesPlyArray(plydata)
    print("The data from ", plydata, " is :\n", data)
    
    #2/ Adding canal
    canal = "green"
    data = addCanalFromPly(plydata, data, canal)
    print("\nAdding the canal ", canal, " to the data :\n", data)
    
    
    
    
    
    