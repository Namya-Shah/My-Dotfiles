# MY DOTFILES

## Required Apps
[Arc Browser](https://arc.net/) \
[Microsoft Office](https://www.microsoft.com/en-us/microsoft-365)

## Installing Homebrew
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

- Install homebrew in `PATH`

## Dock Commands
keep smooth animation time, but remove delay:
`defaults write com.apple.dock autohide-delay -float 0; killall Dock`

instantly reveal:
`defaults write com.apple.dock autohide-time-modifier -int 0; killall Dock`

restore default behavior:
`defaults delete com.apple.dock autohide-delay; killall Dock`

## Zsh

## Brew Packages
### Formulas
```zsh
brew install python miniconda tree neovim git lazygit fzf eza mysql bat ollama zoxide thefuck tldr git-lfs
```
### Applications
```zsh
brew install --cask adobe-acrobat-reader android-file-transfer android-platform-tools anydesk applite brave-browser chatgpt discord ente-auth iina keka linearmouse localsend mysqlworkbench notion numi obsidian alienator88/homebrew-cask/pearcleaner proton-pass raycast rectangle spotify telegram-desktop todoist visual-studio-code warp zed zoom pycharm
```

## Conda Setup
- Use `conda init` to initialize conda

## Python Development
### Installing uv library (based on rust)
```bash
pip install uv
```
### Libraries required
```bash
uv pip install numpy pandas tensorflow scipy matplotlib keras scikit-learn tk torch NLTK seaborn spacy ruff mypy pydantic black requests opencv-python scrapy beautifulsoup4 selenium pygame pyautogui pyttsx3 django Flask kivy pillow pywhatkit turtle streamlit pyPDF2 jupyterlab jupyter
```


## Development
### IDE
1. Visual Studio Code
2. PyCharm
### Font
- MesloLGS NF
### Theme (VS Code)
- Dark Modern
### Terminal
- Warp

## Zsh
- Insert this line in `~/.zshrc` \
```bash
plugins = (git zsh-syntax-highlighting zsh-autosuggestions)
```
#### To install zsh-syntax-highlighting
[ZSH SYNTAX HIGHLIGHTING](https://github.com/zsh-users/zsh-syntax-highlighting/blob/master/INSTALL.md)
#### To install zsh-autosuggestions
[ZSH-AUTOSUGGESTIONS](https://github.com/zsh-users/zsh-autosuggestions/blob/master/INSTALL.md)

## Aliases to be added in `.zshrc` file
```zsh
echo "alias g='git' 
alias gaa='git add .'
alias ga='git add'
alias gc='git commit'
alias gco='git commit -m 'New Notes''
alias c='clear'
alias n='nvim'
alias bu='brew upgrade'
alias s='source'
" >> ~/.zshrc
```