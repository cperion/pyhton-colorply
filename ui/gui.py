""" This is the python-colorply GUI """

import os
import sys

from PyQt5.QtWidgets import  (QWidget, QPushButton, QApplication, QMainWindow, QFileDialog,
QLineEdit, QHBoxLayout, QVBoxLayout, QComboBox, QProgressBar, QLabel)
from PyQt5.QtCore import pyqtSignal, QThread   # Threading
from inputoutput.ply import *
from image.imageProcessing import addChannelToCloud
from inputoutput.imagefile import loadImages
from image.imageProcessing import *
from ui.palette import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        #QThread.__init__(self)
        self.initUI()
        

    def initUI(self):
        self.setWindowTitle('Python-colorply')

        hbox1=QHBoxLayout() # image directory line
        hbox2=QHBoxLayout() # orientation image directory
        hbox3=QHBoxLayout() # calibration directory line
        hbox4=QHBoxLayout() # input ply line
        hbox5=QHBoxLayout() # output ply line
        hbox6=QHBoxLayout() # channel, compute method and run button line
        hbox7=QHBoxLayout()
        vbox=QVBoxLayout()
        """computeMethod."""
        self.computeMethod = QComboBox()
        self.modeDict = {                                   # dictionnary of all methods available
                "Average" : "avg",
                "Random" : "alea",
                "Weighted Average" : "wavg",
                "Distance" : "dist",
                }
        for k in self.modeDict:                             # adding the methods to a drop down menu
            self.computeMethod.addItem(k)
        
        self.imageExt = QComboBox()     
        self.extList = ["JPG", "TIF", "PNG", "CR2", "DNG"]  # list of all extension available     
        for k in range(len(self.extList)):                  # adding the possibilities
            self.imageExt.addItem(self.extList[k])
        self.imageExt.setFixedWidth(50)
    

        """ Text Lines !"""
        self.imageDirLine = QLineEdit()
        self.imageOri = QLineEdit()
        self.imageChannelLabel = QLabel("Channel name :")
        self.imageChannelLine = QLineEdit()
        self.calibDirLine = QLineEdit()
        self.inPlyLine = QLineEdit()
        self.outPlyLine = QLineEdit()
        
        self.warningLabel = QLabel("Error: please fill all the fields !")
        self.warningLabel.setVisible(False)


        """ Buttons ! """
        imageChooseButton = QPushButton("Choose your image folder")
        imageChooseButton.setFixedWidth(194)
        imageChooseButton.clicked.connect(self.select_image_dir)
        
        oriChooseButton = QPushButton("Choose your images orientation folder")
        oriChooseButton.setFixedWidth(250)
        oriChooseButton.clicked.connect(self.select_ori_dir)

        calibChooseButton = QPushButton("Choose your calibration folder")
        calibChooseButton.setFixedWidth(250)
        calibChooseButton.clicked.connect(self.select_calib_dir)

        inPlyChooseButton = QPushButton("Choose your input PLY file")
        inPlyChooseButton.setFixedWidth(250)
        inPlyChooseButton.clicked.connect(self.select_input_ply)

        outPlyChooseButton = QPushButton("Choose your output folder")
        outPlyChooseButton.setFixedWidth(250)
        outPlyChooseButton.clicked.connect(self.select_output_ply)

        computeButton= QPushButton("RUN")
        computeButton.clicked.connect(self.compute)

        """ Progress bar"""
        self.progress = QProgressBar(self)
        self.progress.setVisible(False)

        """ Boxes !"""

        hbox1.addWidget(self.imageDirLine)
        hbox1.addWidget(imageChooseButton)
        
        hbox1.addWidget(self.imageExt)
        
        hbox2.addWidget(self.imageOri)
        hbox2.addWidget(oriChooseButton)

        hbox3.addWidget(self.calibDirLine)
        hbox3.addWidget(calibChooseButton)

        hbox4.addWidget(self.inPlyLine)
        hbox4.addWidget(inPlyChooseButton)

        hbox5.addWidget(self.outPlyLine)
        hbox5.addWidget(outPlyChooseButton)

        hbox6.addWidget(self.computeMethod)
        hbox6.addWidget(self.imageChannelLabel)
        hbox6.addWidget(self.imageChannelLine)
        hbox6.addWidget(computeButton)

        hbox7.addWidget(self.progress)
        hbox7.addWidget(self.warningLabel)
        
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        
        vbox.addStretch(1)
        vbox.addLayout(hbox5)
        vbox.addLayout(hbox6)
        vbox.addLayout(hbox7)

        self.setLayout(vbox)
        self.show()


    def select_image_dir(self):
        fname = QFileDialog.getExistingDirectory(self, 'Select image directory')
        if fname:
            self.imageDirLine.setText(fname)
            
    def select_ori_dir(self):
        fname = QFileDialog.getExistingDirectory(self, 'Select image orientation directory')
        if fname:
            self.imageOri.setText(fname)
    
    def select_calib_dir(self):
        fname = QFileDialog.getExistingDirectory(self, 'Select calibration directory')
        if fname:
            self.calibDirLine.setText(fname)

    def select_input_ply(self):
        fname = QFileDialog.getOpenFileName(self, 'Select input PLY file')
        if fname[0]:
            self.inPlyLine.setText(fname[0])

    def select_output_ply(self):
        fname = QFileDialog.getSaveFileName(self, 'Select output PLY file name')
        if fname[0]:
            self.outPlyLine.setText(fname[0])

    def compute(self):
        go = False
        imDir=self.imageDirLine.text()
        imExt = str(self.imageExt.currentText())
        ori = self.imageOri.text()
        calDir=self.calibDirLine.text()
        inPly=self.inPlyLine.text()
        outPly=self.outPlyLine.text()
        channel=self.imageChannelLine.text()
        modestr = str(self.computeMethod.currentText())
        mode = self.modeDict[modestr]

        ## TEST ONLY
        imDir = "D:\home\Arthur\Documents\Informatique\Projet_GitHub\pyhton-colorply\example"
        imExt = ".TIF"
        ori = "D:\home\Arthur\Documents\Informatique\Projet_GitHub\pyhton-colorply\example\Ori-1bande_All_CampariGCP"
        calDir = "D:\home\Arthur\Documents\Informatique\Projet_GitHub\pyhton-colorply\example\Ori-1bande_All_CampariGCP\AutoCal_Foc-4000_Cam-SequoiaSequoia-NIR.xml"
        inPly = "D:\home\Arthur\Documents\Informatique\Projet_GitHub\pyhton-colorply\C3DC_QuickMac_1bandeAllCampariGCP_5images_SMALL.ply"
        outPly = "test.ply"
        channel = "NTF"
        mode = "avg"
 
        if len(imDir)*len(calDir)*len(inPly)*len(outPly)*len(channel) : # A sexy way to check if none of the fields are empty
            self.progress.setVisible(True)
            self.warningLabel.setVisible(False)
            
            images=loadImages(calDir, imDir, (".jpg", ".tif", ".JPG", ".TIF", ".JPEG", ".TIFF"), channel)
            
            addChannelToCloud(inPly, calDir, ori, imDir, imExt, channel, mode)
            
        else :
            self.warningLabel.setVisible(True)
            self.progress.setVisible(False)
        
            

def runMainWindow():
        
    app = QtWidgets.QApplication(sys.argv)
    app = setDarkTheme(app)
    window= MainWindow()
    app.exec_()
    



if __name__ == "__main__":
    runMainWindow()


    