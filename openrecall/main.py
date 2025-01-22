import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLineEdit, QPushButton, QLabel, QHBoxLayout,
    QVBoxLayout, QGridLayout, QWidget, QScrollArea, QFrame, QDialog
)
from PyQt5.QtGui import QPixmap, QIcon, QFont, QPalette, QColor
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve

class CreditsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Credits")
        self.setFixedSize(400, 300)
        self.setStyleSheet("background-color: #F4FAFF; border-radius: 10px;")

        layout = QVBoxLayout(self)

        title_label = QLabel("OpenRecall - Credits", self)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #333;")
        title_label.setAlignment(Qt.AlignCenter)

        credits_label = QLabel(
            "Developed by:\nJohn Doe\nJane Smith\n\n" 
            "Icons and Images:\nOpenRecall Team\n\n" 
            "Special Thanks:\nCommunity Support", 
            self
        )
        credits_label.setStyleSheet("font-size: 14px; color: #555;")
        credits_label.setAlignment(Qt.AlignCenter)
        credits_label.setWordWrap(True)

        close_button = QPushButton("Close", self)
        close_button.setFixedSize(100, 40)
        close_button.setStyleSheet(
            "background-color: #256ED1; color: white; border-radius: 10px;"
        )
        close_button.clicked.connect(self.close)

        layout.addWidget(title_label)
        layout.addWidget(credits_label)
        layout.addWidget(close_button, alignment=Qt.AlignCenter)

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
        # Widgets definition

        # Sidebar
        self.sidebar = QWidget(self)
        self.sidebar.setFixedWidth(0)  # Initially hidden
        self.sidebar.setStyleSheet("background-color: #5773A5;border-radius: 10px;")
        self.sidebar_layout = QVBoxLayout(self.sidebar)

        self.close_button = QPushButton("Close Sidebar", self.sidebar)
        self.close_button.setFixedSize(180,40)
        self.close_button.setStyleSheet("background-color:rgb(115, 139, 179); color: white; border-radius: 13px;")

        self.credits_button = QPushButton("Credits", self.sidebar)
        self.credits_button.setFixedSize(180, 40)
        self.credits_button.setStyleSheet("background-color: rgb(115, 139, 179); color: white; border-radius: 13px;")

        self.settings_button = QPushButton('Settings',self.sidebar)
        self.settings_button.setFixedSize(180, 40)
        self.settings_button.setStyleSheet("background-color: rgb(115, 139, 179); color: white; border-radius: 13px;")

        # Logo
        self.logo_label = QLabel(self)
        self.logo_pixmap = QPixmap("openrecall/imgs/logo.png")
        self.logo_label.setPixmap(
            self.logo_pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        )
        self.logo_label.setAlignment(Qt.AlignCenter)

        # Buttons with Toggle Functionality
        self.screenshot_button = QPushButton("SCREENSHOT: ON", self)
        self.screenshot_button.setCheckable(True)
        self.screenshot_button.setFixedSize(150, 40)
        self.screenshot_button.setStyleSheet(
            "background-color: #4772AB; color: white; border-radius: 13px;"
        )

        self.description_button = QPushButton("DESCRIPTION: ON", self)
        self.description_button.setCheckable(True)
        self.description_button.setFixedSize(150, 40)
        self.description_button.setStyleSheet(
            "background-color: #256ED1; color: white; border-radius: 13px;"
        )

        # Search Bar
        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("Type your search here...")
        self.search_bar.setStyleSheet(
            "border: 2px solid #cfe2ff; border-radius: 20px; padding: 10px; font-size: 16px;color: #555;"
        )

        self.search_button = QPushButton(self)
        self.search_button.setIcon(QIcon.fromTheme("search"))
        self.search_button.setFixedSize(40, 40)
        self.search_button.setStyleSheet("background-color: #527fbf; border-radius: 13px;")

        # Placeholder Message
        self.placeholder_message = QLabel("Search for something to see results here.", self)
        self.placeholder_message.setAlignment(Qt.AlignCenter)
        self.placeholder_message.setStyleSheet("font-size: 16px; color: #555; padding: 20px;")

        # Cards Area
        self.card_area = QScrollArea(self)
        self.card_area.setWidgetResizable(True)
        self.card_area.setStyleSheet("background-color: #ffffff; border: none;")
        self.card_area.hide()

        self.card_container = QWidget()
        self.card_layout = QGridLayout(self.card_container)
        self.card_layout.setSpacing(10)
        self.card_area.setWidget(self.card_container)

        # Toggle Sidebar Button
        self.sidebar_button = QPushButton("\u22ee", self)
        self.sidebar_button.setFixedSize(50, 50)
        self.sidebar_button.setStyleSheet(
            "background-color: #256ED1; color: white; border-radius: 15px; font-size: 18px;"
        )

        # Sidebar Animation
        self.sidebar_animation = QPropertyAnimation(self.sidebar, b"maximumWidth")
        self.sidebar_animation.setDuration(300)
        self.sidebar_animation.setEasingCurve(QEasingCurve.InOutQuad)

        self.sidebar_open = False  # Track the state of the sidebar

        # Layout Configuration

        # Sidebar Layout
        self.sidebar_layout.setAlignment(Qt.AlignTop)
        self.sidebar_layout.setSpacing(2)
        
        self.sidebar_layout.addWidget(self.close_button)
        self.sidebar_layout.addWidget(self.credits_button)
        self.sidebar_layout.addWidget(self.settings_button)
        

        # Button Layout
        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignTop)
        button_layout.setSpacing(1)
        button_layout.addStretch(1)
        button_layout.addWidget(self.screenshot_button)
        button_layout.addWidget(self.description_button)
        button_layout.addStretch(1)

        # Search Layout
        search_layout = QHBoxLayout()
        search_layout.addStretch(1)
        search_layout.addWidget(self.search_bar, stretch=5)
        search_layout.addWidget(self.search_button, stretch=1)
        search_layout.addStretch(1)

        # Top Layout
        top_layout = QVBoxLayout()
        top_layout.setAlignment(Qt.AlignTop)
        top_layout.addWidget(self.logo_label, alignment=Qt.AlignCenter)
        top_layout.addLayout(button_layout)
        top_layout.addLayout(search_layout)

        # Central Layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QHBoxLayout(self.central_widget)

        self.central_area = QWidget(self)
        self.central_area.setStyleSheet("background-color: #F4FAFF;")
        self.central_layout = QVBoxLayout(self.central_area)

        self.central_layout.addWidget(self.sidebar_button, alignment=Qt.AlignLeft)
        self.central_layout.addLayout(top_layout)
        self.central_layout.addWidget(self.placeholder_message, alignment=Qt.AlignCenter)
        self.central_layout.addWidget(self.card_area)

        # Main Layout
        self.main_layout.addWidget(self.sidebar)
        self.sidebar.setMaximumWidth(0)  # Set initial width to 0 (hidden)
        self.main_layout.addWidget(self.central_area)

        # Signal Connections
        self.close_button.clicked.connect(self.toggle_sidebar)
        self.screenshot_button.clicked.connect(self.toggle_screenshot)
        self.description_button.clicked.connect(self.toggle_description)
        self.sidebar_button.clicked.connect(self.toggle_sidebar)
        self.search_button.clicked.connect(self.search_action)
        self.credits_button.clicked.connect(self.open_credits)

    def toggle_sidebar(self):
        if self.sidebar_open:
            self.sidebar_animation.setStartValue(300)
            self.sidebar.setFixedWidth(0)
            self.sidebar_animation.setEndValue(0)
        else:
            self.sidebar_animation.setStartValue(0)
            self.sidebar.setFixedWidth(200)
            self.sidebar_animation.setEndValue(300)
            
        self.sidebar_animation.start()
        self.sidebar_open = not self.sidebar_open

    def toggle_screenshot(self):
        self.screenshot_button.setText(
            "SCREENSHOT: OFF" if self.screenshot_button.text() == "SCREENSHOT: ON" else "SCREENSHOT: ON"
        )

    def toggle_description(self):
        self.description_button.setText(
            "DESCRIPTION: OFF" if self.description_button.text() == "DESCRIPTION: ON" else "DESCRIPTION: ON"
        )

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
        image_label.setPixmap(
            QPixmap("openrecall/imgs/logo.png").scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        )
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
    
    def open_credits(self):
        CreditsDialog.__init__(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
