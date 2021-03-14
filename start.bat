@echo off 
cls
color 02
SET /A number = 1
:start
    echo STARTING PYTHON SCRIPT - %number%
    SET /A number = %number% + 1
    py run.py
    timeout /t 2
    Taskkill /F /IM chrome.exe /T
goto start
