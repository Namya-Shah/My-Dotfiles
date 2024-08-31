# Making the dock faster
defaults write com.apple.dock autohide-time-modifier -float 0.15; killall Dock

# Creating Directories
mkdir ~/Developer

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
brew install lazygit

# Activating Conda
conda init base
conda activate
conda install python

# Install MacOS Applications
brew install --cask google-chrome
brew install --cask syncthing
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
brew install --cask android-studio
brew install --cask localsend
brew install --cask zoom
brew install --cask github-desktop
brew install --cask linearmouse
brew install alienator88/homebrew-cask/pearcleaner
brew install stats
brew install --cask jordanbaird-ice
brew install --cask applite

# Installing dependencies
brew install ctags
brew install ripgrep

# Installing Neovim
brew install neovim

# Install Fonts
brew install --cask font-jetbrains-mono

# Installing UV (Package installer made from rust)
pip install uv

# Installing dependencies for Neovim-Python
uv pip install -U pynvim
uv pip install 'python-lsp-server[all]' pylsp-mypy pyls-isort

# Python Dependencies for Neovim
uv pip install pylint
uv python -m pip install flake8
uv pip install vim-vint

# Installing Python Libraries
uv pip install pandas
uv pip install numpy
uv pip install matplotlib
uv pip install requests
uv pip install tensorflow
uv pip install scipy
uv pip install keras
uv pip install tk
uv pip install opencv-python
uv pip install scikit-learn
uv pip install torch
uv pip install Scrapy3
uv pip install beautifulsoup4
uv pip install selenium
uv pip install pygame
uv pip install pyautogui
uv pip install pyttsx3
uv pip install seaborn
uv pip install spacy
uv pip install NLTK
uv pip install django
uv pip install flask
uv pip install kivy
uv pip install pillow
uv pip install pywhatkit
uv pip install turtle
uv pip install jupyter notebook
uv pip install jupyterlab

# Neovim Configuration
mkdir ~/.config/
cp -r ~/Developer/My-Dotfiles/nvim/ ~/.config

# Cloning Github Libraries
cd ~/Developer/
git clone git@github.com:Namya-Shah/Obsidian-Notes.git
git clone git@github.com:Namya-Shah/Books.git
git clone git@github.com:Namya-Shah/Leetcode.git
git clone git@github.com:Namya-Shah/Data-Structures-Algorithms-in-Python-CodingNinjas.git
git clone git@github.com:Namya-Shah/Python-Projects.git

# Installing node
brew install node
export PATH="$HOME/tools/node-v14.15.4-linux-x64/bin:$PATH"
source ~/.zshrc

# Installing vim language server
npm install -g vim-language-server

# Installing this configuration
git clone --depth=1 https://github.com/jdhao/nvim-config.git .