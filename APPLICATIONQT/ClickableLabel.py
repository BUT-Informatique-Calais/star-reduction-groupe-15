from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Signal, Qt

class ClickableLabel(QLabel):
    clicked = Signal(str)
    selected_label = None

    def __init__(self, parent=None, img_path=""):
        super().__init__(parent)
        self.img_path = img_path
        self.setAttribute(Qt.WidgetAttribute.WA_Hover, True)
        self.setStyleSheet("""
            QLabel {
                border: none;
            }
            QLabel:hover {
                border: 1px solid white;
            }
        """)

    def mousePressEvent(self, event):
        if ClickableLabel.selected_label and ClickableLabel.selected_label != self:
            ClickableLabel.selected_label.setStyleSheet("""
                QLabel {
                    border: none;
                }
                QLabel:hover {
                    border: 1px solid white;
                }
            """)

        self.setStyleSheet("""
            QLabel {
                border: 1px solid white;
            }
        """)
        ClickableLabel.selected_label = self
        self.clicked.emit(self.img_path)
        super().mousePressEvent(event)
