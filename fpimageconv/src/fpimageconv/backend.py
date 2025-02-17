from PIL import Image, UnidentifiedImageError
from PIL.Image import Image as image
from enum import Enum
import logging
class State(Enum):
    EMPTY    = 0
    READY    = 1
    WARNING  = 2
    ERROR    = 3
    COMPLETE = 4
    
class Converter():
    def __init__(self, logger: logging.Logger):
        self.img:    Image          = None
        self.msg:    str            = "Ready" 
        self.state:  int            = State.EMPTY
        self.logger: logging.Logger = logger
    
    def open_image(self, file_path: str, mode: str = 'r') -> None:
        try:
            self.img   = Image.open(file_path, mode)
            self.msg   = f"got image: {file_path}"
            self.validate_image()
        except FileNotFoundError:
            self.msg   = f"Error: file {file_path} not found"
            self.state = State.ERROR
            self.logger.error(f"image not found: {file_path}")
        except UnidentifiedImageError:
            self.msg   = f"Error: {file_path}\ncan not be opened or identified"
            self.state = State.ERROR
            self.logger.error(f"Error: {file_path} can not be opened or identified")
        except Exception as e:
            self.logger.error(f"Unknown error: {e.with_traceback}")
            raise e.add_note("Unknown error")
            
    def validate_image(self) -> bool:
        if self.img and self.img.width == 896 and self.img.height == 448:
            self.state = State.READY
            return True 
        self.state = State.WARNING
        return False
    
    def convert_image(self, save_path: str) -> None:
        try:
            converted = self.img.convert("P", palette=Image.ADAPTIVE, colors=8)
            self.msg = f"Successfully converted file: {save_path}\\fruitpeel.png"
            self.state = State.COMPLETE 
            converted.save(save_path + r'\fruitpeel.png')
        except OSError:
            self.state = State.ERROR
            self.msg = f"Error: couldn't save file: {save_path}\\fruitpeel.png"
        
        
    def exit(self) -> None:
        if self.img:
            self.img.close()