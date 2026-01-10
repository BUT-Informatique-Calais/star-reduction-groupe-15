import sys
import os
from PySide6.QtWidgets import QApplication, QDialog, QScrollArea, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import QFile, Qt
from PySide6.QtUiTools import QUiLoader
from AstroPictureHandler import AstroPictureHandler as aph
from Picture import Picture

class FitsLibrary(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("G15 - Bibliothèque FITS")
        self.resize(1100, 700)
        
        
    
        # Chargement de l'UI
        loader = QUiLoader()
        ui_path = os.path.join(os.path.dirname(__file__), "biblio_images.ui")
        ui_file = QFile(ui_path)
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        ui_file.close()

        self.scroll_area = self.ui.scrollPictures
        self.scroll_area.setWidgetResizable(True) 
        self.scroll_area.setFrameShape(QScrollArea.NoFrame)

        # Le Widget qui contient la grille
        self.container = QWidget()
        self.vlayout = QVBoxLayout(self.container)
        self.vlayout.setSpacing(10)
        self.vlayout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        
        self.scroll_area.setWidget(self.container)

        self.load_images()

    def load_images(self):

        hlay = QHBoxLayout()
        self.vlayout.addLayout(hlay)


        pictures = aph.getPictures()
        for index, path in enumerate(pictures):
            ligne = index // 3
            
            if ligne == 0 and index != 0 :
                print("new line")
                hlay = QHBoxLayout()
                self.vlayout.addLayout(hlay)
            
            print('adding picture')
            pic_widget = Picture(path)
            pic_widget.setFixedSize(320, 280) 
            
            hlay.addWidget(pic_widget)
            
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FitsLibrary()
    window.ui.show()
    sys.exit(app.exec())