""" This module contains functions that add primitives to a point cloud """

import plyfile
import numpy as np



def addNDVI(inPly, outPly):
    ply = open(inPly, mode='rb')
    plydata = plyfile.PlyData.read(ply)
    red = plydata.elements[0].data['RED']
    nir = plydata.elements[0].data['NIR']
    ndvi = np.divide((nir-red), (nir+red))
    data = plydata.elements[0].data
    dtype = plydata.elements[0].data.dtype.descr
    newdtype = dtype + [('NDVI', 'f4')]
    out= []
    for i in range(len(data)):
        val = ndvi[i]
        if np.isfinite(val):
            l = (*data[i], val)
            out.append(l)
    out=np.array(out, dtype=newdtype)
    el = plyfile.PlyElement.describe(out, 'vertex')
    plyfile.PlyData([el], text=True).write(outPly)

addNDVI("testcolorply/RVB_GRE_RED_REG_NIR.ply", "testcolorply/RVB_GRE_RED_REG_NIR_NDVI.ply")
print('ok')




