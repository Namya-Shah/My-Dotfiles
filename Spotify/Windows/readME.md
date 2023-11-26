# System Requirements
- **OS**: Windows 7-11
- **Spotify**: Latest official [versions](https://cutt.ly/8EH6NuH)
- **For Windows Desktop only (Microsoft store version is not suitable)**
- **PowerShell**: Version 5 and above recommended

# Features
- Blocks all banner, video and audio ads in the client
- Hiding podcasts, episodes and audiobooks from the homepage (optional)
- Block Spotify automatic updates (optional)
- More experimental features have been activated ([see the full list](https://github.com/SpotX-Official/SpotX/discussions/50))
- Disabled Sentry (Prevented Sentry from sending console log/error/warning to Spotify developers)
- Disabled logging (Stopped various elements to log user interaction)
- Removed RTL rules (Removed all right-to-left CSS rules to simplify CSS files)
- Code minification

# Fast Installation/Update
## Choose Installation Type:
### Usual Installation (New Theme)
- During installation, you need to confirm some actions, also contains:
    - New theme activated (new right and left sidebar, some cover change)
    - All experimental features included
- Just download and run [Install.bat](https://raw.githack.com/amd64fox/SpotX/main/Install_New_theme.bat)
***OR***
- Run the following command in PowerShell:
```bash
[Net.ServicePointManager]::SecurityProtocol = 3072; iex "& { $(iwr -useb 'https://spotx-official.github.io/run.ps1') } -new_theme"
```

### Usual Installation (Old Theme)
- During installation, you need to confirm some actions, also contains:
    - Forced installation of version 1.2.13 (since the old theme was removed in subsequent versions)
    - Old theme activated
    - Automatic blocking of Spotify updates
    - All experimental features included
- Just download and run [Install.bat](https://raw.githack.com/amd64fox/SpotX/main/Install_Old_theme.bat)
***OR***
Run the following command in PowerShell:
```bash
[Net.ServicePointManager]::SecurityProtocol = 3072; iex "& { $(iwr -useb 'https://spotx-official.github.io/run.ps1') } -v 1.2.13.661.ga588f749-4064 -confirm_spoti_recomended_over -block_update_on"
```

### Full Installation
- New theme activated (new right and left sidebar, some cover change)
- Hiding podcasts/episodes/audiobooks from the homepage
- Activated [static theme](https://github.com/SpotX-Official/SpotX/discussions/50#discussioncomment-4096066) `spotify` for lyrics
- Hiding [ad-like sections](https://github.com/SpotX-Official/SpotX/discussions/50#discussioncomment-4478943)
- All [experimental features](https://github.com/SpotX-Official/SpotX/discussions/50) included
- Removal of Spotify MS if it was found
- Installation of the recommended version of Spotify (if another client has already been found, it will be installed over)
- Blocking of Spotify updates
- After the installation is completed, the client will autorun.

Just download and run [Install_Auto.bat](https://raw.githack.com/amd64fox/SpotX/main/scripts/Install_Auto.bat)

***OR***

Run the following command in PowerShell:
```bash
[Net.ServicePointManager]::SecurityProtocol = 3072; iex "& { $(iwr -useb 'https://spotx-official.github.io/run.ps1') } -confirm_uninstall_ms_spoti -confirm_spoti_recomended_over -podcasts_off -block_update_on -start_spoti -new_theme -adsections_off -lyrics_stat spotify"
```

### Other types of installations
#### Installation for premium
- Usual installation only without ad blocking, for those who have a premium account, also contains:
    - New theme activated (new right and left sidebar, some cover change)
    - Disabled only audio ads in podcasts
    - All [experimental features](https://github.com/SpotX-Official/SpotX/discussions/50) included

Just download and run [Install_Prem.bat](https://raw.githack.com/amd64fox/SpotX/main/scripts/Install_Prem.bat)

***OR***

Run the following command in PowerShell:
```bash
[Net.ServicePointManager]::SecurityProtocol = 3072; iex "& { $(iwr -useb 'https://spotx-official.github.io/run.ps1') } -premium -new_theme"
```

# Uninstall
- Just run [Uninstall.bat](https://raw.githack.com/amd64fox/SpotX/main/Uninstall.bat)