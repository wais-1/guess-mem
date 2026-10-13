# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddPlayer.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 250)
        Dialog.setStyleSheet(u"background-color: #1A1A2E;")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 20, 311, 41))
        self.label.setStyleSheet(u"font-size: 24px;\n"
"text-transform: uppercase;\n"
"color: #F0F4F8;")
        self.lineEdit_playername = QLineEdit(Dialog)
        self.lineEdit_playername.setObjectName(u"lineEdit_playername")
        self.lineEdit_playername.setGeometry(QRect(40, 90, 321, 61))
        self.lineEdit_playername.setStyleSheet(u"font-size: 20px;\n"
"border-radius: 10px;\n"
"color: #F0F4F8;\n"
"background-color: #31315B;")
        self.pushButton_addplayer = QPushButton(Dialog)
        self.pushButton_addplayer.setObjectName(u"pushButton_addplayer")
        self.pushButton_addplayer.setGeometry(QRect(90, 170, 221, 51))
        self.pushButton_addplayer.setStyleSheet(u"font-size: 20px;\n"
"border-radius: 10px;\n"
"color: #F0F4F8;\n"
"background-color: #31315B;")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043a\u043e\u043c\u0430\u043d\u0434\u044b", None))
        self.lineEdit_playername.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043e\u043c\u0430\u043d\u0434\u044b...", None))
        self.pushButton_addplayer.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043a\u043e\u043c\u0430\u043d\u0434\u0443", None))
    # retranslateUi

