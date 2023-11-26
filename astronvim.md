# Leader Key is `<leader> -> SPACE`
# ⚡ Requirements

- [Nerd Fonts](https://www.nerdfonts.com/font-downloads)
- [Neovim v0.8+](https://github.com/neovim/neovim/releases/tag/stable)
- [Tree-sitter CLI](https://github.com/tree-sitter/tree-sitter/blob/master/cli/README.md)
- A clipboard tool is necessary for the integration with the system clipboard
- Terminal with true color support
- Optional Requirements
  - [ripgrep](https://github.com/BurntSushi/ripgrep) - live grep telescope search (`<leader>fw`)
  - [lazygit](https://github.com/jesseduffield/lazygit) - git ui toggle terminal (`<leader>tl` or `<leader>gg`)
  - [go DiskUsage()](https://github.com/dundee/gdu) - disk usage toggle terminal (`<leader>tu`)
  - [bottom](https://github.com/ClementTsang/bottom) - process viewer toggle terminal (`<leader>tt`)
  - [Python](https://www.python.org/) - python repl toggle terminal (`<leader>tp`)
  - [Node](https://nodejs.org/en/) - Node is needed for a lot of the LSPs, and for the node repl toggle terminal (`<leader>tn`)

# 🛠️ Installation

- ## Linux/MacOS (Unix)

  - ### Make a backup of your current nvim folder
    ```bash
      mv ~/.config/nvim ~/.config/nvim.bak
    ```
  - ### Clean neovim folders (Optional but Recommended)
    ```bash
      mv ~/.local/share/nvim ~/.local/share/nvim.bak
      mv ~/.local/state/nvim ~/.local/state/nvim.bak
      mv ~/.cache/nvim ~/.cache/nvim.bak
    ```
  - ### Clone the repository
    ```bash
    git clone --depth 1 https://github.com/AstroNvim/AstroNvim ~/.config/nvim
    nvim
    ```
# 📦 Setup
  - ### Install LSP
    - Enter `:LSPInstall` followed by the name of the server you want to install
  - ### Install Language Parser
    - Enter `:TSInstall` followed by the name of the language you want to install
  - ### Install Debugger
    - Enter `:DapInstall` followed by the name of the debugger you want to install
  - ### Manage Plugins
    - Run `:Lazy check` to check for plugin updates
    - Run `:Lazy update` to apply any pending plugin updates
    - Run `:Lazy clean` to remove any disabled or unused plugins
    - Run `:Lazy sync` to update and clean plugins
  - ### Update AstroNvim
    - Run `:AstroUpdate (<leader>pA)` to get the latest updates from the repository
  - ### Update AstroNvim Packages
    - Run `:AstroUpdatePackages (<leader>pa)` to update both Neovim plugins and Mason packages
  - ### Reload AstroNvim *(EXPERIMENTAL)*
    - Run `:AstroReload` to reload the AstroNvim configuration and any new user configuration chages without restarting. This is currently an experimental feature and may lead to instability until the next restart.

# ✨Features
- Common plugin specifications with [AstroCommunity](https://github.com/AstroNvim/astrocommunity)
- Statusline, Winbar, and Tabline with [Heirline](https://github.com/rebelot/heirline.nvim)
- Plugin management with [lazy.nvim](https://github.com/folke/lazy.nvim)
- Package management with [mason.nvim](https://github.com/williamboman/mason.nvim)
- File explorer with [Neo-tree](https://github.com/nvim-neo-tree/neo-tree.nvim)
- Autocompletion with [Cmp](https://github.com/hrsh7th/nvim-cmp)
- Git integration with [Gitsigns](https://github.com/lewis6991/gitsigns.nvim)
- Terminal with [Toggleterm](https://github.com/akinsho/toggleterm.nvim)
- Fuzzy finding with [Telescope](https://github.com/nvim-telescope/telescope.nvim)
- Syntax highlighting with [Treesitter](https://github.com/nvim-treesitter/nvim-treesitter)
- Formatting and linting with [Null-ls](https://github.com/jose-elias-alvarez/null-ls.nvim)
- Language Server Protocol with [Native LSP](https://github.com/neovim/nvim-lspconfig)

# ⚙️ Configuration
To begin making custom user configurations you must create a user/ folder. We have created a template repository for easily making a user configuration file: [Astronvim/user_example](https://github.com/AstroNvim/user_example)

The provided template repo can be used to create a new user configuration repository on your GitHub account or cloned directly. After creating a new repository from the template you can run:
```bash
git clone https://github.com/<username>/<config_repo> ~/.config/nvim/lua/user
```