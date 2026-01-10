import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import QFile, Qt
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QImage, QPixmap
from FitsLibrary import FitsLibrary

from AstroPictureHandler import AstroPictureHandler as model

class StarReductionApp(QMainWindow):
    
    
    def __init__(self):
        
        super().__init__()

        self.setWindowTitle("G15 - Astrophoto")

        # chargement du fichier .ui
        loader = QUiLoader()
        self.fits_lib = None

        #chargement du QSS
        qss_path = os.path.join(os.path.dirname(__file__), "style.qss")
        if os.path.exists(qss_path):
            with open(qss_path, "r") as f:
                self.setStyleSheet(f.read())

        ui_path = os.path.join(os.path.dirname(__file__), "form.ui")
        ui_file = QFile(ui_path)
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        ui_file.close()

        self.current_path = ""

        #connexions des signaux
        self.ui.btn_open.clicked.connect(self.open_file)
        self.ui.btn_lib.clicked.connect(self.open_lib)
        self.ui.sld_kernel.valueChanged.connect(self.update_image)
        self.ui.sld_blur.valueChanged.connect(self.update_image)
        self.ui.sld_iter.valueChanged.connect(self.update_image)
        self.ui.sld_threshold.valueChanged.connect(self.update_image)
        self.ui.btn_reset.clicked.connect(self.reset_parameters)


    def choosenFile(self, filepath: str) -> None :
        self.current_path = filepath
        self.update_image()

    def open_lib(self) -> None:
        self.fits_lib = FitsLibrary()
        self.fits_lib.choosenFile.connect(self.choosenFile)
        self.fits_lib.ui.show()

    def open_file(self):
        """Ouvre l'explorateur de fichiers."""
        path, _ = QFileDialog.getOpenFileName(self, "Ouvrir FITS", "", "FITS (*.fits)")
        if path:
            self.current_path = path
            self.update_image()

    def update_image(self):
        if not self.current_path: return

        k = self.ui.sld_kernel.value()
        b = self.ui.sld_blur.value()
        it = self.ui.sld_iter.value()
        th = self.ui.sld_threshold.value()

        if k % 2 == 0: k += 1
        if b % 2 == 0: b += 1

        img_data = model.process_reduction(self.current_path, (k, k), (b, b), it, th)
        
        if img_data is not None:
            self.show_image(img_data)

    def show_image(self, cv_img):
        """Affiche l'image avec les couleurs originales respectées."""
        if cv_img is not None:
            height, width = cv_img.shape[:2]
            
            # cas image noir et blanc
            if len(cv_img.shape) == 2:
                bytes_per_line = width
                qt_img = QImage(cv_img.data, width, height, bytes_per_line, QImage.Format_Grayscale8)
            
            #cas image couleur
            else:
                bytes_per_line = 3 * width
                qt_img = QImage(cv_img.data, width, height, bytes_per_line, QImage.Format_RGB888)
            

            self.ui.lbl_display.setPixmap(QPixmap.fromImage(qt_img).scaled(
                self.ui.lbl_display.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            
    def reset_parameters(self):
        """Remet tous les sliders aux valeurs par défaut."""
        self.ui.sld_kernel.setValue(3)
        self.ui.sld_blur.setValue(1)
        self.ui.sld_iter.setValue(1)
        self.ui.sld_threshold.setValue(-3)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StarReductionApp()
    window.ui.show()
    sys.exit(app.exec())
