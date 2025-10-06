import os
import webbrowser
from help_cmds import show_help

version = "beta_1.0"

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, 'asc.txt')

with open(file_path, 'r', encoding='utf-8') as f:
    r = f.read()

print(r)

while True:
    cmd = input("$ ➜ ")

    if cmd in ("help", "?"):
        show_help()

    elif cmd == "version":
        print(f"Current version: {version}.")
    
    elif cmd in ("update","upgrade","upd","updates"):
        webbrowser.open("https://github.com/djael-ml/improver/releases")
        print(f"Successfuly opened you the link to latest versions")
    
    elif cmd == ("optimize-pp"):
        os.system('powercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c')
        print("Power plan successfuly changed to High Performances")

    elif cmd == ("disable -a"):
        cmds = [
            # Effets visuels dans les fenêtres et menus
            'reg add "HKCU\\Control Panel\\Desktop" /v UserPreferencesMask /t REG_BINARY /d 9012078010000000 /f',

            # Désactive les animations de la barre des tâches
            'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced" /v TaskbarAnimations /t REG_DWORD /d 0 /f',

            # Désactive les animations générales d’interface
            'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VisualEffects" /v VisualFXSetting /t REG_DWORD /d 2 /f',

            # Désactive les animations dans les fenêtres
            'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced" /v ListviewAlphaSelect /t REG_DWORD /d 0 /f',
            'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced" /v ListviewShadow /t REG_DWORD /d 0 /f'
        ]

        for cmd in cmds:
            os.system(cmd)

        print("Successfuly disabled Windows animations")

    elif cmd == ("enable -a"):
        cmds = [
            'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced" /v TaskbarAnimations /t REG_DWORD /d 1 /f',
            'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VisualEffects" /v VisualFXSetting /t REG_DWORD /d 1 /f',
            'reg add "HKCU\\Control Panel\\Desktop" /v UserPreferencesMask /t REG_BINARY /d 9e1e078010000000 /f'
        ]
        print("Successfuly enabled Windows Animations")

        for cmd in cmds:
            os.system(cmd)

    

    else:
        print(f"Unroconized command, please type 'help' to get the list of commands")