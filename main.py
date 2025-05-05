import streamlit as st
import subprocess
import time

# Functions
def is_app_installed(app_name):
    result = subprocess.run(f"brew list --cask {app_name}", shell=True,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0

st.title("Dotfiles Configurator")

st.header("My Dotfiles")

st.write("Use it if you have MacOS or Linux Environment. It won't work on Windows")

# Homebrew
homebrew_command = '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"'


check_brew = subprocess.run("which brew", shell=True, capture_output=True, text=True)
if check_brew.stdout.strip():
    st.info("Homebrew is already installed.")
else:
    st.info("Installing homebrew will take time")
    # User input for installing homebrew
    selected_homebrew = st.radio("Do you want to install homebrew?", ["Yes", "No"], index=None)

    if selected_homebrew:
        with st.spinner("Installing homebrew...", show_time=True):
            homebrew_process = subprocess.run(homebrew_command,shell=True, capture_output=True, text=True)
            if homebrew_process.stderr:
                st.error("There is an error installing Homebrew")
                st.text(homebrew_process.stderr)
            else:
                st.success("Homebrew is installed")

# Dock
selected_dock = st.radio("Do you want to make the dock animation fast?", options=["Add", "Remove"], index=None)

animation_add_command = 'defaults write com.apple.dock autohide-delay -float 0; killall Dock'
animation_remove_command = 'defaults delete com.apple.dock autohide-delay; killall Dock'

if selected_dock == 'Add':
    with st.spinner("Animation converting...", show_time=True):
        subprocess.run(animation_add_command, shell=True, capture_output=True, text=True)
        st.success("Animation converted!")
elif selected_dock == 'Remove':
    with st.spinner("Removing animation...", show_time=True):
        subprocess.run(animation_remove_command, shell=True, capture_output=True, text=True)
        st.error("Animation Removed!")

brew_prefix = 'brew install '
formula_selections = {}
# Formulas
st.header("Formulas")
col1, col2, col3 = st.columns(3)
with col1:
    formula_selections["Python"] = st.checkbox("Python")
    formula_selections["Miniconda"] = st.checkbox("Miniconda")
    formula_selections["Tree"] = st.checkbox("Tree")
    formula_selections["Neovim"] = st.checkbox("Neovim")
    formula_selections["Git"] = st.checkbox("Git")
    formula_selections["Lazygit"] = st.checkbox("Lazygit")

with col2:
    formula_selections["Lazydocker"] = st.checkbox("Lazydocker")
    formula_selections["Fuzzy Finder"] = st.checkbox("Fuzzy Finder")
    formula_selections["Eza"] = st.checkbox("Eza")
    formula_selections["MySQL"] = st.checkbox("MySQL")
    formula_selections["Bat"] = st.checkbox("Bat")
    formula_selections["ollama"] = st.checkbox("Ollama")

with col3:
    formula_selections["Zoxide"] = st.checkbox("Zoxide")
    formula_selections["TLDR"] = st.checkbox("TLDR")
    formula_selections["Git-LFS"] = st.checkbox("Git LFS")
    formula_selections["UV"] = st.checkbox("UV")
    formula_selections["Ruff"] = st.checkbox("Ruff")
    formula_selections["Zsh Autosuggestions"] = st.checkbox("Zsh Autosuggestions")

# Show selected items
if st.button("Install selected formulas"):
    for formula, checked in formula_selections.items():
        if checked:
            subprocess.Popen(brew_prefix+formula, shell=True, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
            st.write(f"✅ {formula} formula installed!")
# Applications
st.header("Applications")
column1, column2, column3 = st.columns(3)

# Brew prefix for installing apps
brew_prefix_cask = 'brew install --cask '

# application selected dictionary
application_selections = {}

with column1:
    st.subheader("Browsers")
    application_selections["brave-browser"] = st.checkbox("Brave Browser")
    application_selections["google-chrome"] = st.checkbox("Google Chrome")
    application_selections["firefox"] = st.checkbox("Mozilla Firefox")
    application_selections["vivaldi"] = st.checkbox("Vivaldi")
    application_selections["opera"] = st.checkbox("Opera")
    application_selections["librewolf"] = st.checkbox("LibreWolf")
    application_selections["waterfox"] = st.checkbox("WaterFox")
    application_selections["zen"] = st.checkbox("Zen")
    application_selections["thorium"] = st.checkbox("Thorium")
with column2:
    st.subheader("Utilities")
    application_selections["linearmouse"] = st.checkbox("Linear Mouse")
    application_selections["android-file-transfer"] = st.checkbox("Android File Transfer")
    application_selections["ente-auth"] = st.checkbox("Ente Authenticator")
    application_selections["localsend"] = st.checkbox("Local Send")
    application_selections["proton-pass"] = st.checkbox("Proton Password Manager")
    application_selections["android-platform-tools"] = st.checkbox("Android Platform Tools")
    application_selections["maccy"] = st.checkbox("Maccy")
    application_selections["raycast"] = st.checkbox("Raycast")
    application_selections["rectangle"] = st.checkbox("Rectangle")
    application_selections["anydesk"] = st.checkbox("AnyDesk")
    application_selections["keka"] = st.checkbox("Keka")
    application_selections["iina"] = st.checkbox("IINA")
    application_selections["monitor-control"] = st.checkbox("Monitor Control")
with column3:
    st.subheader("Education")
    application_selections["adobe-acrobat-reader"] = st.checkbox("Adobe Acrobat Reader")
    application_selections["visual-studio-code"] = st.checkbox("Visual Studio Code")
    application_selections["zed"] = st.checkbox("Zed")
    application_selections["pycharm-ce"] = st.checkbox("Pycharm")
    application_selections["warp"] = st.checkbox("Warp")
    application_selections["rstudio"] = st.checkbox("R Studio")
    application_selections["notion"] = st.checkbox("Notion")
    application_selections["todoist"] = st.checkbox("Todoist")
    application_selections["mysqlworkbench"] = st.checkbox("My SQL Workbench")
    application_selections["docker"] = st.checkbox("Docker")

column4, column5, column6 = st.columns(3)
with column4:
    st.subheader("Communication")
    application_selections["discord"] = st.checkbox("Discord")
    application_selections["whatsapp"] = st.checkbox("Whatsapp")
    application_selections["zoom"] = st.checkbox("Zoom")
    application_selections["slack"] = st.checkbox("Slack")
    application_selections["telegram-desktop"] = st.checkbox("Telegram Desktop")
with column5:
    st.subheader("LLMs")
    application_selections["chatgpt"] = st.checkbox("ChatGPT")
    application_selections["claude"] = st.checkbox("Claude")
    application_selections["gemini"] = st.checkbox("Gemini")

if st.button("Install checked apps"):
    for app, checked in application_selections.items():
        if checked:
            if is_app_installed(app):
                st.info(f"{app} is already installed. Skipping.")
                continue
            with st.spinner(f"Installing {app}..."):
                install_command = brew_prefix_cask + app
                result = subprocess.run(install_command, shell=True, capture_output=True, text=True)

                if result.returncode == 0:
                    st.success(f"{app} installed successfully.")
                else:
                    st.error(f"Failed to install {app}.")
                    st.text(result.stderr)

# Python Libraries
st.header("Python Libraries")
st.checkbox("Numpy")
st.checkbox("Pandas")
st.checkbox("Matplotlib")
st.checkbox("Seaborn")
st.checkbox("Scikit Learn")
st.checkbox("PyTorch")
st.checkbox("TensorFlow")
st.checkbox("Keras")

# Oh My Zsh
omz_install = 'sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"'
