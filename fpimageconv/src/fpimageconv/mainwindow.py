# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSplitter,
    QStatusBar, QToolButton, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 160)
        MainWindow.setStyleSheet(u"background-color: rgb(144, 144, 144);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.convert_btn = QPushButton(self.centralwidget)
        self.convert_btn.setObjectName(u"convert_btn")
        self.convert_btn.setEnabled(True)
        self.convert_btn.setGeometry(QRect(250, 100, 84, 24))
        self.convert_btn.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.convert_btn.setCheckable(False)
        self.convert_btn.setChecked(False)
        self.convert_btn.setFlat(False)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 571, 91))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.splitter_2 = QSplitter(self.layoutWidget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Orientation.Horizontal)
        self.select_filepath = QLineEdit(self.splitter_2)
        self.select_filepath.setObjectName(u"select_filepath")
        self.select_filepath.setStyleSheet(u"QLineEdit#select_filepath {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 4px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
"}")
        self.select_filepath.setReadOnly(True)
        self.splitter_2.addWidget(self.select_filepath)
        self.select_file_btn = QToolButton(self.splitter_2)
        self.select_file_btn.setObjectName(u"select_file_btn")
        self.select_file_btn.setStyleSheet(u"QToolButton#select_file_btn {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 4px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 4px;\n"
"}")
        self.splitter_2.addWidget(self.select_file_btn)

        self.gridLayout.addWidget(self.splitter_2, 1, 0, 1, 1)

        self.splitter = QSplitter(self.layoutWidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.save_filepath = QLineEdit(self.splitter)
        self.save_filepath.setObjectName(u"save_filepath")
        self.save_filepath.setStyleSheet(u"QLineEdit#save_filepath {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 4px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
"}")
        self.save_filepath.setReadOnly(True)
        self.splitter.addWidget(self.save_filepath)
        self.select_file_btn_2 = QToolButton(self.splitter)
        self.select_file_btn_2.setObjectName(u"select_file_btn_2")
        self.select_file_btn_2.setStyleSheet(u"QToolButton#select_file_btn_2 {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 4px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 4px;\n"
"}")
        self.splitter.addWidget(self.select_file_btn_2)

        self.gridLayout.addWidget(self.splitter, 2, 0, 1, 1)

        self.splitter_3 = QSplitter(self.layoutWidget)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Orientation.Horizontal)
        self.state_label = QLabel(self.splitter_3)
        self.state_label.setObjectName(u"state_label")
        self.state_label.setEnabled(True)
        self.state_label.setStyleSheet(u"QLabel#state_label {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 4px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}")
        self.splitter_3.addWidget(self.state_label)
        self.state_label_2 = QLabel(self.splitter_3)
        self.state_label_2.setObjectName(u"state_label_2")
        self.state_label_2.setEnabled(True)
        self.state_label_2.setStyleSheet(u"QLabel#state_label_2 {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 4px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 460px;\n"
"}")
        self.splitter_3.addWidget(self.state_label_2)

        self.gridLayout.addWidget(self.splitter_3, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Image Converter for Fruitpeel", None))
        self.convert_btn.setText(QCoreApplication.translate("MainWindow", u"Convert!", None))
        self.select_filepath.setInputMask("")
        self.select_filepath.setText(QCoreApplication.translate("MainWindow", u"Choose path to image file...", u"Choose path to image file..."))
        self.select_file_btn.setText(QCoreApplication.translate("MainWindow", u"📂", None))
        self.save_filepath.setText(QCoreApplication.translate("MainWindow", u"Choose path to save converted image...", u"Choose path to save..."))
        self.select_file_btn_2.setText(QCoreApplication.translate("MainWindow", u"📁", None))
        self.state_label.setText(QCoreApplication.translate("MainWindow", u"Current state:", None))
        self.state_label_2.setText(QCoreApplication.translate("MainWindow", u"State\n"
"", None))
    # retranslateUi

