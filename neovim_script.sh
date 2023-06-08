#! /bin/zsh

# Installing Python and Miniconda
brew install miniconda
conda init base
conda activate
conda install python

# Installing dependencies for Neovim-Python
pip install -U pynvim
pip install 'python-lsp-server[all]' pylsp-mypy pyls-isort

# Installing node
brew install node
export PATH="$HOME/tools/node-v14.15.4-linux-x64/bin:$PATH"
source ~/.zshrc

# Installing vim language server
npm install -g vim-language-server

# Installing dependencies
brew install ctags
brew install ripgrep

# Installing python dependencies
pip install pylint
python -m pip install flake8
pip install vim-vint

# Installing Neovim
brew install neovim

# Installing plugin manager packer.nvim
git clone --depth=1 https://github.com/wbthomason/packer.nvim ~/.local/share/nvim/site/pack/packer/opt/packer.nvim

# Installing this configuration
git clone --depth=1 https://github.com/jdhao/nvim-config.git .
