from os import getcwd, listdir
from os.path import isfile, join, exists
import matplotlib.pyplot as plt
from inputoutput.read_xml import readOri
from image.image import Image


def loadImages(calibDir = ".", imDir = ".", exts = (".jpg", ".tif", ".JPG", ".TIF", ".JPEG", ".TIFF") , channel = "unknown") :
    """ 
    Reads all images and returns a list of images
    """
    ls=listdir(imDir)
    image_list = []
    for f in listdir :
        if isfile(join(imDir, f)) and f.endswith(exts) and exists(join(calibDir, f) + ".xml"):
            imgfile=join(imDir, f)
            xmlfile=join(calibDir, f)
            data=plt.imread(imgfile)
            R, S = readOri(xmlfile)
            img = Image(f, channel,data, R, S)
            image_list.append(img)
    return image_list
    

if __name__=="__main__" :
    print(loadImages("/home/cedric/Images"))