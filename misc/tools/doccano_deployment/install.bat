@echo off
SET DIR=%~dp0%
cd /
mkdir doccano
cd c:/doccano
mkdir logs
cd %DIR%
set hr=%time:~0,2%
set hr=%hr: =0%
set LOGFILE=C:\doccano\logs\install_log_%date:~-4,4%%date:~-10,2%%date:~-7,2%_%hr%%time:~3,2%%time:~6,2%.txt

call :LOG1 2> %LOGFILE%

python "%DIR%doccano\app\manage.py" migrate
python "%DIR%doccano\app\manage.py" createsuperuser

call :LOG2 2>> %LOGFILE%

exit /B

:LOG2

call "C:/doccano/venv/scripts/deactivate"
cd "%DIR%doccano\app\server\static"
call npm install
cd "%DIR%"
copy "%DIR%annotation.html" "%DIR%doccano\app\server\templates" /Y
net stop doccano /Y
nssm remove doccano confirm
nssm install doccano %DIR%run_doccano.bat %DIR%
nssm start doccano
net stop start_webpack /Y
nssm remove start_webpack confirm
nssm install start_webpack %DIR%start_webpack.bat %DIR%
nssm start start_webpack
pause
exit /B

:LOG1

::install chocolatey
echo installing chocolatey
%systemroot%\System32\WindowsPowerShell\v1.0\powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "& '%DIR%install_chocolatey.ps1' %*" -Verb RunAs
call refresh_path.bat
echo installing git,node and python
::install git,node and python
%systemroot%\System32\WindowsPowerShell\v1.0\powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "& '%DIR%install_deps.ps1' %*" -Verb RunAs
SET PATH=%PATH%;C:\Program Files\Git\bin;C:\Program Files\nodejs
call refresh_path.bat
pip install virtualenv 
virtualenv "C:/doccano/venv"
call C:/doccano/venv/scripts/activate
python -m pip install --force-reinstall pip
call git clone https://github.com/doccano/doccano.git doccano
cd "%DIR%doccano"
call git checkout bdba2961bf7942eb529a1591a7499b5d15af73bf
git config --global url."https://".insteadOf git://
pip install -r "%DIR%doccano\requirements.txt"
cd "%DIR%doccano\frontend"
SET PATH=%PATH%;%systemroot%\System32\WindowsPowerShell\v1.0\
call npm install --global windows-build-tools --vs2015
SET NODE_GYP_FORCE_PYTHON=%userprofile%\.windows-build-tools\python27\python.exe
call npm install
call npm run build
cd "%DIR%doccano\app"
