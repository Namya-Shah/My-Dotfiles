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
```bash
defaults write com.apple.dock autohide-delay -float 0; killall Dock
```

restore default behavior: \
```bash
defaults delete com.apple.dock autohide-delay; killall Dock
```

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

## Obsidian Setup
**Theme:** Ayu Light & Mirage (Link for theme)[https://github.com/taronull/ayu-obsidian]
**Font:** 
- IBM Plex Mono (Text Font) [Link](https://fonts.google.com/specimen/IBM+Plex+Mono)
- Jetbrains Mono (Code Font) [Link](https://www.jetbrains.com/lp/mono/)

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
- Jetbrains Mono & IBM Plex Mono
### Theme (VS Code)
- Ayu Dark
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

## VS Code Setup
### VS Code Extensions
1. Python Extension Pack
2. Code Runner
3. Jupyter
4. Jupyter Cell Tags
5. Pylance
6. Path Intellisense
7. Python
8. Rainbow CSV
9. Custom CSS & JS Loader
10. Fix VSCode Checksums

### Custom CSS Load
- Copy the below command into terminal
```zsh
cp ~/Developer/My-Dotfiles/styles.css ~/Desktop/styles.css
```

- Copy the below code into `settings.json`
```json
"vscode_custom_css.imports": [
        "file:///~/Desktop/styles.css"
    ]
```

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
alias z='zoxide'
" >> ~/.zshrc
```