@echo off
set hr=%time:~0,2%
set hr=%hr: =0%
set LOGFILE=C:\doccano\logs\uninstall_log_%date:~-4,4%%date:~-10,2%%date:~-7,2%_%hr%%time:~3,2%%time:~6,2%.txt
call :LOG 2> %LOGFILE%
exit /B

:LOG

SET DIR=%~dp0%
net stop doccano /Y
nssm remove doccano confirm
net stop start_webpack /Y
nssm remove start_webpack confirm
::uninstall doccano
%systemroot%\System32\WindowsPowerShell\v1.0\powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "& '%DIR%uninstall.ps1' %*" -Verb RunAs
%systemroot%\System32\WindowsPowerShell\v1.0\powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "& '%DIR%uninstall_chocolatey.ps1' %*" -Verb RunAs
cd %DIR%
del /f /s /q %DIR%doccano 1>nul
call rmdir /Q /S %DIR%doccano
del /f /s /q C:/doccano/venv 1>nul
call rmdir /Q /S "C:/doccano/venv"
echo "Uninstalled"
pause