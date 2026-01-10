from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import Qt, QFile
from PySide6.QtUiTools import QUiLoader
from astropy.io import fits
import numpy as np
import os
from ClickableLabel import ClickableLabel

class Picture(QWidget):
    def __init__(self, picture_path: str) -> None:
        super().__init__()

        self.PICTURE_PATH = picture_path
        self.original_image = None

        loader = QUiLoader()
        ui_path = os.path.join(os.path.dirname(__file__), "picture.ui")
        ui_file = QFile(ui_path)
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        ui_file.close()

        old_label = self.ui.lbl_display
        parent_layout = old_label.parentWidget().layout()
        index = parent_layout.indexOf(old_label)
        old_label.setParent(None)

        self.ui.lbl_display = ClickableLabel(old_label.parentWidget(), self.PICTURE_PATH)
        self.ui.lbl_display.setText("Chargement...")
        self.ui.lbl_display.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.ui.lbl_display.setScaledContents(False)
        parent_layout.insertWidget(index, self.ui.lbl_display)

        self.set_image_data(picture_path)


    def set_image_data(self, fits_path):
        try:
            with fits.open(fits_path) as hdul:
                data = hdul[0].data

            if data is None:
                return

            data = np.nan_to_num(data)
            d_min, d_max = np.min(data), np.max(data)

            if d_max - d_min == 0:
                normalized = np.zeros(data.shape, dtype=np.uint8)
            else:
                normalized = ((data - d_min) / (d_max - d_min) * 255).astype('uint8')

            normalized = np.ascontiguousarray(normalized)

            if data.ndim == 2:
                h, w = normalized.shape
                self.original_image = QImage(normalized.data, w, h, w, QImage.Format_Grayscale8).copy()
            elif data.ndim == 3:
                if normalized.shape[0] == 3:
                    normalized = np.transpose(normalized, (1, 2, 0))
                    normalized = np.ascontiguousarray(normalized)
                h, w, c = normalized.shape
                self.original_image = QImage(normalized.data, w, h, w * 3, QImage.Format_RGB888).copy()

            self.ui.lbl_display.setText("")
            self.update_display()

        except Exception as e:
            print(f"Erreur {os.path.basename(fits_path)}: {e}")
            self.ui.lbl_display.setText("Erreur")

    def update_display(self):
        if self.original_image and not self.original_image.isNull():
            target_size = self.ui.lbl_display.size()
            if target_size.width() > 1 and target_size.height() > 1:
                pixmap = QPixmap.fromImage(self.original_image)
                scaled_pix = pixmap.scaled(target_size, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
                self.ui.lbl_display.setPixmap(scaled_pix)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.ui.resize(self.size())
        self.ui.lbl_display.resize(self.ui.size())
        self.update_display()
