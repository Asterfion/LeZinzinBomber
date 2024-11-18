@echo off
title LeZinzin-Bomber by @LeZinzin - Version 1.0
echo.
echo By @LeZinzin - Version 1.0
echo Github: https://github.com/LeZinzin
echo Thanks for using my tools!
echo.
echo ----------------------------------------------
echo.

timeout /t 2 /nobreak >nul

where python >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [!] Python is not installed or not found in PATH.
    echo Please install Python and try again.
    pause
    exit /b
)

if not exist "LeZinzin-Bomber.py" (
    echo [!] LeZinzin-Bomber.py not found in the current directory.
    echo Make sure the file exists and try again.
    pause
    exit /b
)

echo [+] Running LeZinzin-Bomber.py...
echo.
python LeZinzin-Bomber.py

if %ERRORLEVEL% EQU 0 (
    echo.
    echo [+] The script executed successfully!
) else (
    echo.
    echo [!] There was an error executing the script.
)

:: Pause at the end to allow the user to read the output
pause
