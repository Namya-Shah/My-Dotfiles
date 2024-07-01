# Creating Directories
mkdir ~/Developer

# Cloning Github Libraries
cd ~/Developer/
git clone https://github.com/Namya-Shah/Programming-Notes.git
git clone https://github.com/Namya-Shah/Notebooks.git
git clone https://github.com/Namya-Shah/Python-Codes.git
git clone https://github.com/Namya-Shah/Python-Projects.git
git clone https://github.com/Namya-Shah/My-Dotfiles.git
git clone https://github.com/Namya-Shah/Obisidian-Vault.git
git clone https://github.com/Namya-Shah/Web-Dev-Codes.git
git clone https://github.com/Namya-Shah/CPP_Programs.git
git clone https://github.com/Namya-Shah/C_CPP_Programs.git

# Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Brew Packages
brew install python # It will install system-wide python
brew install miniconda
brew install fig
brew install tree
brew install neovim
brew install vim
brew install mingw-w64
brew install git

# Install MacOS Applications
brew install --cask vlc
brew install --cask authy
brew install --cask google-chrome
brew install --cask firefox
brew install --cask todoist
brew install --cask discord
brew install --cask iina
brew install --cask notion
brew install --cask visual-studio-code
brew install --cask iterm2
brew install --cask rectangle
brew install --cask raycast
brew install --cask anydesk
brew install --cask keka
brew install --cask android-file-transfer
brew install --cask android-platform-tools
brew install --cask pycharm-ce
brew install --cask spotify
brew install --cask obsidian
brew install --cask sublime-text
brew install --cask android-studio


# Install Fonts
brew install --cask font-jetbrains-mono

# Activating Conda
conda init base
conda activate
conda install python

# Installing Python Libraries
pip install pandas
pip install numpy
pip install matplotlib
pip install requests
pip install tensorflow
pip install scipy
pip install keras
pip install tkinter
pip install opencv-python
pip install scikit-learn
pip install pytorch
pip install Scrapy3
pip install beautifulsoup4
pip install selenium
pip install pygame
pip install pyautogui
pip install pyttsx3
pip install seaborn
pip install spacy
pip install NLTK
pip install django
pip install flask
pip install kivy
pip install pillow
pip install pywhatkit
pip install turtle
pip install jupyter notebook
pip install jupyterlab

# Neovim Configuration
mkdir ~/.config/
cp -r ~/Developer/My-Dotfiles/nvim/ ~/.config
