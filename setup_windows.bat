@echo off
setlocal
cd /d "%~dp0"

echo.
echo ========================================
echo        LegalEase first-time setup
echo ========================================
echo.

if not exist env\Scripts\python.exe (
    echo Creating Python environment...
    py -m venv env
    if errorlevel 1 goto :error
)

call env\Scripts\activate.bat

echo Installing project requirements...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
if errorlevel 1 goto :error

if not exist .env (
    copy .env.example .env >nul
    echo.
    echo Created .env from .env.example.
    echo Add your Gemini API key to .env to enable AI responses.
)

echo Applying database migrations...
python manage.py migrate
if errorlevel 1 goto :error

echo.
echo Setup complete.
echo Create an admin account with:
echo     env\Scripts\python manage.py createsuperuser
echo.
echo Start the project with run_windows.bat
pause
exit /b 0

:error
echo.
echo Setup stopped because a command failed.
echo Read README.md and check the error shown above.
pause
exit /b 1
