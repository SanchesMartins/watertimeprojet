@echo off

if NOT [%1] == [] goto setvar
if [%1] == [] goto setauto

:setvar
set watertimehome=%1
goto run

:setauto:
set watertimehome=./src
goto run

:run
echo %watertimehome%
cd %watertimehome%
pythonw main.py >> ./logs/logs