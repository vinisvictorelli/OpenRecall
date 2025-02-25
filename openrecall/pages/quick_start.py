from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QHBoxLayout, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from openrecall.config.config_loader import update_config,load_config

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
        selector_model_selection.addItem("Automatic")
        selector_model_selection.addItem("minicpm-v")
        selector_model_selection.addItem("llava")
        selector_model_selection.addItem("llava-llama3")
        selector_model_selection.addItem("moondream")
        selector_model_selection.addItem("bakllava")
        selector_model_selection.addItem("llava-phi3")
        
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

        #Auto screenshot on or off
        layout_auto_screenshot = QHBoxLayout(self)
        layout_auto_screenshot.setAlignment(Qt.AlignCenter)
        label_auto_screenshot = QLabel("Activate screenshot",self)
        label_auto_screenshot.setObjectName("label_auto_screenshot")
        label_auto_screenshot.setAlignment(Qt.AlignCenter)
        selector_auto_screenshot = QComboBox()
        selector_auto_screenshot.setObjectName("selector_auto_screenshot")
        selector_auto_screenshot.addItem("ON")
        selector_auto_screenshot.addItem("OFF")
        layout_auto_screenshot.addWidget(label_auto_screenshot)
        layout_auto_screenshot.addWidget(selector_auto_screenshot)

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
        layout.addLayout(layout_auto_screenshot)
        layout.addLayout(layout_close_button)

        #Action
        apply_button.clicked.connect(lambda: self.apply_config(
            selector_model_selection.currentText(),
            selector_interval_screenshot.currentText(),
            selector_send_description.currentText(),
            selector_auto_screenshot.currentText()))
    
    def apply_config(self,selector_model_selection,selector_interval_screenshot,selector_send_description,selector_auto_screenshot):
        config = load_config()
        update_config(config,
            {"settings": 
             {"model": selector_model_selection,
              "interval_screenshot": selector_interval_screenshot,
              "send_description": selector_send_description,
              "auto_screenshot": selector_auto_screenshot}}
        )