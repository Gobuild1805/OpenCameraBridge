from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class PlaceholderPage(QWidget):
    def __init__(self, title: str):
        super().__init__()

        layout = QVBoxLayout(self)

        label = QLabel(title)
        label.setAlignment(Qt.AlignCenter)
        label.setObjectName("Title")

        layout.addStretch()
        layout.addWidget(label)
        layout.addStretch()