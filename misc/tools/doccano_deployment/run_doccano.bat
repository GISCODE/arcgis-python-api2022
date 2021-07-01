@echo off
SET DIR_=%~dp0
call "c:/doccano/venv/scripts/activate"
cd \doccano
doccano --username %1 --password %2
cd %DIR_%



