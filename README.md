# MY DOTFILES

## Start with `install.sh` file
Command: 
```bash
sh install.sh
```

Once the bash script is done running, run the following command:
```bash
brew bundle
```

### Setting up git
```bash
ssh-keygen -t rsa -b 4096 -C "user@email.com"
```
```bash
pbcopy < ~/.ssh/id_rsa.pub
```

## Tmux
```bash
cp -rf config/tmux/ ~/.config/
```

## Neovim
```bash
cp -rf config/nvim/ ~/.config/
```

## Linear Mouse
```bash
cp -rf config/linearmouse/ ~/.config/
```

## Fastfetch
```bash
cp -rf config/fastfetch/ ~/.config/
```

## Btop
```bash
cp -rf config/btop/ ~/.config/
```

## Zsh Config
```bash
cp .zshrc
```

## Rectangle Config
```bash
cp RectangleConfig.json ~/.config
```

## Terminal
Terminal: Warp
Config: Starship
Font: MesloLGS NF

## VS Code
Theme: Light+
Font: MesloLGS NF

## PyCharm
Theme: Dark
Font: MesloLGS NF

## Cursor
Theme: Light+
Font: MesloLGS NF