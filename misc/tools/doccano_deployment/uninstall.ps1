Set-ExecutionPolicy Bypass -Scope Process -Force
"y"|choco uninstall git -n --skip-autouninstaller
choco uninstall python -y -n --skip-autouninstal
"y"|choco uninstall nodejs -n --skip-autouninstal
"y"|choco uninstall yarn -n --skip-autouninstal
"y"|choco uninstall nssm -n --skip-autouninstal

