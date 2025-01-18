import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLineEdit, QPushButton, QLabel, QHBoxLayout,
    QVBoxLayout, QGridLayout, QWidget, QScrollArea, QFrame, QSizePolicy
)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OpenRecall")
        self.setGeometry(50, 50, 1280, 720)
        self.setStyleSheet("background-color: #F4FAFF;")

        # Set the window icon to the logo
        self.setWindowIcon(QIcon("src/imgs/logo.png"))

        self.initUI()

    def initUI(self):
        # Logo
        logo_label = QLabel(self)
        logo_pixmap = QPixmap("src/imgs/logo.png")
        logo_label.setPixmap(logo_pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        logo_label.setAlignment(Qt.AlignCenter)

        # Buttons with Toggle Functionality
        self.screenshot_button = QPushButton("SCREENSHOT: ON", self)
        self.screenshot_button.setCheckable(True)
        self.screenshot_button.setFixedSize(150,40)  # Altura fixa
        self.screenshot_button.clicked.connect(self.toggle_screenshot)
        self.screenshot_button.setStyleSheet("background-color: #4772AB; color: white; border-radius: 13px;")
        self.screenshot_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.description_button = QPushButton("DESCRIPTION: ON", self)
        self.description_button.setCheckable(True)
        self.description_button.setFixedSize(150,40)  # Altura fixa
        self.description_button.clicked.connect(self.toggle_description)
        self.description_button.setStyleSheet("background-color: #256ED1; color: white; border-radius: 13px;")
        self.description_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignCenter)
        button_layout.setSpacing(10)
        button_layout.addStretch(1)
        button_layout.addWidget(self.screenshot_button)
        button_layout.addWidget(self.description_button)
        button_layout.addStretch(1)

        # Search Bar
        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("Type your search here...")
        self.search_bar.setStyleSheet(
            "border: 2px solid #cfe2ff; border-radius: 20px; padding: 10px; font-size: 16px;color: #555;"
        )
        self.search_bar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        search_button = QPushButton(self)
        search_button.setIcon(QIcon.fromTheme("search"))
        search_button.setFixedSize(40, 40)
        search_button.setStyleSheet("background-color: #527fbf; border-radius: 13px;")
        search_button.clicked.connect(self.search_action)

        search_layout = QHBoxLayout()
        search_layout.addStretch(1)
        search_layout.addWidget(self.search_bar, stretch=5)
        search_layout.addWidget(search_button, stretch=1)
        search_layout.addStretch(1)

        # Top Layout (Logo, Buttons, Search Bar)
        top_layout = QVBoxLayout()
        top_layout.setAlignment(Qt.AlignTop)
        top_layout.addWidget(logo_label, alignment=Qt.AlignCenter)
        top_layout.addLayout(button_layout)
        top_layout.addLayout(search_layout)

        # Placeholder Message
        self.placeholder_message = QLabel("Search for something to see results here.", self)
        self.placeholder_message.setAlignment(Qt.AlignCenter)
        self.placeholder_message.setStyleSheet("font-size: 16px; color: #555; padding: 20px;")

        # Cards Area (initially hidden)
        self.card_area = QScrollArea(self)
        self.card_area.setWidgetResizable(True)
        self.card_area.setStyleSheet("background-color: #ffffff; border: none;")
        self.card_area.hide()

        self.card_container = QWidget()
        self.card_layout = QGridLayout(self.card_container)
        self.card_layout.setSpacing(10)
        self.card_area.setWidget(self.card_container)

        # Main Layout (Combine top and bottom)
        main_layout = QVBoxLayout()
        main_layout.addLayout(top_layout, stretch=1)
        main_layout.addWidget(self.placeholder_message, stretch=1)
        main_layout.addWidget(self.card_area, stretch=5)

        # Central Widget
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def create_card(self, title, description):
        """Create a single card widget."""
        card = QFrame(self)
        card.setStyleSheet(
            "background-color: #f9f9f9; border: 1px solid #dcdcdc; border-radius: 10px; padding: 10px;"
        )
        card_layout = QVBoxLayout(card)

        image_label = QLabel(self)
        image_label.setPixmap(QPixmap("src/imgs/logo.png").scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        image_label.setAlignment(Qt.AlignCenter)

        title_label = QLabel(title, self)
        title_label.setStyleSheet("font-weight: bold; font-size: 14px; color: #333;")
        title_label.setAlignment(Qt.AlignCenter)

        description_label = QLabel(description, self)
        description_label.setStyleSheet("font-size: 12px; color: #555;")
        description_label.setWordWrap(True)
        description_label.setAlignment(Qt.AlignCenter)

        card_layout.addWidget(image_label)
        card_layout.addWidget(title_label)
        card_layout.addWidget(description_label)

        return card

    def toggle_screenshot(self):
        if self.screenshot_button.text() == "SCREENSHOT: ON":
            self.screenshot_button.setText("SCREENSHOT: OFF")
            self.screenshot_button.setStyleSheet("background-color: #ff6666; color: white; border-radius: 13px; padding: 5px;")
        else:
            self.screenshot_button.setText("SCREENSHOT: ON")
            self.screenshot_button.setStyleSheet("background-color: #4772AB; color: white; border-radius: 13px; padding: 5px;")

    def toggle_description(self):
        if self.description_button.text() == "DESCRIPTION: ON":
            self.description_button.setText("DESCRIPTION: OFF")
            self.description_button.setStyleSheet("background-color: #ff6666; color: white; border-radius: 13px; padding: 5px;")
        else:
            self.description_button.setText("DESCRIPTION: ON")
            self.description_button.setStyleSheet("background-color: #256ED1; color: white; border-radius: 13px; padding: 5px;")

    def search_action(self):
        query = self.search_bar.text().strip()

        if not query:
            return  # Do nothing if search bar is empty

        # Remove placeholder message and show card area
        self.placeholder_message.hide()
        self.card_area.show()

        # Clear existing cards
        for i in reversed(range(self.card_layout.count())):
            widget = self.card_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        # Populate with new cards (example results)
        for i in range(6):  # Replace with actual search results
            card = self.create_card(f"Result {i + 1}", f"Description for result {i + 1}.")
            self.card_layout.addWidget(card, i // 2, i % 2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
