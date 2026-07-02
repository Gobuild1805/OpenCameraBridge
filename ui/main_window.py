from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QHBoxLayout,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QStackedWidget,
    QToolBar,
    QWidget,
)

from ui.pages.dashboard import DashboardPage
from ui.pages.placeholder import PlaceholderPage
from ui.themes.dark import DARK_STYLE


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("OpenCameraBridge")
        self.resize(1400, 850)

        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        toolbar.addAction(QAction("Refresh", self))
        toolbar.addAction(QAction("Settings", self))

        root = QWidget()
        root_layout = QHBoxLayout(root)
        root_layout.setContentsMargins(0, 0, 0, 0)

        self.menu = QListWidget()
        self.menu.setMaximumWidth(220)

        self.stack = QStackedWidget()

        pages = [
            ("Dashboard", DashboardPage()),
            ("Cameras", PlaceholderPage("Cameras")),
            ("Destinations", PlaceholderPage("Destinations")),
            ("Plugins", PlaceholderPage("Plugins")),
            ("Settings", PlaceholderPage("Settings")),
            ("About", PlaceholderPage("OpenCameraBridge v0.1")),
        ]

        for index, (name, page) in enumerate(pages):
            QListWidgetItem(name, self.menu)
            self.stack.addWidget(page)

        self.menu.currentRowChanged.connect(self.stack.setCurrentIndex)
        self.menu.setCurrentRow(0)

        root_layout.addWidget(self.menu)
        root_layout.addWidget(self.stack)

        self.setCentralWidget(root)
        self.statusBar().showMessage("Ready")
        self.setStyleSheet(DARK_STYLE)