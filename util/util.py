import plyfile

def toascii(inputFile, outPutfile) :
    el = plyfile.PlyData.read(inputFile)
    el2 = plyfile.PlyElement.describe(el.elements[0].data, 'vertex')
    plyfile.PlyData([el2], text=True).write(outPutfile)