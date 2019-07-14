
"""
@author Cedric Perion | Arthur Dujardin
"""

import plyfile

def readply(fname):
    """ Reads data from the ply file"""
    plydata=plyfile.PlyData.read(fname)

def writeply(data, fname):
    """ Writes data to the plyfile"""
    el = plyfile.PlyElement.describe(data, 'vertex')
    plyfile.PlyData([el], text=True).write(fname)
