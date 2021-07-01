Set-ExecutionPolicy Bypass -Scope Process -Force
# choco uninstall python --version=3.9.4 -y
choco uninstall python3 --version=3.9.4 -y
"y"|choco uninstall nssm -n --skipautouninstaller

