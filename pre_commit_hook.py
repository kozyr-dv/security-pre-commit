import subprocess
import sys
import platform
import os

def install_gitleaks():
    try:
        # Перевіряємо, чи встановлено gitleaks
        subprocess.check_call(['gitleaks', '--version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("Gitleaks is already installed.")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Gitleaks is not installed. Installing...")
        os_type = platform.system().lower()
        if os_type == 'linux' or os_type == 'darwin':
            subprocess.check_call(['curl', '-sfL', 'https://raw.githubusercontent.com/gitleaks/gitleaks/main/install.sh', '|', 'sh', '-s', '--', '-b', '/usr/local/bin'], shell=True)
        elif os_type == 'windows':
            print("Manual installation required on Windows. Please visit https://github.com/gitleaks/gitleaks")
            sys.exit(1)
        else:
            print(f"Unsupported OS: {os_type}")
            sys.exit(1)

def is_hook_enabled():
    try:
        # Перевіряємо налаштування git config
        enabled = subprocess.check_output(['git', 'config', '--get', 'hooks.gitleaks.enabled']).strip()
        return enabled == b'true'
    except subprocess.CalledProcessError:
        return False

def run_gitleaks():
    try:
        # Запускаємо gitleaks на поточній директорії
        subprocess.check_call(['gitleaks', 'detect', '--source=.'])
        print("No secrets found, commit allowed.")
    except subprocess.CalledProcessError:
        print("Potential secrets detected, commit aborted.")
        sys.exit(1)

def main():
    if not is_hook_enabled():
        print("Gitleaks hook is not enabled. To enable, run 'git config --bool hooks.gitleaks.enabled true'")
        sys.exit(0)

    install_gitleaks()
    run_gitleaks()

if __name__ == "__main__":
    main()

