from backend import Converter
import sys
from PySide6.QtWidgets import QApplication
import logging
from frontend import ImageConverterApp

def setup_logger() -> logging.Logger:
    imgconv_logger = logging.getLogger(__name__)
    imgconv_logger.setLevel(logging.INFO)
    
    handler = logging.FileHandler(f"{__name__}.log", mode='w')
    formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

    handler.setFormatter(formatter)
    imgconv_logger.addHandler(handler)
    
    return imgconv_logger


if __name__ == "__main__":
    logger = setup_logger()
    logger.info("Service started")
    conv = Converter(logger)
    logger.info("Converter started")
    app = QApplication(sys.argv)
    window = ImageConverterApp(logger, conv)
    window.show()
    logger.info("App started")
    
    sys.exit(app.exec())