from PySide6.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,
    QPushButton, QLabel, QStackedWidget
)
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("OpenCameraBridge")
        self.resize(1100, 700)

        root = QWidget()
        layout = QHBoxLayout(root)

        nav = QVBoxLayout()
        self.stack = QStackedWidget()

        pages = [
            ("Dashboard", "Camera and upload status will appear here."),
            ("Cameras", "Add RTSP cameras here."),
            ("Destinations", "Prusa Connect and other upload targets."),
            ("Settings", "Application settings."),
            ("About", "OpenCameraBridge v0.1"),
        ]

        for index, (name, text) in enumerate(pages):
            btn = QPushButton(name)
            btn.clicked.connect(lambda checked=False, i=index: self.stack.setCurrentIndex(i))
            nav.addWidget(btn)

            label = QLabel(text)
            label.setAlignment(Qt.AlignCenter)
            self.stack.addWidget(label)

        nav.addStretch()

        layout.addLayout(nav, 1)
        layout.addWidget(self.stack, 5)

        self.setCentralWidget(root)