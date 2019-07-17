""" This is the python-colorply GUI """

import os
import sys
from PyQt5.QtWidgets import  (QWidget, QToolTip, QPushButton, QApplication, QMainWindow, QFileDialog, QAction, QLabel, 
QLineEdit, QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import pyqtSignal
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        

    def initUI(self):
        self.setWindowTitle('Python-colorply')

        hbox1=QHBoxLayout()
        hbox2=QHBoxLayout()
        hbox3=QHBoxLayout()
        hbox4=QHBoxLayout()
        hbox5=QHBoxLayout()
        vbox=QVBoxLayout()
        """ Text Lines !"""
        self.imageDirLine = QLineEdit("Choose an image directory")
        self.calibDirLine = QLineEdit("Choose a calibration directory")
        self.inPlyLine = QLineEdit("Choose an input ply file")
        self.outPlyLine = QLineEdit("Choose an output ply file")


        """ Buttons ! """
        imageChooseButton = QPushButton("Choose your image folder")
        imageChooseButton.clicked.connect(self.select_image_dir)

        calibChooseButton = QPushButton("Choose your calibration folder")
        calibChooseButton.clicked.connect(self.select_calib_dir)

        inPlyChooseButton = QPushButton("Choose your input PLY file")
        inPlyChooseButton.clicked.connect(self.select_input_ply)

        outPlyChooseButton = QPushButton("Choose your output PLY file")
        outPlyChooseButton.clicked.connect(self.select_output_ply)

        computeButton= QPushButton("COMPUTE")


        """ Boxes !"""

        hbox1.addWidget(self.imageDirLine)
        hbox1.addWidget(imageChooseButton)

        hbox2.addWidget(self.calibDirLine)
        hbox2.addWidget(calibChooseButton)

        hbox3.addWidget(self.inPlyLine)
        hbox3.addWidget(inPlyChooseButton)

        hbox4.addWidget(self.outPlyLine)
        hbox4.addWidget(outPlyChooseButton)

        hbox5.addWidget(computeButton)

        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addStretch(1)
        vbox.addLayout(hbox5)

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
        


app = QApplication(sys.argv)
window= MainWindow()
app.exec_()