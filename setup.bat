@echo off
setlocal enabledelayedexpansion

echo ========================================
echo Setting up R2RML/YARRRML pipeline
echo ========================================

set PROJECT_ROOT=%~dp0

cd /d "%PROJECT_ROOT%"

REM --------------------------------------------------
REM Check required system dependencies
REM --------------------------------------------------

echo.
echo Checking system dependencies...

where java >nul 2>nul
if errorlevel 1 (
    echo ERROR: java is not installed or not in PATH.
    exit /b 1
)

where node >nul 2>nul
if errorlevel 1 (
    echo ERROR: node is not installed or not in PATH.
    exit /b 1
)

where npm >nul 2>nul
if errorlevel 1 (
    echo ERROR: npm is not installed or not in PATH.
    exit /b 1
)

where python >nul 2>nul
if errorlevel 1 (
    echo ERROR: python is not installed or not in PATH.
    exit /b 1
)

echo All required system dependencies found.

REM --------------------------------------------------
REM Print versions
REM --------------------------------------------------

echo.
echo Detected versions:

echo - Java:
java --version

echo.
echo - Node:
node --version

echo.
echo - npm:
call npm --version

echo.
echo - Python:
python --version

REM --------------------------------------------------
REM Install Node.js dependencies
REM --------------------------------------------------

echo.
echo Installing Node.js dependencies...

call npm install
if errorlevel 1 exit /b 1

echo Node.js dependencies installed.

REM --------------------------------------------------
REM Create Python virtual environment
REM --------------------------------------------------

echo.
echo Creating Python virtual environment...

if not exist ".venv" (
    python -m venv .venv
    echo Virtual environment created.
) else (
    echo Virtual environment already exists.
)

REM --------------------------------------------------
REM Activate virtual environment
REM --------------------------------------------------

call ".venv\Scripts\activate.bat"

REM --------------------------------------------------
REM Upgrade pip
REM --------------------------------------------------

echo.
echo Upgrading pip...

python -m pip install --upgrade pip
if errorlevel 1 exit /b 1

REM --------------------------------------------------
REM Install Python dependencies
REM --------------------------------------------------

echo.
echo Installing Python dependencies...

pip install -r requirements.txt
if errorlevel 1 exit /b 1

echo Python dependencies installed.

REM --------------------------------------------------
REM Final validation
REM --------------------------------------------------

echo.
echo Running final validation...

call npx yarrrml-parser --help >nul 2>nul
if errorlevel 1 (
    echo ERROR: yarrrml-parser is not working correctly.
    exit /b 1
)

echo yarrrml-parser OK.

echo.
echo ========================================
echo Setup completed successfully.
echo ========================================
echo.
echo To activate the Python environment manually:
echo.
echo     .venv\Scripts\activate
echo.
echo You can now run the pipeline.