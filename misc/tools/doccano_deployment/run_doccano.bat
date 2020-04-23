@echo off

SET DIR=%~dp0%
cd %DIR%doccano/app
call %DIR%venv/scripts/activate
python manage.py runserver
cd %DIR%