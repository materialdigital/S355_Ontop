@echo off
setlocal

REM --------------------------------------------------
REM Check arguments
REM --------------------------------------------------

if "%~1"=="" (
    echo Usage: query.bat path\to\query.sparql
    exit /b 1
)

set QUERY_FILE=%~1

REM --------------------------------------------------
REM Check mapping file
REM --------------------------------------------------

if not exist "mappings\full_mapping.ttl" (
    echo ERROR: mappings\full_mapping.ttl is missing.
    echo Please run run.bat first.
    exit /b 1
)

REM --------------------------------------------------
REM Check query file
REM --------------------------------------------------

if not exist "%QUERY_FILE%" (
    echo ERROR: Query file "%QUERY_FILE%" does not exist.
    exit /b 1
)

REM --------------------------------------------------
REM Execute query
REM --------------------------------------------------

echo Executing SPARQL query...

call ontop-cli-5\ontop query ^
    --mapping mappings/full_mapping.ttl ^
    --properties ontop.properties ^
    --query "%QUERY_FILE%"

if errorlevel 1 exit /b 1