# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'biblio_images.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1200, 697)
        self.gridLayoutWidget = QWidget(Dialog)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 1181, 621))
        self.grid_img_display = QGridLayout(self.gridLayoutWidget)
        self.grid_img_display.setObjectName(u"grid_img_display")
        self.grid_img_display.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutWidget = QWidget(Dialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(750, 640, 441, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_quit = QPushButton(self.horizontalLayoutWidget)
        self.btn_quit.setObjectName(u"btn_quit")

        self.horizontalLayout.addWidget(self.btn_quit)

        self.btn_choose = QPushButton(self.horizontalLayoutWidget)
        self.btn_choose.setObjectName(u"btn_choose")

        self.horizontalLayout.addWidget(self.btn_choose)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.btn_quit.setText(QCoreApplication.translate("Dialog", u"Quitter", None))
        self.btn_choose.setText(QCoreApplication.translate("Dialog", u"Choisir", None))
    # retranslateUi

