# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSlider, QSpinBox,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(904, 649)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_open = QPushButton(self.centralwidget)
        self.btn_open.setObjectName(u"btn_open")
        self.btn_open.setGeometry(QRect(360, 410, 201, 24))
        self.sld_kernel = QSlider(self.centralwidget)
        self.sld_kernel.setObjectName(u"sld_kernel")
        self.sld_kernel.setGeometry(QRect(170, 460, 611, 16))
        self.sld_kernel.setMinimum(3)
        self.sld_kernel.setMaximum(71)
        self.sld_kernel.setOrientation(Qt.Orientation.Horizontal)
        self.sld_kernel.setTickPosition(QSlider.TickPosition.NoTicks)
        self.sld_blur = QSlider(self.centralwidget)
        self.sld_blur.setObjectName(u"sld_blur")
        self.sld_blur.setGeometry(QRect(170, 490, 611, 41))
        self.sld_blur.setMinimum(1)
        self.sld_blur.setMaximum(31)
        self.sld_blur.setSingleStep(2)
        self.sld_blur.setValue(1)
        self.sld_blur.setOrientation(Qt.Orientation.Horizontal)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 460, 111, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 500, 111, 16))
        self.lbl_display = QLabel(self.centralwidget)
        self.lbl_display.setObjectName(u"lbl_display")
        self.lbl_display.setGeometry(QRect(170, 20, 581, 361))
        self.lbl_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sld_iter = QSlider(self.centralwidget)
        self.sld_iter.setObjectName(u"sld_iter")
        self.sld_iter.setGeometry(QRect(170, 540, 611, 16))
        self.sld_iter.setMinimum(1)
        self.sld_iter.setMaximum(99)
        self.sld_iter.setValue(1)
        self.sld_iter.setOrientation(Qt.Orientation.Horizontal)
        self.lbl_iter = QLabel(self.centralwidget)
        self.lbl_iter.setObjectName(u"lbl_iter")
        self.lbl_iter.setGeometry(QRect(70, 540, 49, 16))
        self.spin_kernel = QSpinBox(self.centralwidget)
        self.spin_kernel.setObjectName(u"spin_kernel")
        self.spin_kernel.setGeometry(QRect(790, 460, 61, 21))
        self.spin_kernel.setMinimum(3)
        self.spin_kernel.setMaximum(71)
        self.spin_blur = QSpinBox(self.centralwidget)
        self.spin_blur.setObjectName(u"spin_blur")
        self.spin_blur.setGeometry(QRect(790, 500, 61, 21))
        self.spin_blur.setMinimum(1)
        self.spin_blur.setMaximum(31)
        self.spin_blur.setSingleStep(2)
        self.spin_iter = QSpinBox(self.centralwidget)
        self.spin_iter.setObjectName(u"spin_iter")
        self.spin_iter.setGeometry(QRect(790, 540, 61, 21))
        self.spin_iter.setMinimum(1)
        self.sld_threshold = QSlider(self.centralwidget)
        self.sld_threshold.setObjectName(u"sld_threshold")
        self.sld_threshold.setGeometry(QRect(170, 580, 611, 16))
        self.sld_threshold.setMinimum(-30)
        self.sld_threshold.setMaximum(-1)
        self.sld_threshold.setSingleStep(0)
        self.sld_threshold.setValue(-3)
        self.sld_threshold.setOrientation(Qt.Orientation.Horizontal)
        self.spin_threshold = QSpinBox(self.centralwidget)
        self.spin_threshold.setObjectName(u"spin_threshold")
        self.spin_threshold.setGeometry(QRect(790, 580, 61, 21))
        self.spin_threshold.setMinimum(-30)
        self.spin_threshold.setMaximum(-1)
        self.spin_threshold.setValue(-3)
        self.lbl_threshold = QLabel(self.centralwidget)
        self.lbl_threshold.setObjectName(u"lbl_threshold")
        self.lbl_threshold.setGeometry(QRect(70, 580, 91, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 904, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.sld_kernel.valueChanged.connect(self.spin_kernel.setValue)
        self.spin_kernel.valueChanged.connect(self.sld_kernel.setValue)
        self.sld_blur.valueChanged.connect(self.spin_blur.setValue)
        self.spin_blur.valueChanged.connect(self.sld_blur.setValue)
        self.sld_iter.valueChanged.connect(self.spin_iter.setValue)
        self.spin_iter.valueChanged.connect(self.sld_iter.setValue)
        self.sld_threshold.valueChanged.connect(self.spin_threshold.setValue)
        self.spin_threshold.valueChanged.connect(self.sld_threshold.setValue)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_open.setText(QCoreApplication.translate("MainWindow", u"Choisir un fichier FITS", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Kernel Masque", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Flou Masque", None))
        self.lbl_display.setText(QCoreApplication.translate("MainWindow", u"Pas d'image charg\u00e9", None))
        self.lbl_iter.setText(QCoreApplication.translate("MainWindow", u"Iterations", None))
        self.lbl_threshold.setText(QCoreApplication.translate("MainWindow", u"D\u00e9tecte Etoiles", None))
    # retranslateUi

