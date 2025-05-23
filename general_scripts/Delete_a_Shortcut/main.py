import winshell
import os

desktop = winshell.desktop()
shortcut_path = os.path.join(desktop, "Google Chrome.Ink")

if os.path.exists(shortcut_path):
    os.remove(shortcut_path)
    print(f"Shortcut '{shortcut_path}' deleted successfully.")
else:
    print(f"Shortcut '{shortcut_path}' does not exist.")