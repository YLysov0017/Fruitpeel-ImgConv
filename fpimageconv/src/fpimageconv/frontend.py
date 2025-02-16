from PySide6 import QtWidgets
import sys


class App(QtWidgets.QApplication):
    def __init__(self, args):
        super(MyApp, self).__init__(args)
        self.mainWindow = MainWindow()
        self.exec_()    # enter event loop

