from backend import Converter, State
from PySide6.QtWidgets import QMainWindow, QFileDialog
from mainwindow import Ui_MainWindow
import logging
class ImageConverterApp(QMainWindow):
    def __init__(self, logger: logging.Logger, converter: Converter):
        super(ImageConverterApp, self).__init__()
        self.converter: Converter = converter
        self.ui: Ui_MainWindow = Ui_MainWindow() 
        self.ui.setupUi(self)
        self.change_state_text(self.converter.state)
        self.ui.convert_btn.setEnabled(False)
        self.ui.select_file_btn.clicked.connect(self.select_file_callback)
        self.ui.select_file_btn_2.clicked.connect(self.select_save_path_callback)
        self.ui.convert_btn.clicked.connect(self.convert_callback)
        
        self.logger: logging.Logger = logger
        self.logger.info("App initialized")
        self.savepath = ""
        self.filepath = ""
        
    def select_file_callback(self) -> None:
        self.filepath: str = QFileDialog.getOpenFileName(self, 'Choose image', filter="Image Files (*.png *.jpg *.bmp)")[0]
        self.logger.info(f"got filepath: {self.filepath}")
        
        self.ui.select_filepath.setText(self.filepath)
        self.converter.open_image(self.filepath)
        
        if self.converter.state == State.ERROR:
            self.logger.error(self.converter.msg)
        else:
            self.logger.info(self.converter.msg)
            
        self.change_state_text(self.converter.state)
        if self.savepath and self.converter.state == State.READY:
            self.ui.convert_btn.setEnabled(True)
        else:
            self.ui.convert_btn.setEnabled(False)

        
    def select_save_path_callback(self) -> None:
        self.savepath: str = QFileDialog.getExistingDirectory(self, 'Choose directory')
        self.logger.info(f"got savepath: {self.savepath}")
        self.ui.save_filepath.setText(self.savepath)
        if self.savepath and self.converter.state == State.READY:
            self.ui.convert_btn.setEnabled(True)
        else:
            self.ui.convert_btn.setEnabled(False)
            
            
    def convert_callback(self) -> None:
        self.converter.convert_image(self.savepath)
        self.change_state_text(self.converter.state)
        
        if self.converter.state == State.ERROR:
            self.logger.error(self.converter.msg)
        else:
            self.logger.info(self.converter.msg)
            
        self.ui.convert_btn.setEnabled(False)
        self.filepath = ""

    def change_state_text(self, state: State) -> None:
        match state:
            case State.EMPTY:
                self.ui.state_label_2.setText(u"Converter is empty")
                self.ui.state_label_2.setStyleSheet(u"QLabel#state_label_2 {\n"
                                                    "color: black;\n"
                                                    "border: 2px solid #8f8f91;\n"
                                                    "border-radius: 4px;\n"
                                                    "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                                    "stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
                                                    "min-width: 460px;\n"
                                                    "}")    
            case State.READY:
                self.ui.state_label_2.setText(u"Converter is ready")
                self.ui.state_label_2.setStyleSheet(u"QLabel#state_label_2 {\n"
                                                    "color: green;\n"
                                                    "border: 2px solid #8f8f91;\n"
                                                    "border-radius: 4px;\n"
                                                    "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                                    "stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
                                                    "min-width: 460px;\n"
                                                    "}")  
            case State.WARNING:
                self.ui.state_label_2.setText(u"Image is not 896x448. Crop image before convering.")
                self.ui.state_label_2.setStyleSheet(u"QLabel#state_label_2 {\n"
                                                    "color: orange;\n"
                                                    "border: 2px solid #8f8f91;\n"
                                                    "border-radius: 4px;\n"
                                                    "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                                    "stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
                                                    "min-width: 460px;\n"
                                                    "}")  
            case State.ERROR:
                self.ui.state_label_2.setText(self.converter.msg)
                self.ui.state_label_2.setStyleSheet(u"QLabel#state_label_2 {\n"
                                                    "color: red;\n"
                                                    "border: 2px solid #8f8f91;\n"
                                                    "border-radius: 4px;\n"
                                                    "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                                    "stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
                                                    "min-width: 460px;\n"
                                                    "}")  
            case State.COMPLETE:
                self.ui.state_label_2.setText(u"Image converted and saved")
                self.ui.state_label_2.setStyleSheet(u"QLabel#state_label_2 {\n"
                                                    "color: cyan;\n"
                                                    "border: 2px solid #8f8f91;\n"
                                                    "border-radius: 4px;\n"
                                                    "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                                    "stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
                                                    "min-width: 460px;\n"
                                                    "}")     