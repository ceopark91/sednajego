@echo off
setlocal

where py >nul 2>nul
if %errorlevel% neq 0 (
  echo py ??? ?? ?????. Python ??? ?????.
  pause
  exit /b 1
)

py -m pip install --upgrade pip pyinstaller
py -m PyInstaller --noconfirm --onefile --name AIMagneticDetection app.py

echo.
echo ?? ??: dist\AIMagneticDetection.exe
pause
