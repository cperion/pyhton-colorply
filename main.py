from os import getcwd
import numpy as np
from image.image import *
from image.imageProcessing import *
from image.fimage import *
from inputoutput.read_xml import *
from util.util import *
from inputoutput.ply import *





calibxml = "example/Ori-Calib/AutoCal_Foc-24000_Cam-DSLRA850.xml"
calibration = readCalib(calibxml)   # F , PPS, coeffDistorsion
#print(calibration)
M = np.array([984.647, 996.995, 491.721])

images_loaded = loadImages("Calib", "example", ".jpg", "red")
#print(images_loaded)

image = images_loaded[0]
print(image.name)
#print(image.R)

#print(computeRadiometryProjection(M, images_loaded, calibration))





cloudPath = "C3DC_QuickMac_1bandeAllCampariGCP_5images.ply"
channelCloud = "red"

calibration = "example/Ori-1bande_All_CampariGCP/AutoCal_Foc-4000_Cam-SequoiaSequoia-GRE.xml"
calibration = readCalib(calibxml)

### BUG TAILLE CAPTEUR TROP GRAND QUE REALITE
print(calibration[3])
calibration = (calibration[0], calibration[1], calibration[2], np.array([1280, 960]))
print(calibration[3])


outOri = "1bande_All_CampariGCP"
dirName = "example"
ext = ".TIF"
channelImages = "NIR"
mode = "avg"


addChannelToCloud(cloudPath, channelCloud, calibration, outOri, dirName, ext, channelImages, mode)








## DO NOT WORK BELOW

#print(mean(M, images_loaded, calibration))
#print(aleatoire(M, images_loaded, calibration))
#print(distance(M,image.S, images_loaded, calibration))
#print(distanceCentre(M, images_loaded, calibration))
#print(scalaire(M,images_loaded,calibration))
#print(meanPonderation(M,images_loaded,calibration))