import winshell

# PIP INSTALL WINSHELL

try:
    # Empty the Recycle Bin
    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
    print("Recycle Bin emptied successfully.")
except Exception as e:
    print(f"An error occurred while emptying the Recycle Bin: {e}")