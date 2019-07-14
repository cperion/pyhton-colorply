# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 13:10:22 2019

@author: Utilisateur
"""




from xml.etree import ElementTree
from xml import *


#1/ Matrix Rotation
nameIMGxml = "Orientation-Im3.JPG.xml"
print("The rotation matrix of the image " + nameIMGxml + " is : \n", readOrientation(nameIMGxml)) 

#2/ Center S of the IMG
print("\nThe image's center is : \n", readS(nameIMGxml))

#2.5/ Opti read Orientation
print("\nThe orientation and center of the image are :\n", readOri(nameIMGxml),"\n")

#3/ F focale
calibxml = "AutoCal_Foc-24000_Cam-DSLRA850.xml"
print("\nThe F point from the camera " + calibxml + " is : \n", readCalibF(calibxml))

#4/ PPS 
print("\nThe PPS from the camera " + calibxml + " is : \n", readCalibPPS(calibxml))

#5/ PPS 
print("\nThe coefficients a, b, c from the camera " + calibxml + " is : \n", readCalibDist(calibxml))

#6/ Opti param
print("\nThe calibration parameters of this image are : \n", readCalib(calibxml))