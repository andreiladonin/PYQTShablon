from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from dis_modal import Ui_Dialog

def window_modal():

    win_modal = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(win_modal)

    win_modal.show()

    win_modal.setWindowModality(2)

    return win_modal.exec_()

