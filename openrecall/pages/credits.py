from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

# Credits Dialog
class CreditsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Credits")
        self.setFixedSize(400, 300)
        self.setWindowIcon(QIcon("openrecall/imgs/logo.png"))
        self.setObjectName("CreditsWindow")
        layout = QVBoxLayout(self)

        title_label = QLabel("OpenRecall - Credits", self)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setObjectName("title_label")

        credits_label = QLabel(
            "Developed by: Vinicius Victorelli\n\n" 
            "Logo: rawpixel.com\n\n" 
            "Special Thanks: Community Support\n", 
            self
        )
        credits_label.setAlignment(Qt.AlignCenter)
        credits_label.setWordWrap(True)
        credits_label.setObjectName("credits_label")

        close_button = QPushButton("Close", self)
        close_button.setFixedSize(100, 40)
        close_button.setObjectName("close_button")
        close_button.clicked.connect(self.close)

        layout.addWidget(title_label)
        layout.addWidget(credits_label)
        layout.addWidget(close_button, alignment=Qt.AlignCenter)
        
