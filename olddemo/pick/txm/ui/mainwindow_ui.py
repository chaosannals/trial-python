# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 240)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.keyLineEdit = QLineEdit(self.centralwidget)
        self.keyLineEdit.setObjectName(u"keyLineEdit")
        self.keyLineEdit.setStyleSheet(u"font-size: 18px;\n"
"border: 1px solid #333;\n"
"border-radius: 5px;")

        self.verticalLayout.addWidget(self.keyLineEdit)

        self.secretLineEdit = QLineEdit(self.centralwidget)
        self.secretLineEdit.setObjectName(u"secretLineEdit")
        self.secretLineEdit.setStyleSheet(u"font-size: 18px;\n"
"border: 1px solid #333;\n"
"border-radius: 5px;")

        self.verticalLayout.addWidget(self.secretLineEdit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pickButton = QPushButton(self.centralwidget)
        self.pickButton.setObjectName(u"pickButton")
        self.pickButton.setStyleSheet(u"padding: 10px;\n"
"border-radius: 5px;\n"
"color: #fff;\n"
"background:rgb(0, 170, 255);\n"
"\n"
"QPushButton::hover {\n"
"	background:rgb(0, 200, 255);\n"
"}")

        self.verticalLayout.addWidget(self.pickButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 300, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u817e\u8baf\u5730\u56fe\u884c\u653f\u5212\u533a", None))
        self.pickButton.setText(QCoreApplication.translate("MainWindow", u"\u83b7\u53d6", None))
    # retranslateUi

