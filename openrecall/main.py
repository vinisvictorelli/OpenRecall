import sys
from os import listdir
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLineEdit, QPushButton, QLabel, QHBoxLayout,
    QVBoxLayout, QGridLayout, QWidget, QScrollArea, QFrame, QComboBox
)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve
from PyQt5 import QtCore
from openrecall.config.config_loader import update_config,load_config

CONFIG_FILE = "openrecall/config/config.json"

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
        
#Settings Window
class Settings(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Settings")
        self.setFixedSize(600, 400)
        self.setWindowIcon(QIcon("openrecall/imgs/settings.png"))
        self.setObjectName("SettingsWindow")
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)

        # Logo
        self.logo_label = QLabel(self)
        self.logo_pixmap = QPixmap("openrecall/imgs/settings.png")
        self.logo_label.setPixmap(
            self.logo_pixmap.scaled(50, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        )
        self.logo_label.setAlignment(Qt.AlignCenter)
        self.logo_label.setObjectName('logo_label')

        title_label = QLabel("Settings", self)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setObjectName("title_settings")

        # Buttons with Toggle Functionality
        screenshot_layout = QHBoxLayout(self)
        screenshot_layout.setAlignment(Qt.AlignCenter)
        self.screenshot_label = QLabel('Activate auto screenshot',self)
        self.screenshot_label.setObjectName('screenshot_label')
        self.screenshot_button = QPushButton("SCREENSHOT: ON", self)
        self.screenshot_button.setCheckable(True)
        self.screenshot_button.setFixedSize(150, 40)
        self.screenshot_button.setObjectName('screenshot_button')
        screenshot_layout.addWidget(self.screenshot_label)
        screenshot_layout.addWidget(self.screenshot_button)

        # Option to choose de amount of images send to description
        description_layout = QHBoxLayout(self)
        description_layout.setAlignment(Qt.AlignCenter)
        self.description_label = QLabel('Choose the amount of images to be sent to llm for description')
        self.description_label.setObjectName('screenshot_label')
        self.description_label.setWordWrap(True)
        self.description_button = QLineEdit(self)
        self.description_button.setFixedSize(150, 40)
        self.description_button.setObjectName('description_button')
        description_layout.addWidget(self.description_label)
        description_layout.addWidget(self.description_button)

        close_button = QPushButton("Close", self)
        close_button.setFixedSize(100, 40)
        close_button.setObjectName("close_button")

        layout.addWidget(self.logo_label)
        layout.addWidget(title_label)
        layout.addLayout(screenshot_layout)
        layout.addLayout(description_layout)
        layout.addWidget(close_button)

        #Signals
        self.screenshot_button.clicked.connect(self.toggle_screenshot)
        close_button.clicked.connect(self.close)
    
    def toggle_screenshot(self):
        self.screenshot_button.setText(
            "SCREENSHOT: OFF" if self.screenshot_button.text() == "SCREENSHOT: ON" else "SCREENSHOT: ON"
        )

    def toggle_description(self):
        self.description_button.setText(
            "DESCRIPTION: OFF" if self.description_button.text() == "DESCRIPTION: ON" else "DESCRIPTION: ON"
        )

class QuickStartWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QuickStart")
        self.setFixedSize(600, 350)
        # Set the window icon to the logo
        self.setWindowIcon(QIcon("openrecall/imgs/quickstart.png"))
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setObjectName('QuickStartWindow')
        #Main Layout
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        layout.setAlignment(Qt.AlignTop)
        #Title Layout
        label_title = QLabel("Quick Start",self)
        label_title.setObjectName("label_title")
        label_title.setAlignment(Qt.AlignCenter)
        label_description = QLabel("Configure the essential settings required\n for the application to function properly.",self)
        label_description.setObjectName("label_description")
        label_description.setAlignment(Qt.AlignCenter)
        #Send description - AUTO OR MANUAL - Configuration Layout
        layout_send_description = QHBoxLayout(self)
        layout_send_description.setAlignment(Qt.AlignCenter)
        label_send_description = QLabel("Send images to generate AI descriptions",self)
        label_send_description.setObjectName("label_send_description")
        label_send_description.setAlignment(Qt.AlignCenter)
        selector_send_description = QComboBox(self)
        selector_send_description.setObjectName("selector_send_description")
        selector_send_description.addItem("Automatic")
        selector_send_description.addItem("Manual")
        layout_send_description.addWidget(label_send_description)
        layout_send_description.addWidget(selector_send_description)

        #Model Selection - Select the model to be used
        layout_model_selection = QHBoxLayout(self)
        layout_model_selection.setAlignment(Qt.AlignCenter)
        label_model_selection = QLabel("Select an LLM model to generate a detailed description",self)
        label_model_selection.setObjectName("label_model_selection")
        label_model_selection.setAlignment(Qt.AlignCenter)
        selector_model_selection = QComboBox(self)
        selector_model_selection.setObjectName("selector_model_selection")
        selector_model_selection.addItem("minicpm-v")
        selector_model_selection.addItem("other model")
        layout_model_selection.addWidget(label_model_selection)
        layout_model_selection.addWidget(selector_model_selection)

        #Interval between Screenshot - 30 - 60 or AUTO
        layout_interval_screenshot = QHBoxLayout(self)
        layout_interval_screenshot.setAlignment(Qt.AlignCenter)
        label_interval_screenshot = QLabel("Interval between screenshots before capturing a new one",self)
        label_interval_screenshot.setObjectName("label_interval_screenshot")
        label_interval_screenshot.setAlignment(Qt.AlignCenter)
        selector_interval_screenshot = QComboBox()
        selector_interval_screenshot.setObjectName("selector_interval_screenshot")
        selector_interval_screenshot.addItem("AUTO")
        selector_interval_screenshot.addItem("30s")
        selector_interval_screenshot.addItem("60s")
        layout_interval_screenshot.addWidget(label_interval_screenshot)
        layout_interval_screenshot.addWidget(selector_interval_screenshot)

        #Close button
        layout_close_button = QHBoxLayout(self)
        layout_close_button.setAlignment(Qt.AlignCenter)
        close_button = QPushButton("Close", self)
        close_button.setFixedSize(80, 40)
        close_button.setObjectName("close_button")
        close_button.clicked.connect(self.close)
        apply_button = QPushButton("Apply", self)
        apply_button.setFixedSize(80, 40)
        apply_button.setObjectName("apply_button")
        layout_close_button.addWidget(close_button)
        layout_close_button.addWidget(apply_button)
            
        #Main Layout Configuration
        layout.addWidget(label_title)
        layout.addWidget(label_description)
        layout.addLayout(layout_send_description)
        layout.addLayout(layout_model_selection)
        layout.addLayout(layout_interval_screenshot)
        layout.addLayout(layout_close_button)

        #Action
        apply_button.clicked.connect(lambda: self.apply_config(
            selector_model_selection.currentText(),
            selector_interval_screenshot.currentText(),
            selector_send_description.currentText(),))
    
    def apply_config(self,selector_model_selection,selector_interval_screenshot,selector_send_description):
        config = load_config()
        update_config(config,
            {"settings": 
             {"model": selector_model_selection,
              "interval_screenshot": selector_interval_screenshot,
              "send_description": selector_send_description}}
        )

# Main Window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.quick_window = QuickStartWindow()
        self.credit_window = CreditsWindow()
        self.settings_window = Settings()
        self.setWindowTitle("OpenRecall")
        self.setGeometry(50, 50, 1280, 720)
        self.quick_window.show()

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
        self.search_button.setIcon(QIcon('openrecall/imgs/search.png'))
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
    with open("openrecall/style.css", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)
    sys.exit(app.exec_())
