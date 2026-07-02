from PySide6.QtWidgets import QWidget, QGridLayout

from ui.widgets.stat_card import StatCard


class DashboardPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout(self)

        layout.addWidget(StatCard("Connected Cameras", "0"), 0, 0)
        layout.addWidget(StatCard("Upload Targets", "0"), 0, 1)
        layout.addWidget(StatCard("Bridge Status", "Idle"), 0, 2)