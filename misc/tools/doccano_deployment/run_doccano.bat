@echo off

SET DIR=%~dp0%
cd %DIR%doccano/app
call "c:/doccano/venv/scripts/activate"
python manage.py runserver
cd %DIR%