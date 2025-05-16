
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/opt/homebrew/Caskroom/miniconda/base/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/opt/homebrew/Caskroom/miniconda/base/etc/profile.d/conda.sh" ]; then
        . "/opt/homebrew/Caskroom/miniconda/base/etc/profile.d/conda.sh"
    else
        export PATH="/opt/homebrew/Caskroom/miniconda/base/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
alias g='git'
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
alias cmd='cd ~/Developer/My-Dotfiles/'
alias ff=fastfetch

export PATH="$PATH:/Users/bigsmoke/Developer/browser/depot_tools"
eval "$(starship init zsh)"