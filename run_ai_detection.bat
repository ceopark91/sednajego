@echo off
setlocal

where py >nul 2>nul
if %errorlevel%==0 (
  py app.py
  goto :eof
)

where python >nul 2>nul
if %errorlevel%==0 (
  python app.py
  goto :eof
)

echo Python executable not found.
pause
