@echo off

SET DIR=%~dp0%
cd %DIR%doccano/app/server/static
call npm start
cd %DIR%