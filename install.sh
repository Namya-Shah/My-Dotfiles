#! /bin/zsh

# Apple Dock Animation
defaults write com.apple.dock autohide-delay -float 0; killall Dock

# Enabling tap to click for the trackpad and show the correct state in System Preferences
defaults write com.apple.AppleMutlitouchTrackpad Clicking -bool true
defaults -currentHost write -g com.apple.mouse.tapBehavior -int 1

# Disable the .DS file creation
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool true
defaults write com.apple.desktopservices DSDontWriteUSBStores -bool true

# Show the path bar in finder
defaults write com.apple.finder "ShowPathbar" -bool "true" && killall Finder

# Show hidden files in the Finder
defaults write com.apple.finder "AppleShowAllFiles" -bool "false" && killall Finder

# Apply the settings
/System/Library/PrivateFrameworks/SystemAdministration.framework/Resources/activateSettings -u

# Homebrew installation
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Installing formulas & apps
brew bundle

# Conda activation
conda init
conda activate base

# Installing python libraries
xargs pip install < libraries.txt

# Neovim config copy
cp nvim ~/.config/

# Tmux config copy
cp tmux ~/.config/

# Starship install
curl -sS https://starship.rs/install.sh | sh

# Installing starship in zsh
echo 'eval "$(starship init zsh)"' >> ~/.zshrc

# Preset for starship
starship preset catppuccin-powerline -o ~/.config/starship.toml

# ZSH Syntax Highlighting
echo "source $(brew --prefix)/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> ${ZDOTDIR:-$HOME}/.zshrc

# ZSH Auto Suggestions
source $(brew --prefix)/share/zsh-autosuggestions/zsh-autosuggestions.zsh

# Plugins in zshrc
plugins = (git zsh-syntax-highlighting zsh-autosuggestions) >> .zshrc

# Aliases in .zshrc
echo "alias g='git' 
alias gaa='git add .'
alias ga='git add'
alias gc='git commit'
alias gco='git commit -m 'New Notes''
alias gp='git push'
alias gst='git status'
alias lg='lazygit'
alias c='clear'
alias n='nvim'
alias bu='brew upgrade'
alias s='source'
alias ld='lazydocker'
alias cmd='cd ~/Developer/My-Dotfiles'
alias ff='fastfetch'
" >> ~/.zshrc