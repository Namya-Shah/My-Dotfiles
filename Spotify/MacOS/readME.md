# Run this command using bash terminal
```bash
sh spotify-patch.sh
```
This will run the code without copy pasting any thing. If you want to use `Arguments` then you need to use the below mentioned script

```bash
sh spotify-patch-arguments.sh
```

# Features
- Blocks all banner/video/audio ads within the app
- Blocks logging (Sentry, etc)
- Unlocks the skip function for any track
- Blocks Spotify automatic updates (optional)
- Hides podcasts, episodes and audiobooks on Home Screen (optional)

# Installation/Update
- Close Spotify completely
- Run the following command in Terminal:
    ```bash
    bash <(curl -sSL https://raw.githubusercontent.com/SpotX-CLI/SpotX-Mac/main/install.sh)
    ```

# Optinal Install Arguments
`-f` Force patch -> forces re-patching if backup detected
`-h` Hide podcasts, episodes, and audiobooks on homescreen
`-P` Path to Spotify.app -> set custom Spotify app path
`-u` Block updated -> blocks automatic updates
`-S` Skip Codesign -> only to be used if you have intel mac

# Uninstall
- Close Spotify completely
- Run the following command in Terminal:
    ```bash
    bash <(curl -sSL https://raw.githubusercontent.com/SpotX-CLI/SpotX-Mac/main/uninstall.sh)
    ```

# Notes
- Audio/Video ads during Podcast playback are currently NOT blocked with SpotX.
- Spicetify users: When using SpotX-Mac + Spicetify, the current script requires running SpotX first.