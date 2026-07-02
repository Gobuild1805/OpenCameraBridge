from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QSizePolicy,
    QStatusBar,
    QToolBar,
    QVBoxLayout,
    QWidget,
)


class DashboardPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Dashboard")
        title.setObjectName("Title")

        subtitle = QLabel("Welcome to OpenCameraBridge")
        subtitle.setObjectName("Subtitle")

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addSpacing(20)

        cards = QHBoxLayout()

        for title_text, value in [
            ("Connected Cameras", "0"),
            ("Upload Targets", "0"),
            ("Bridge Status", "Idle"),
        ]:
            card = QFrame()
            card.setObjectName("Card")

            card_layout = QVBoxLayout(card)

            label = QLabel(title_text)
            label.setObjectName("CardTitle")

            number = QLabel(value)
            number.setObjectName("CardValue")

            card_layout.addWidget(label)
            card_layout.addWidget(number)

            cards.addWidget(card)

        layout.addLayout(cards)
        layout.addStretch()


class PlaceholderPage(QWidget):
    def __init__(self, title):
        super().__init__()

        layout = QVBoxLayout(self)

        label = QLabel(title)
        label.setAlignment(Qt.AlignCenter)
        label.setObjectName("Title")

        layout.addStretch()
        layout.addWidget(label)
        layout.addStretch()


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("OpenCameraBridge")
        self.resize(1400, 850)

        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        refresh = QAction("Refresh", self)
        toolbar.addAction(refresh)

        settings = QAction("Settings", self)
        toolbar.addAction(settings)

        root = QWidget()
        self.setCentralWidget(root)

        root_layout = QHBoxLayout(root)
        root_layout.setContentsMargins(0, 0, 0, 0)

        self.menu = QListWidget()
        self.menu.setMaximumWidth(220)

        pages = [
            "Dashboard",
            "Cameras",
            "Destinations",
            "Plugins",
            "Settings",
            "About",
        ]

        for page in pages:
            QListWidgetItem(page, self.menu)

        self.content = QWidget()

        self.page_layout = QVBoxLayout(self.content)

        self.dashboard = DashboardPage()

        self.page_layout.addWidget(self.dashboard)

        root_layout.addWidget(self.menu)
        root_layout.addWidget(self.content)

        self.statusBar().showMessage("Ready")

        self.setStyleSheet("""
        QMainWindow{
            background:#202225;
        }

        QWidget{
            background:#202225;
            color:white;
            font-size:10pt;
        }

        QListWidget{
            background:#2B2D31;
            border:none;
            padding:10px;
        }

        QListWidget::item{
            padding:12px;
            border-radius:6px;
        }

        QListWidget::item:selected{
            background:#5865F2;
        }

        QToolBar{
            background:#2B2D31;
            spacing:10px;
        }

        QPushButton{
            background:#5865F2;
            border:none;
            padding:8px;
            border-radius:6px;
        }

        #Title{
            font-size:26px;
            font-weight:bold;
        }

        #Subtitle{
            color:#BBBBBB;
            font-size:12px;
        }

        #Card{
            background:#2B2D31;
            border-radius:10px;
            padding:15px;
            min-height:140px;
        }

        #CardTitle{
            color:#BBBBBB;
        }

        #CardValue{
            font-size:30px;
            font-weight:bold;
        }

        QStatusBar{
            background:#2B2D31;
        }
        """)