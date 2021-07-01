@echo off

SET DIR_=%~dp0
for /f "delims=" %%i in ('powershell -file  %DIR_%elevated_prompt_check.ps1') do set admin=%%i

if  %admin%==0 (
    powershell start '%~f0' ' %*' -verb runas 2>nul && exit /b
    echo Need to run this installation as an administrator
    pause
    exit)

cd /
mkdir doccano
cd c:/doccano
mkdir logs
cd %DIR_%
set hr=%time:~0,2%
set hr=%hr: =0%
set LOGFILE=C:\doccano\logs\install_log_%date:~-4,4%%date:~-10,2%%date:~-7,2%_%hr%%time:~3,2%%time:~6,2%.txt

echo "-----Installing chocolatey-----"> %LOGFILE%
call :install_chocolatey 2>> %LOGFILE%
choco feature enable -n allowGlobalConfirmation
echo "-----Installing dependencies-----">> %LOGFILE%
call :install_deps 2>> %LOGFILE%
echo "-----Setting doccano username-----">> %LOGFILE%
call :getusrname 2>> %LOGFILE%
echo "-----Setting doccano password-----">> %LOGFILE%
call :getpwd 2>> %LOGFILE%
echo "-----Setting up doccano service-----">> %LOGFILE%
@REM GOTO :end
call :setup_doccano_service 2>> %LOGFILE%
echo Doccano successfully installed
echo Starting doccano at http://localhost:8000 ......
timeout 20 > %temp%\null
start explorer http://localhost:8000
exit /B

:install_chocolatey

::install chocolatey
echo Installing chocolatey...
%systemroot%\System32\WindowsPowerShell\v1.0\powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "& '%DIR_%install_chocolatey.ps1' %*" -Verb RunAs
call refresh_path.bat
echo Installing python...
::install python
%systemroot%\System32\WindowsPowerShell\v1.0\powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "& '%DIR_%install_deps.ps1' %*" -Verb RunAs
call refresh_path.bat
exit /B


:install_deps
pip install virtualenv 
virtualenv "C:/doccano/venv"
call C:/doccano/venv/scripts/activate
pip install doccano==1.2.4
cd "%DIR_%"
net stop doccano /Y >%temp%\null
nssm remove doccano confirm
@REM set /p doccano_username="Enter username:"
@REM set /p doccano_password="Enter Password:"
@REM :getpwd
exit /B



:setup_doccano_service
call refresh_path.bat
nssm install doccano %DIR_%run_doccano.bat  "%doccano_username% %doccano_password%"
nssm start doccano > %temp%\null
call C:/doccano/venv/scripts/deactivate
exit /B

:getpwd

for /f "delims=" %%i in ('powershell -file  getpwd.ps1') do set doccano_password=%%i
if /I  %doccano_password%==0 echo Passwords don't match && GOTO :getpwd
if /I  %doccano_password%==1 echo "Password does not meet length(>5) requirement" && GOTO :getpwd
exit /B


:getusrname
for /f "delims=" %%i in ('powershell -file  get_username.ps1') do set doccano_username=%%i
if /I  %doccano_username%==0 echo Username does not meet length(^>5) requirement && GOTO :getusrname
exit /B


:end



