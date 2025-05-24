# Fruitpeel Image Converter
Converts images to correct format for Vita Fruitpeel plugin.

## Usage

1. Install [Fruitpeel](https://forum.devchroma.nl/index.php/topic,338.0.html) plugin on your PlayStation Vita;
2. Crop the image you want to use to `896x448`;
3. Run `ImgConv.exe`, chose image path and destination path, run `Convert!`;
4. Drop the converted image to `ur0:/data/` folder on your console.
5. Reboot your console.


## Build
1. Create a new Python venv in /fpimageconv directory;
2. install poetry - `pip install poetry`;
3. `poetry install` in project root;
4. `python -m nuitka --onefile --enable-plugin=pyside6 fpimageconv\src\fpimageconv\main.py`;


## Tools used

Nuitka, Poetry, Pillow, PySide6, logging.
