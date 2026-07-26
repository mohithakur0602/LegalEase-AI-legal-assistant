@echo off
setlocal
cd /d "%~dp0"

if not exist env\Scripts\python.exe (
    echo The Python environment is missing.
    echo Run setup_windows.bat first.
    pause
    exit /b 1
)

call env\Scripts\activate.bat
python manage.py migrate
python manage.py runserver
pause
