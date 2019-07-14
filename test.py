# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 10:17:54 2019

@author: Cédric Perion | Arthur Dujardin
"""

import numpy
import plyfile


vertex = numpy.array([(0,0,0,1,0,0),(0,1,1,0,1,0),(1,0,1,0,0,1),(1,1,0,0,1,1)], dtype=[('x', 'f4'), ('y', 'f4'), ('z', 'f4'), ('red', 'f8'), ('green', 'f8'), ('blue', 'f8')])

el = plyfile.PlyElement.describe(vertex, 'vertex')

plyfile.PlyData([el], text=True).write('el.ply')