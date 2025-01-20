import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLineEdit, QPushButton, QLabel, QHBoxLayout,
    QVBoxLayout, QGridLayout, QWidget, QScrollArea, QFrame, QSizePolicy
)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OpenRecall")
        self.setGeometry(50, 50, 1280, 720)
        self.setStyleSheet("background-color: #F4FAFF;")

        # Set the window icon to the logo
        self.setWindowIcon(QIcon("openrecall/imgs/logo.png"))

        self.initUI()

    def initUI(self):
        # Main layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QHBoxLayout(self.central_widget)

        # Sidebar
        self.sidebar = QWidget(self)
        self.sidebar.setFixedWidth(0)  # Initially hidden
        self.sidebar.setStyleSheet("background-color: #ECEFF4;")
        self.sidebar_layout = QVBoxLayout(self.sidebar)
        self.sidebar.setLayout(self.sidebar_layout)

        close_button = QPushButton("Close Sidebar", self.sidebar)
        close_button.clicked.connect(self.toggle_sidebar)
        self.sidebar_layout.addWidget(close_button)

        # Central area
        self.central_area = QWidget(self)
        self.central_area.setStyleSheet("background-color: #F4FAFF;")
        self.central_layout = QVBoxLayout(self.central_area)

        # Logo
        logo_label = QLabel(self)
        logo_pixmap = QPixmap("openrecall/imgs/logo.png")
        logo_label.setPixmap(logo_pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        logo_label.setAlignment(Qt.AlignCenter)

        # Buttons with Toggle Functionality
        self.screenshot_button = QPushButton("SCREENSHOT: ON", self)
        self.screenshot_button.setCheckable(True)
        self.screenshot_button.setFixedSize(150, 40)
        self.screenshot_button.clicked.connect(self.toggle_screenshot)
        self.screenshot_button.setStyleSheet("background-color: #4772AB; color: white; border-radius: 13px;")

        self.description_button = QPushButton("DESCRIPTION: ON", self)
        self.description_button.setCheckable(True)
        self.description_button.setFixedSize(150, 40)
        self.description_button.clicked.connect(self.toggle_description)
        self.description_button.setStyleSheet("background-color: #256ED1; color: white; border-radius: 13px;")

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

        # Toggle Sidebar Button
        self.sidebar_button = QPushButton("⋮", self)
        self.sidebar_button.setFixedSize(50, 50)
        self.sidebar_button.setStyleSheet(
            "background-color: #256ED1; color: white; border-radius: 25px; font-size: 18px;"
        )
        self.sidebar_button.clicked.connect(self.toggle_sidebar)

        # Add items to central layout
        self.central_layout.addWidget(logo_label, alignment=Qt.AlignCenter)
        self.central_layout.addWidget(self.sidebar_button, alignment=Qt.AlignLeft)

        # Add central and sidebar to the main layout
        self.main_layout.addWidget(self.sidebar)
        self.main_layout.addWidget(self.central_area)

        # Animation
        self.sidebar_animation = QPropertyAnimation(self.sidebar, b"maximumWidth")
        self.sidebar_animation.setDuration(300)
        self.sidebar_animation.setEasingCurve(QEasingCurve.InOutQuad)

        self.sidebar_open = False  # Track the state of the sidebar

         # Main Layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(top_layout, stretch=1)
        main_layout.addWidget(self.placeholder_message, stretch=1)
        main_layout.addWidget(self.card_area, stretch=5)

        # Central Widget
        central_widget = QWidget()
        central_widget.setLayout(main_layout)

        # Add sidebar button to main layout
        layout_with_sidebar_button = QVBoxLayout()
        layout_with_sidebar_button.addWidget(self.sidebar_button, alignment=Qt.AlignRight)
        layout_with_sidebar_button.addWidget(central_widget)

        container = QWidget()
        container.setLayout(layout_with_sidebar_button)
        self.setCentralWidget(container)

    def toggle_sidebar(self):
        if self.sidebar_open:
            # Animate to hide the sidebar
            self.sidebar_animation.setStartValue(200)  # Fully visible width
            self.sidebar_animation.setEndValue(0)  # Hidden width
        else:
            # Animate to show the sidebar
            self.sidebar_animation.setStartValue(0)  # Hidden width
            self.sidebar_animation.setEndValue(200)  # Fully visible width

        self.sidebar_animation.start()
        self.sidebar_open = not self.sidebar_open

    def toggle_screenshot(self):
        if self.screenshot_button.text() == "SCREENSHOT: ON":
            self.screenshot_button.setText("SCREENSHOT: OFF")
        else:
            self.screenshot_button.setText("SCREENSHOT: ON")

    def toggle_description(self):
        if self.description_button.text() == "DESCRIPTION: ON":
            self.description_button.setText("DESCRIPTION: OFF")
        else:
            self.description_button.setText("DESCRIPTION: ON")

    def search_action(self):
        query = self.search_bar.text().strip()

        if not query:
            return

        self.placeholder_message.hide()
        self.card_area.show()

        for i in reversed(range(self.card_layout.count())):
            widget = self.card_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        for i in range(6):
            card = self.create_card(f"Result {i + 1}", f"Description for result {i + 1}.")
            self.card_layout.addWidget(card, i // 2, i % 2)

    def create_card(self, title, description):
        card = QFrame(self)
        card.setStyleSheet(
            "background-color: #f9f9f9; border: 1px solid #dcdcdc; border-radius: 10px; padding: 10px;"
        )
        card_layout = QVBoxLayout(card)

        image_label = QLabel(self)
        image_label.setPixmap(QPixmap("openrecall/imgs/logo.png").scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
