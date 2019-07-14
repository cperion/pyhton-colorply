# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 10:17:54 2019

@author: Cédric Perion | Arthur Dujardin
"""

import numpy as np
import matplotlib.pyplot as plt
import inputoutput.read_xml as read_xml

class Image :
    channel = ""
    name = ""
    data = np.array([])
    R = np.eye(3)
    S = np.array((0, 0, 0))
    def readfromfile(self, fname, channel) :
        """ Constructor : reads an image file and its associated xml file in order to populate an image object"""
        self.channel=channel
        xmlfile = fname + ".xml"
        self.R, this.S = read_xml.readOrientation(xmlfile)
        self.data = plt.imread(fname)
        self.name=fname

    





def loadImages(dirName) :
    """ Reads all images a,d returns a list of images"""
    pass