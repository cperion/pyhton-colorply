# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 20:53:48 2019

@author: Utilisateur
"""


import sys
from PyQt5 import QtCore, QtGui, QtWidgets

def setDarkTheme(app):
    palette = QtGui.QPalette()
    palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53,53,53))
    palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Base, QtGui.QColor(15,15,15))
    palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53,53,53))
    palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53,53,53))
    palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
         
    palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(142,45,197).lighter())
    palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
    app.setPalette(palette)
    return app


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    app = setDarkTheme(app)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.show()
    sys.exit(app.exec_())