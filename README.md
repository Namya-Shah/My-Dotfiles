# MY DOTFILES

## Required Apps (Not available in Homebrew)
[Arc Browser](https://arc.net/) \
[Microsoft Office](https://www.microsoft.com/en-us/microsoft-365)

## Installing Homebrew
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

- Install homebrew in `PATH`

## Dock Commands
keep smooth animation time, but remove delay: \
`defaults write com.apple.dock autohide-delay -float 0; killall Dock`

restore default behavior: \
`defaults delete com.apple.dock autohide-delay; killall Dock`

## Zsh

## Brew Packages
### Formulas
```zsh
xargs brew install < formulas.txt
```

### Applications
```zsh
xargs brew install --cask < apps.txt
```

## Conda Setup
- Use `conda init` to initialize conda

## Python Development
### Libraries required
```zsh
xargs pip install < libraries.txt
```

## Config files
### Neovim
```zsh
cp nvim ~/.config/
```

### Tmux
```zsh
cp tmux ~/.config/
```

## Development
### IDE
1. Visual Studio Code
2. PyCharm
### Font
- MesloLGS NF
### Theme (VS Code)
- Dark Modern
### Theme (PyCharm)
- Dark
### Terminal
- Warp
### Terminal Theme
- [Powerlevel10k](https://github.com/romkatv/powerlevel10k)


## Terminal

### Oh My Zsh
```zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

### Zsh Plugins
- Insert this line in `~/.zshrc`
```bash
plugins = (git zsh-syntax-highlighting zsh-autosuggestions)
```
#### To install zsh-syntax-highlighting
[ZSH SYNTAX HIGHLIGHTING](https://github.com/zsh-users/zsh-syntax-highlighting/blob/master/INSTALL.md)
#### To install zsh-autosuggestions
[ZSH-AUTOSUGGESTIONS](https://github.com/zsh-users/zsh-autosuggestions/blob/master/INSTALL.md)

## VS Code Extensions
1. Python Extension Pack
2. Code Runner
3. Jupyter
4. Jupyter Cell Tags
5. Pylance
6. Path Intellisense
7. Python
8. Rainbow CSV

### Aliases to be added in `.zshrc` file
```zsh
echo "alias g='git' 
alias gaa='git add .'
alias ga='git add'
alias gc='git commit'
alias gco='git commit -m 'New Notes''
alias gst='git status'
alias lg='lazygit'
alias c='clear'
alias n='nvim'
alias bu='brew upgrade'
alias s='source'
" >> ~/.zshrc
```