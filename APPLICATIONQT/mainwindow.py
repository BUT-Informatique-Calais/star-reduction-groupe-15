import sys
import os
import cv2
import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtCore import QFile, Qt
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QImage, QPixmap

# Import de ton fichier de calcul
from AstroPictureHandler import AstroPictureHandler as model

class StarReductionApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # Chargement du fichier .ui
        loader = QUiLoader()
        ui_path = os.path.join(os.path.dirname(__file__), "form.ui")
        ui_file = QFile(ui_path)
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        ui_file.close()

        self.current_path = ""

        # Connexions des signaux (Bouton et Sliders)
        self.ui.btn_open.clicked.connect(self.open_file)
        self.ui.sld_kernel.valueChanged.connect(self.update_image)
        self.ui.sld_blur.valueChanged.connect(self.update_image)
        self.ui.sld_iter.valueChanged.connect(self.update_image)
        self.ui.sld_threshold.valueChanged.connect(self.update_image)

    def open_file(self):
        """Ouvre l'explorateur de fichiers."""
        path, _ = QFileDialog.getOpenFileName(self, "Ouvrir FITS", "", "FITS (*.fits)")
        if path:
            self.current_path = path
            self.update_image()

    def update_image(self):
        """Récupère les réglages et appelle le modèle."""
        if not self.current_path:
            return

        # Récupération des valeurs depuis l'UI
        k = self.ui.sld_kernel.value()
        b = self.ui.sld_blur.value()
        it = self.ui.sld_iter.value()
        th = self.ui.sld_threshold.value()

        # Sécurité : Toujours envoyer des nombres impairs pour les kernels OpenCV
        if k % 2 == 0: k += 1
        if b % 2 == 0: b += 1

        # Appel du modèle avec les 5 arguments corrigés
        img = model.process_reduction(self.current_path, (k,k), (b,b), it, th)
        if img :
            print(os.path.dirname(__file__))
            print(os.path.join(os.path.dirname(__file__), img))
            self.show_image(os.path.join(os.path.dirname(__file__), img))

    def show_image(self, cv_img: str):
        """Affiche l'image traitée dans le label de l'interface."""
        if cv_img is not None:
            print("cv image : ", cv_img)
            # Conversion BGR vers RGB pour Qt
            qt_img = QImage(cv_img)
            self.ui.lbl_display.setPixmap(QPixmap.fromImage(qt_img).scaled(
                self.ui.lbl_display.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StarReductionApp()
    window.ui.show() # Affiche l'interface chargée depuis le .ui
    sys.exit(app.exec())
