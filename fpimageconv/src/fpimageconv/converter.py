from PIL import Image, UnidentifiedImageError
from PIL.Image import Image as image
from enum import Enum
from logging import basicConfig, Logger

class State(Enum):
    EMPTY    = 0
    READY    = 1
    WARNING  = 2
    ERROR    = 3
    COMPLETE = 4
    
class Converter():
    def __init__(self):
        self.img:   Image = None
        self.msg:   str   = "Готов" 
        self.state: int   = State.EMPTY
    
    def open_image(self, file_path: str, mode: str = 'r') -> image:
        try:
            self.img   = Image.open(file_path, mode)
            self.state = State.READY
        except FileNotFoundError:
            self.msg   = "Ошибка: файл " + file_path +  " не найден"
            self.state = State.ERROR
        except UnidentifiedImageError:
            self.msg   = "Ошибка: {file_path} не может быть открыт или не является изображением"
            self.state = State.ERROR
        except Exception as e:
            raise e.add_note("Неизвестная ошибка")
            
    def validate_image(self) -> bool:
        if self.img and self.img.width == 896 and self.img.height == 448:
            return True 
        self.state = State.WARNING
        return False
    
    def convert_image(self, save_path: str) -> None:
        converted = self.img.convert("P", palette=Image.ADAPTIVE, colors=8) 
        converted.save(save_path + r'\fruitpeel.png')
        
    def exit(self) -> None:
        if self.img:
            self.img.close()
        
            
            

if __name__ == "__main__":
    main()