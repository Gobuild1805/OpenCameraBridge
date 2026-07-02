from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout


class StatCard(QFrame):
    def __init__(self, title: str, value: str):
        super().__init__()

        self.setObjectName("Card")

        layout = QVBoxLayout(self)

        title_label = QLabel(title)
        title_label.setObjectName("CardTitle")

        value_label = QLabel(value)
        value_label.setObjectName("CardValue")

        layout.addWidget(title_label)
        layout.addWidget(value_label)