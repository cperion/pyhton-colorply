# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 10:17:54 2019

@author: Cédric Perion | Arthur Dujardin
"""

from fimage import *
from inputoutput.read_xml import readCalib
from inputoutput.ply import *
from image.py import *





def computeRadiometryProjection(M, images_loaded, calibration, mode = "avg"):
    n = len(images_loaded)
    for i in range(n):
        image = images_loaded[i].data
        R = image.R
        S = image.S
        
        size = calibration[3]
        
        F = calibration[0]
        pps = calibration[1]
        a = calibration[2][0]
        b = calibration[2][1]
        c = calibration[2][2]
        m = radialStd(fimage(F, M, R, S), pps, a, b ,c)
        
        if mode.lower() == "avg":
            avg_radiometry = 0
            compt = 0
            if (0 < m[0] < size[0]) and (0 < m[1] < size[1]):
                avg_radiometry += image[m[0], m[1]]
                compt += 1
            avg_radiometry = avg_radiometry/compt
        else:
            print("The mode is unknown. Please change it by : avg.")
            return -1
        return avg_radiometry




if __name__ == "__main__" :
    calibxml = "AutoCal_Foc-24000_Cam-DSLRA850.xml"
    calibration = readCalib(calibxml)   # F , PPS, coeffDistorsion
    
    
    