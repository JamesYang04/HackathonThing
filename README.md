# PantryPal
PantryPal is a program which searches databases for recipes, given a set of grocery materials, restraints (High/Low Calories, Protein, Sugar, etc).
Developed as part of CMU TartanHacks 2023 (James Yang, Alan Lin, Max Hu, Sophie Feng, collectively known as team Canadian Geese).

## Dataset
Download the recipes dataset [here](https://drive.google.com/file/d/1RrCHyl7BqPEDS33FRhFzN9RawMB18S7e/view?usp=sharing), and copy it to your local repository of PantryPal once cloned.

## Dependencies
- [OpenCV](https://pypi.org/project/opencv-python/)
- [Tesseract](https://pypi.org/project/pytesseract/)
- [OpenAI](https://pypi.org/project/openai/)

## Setup
- Tested with Python 3.10.
- Install dependencies from `requirements.txt` by running `pip install -r requirements.txt`
- Edit the `config.py` file with an API key for OpenAI.
- On Mac OS: If 'pytesseract' doesn't set up the module path correctly, try running the installation with [Homebrew](https://brew.sh/).
