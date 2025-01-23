import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLineEdit, QPushButton, QLabel, QHBoxLayout,
    QVBoxLayout, QGridLayout, QWidget, QScrollArea, QFrame, QStackedWidget
)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve

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
            "Developed by: Vinicius Victorelli\n" 
            "Logo: rawpixel.com\n" 
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

#Settings Window
class Settings(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Settings")
        self.setFixedSize(400, 300)
        self.setWindowIcon(QIcon("openrecall/imgs/logo.png"))
        self.setObjectName("SettingsWindow")
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)

        title_label = QLabel("Settings", self)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setObjectName("title_label")

        # Logo
        self.logo_label = QLabel(self)
        self.logo_pixmap = QPixmap("openrecall/imgs/logo.png")
        self.logo_label.setPixmap(
            self.logo_pixmap.scaled(50, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        )
        self.logo_label.setAlignment(Qt.AlignCenter)
        self.logo_label.setObjectName('logo_label')


        # Buttons with Toggle Functionality
        self.screenshot_button = QPushButton("SCREENSHOT: ON", self)
        self.screenshot_button.setCheckable(True)
        self.screenshot_button.setFixedSize(150, 40)
        self.screenshot_button.setObjectName('screenshot_button')

        self.description_button = QPushButton("DESCRIPTION: ON", self)
        self.description_button.setCheckable(True)
        self.description_button.setFixedSize(150, 40)
        self.description_button.setObjectName('description_button')

        close_button = QPushButton("Close", self)
        close_button.setFixedSize(100, 40)
        close_button.setObjectName("close_button")
        
        layout.addWidget(title_label)
        layout.addWidget(self.logo_label)
        layout.addWidget(self.screenshot_button)
        layout.addWidget(self.description_button)
        layout.addWidget(close_button)
        

        #Signals
        self.screenshot_button.clicked.connect(self.toggle_screenshot)
        self.description_button.clicked.connect(self.toggle_description)
        close_button.clicked.connect(self.close)
    
    def toggle_screenshot(self):
        self.screenshot_button.setText(
            "SCREENSHOT: OFF" if self.screenshot_button.text() == "SCREENSHOT: ON" else "SCREENSHOT: ON"
        )

    def toggle_description(self):
        self.description_button.setText(
            "DESCRIPTION: OFF" if self.description_button.text() == "DESCRIPTION: ON" else "DESCRIPTION: ON"
        )
# Main Window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.credit_window = CreditsWindow()
        self.settings_window = Settings()
        self.setWindowTitle("OpenRecall")
        self.setGeometry(50, 50, 1280, 720)

        # Set the window icon to the logo
        self.setWindowIcon(QIcon("openrecall/imgs/logo.png"))

        self.initUI()

    def initUI(self):
        # Widgets definition

        # Sidebar
        self.sidebar = QWidget(self)
        self.sidebar.setFixedWidth(0)  # Initially hidden
        self.sidebar.setObjectName("sidebar")
        self.sidebar_layout = QVBoxLayout(self.sidebar)

        self.credits_button = QPushButton("Credits", self.sidebar)
        self.credits_button.setFixedSize(180, 40)
        self.credits_button.setObjectName('credits_button')

        self.settings_button = QPushButton('Settings', self.sidebar)
        self.settings_button.setFixedSize(180, 40)
        self.settings_button.setObjectName('settings_button')


        # Search Bar
        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("Type your search here...")
        self.search_bar.setObjectName('search_bar')

        self.search_button = QPushButton(self)
        self.search_button.setIcon(QIcon.fromTheme("search"))
        self.search_button.setFixedSize(40, 40)
        self.search_button.setObjectName('search_button')

        # Placeholder Message
        self.placeholder_message = QLabel("Search for something to see results here.", self)
        self.placeholder_message.setAlignment(Qt.AlignCenter)
        self.placeholder_message.setObjectName('placeholder_message')

        # Cards Area
        self.card_area = QScrollArea(self)
        self.card_area.setWidgetResizable(True)
        self.card_area.setObjectName('card_area')
        self.card_area.hide()

        self.card_container = QWidget()
        self.card_container.setObjectName('card_container')
        self.card_layout = QGridLayout(self.card_container)
        self.card_layout.setSpacing(10)
        self.card_area.setWidget(self.card_container)

        # Toggle Sidebar Button
        self.sidebar_button = QPushButton("\u22ee", self)
        self.sidebar_button.setFixedSize(50, 50)
        self.sidebar_button.setObjectName('sidebar_button')

        # Sidebar Animation
        self.sidebar_animation = QPropertyAnimation(self.sidebar, b"maximumWidth")
        self.sidebar_animation.setObjectName('sidebar_animation')
        self.sidebar_animation.setDuration(300)
        self.sidebar_animation.setEasingCurve(QEasingCurve.InOutQuad)

        self.sidebar_open = False  # Track the state of the sidebar

        # Layout Configuration

        # Sidebar Layout
        self.sidebar_layout.setAlignment(Qt.AlignTop)
        self.sidebar_layout.setSpacing(2)
        self.sidebar_layout.addWidget(self.credits_button)
        self.sidebar_layout.addWidget(self.settings_button)
        
        # Search Layout
        search_layout = QHBoxLayout()
        search_layout.setAlignment(Qt.AlignCenter)
        search_layout.setObjectName('search_layout')
        search_layout.addStretch(1)
        search_layout.addWidget(self.search_bar, stretch=5)
        search_layout.addWidget(self.search_button, stretch=1)
        search_layout.addStretch(1)


        # Central Layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QHBoxLayout(self.central_widget)

        self.central_area = QWidget(self)
        self.central_area.setObjectName('central_area')
        self.central_layout = QVBoxLayout(self.central_area)
        self.central_layout.setObjectName('central_layout')
        self.central_layout.setAlignment(Qt.AlignTop)

        self.central_layout.addWidget(self.sidebar_button, alignment=Qt.AlignLeft)
        self.central_layout.addLayout(search_layout)
        self.central_layout.addSpacing(5)
        self.central_layout.addWidget(self.placeholder_message, alignment=Qt.AlignCenter)
        self.central_layout.addWidget(self.card_area)

        # Main Layout
        self.main_layout.addWidget(self.sidebar)
        self.sidebar.setMaximumWidth(0)  # Set initial width to 0 (hidden)
        self.main_layout.addWidget(self.central_area)

        # Signal Connections
        self.sidebar_button.clicked.connect(self.toggle_sidebar)
        self.search_button.clicked.connect(self.search_action)
        self.credits_button.clicked.connect(self.open_credits)
        self.settings_button.clicked.connect(self.open_settings)

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

        for i in range(10):
            card = self.create_card(f"Result {i + 1}", f"Description for result {i + 1}.")
            self.card_layout.addWidget(card, i // 2, i % 2)

    def create_card(self, title, description):
        card = QFrame(self)
        card_layout = QVBoxLayout(card)

        image_label = QLabel(self)
        image_label.setPixmap(
            QPixmap("openrecall/imgs/logo.png").scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        )
        image_label.setAlignment(Qt.AlignCenter)

        title_label = QLabel(title, self)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setObjectName('title_label')

        description_label = QLabel(description, self)
        description_label.setObjectName('description_label')
        description_label.setWordWrap(True)
        description_label.setAlignment(Qt.AlignCenter)

        card_layout.addWidget(image_label)
        card_layout.addWidget(title_label)
        card_layout.addWidget(description_label)

        return card
    
    def open_credits(self):
        self.credit_window.show()

    def open_settings(self):
        self.settings_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    with open("openrecall/style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)
    sys.exit(app.exec_())
