#! /bin/zsh

# Apple Dock Animation
defaults write com.apple.dock autohide-delay -float 0; killall Dock

# Homebrew installation
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Installing formulas
xargs brew install < formulas.txt

# Installing apps
xargs brew install --cask < apps.txt

# Conda activation
conda init
conda activate base

# Installing python libraries
xargs pip install < libraries.txt

# Neovim config copy
cp nvim ~/.config/

# Tmux config copy
cp tmux ~/.config/

# Installing Oh My Zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Plugins in zshrc
plugins = (git zsh-syntax-highlighting zsh-autosuggestions) >> .zshrc

# ZSH Syntax Highlighting
echo "source $(brew --prefix)/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> ${ZDOTDIR:-$HOME}/.zshrc

# ZSH Auto Suggestions
source $(brew --prefix)/share/zsh-autosuggestions/zsh-autosuggestions.zsh

# Aliases in .zshrc
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