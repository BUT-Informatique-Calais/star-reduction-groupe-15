import sys
import os
from PySide6.QtWidgets import QApplication, QDialog, QScrollArea, QWidget, QVBoxLayout, QHBoxLayout, QSizePolicy, QMessageBox
from PySide6.QtCore import QFile, Qt
from PySide6.QtUiTools import QUiLoader
from AstroPictureHandler import AstroPictureHandler as aph
from Picture import Picture
from PySide6.QtCore import Signal, Qt

class FitsLibrary(QDialog):

    choosenFile = Signal(str)

    def __init__(self):
        super().__init__()


        self.selected_picture: None = None



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

        self.ui.btn_quit.clicked.connect(self.quitPage)
        self.ui.btn_choose.clicked.connect(self.chooseClicked)
        
        self.scroll_area.setWidget(self.container)
        

        self.load_images()

    def load_images(self):

        hlay = QHBoxLayout()
        self.vlayout.addLayout(hlay)


        pictures = aph.getPictures()
        for index, path in enumerate(pictures):
            
            
            if index % 3 == 0 and index != 0 :
                hlay = QHBoxLayout()
                self.vlayout.addLayout(hlay)
            
            pic_widget = Picture(path)
            pic_widget.ui.lbl_display.clicked.connect(self.setSelectedImage)
            pic_widget.setMinimumHeight(300)
            pic_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            
            hlay.addWidget(pic_widget)

    def setSelectedImage(self, image_path) -> None :
        self.selected_picture = image_path

    def chooseClicked(self) -> None :
        if not self.selected_picture == None :
            self.choosenFile.emit(self.selected_picture)
            self.quitPage()
        else :
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setText("Veuillez selectionner une image !")
            msgBox.setWindowTitle("Erreur")
            msgBox.setStandardButtons(QMessageBox.Ok)
                        


    def quitPage(self) -> None :
        self.ui.close()

            

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FitsLibrary()
    window.ui.show()
    sys.exit(app.exec())
