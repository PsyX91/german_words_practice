@echo off
setlocal enabledelayedexpansion

set "cache_found=false"

:: Check for pychache dirs
for /d /r %%d in (__pycache__) do (
    set "cache_found=true"
    rd /s /q "%%d" 2>nul
)

:: Display message only if cache files were found
if "%cache_found%"=="true" (
    echo Cache files cleaned up successfully.
) else (
    echo No cache files found.
)

:: Set the Python version to use
set PYTHON_VERSION=3.11

:: Delete virtual environment if it exists
if exist venv (rmdir /s /q venv)

:: Create a virtual environment for the project
py -%PYTHON_VERSION% -m venv venv

:: Activate the virtual environment
call venv\Scripts\activate.bat

:: Upgrade pip to the latest version
pip install --upgrade pip

:: Install the project dependencies from requirements.txt
pip install -r requirements.txt --no-cache-dir

:: Deactivate the virtual environment
deactivate