from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
from modal import window_modal
from dis_main import *
app = QApplication(sys.argv)
mainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(mainWindow)
mainWindow.show()
def  open_modal_window():
    mainWindow.close()
    window_modal()




ui.pushButton.clicked.connect(open_modal_window)
sys.exit(app.exec_())