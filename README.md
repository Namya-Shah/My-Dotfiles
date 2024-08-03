# MY DOTFILES

1. To install other files other than in brew shell script then insert it

# To install Arc Browser
[Arc Browser](https://arc.net/)
[Microsoft Office](https://www.microsoft.com/en-us/microsoft-365)
[Desk Lamp](www.desklamp.io/)

### BREW FILES USING ZSH

- Brew files inserted in brew.sh (but you should have installed zsh in terminal)

### BREW FILES USING BASH

- Brew files inserted in brew_bash.sh (but you should use bash script to install it)

### CONDA SCRIPT

- Use this script to create and activate conda environment in python (If you require a specific version of python skip to next file)

### PYTHON LIBRARIES

- Python libraries are inserted in python.sh file which will install all required libraries
- Libraries Names
  - NumPy
  - Pandas
  - TensorFlow
  - SciPy
  - Matplotlib
  - Keras
  - Scikit-Learn
  - Tkinter
  - PyTorch
  - NLTK
  - Seaborn
  - Spacy
  - Ruff
  - MyPy
  - Pydantic
  - Black
  - Requests
  - OpenCV
  - Scrapy
  - Beautiful Soup
  - Selenium
  - Pygame
  - Pyautogui
  - Pyttsx3 (Text to speech)
  - Django
  - Flask
  - Kivy
  - Pillow
  - Pywhatkit
  - Turtle

### ZSH FILES

- Power10k

### FONTS

You can use install.sh to install all the fonts present in the directory
```bash
cd Fonts/
sh install.sh
```

### Terminal
- plugins = (git zsh-syntax-highlighting zsh-autosuggestions)
#### To install zsh-syntax-highlighting
[ZSH SYNTAX HIGHLIGHTING](https://github.com/zsh-users/zsh-syntax-highlighting/blob/master/INSTALL.md)
#### To install zsh-autosuggestions
[ZSH-AUTOSUGGESTIONS](https://github.com/zsh-users/zsh-autosuggestions/blob/master/INSTALL.md)

## Aliases to be added in `.zshrc` file
alias g="git"
alias gaa="git add ."
alias ga="git add"
alias gc="git commit"
alias gco="git commit -m "New Notes"

alias c="clear"
alias n="nvim"
