# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 900)
        MainWindow.setStyleSheet(u"background-color: #1A1A2E;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 0, 161, 31))
        self.label.setStyleSheet(u"font-size: 24px;\n"
"text-transform: uppercase;\n"
"color: #F0F4F8;")
        self.label_image = QLabel(self.centralwidget)
        self.label_image.setObjectName(u"label_image")
        self.label_image.setGeometry(QRect(20, 120, 761, 340))
        self.label_image.setStyleSheet(u"background-color: none;")
        self.label_image.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 500, 231, 31))
        self.label_5.setStyleSheet(u"font-size: 20px;\n"
"color: #F0F4F8;")
        self.lineEdit_answer = QLineEdit(self.centralwidget)
        self.lineEdit_answer.setObjectName(u"lineEdit_answer")
        self.lineEdit_answer.setGeometry(QRect(20, 550, 761, 61))
        self.lineEdit_answer.setStyleSheet(u"font-size: 20px;\n"
"border-radius: 10px;\n"
"color: #F0F4F8;\n"
"background-color: #31315B;")
        self.pushButton_answer = QPushButton(self.centralwidget)
        self.pushButton_answer.setObjectName(u"pushButton_answer")
        self.pushButton_answer.setGeometry(QRect(20, 620, 761, 51))
        self.pushButton_answer.setStyleSheet(u"font-size: 20px;\n"
"border-radius: 10px;\n"
"color: #F0F4F8;\n"
"background-color: #31315B;")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(660, 60, 121, 21))
        self.label_10.setStyleSheet(u"font-size: 20px;\n"
"color: #F0F4F8;")
        self.label_playerscore = QLabel(self.centralwidget)
        self.label_playerscore.setObjectName(u"label_playerscore")
        self.label_playerscore.setGeometry(QRect(750, 90, 31, 21))
        self.label_playerscore.setStyleSheet(u"font-size: 20px;\n"
"color: #F0F4F8;")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 50, 128, 58))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font-size: 20px;\n"
"color: #F0F4F8;")

        self.verticalLayout.addWidget(self.label_2)

        self.label_playername = QLabel(self.widget)
        self.label_playername.setObjectName(u"label_playername")
        self.label_playername.setStyleSheet(u"font-size: 20px;\n"
"color: #F0F4F8;")

        self.verticalLayout.addWidget(self.label_playername)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(690, 0, 81, 26))
        self.horizontalLayout = QHBoxLayout(self.widget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.widget1)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"font-size: 20px;\n"
"color: #F0F4F8;")

        self.horizontalLayout.addWidget(self.label_12)

        self.label_numberround = QLabel(self.widget1)
        self.label_numberround.setObjectName(u"label_numberround")
        self.label_numberround.setStyleSheet(u"font-size: 20px;\n"
"color: #F0F4F8;")

        self.horizontalLayout.addWidget(self.label_numberround)

        self.widget2 = QWidget(self.centralwidget)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(30, 700, 72, 58))
        self.verticalLayout_2 = QVBoxLayout(self.widget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_playername2 = QLabel(self.widget2)
        self.label_playername2.setObjectName(u"label_playername2")
        self.label_playername2.setStyleSheet(u"font-size: 20px;\n"
"color: #F0F4F8;")

        self.verticalLayout_2.addWidget(self.label_playername2)

        self.label_playername3 = QLabel(self.widget2)
        self.label_playername3.setObjectName(u"label_playername3")
        self.label_playername3.setStyleSheet(u"font-size: 20px;\n"
"color: #F0F4F8;")

        self.verticalLayout_2.addWidget(self.label_playername3)

        self.widget3 = QWidget(self.centralwidget)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(690, 700, 87, 64))
        self.verticalLayout_3 = QVBoxLayout(self.widget3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_playerscore2 = QLabel(self.widget3)
        self.label_playerscore2.setObjectName(u"label_playerscore2")
        self.label_playerscore2.setStyleSheet(u"font-size: 20px;\n"
"color: #F0F4F8;")

        self.horizontalLayout_4.addWidget(self.label_playerscore2)

        self.label_16 = QLabel(self.widget3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"font-size: 20px;\n"
"color: #F0F4F8;")

        self.horizontalLayout_4.addWidget(self.label_16)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_playerscore3 = QLabel(self.widget3)
        self.label_playerscore3.setObjectName(u"label_playerscore3")
        self.label_playerscore3.setStyleSheet(u"font-size: 20px;\n"
"color: #F0F4F8;")

        self.horizontalLayout_3.addWidget(self.label_playerscore3)

        self.label_15 = QLabel(self.widget3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"font-size: 20px;\n"
"color: #F0F4F8;")

        self.horizontalLayout_3.addWidget(self.label_15)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0433\u0430\u0434\u0430\u0439 \u043c\u0435\u043c", None))
        self.label_image.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0433\u0430\u0434\u0430\u0439\u0442\u0435 \u043c\u0435\u043c \u043f\u043e \u0444\u043e\u0442\u043e", None))
        self.lineEdit_answer.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043e\u0442\u0432\u0435\u0442...", None))
        self.pushButton_answer.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c \u043e\u0442\u0432\u0435\u0442", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u043a\u0438 \u0438\u0433\u0440\u043e\u043a\u0430:", None))
        self.label_playerscore.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0439\u0447\u0430\u0441 \u0445\u043e\u0434\u0438\u0442:", None))
        self.label_playername.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0433\u0440\u043e\u043a 1", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0443\u043d\u0434:", None))
        self.label_numberround.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_playername2.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0433\u0440\u043e\u043a 3", None))
        self.label_playername3.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0433\u0440\u043e\u043a 2", None))
        self.label_playerscore2.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u043e\u0447\u043a\u043e\u0432", None))
        self.label_playerscore3.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u043e\u0447\u043a\u043e\u0432", None))
    # retranslateUi

