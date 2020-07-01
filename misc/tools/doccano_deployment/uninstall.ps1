Set-ExecutionPolicy Bypass -Scope Process -Force
"y"|choco uninstall git.install -n --skipautouninstaller
"y"|choco uninstall python --version=3.7.2 -n --skipautouninstaller
"y"|choco uninstall nodejs --version=13.11.0 -n --skipautouninstaller
"y"|choco uninstall nssm -n --skipautouninstaller