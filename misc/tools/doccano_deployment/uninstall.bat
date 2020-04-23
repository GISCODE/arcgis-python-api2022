@echo off

SET DIR=%~dp0%
net stop doccano /Y
nssm remove doccano confirm
net stop start_webpack /Y
nssm remove start_webpack confirm
::uninstall doccano
%systemroot%\System32\WindowsPowerShell\v1.0\powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "& '%DIR%uninstall.ps1' %*" -Verb RunAs
%systemroot%\System32\WindowsPowerShell\v1.0\powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "& '%DIR%uninstall_chocolatey.ps1' %*" -Verb RunAs
cd %DIR%
call rmdir /Q /S %DIR%doccano
call rmdir /Q /S %DIR%venv
echo "Uninstalled"