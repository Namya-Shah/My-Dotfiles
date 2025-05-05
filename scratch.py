import streamlit as st
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed

def is_app_installed(app_name):
    result = subprocess.run(f"brew list --cask {app_name}", shell=True,
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result.returncode == 0

def install_app(app_name, prefix_cmd):
    if is_app_installed(app_name):
        return f"ℹ️ {app_name} is already installed. Skipping."

    install_command = prefix_cmd + app_name
    process = subprocess.run(install_command, shell=True, capture_output=True, text=True)
    if process.returncode == 0:
        return f"✅ {app_name} installed successfully."
    else:
        return f"❌ {app_name} failed to install:\n{process.stderr}"

# Trigger on button press
if st.button("Install selected apps in parallel"):
    selected_apps = [app for app, checked in application_selections.items() if checked]

    if not selected_apps:
        st.warning("Please select at least one app.")
    else:
        st.write(f"Starting installation of {len(selected_apps)} apps...")

        results = []
        with ThreadPoolExecutor(max_workers=3) as executor:
            futures = {executor.submit(install_app, app, brew_prefix_cask): app for app in selected_apps}
            for future in as_completed(futures):
                result = future.result()
                st.write(result)

        st.success("All installations finished.")
