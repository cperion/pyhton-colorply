""" This is the python-colorply GUI """

import os
import sys
from palette import *
from PyQt5.QtWidgets import  (QWidget, QPushButton, QApplication, QMainWindow, QFileDialog,
QLineEdit, QHBoxLayout, QVBoxLayout, QComboBox, QProgressBar, QLabel)
from PyQt5.QtCore import pyqtSignal
from inputoutput.imagefile import loadImages

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        

    def initUI(self):
        self.setWindowTitle('Python-colorply')

        hbox1=QHBoxLayout() # image directory line
        hbox2=QHBoxLayout() # calibration directory line
        hbox3=QHBoxLayout() # input ply line
        hbox4=QHBoxLayout() # output ply line
        hbox5=QHBoxLayout() # channel, compute method and run button line
        hbox6=QHBoxLayout()
        vbox=QVBoxLayout()
        """computeMethod."""
        computeMethod = QComboBox()
        computeMethod.addItem("Average")
       
        

        """ Text Lines !"""
        self.imageDirLine = QLineEdit()
        self.imageChannelLabel = QLabel("Channel name :")
        self.imageChannelLine = QLineEdit()
        self.calibDirLine = QLineEdit()
        self.inPlyLine = QLineEdit()
        self.outPlyLine = QLineEdit()
        self.warningLabel = QLabel("Error: please fill all the fields !")
        self.warningLabel.setVisible(False)


        """ Buttons ! """
        imageChooseButton = QPushButton("Choose your image folder")
        imageChooseButton.setFixedWidth(250)
        imageChooseButton.clicked.connect(self.select_image_dir)

        calibChooseButton = QPushButton("Choose your calibration folder")
        calibChooseButton.setFixedWidth(250)
        calibChooseButton.clicked.connect(self.select_calib_dir)

        inPlyChooseButton = QPushButton("Choose your input PLY file")
        inPlyChooseButton.setFixedWidth(250)
        inPlyChooseButton.clicked.connect(self.select_input_ply)

        outPlyChooseButton = QPushButton("Choose your output PLY file")
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

        hbox2.addWidget(self.calibDirLine)
        hbox2.addWidget(calibChooseButton)

        hbox3.addWidget(self.inPlyLine)
        hbox3.addWidget(inPlyChooseButton)

        hbox4.addWidget(self.outPlyLine)
        hbox4.addWidget(outPlyChooseButton)

        hbox5.addWidget(computeMethod)
        hbox5.addWidget(self.imageChannelLabel)
        hbox5.addWidget(self.imageChannelLine)
        hbox5.addWidget(computeButton)

        hbox6.addWidget(self.progress)
        hbox6.addWidget(self.warningLabel)
        
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addStretch(1)
        vbox.addLayout(hbox5)
        vbox.addLayout(hbox6)

        self.setLayout(vbox)


        self.show()


    def select_image_dir(self):
        fname = QFileDialog.getExistingDirectory(self, 'Select image directory')
        if fname:
            self.imageDirLine.setText(fname)
    
    def select_calib_dir(self):
        fname = QFileDialog.getExistingDirectory(self, 'Select calibration directory')
        if fname:
            self.calibDirLine.setText(fname)

    def select_input_ply(self):
        fname = QFileDialog.getOpenFileName(self, 'Select input PLY file')
        if fname[0]:
            self.inPlyLine.setText(fname[0])

    def select_output_ply(self):
        fname = QFileDialog.getSaveFileName(self, 'Select output PLY file')
        if fname[0]:
            self.outPlyLine.setText(fname[0])

    def compute(self):
        go = False
        imDir=self.imageDirLine.text()
        calDir=self.calibDirLine.text()
        inPly=self.inPlyLine.text()
        outPly=self.outPlyLine.text()
        channel=self.imageChannelLine.text()
        if len(imDir)*len(calDir)*len(inPly)*len(outPly)*len(channel) : # A sexy way to check if none of the fields are empty
            self.progress.setVisible(True)
            self.warningLabel.setVisible(False)
            images=loadImages(calDir, imDir, (".jpg", ".tif", ".JPG", ".TIF", ".JPEG", ".TIFF"), channel)

        else :
            self.warningLabel.setVisible(True)
            self.progress.setVisible(False)
        
            
        

app = QApplication(sys.argv)


app = setDarkTheme(app)



window= MainWindow()
app.exec_()