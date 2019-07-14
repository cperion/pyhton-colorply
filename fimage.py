# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 10:17:54 2019

@author: Cédric Perion | Arthur Dujardin
"""

import  numpy as np

def fimage(F, M, R, S) :
    """ Compute the image formula for the point M
        WITHOUT distorsion
    """
    k = np.array([0,0,1])
    R_inv = np.linalg.inv(R)
    topdot = np.dot(k, F)
    topdot = np.dot(topdot, R_inv)
    topdot = np.dot(topdot, M - S)
    bottomdot = np.dot(k, R_inv)
    bottomdot = np.dot(bottomdot, M - S)
    
    return F - topdot/bottomdot

def radialStd(m_image, pps, a, b, c) :
    """ Corrects the postion of the point according to the standard radial distorsion model"""
    r = np.dot(m_image[0:2] - pps, m_image[0:2] - pps)**0.5     #norm between m and pps

    
    rsquared= r*r
    """ We use HORNER to evaluate ar2+br4+cr6"""
    poly = c
    poly = poly*rsquared + b
    poly = poly*rsquared + a
    poly = poly*rsquared
    """ HORNER DONE """
    dr = poly*(m_image[0:2] - pps) # correction vector
    return m_image[0:2] + dr

def cimage(F, M, R, S, pps, a, b, c,) :
    """ Compute the image formula for the point M
        WITH distorsion
    """
    return radialStd(fimage(F, M, R, S), pps, a, b ,c)








if __name__ == "__main__" :
    
    
    calibxml = "example\\Ori-Calib\\AutoCal_Foc-24000_Cam-DSLRA850.xml"
    F, pps, dist, size = readCalib(calibxml)   # F , PPS, coeffDistorsion
    print(F, pps, dist)
    
    nameIMGxml = "example\\Ori-Calib\\Orientation-Im3.JPG.xml"
    R, S = readOri(nameIMGxml)   # F , PPS, coeffDistorsion
    print(R, S)
    
    M = np.transpose(np.array([984.647, 996.995, 491.721]))
    
    m  = fimage(F, M, R, S)
    print("Projection of M in the image : ", m)
    
    a, b, c = dist[0], dist[1], dist[2]
    print("radialStd : ", radialStd(m, pps, a, b, c))
    
    print("Formula image with distorsion : ", cimage(F, M, R, S, pps, a, b, c))
    
    
    
    
    