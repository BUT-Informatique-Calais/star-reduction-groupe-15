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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QSpinBox, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(910, 590)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(24, 24, 24, 24)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_display = QLabel(self.centralwidget)
        self.lbl_display.setObjectName(u"lbl_display")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_display.sizePolicy().hasHeightForWidth())
        self.lbl_display.setSizePolicy(sizePolicy)
        self.lbl_display.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.lbl_display)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.btn_open = QPushButton(self.centralwidget)
        self.btn_open.setObjectName(u"btn_open")

        self.verticalLayout_2.addWidget(self.btn_open)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.sld_kernel = QSlider(self.centralwidget)
        self.sld_kernel.setObjectName(u"sld_kernel")
        self.sld_kernel.setMinimum(3)
        self.sld_kernel.setMaximum(71)
        self.sld_kernel.setOrientation(Qt.Orientation.Horizontal)
        self.sld_kernel.setTickPosition(QSlider.TickPosition.NoTicks)

        self.horizontalLayout.addWidget(self.sld_kernel)

        self.spin_kernel = QSpinBox(self.centralwidget)
        self.spin_kernel.setObjectName(u"spin_kernel")
        self.spin_kernel.setMinimum(3)
        self.spin_kernel.setMaximum(71)

        self.horizontalLayout.addWidget(self.spin_kernel)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.sld_blur = QSlider(self.centralwidget)
        self.sld_blur.setObjectName(u"sld_blur")
        self.sld_blur.setMinimum(1)
        self.sld_blur.setMaximum(31)
        self.sld_blur.setSingleStep(2)
        self.sld_blur.setValue(1)
        self.sld_blur.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_3.addWidget(self.sld_blur)

        self.spin_blur = QSpinBox(self.centralwidget)
        self.spin_blur.setObjectName(u"spin_blur")
        self.spin_blur.setMinimum(1)
        self.spin_blur.setMaximum(31)
        self.spin_blur.setSingleStep(2)

        self.horizontalLayout_3.addWidget(self.spin_blur)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lbl_iter = QLabel(self.centralwidget)
        self.lbl_iter.setObjectName(u"lbl_iter")

        self.horizontalLayout_4.addWidget(self.lbl_iter)

        self.sld_iter = QSlider(self.centralwidget)
        self.sld_iter.setObjectName(u"sld_iter")
        self.sld_iter.setMinimum(1)
        self.sld_iter.setMaximum(99)
        self.sld_iter.setValue(1)
        self.sld_iter.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_4.addWidget(self.sld_iter)

        self.spin_iter = QSpinBox(self.centralwidget)
        self.spin_iter.setObjectName(u"spin_iter")
        self.spin_iter.setMinimum(1)

        self.horizontalLayout_4.addWidget(self.spin_iter)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lbl_threshold = QLabel(self.centralwidget)
        self.lbl_threshold.setObjectName(u"lbl_threshold")

        self.horizontalLayout_5.addWidget(self.lbl_threshold)

        self.sld_threshold = QSlider(self.centralwidget)
        self.sld_threshold.setObjectName(u"sld_threshold")
        self.sld_threshold.setMinimum(-30)
        self.sld_threshold.setMaximum(-1)
        self.sld_threshold.setSingleStep(0)
        self.sld_threshold.setValue(-3)
        self.sld_threshold.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_5.addWidget(self.sld_threshold)

        self.spin_threshold = QSpinBox(self.centralwidget)
        self.spin_threshold.setObjectName(u"spin_threshold")
        self.spin_threshold.setMinimum(-30)
        self.spin_threshold.setMaximum(-1)
        self.spin_threshold.setValue(-3)

        self.horizontalLayout_5.addWidget(self.spin_threshold)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btn_reset = QPushButton(self.centralwidget)
        self.btn_reset.setObjectName(u"btn_reset")

        self.horizontalLayout_6.addWidget(self.btn_reset)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_6)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 910, 21))
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
        self.lbl_display.setText(QCoreApplication.translate("MainWindow", u"Pas d'image charg\u00e9", None))
        self.btn_open.setText(QCoreApplication.translate("MainWindow", u"Choisir un fichier FITS", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Kernel Erosion    ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Flou Masque      ", None))
        self.lbl_iter.setText(QCoreApplication.translate("MainWindow", u"Iterations            ", None))
        self.lbl_threshold.setText(QCoreApplication.translate("MainWindow", u"Seuil Masque     ", None))
        self.btn_reset.setText(QCoreApplication.translate("MainWindow", u"R\u00e9initialiser", None))
    # retranslateUi

