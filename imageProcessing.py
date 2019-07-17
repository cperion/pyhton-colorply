# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 10:17:54 2019

@author: Cédric Perion | Arthur Dujardin
"""

import random
import numpy as np
import matplotlib.pyplot as plt
import math

from fimage import cimage
from inputoutput.read_xml import readOri, readCalib
from image import Image


#Import path to read files in a directory
from os import listdir
from os import getcwd
from os.path import isfile, join

def loadImages(outOri, dirName = "", ext = ".jpg", channel = "unknown") :
    """ 
    Reads all images and returns a list of images
    """
    dirPath = getcwd() + "\\" + dirName
    files = [f for f in listdir(dirPath) if (isfile(join(dirPath, f)) and f[len(f)-4:len(f)] == ext)]
    
    images_loaded = []
    for k in range(len(files)):
        xmlfile = dirPath + "\\" + "Ori-" + outOri + "\\Orientation-" + files[k] + ".xml"
        R, S = readOri(xmlfile)      
        images_loaded.append(Image((files[k]), channel, plt.imread(dirName + "\\" + files[k]), R, S))
    return images_loaded

def computeRadiometryProjection(M, images_loaded, calibration):
        image = images_loaded
        data = image.data
        R = image.R
        S = image.S
        size = calibration[3]
        F = calibration[0]
        pps = calibration[1]
        a = calibration[2][0]
        b = calibration[2][1]
        c = calibration[2][2]
        m = cimage(F, M, R, S, pps, a, b, c,)
        mx = int(np.round(m[0]))
        my = int(np.round(m[1]))
        return mx,my       
    
def mean(M,images_loaded,calibration):
    avg_radiometry=0
    compt=0
    size = calibration[3]
    n=len(images_loaded) 
    for i in range(n):
        m=computeRadiometryProjection(M,images_loaded[i],calibration)  
        if ((0 < m[0] < size[0]) and (0 < m[1] < size[1])):
            data = images_loaded[i].data
            avg_radiometry+=data[m[1],m[0]]
            compt+=1
    return avg_radiometry/compt

def aleatoire(M,images_loaded,calibration):
    radio=[]        
    size = calibration[3]
    n=len(images_loaded)
    for i in range(n):
        m=computeRadiometryProjection(M,images_loaded[i],calibration)  
        if ((0 < m[0] < size[0]) and (0 < m[1] < size[1])):
            data = images_loaded[i].data
            radio.append(data[m[1],m[0]])
    return random.choice(radio)

def distance(M,S,images_loaded,calibration):
    radio=[]
    dist=[]
    size = calibration[3]
    n=len(images_loaded)
    for i in range(n):
        m=computeRadiometryProjection(M,images_loaded[i],calibration)  
        if ((0 < m[0] < size[0]) and (0 < m[1] < size[1])):
                dist.append(np.linalg.norm(S-M))
                data = images_loaded[i].data
                radio.append(data[m[1],m[0]])
                index=dist.index(min(dist))
    return radio[index]
            
def distanceCentre(M,images_loaded,calibration):
    distcentre=[]
    radio=[]
    size = calibration[3]
    n=len(images_loaded)
    for i in range(n):
        m=computeRadiometryProjection(M,images_loaded[i],calibration)  
        if ((0 < m[0] < size[0]) and (0 < m[1] < size[1])):
            data = images_loaded[i].data
            radio.append(data[m[1],m[0]])
            dist=(m[0]-size[0]/2)**2+(m[1]-size[1]/2)**2
            distcentre.append(dist)        
    index=distcentre.index(min(distcentre))        
    return radio[index]

def scalaire(M,images_loaded,calibration):
    scal=[]
    radio=[]
    size = calibration[3]
    F=calibration[0]
    n=len(images_loaded)
    for i in range(n):
        m=computeRadiometryProjection(M,images_loaded[i],calibration)  
        if ((0<m[0]<size[0]) and (0<m[1]<size[1])):
            data = images_loaded[i].data
            radio.append(data[m[1],m[0]])
            angle=math.acos(1/(math.sqrt((F[0]-m[0])**2+(F[1]-m[1])**2+F[2]**2)))
            scal.append(angle)
    index=scal.index(min(scal))
    return radio[index]

def meanPonderation(M,images_loaded,calibration):
    moy=mean(M,images_loaded,calibration)
    avg_radiometry=0
    compt=0
    size = calibration[3]
    n=len(images_loaded) 
    for i in range(n):
        m=computeRadiometryProjection(M,images_loaded[i],calibration)  
        if ((0<m[0]<size[0]) and (0<m[1]<size[1])):
            data = images_loaded[i].data
            if moy-data[m[1],m[0]]==np.array([0,0,0]):
                continue
            avg_radiometry+=(1/abs(moy-data[m[1],m[0]]))*data[m[1],m[0]]
            compt+=1/abs(moy-data[m[1]-m[0]])
    return avg_radiometry/compt

if __name__ == "__main__" :        
    calibxml = "example\\Ori-Calib\\AutoCal_Foc-24000_Cam-DSLRA850.xml"
    calibration = readCalib(calibxml)   # F , PPS, coeffDistorsion
    #print(calibration)
    M = np.array([984.647, 996.995, 491.721])

    images_loaded = loadImages("Calib", "example", ".jpg", "red")
    #print(images_loaded)
    
    image = images_loaded[0]
    print(image.name)
    #print(image.R)

    #print(computeRadiometryProjection(M, images_loaded, calibration))
    print(mean(M, images_loaded, calibration))
    #print(aleatoire(M, images_loaded, calibration))
    #print(distance(M,image.S, images_loaded, calibration))
    #print(distanceCentre(M, images_loaded, calibration))
    #print(scalaire(M,images_loaded,calibration))
    print(meanPonderation(M,images_loaded,calibration))
   