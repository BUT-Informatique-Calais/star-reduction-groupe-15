import sys
import os
from PySide6.QtWidgets import QApplication, QDialog
from PySide6.QtCore import QFile, Qt
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QImage, QPixmap
from AstroPictureHandler import AstroPictureHandler as aph
from Picture import Picture



class FitsLibrary(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("G15 - Bibliotheque Image")

        # chargement du fichier .ui
        loader = QUiLoader()

        #chargement du QSS
        qss_path = os.path.join(os.path.dirname(__file__), "style.qss")
        if os.path.exists(qss_path):
            with open(qss_path, "r") as f:
                self.setStyleSheet(f.read())

        ui_path = os.path.join(os.path.dirname(__file__), "biblio_images.ui")
        ui_file = QFile(ui_path)
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        ui_file.close()
        
        
        pictures = aph.getPictures()
        for index, picture in enumerate(pictures):
            print(picture)
            ligne = index // 3
            colonne = index % 3
            url = picture
            self.ui.grid_img_display.addWidget(Picture(url), ligne, colonne)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FitsLibrary()
    window.ui.show()
    sys.exit(app.exec())
