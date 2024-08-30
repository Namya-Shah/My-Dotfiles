# MY DOTFILES

## Required Apps
[Arc Browser](https://arc.net/) \
[Microsoft Office](https://www.microsoft.com/en-us/microsoft-365)

## Installing Homebrew
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

- Install homebrew in `PATH`

## Installing Conda

```bash
brew install miniconda
```

- Use `conda init` to initialize conda

## Python Development
### Installing uv library (based on rust)
```bash
pip install uv
```
### Libraries required
```bash
uv pip install numpy pandas tensorflow scipy matplotlib keras scikit-learn tk torch NLTK seaborn spacy ruff mypy pydantic black requests opencv-python scrapy beautifulsoup4 selenium pygame pyautogui pyttsx3 django Flask kivy pillow pywhatkit turtle
```
### ZSH FILES

- Power10k

## Development
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
`alias g="git"`

`alias gaa="git add ."`

`alias ga="git add"` 

`alias gc="git commit"` 

`alias gco="git commit -m "New Notes"`

`alias c="clear"`

`alias n="nvim"`

`alias bu="brew upgrade"`