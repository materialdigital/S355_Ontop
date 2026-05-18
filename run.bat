@echo off
setlocal

echo creating sql-file...

call ".venv\Scripts\activate.bat"

python createDB.py
if errorlevel 1 exit /b 1

echo removing old H2 database...

if exist H2s355.mv.db del /f /q H2s355.mv.db
if exist H2s355.trace.db del /f /q H2s355.trace.db

echo creating H2 database...

java -cp "ontop-cli-5\jdbc\h2.jar" org.h2.tools.RunScript ^
  -url jdbc:h2:./H2s355 ^
  -user sa ^
  -password "" ^
  -script s355.sql

if errorlevel 1 exit /b 1

echo parsing YARRRML files to create r2rml mapping...

npx yarrrml-parser ^
  -i mappings/sheet1.yml ^
  -i mappings/charpy.yml ^
  -i mappings/tensile.yml ^
  -i mappings/sonic_resonance.yml ^
  -o mappings/full_mapping.ttl ^
  -f r2rml

if errorlevel 1 exit /b 1

echo materializing graph with ontop...

call ontop-cli-5\ontop materialize ^
  --mapping mappings/full_mapping.ttl ^
  --properties ontop.properties ^
  --output graph.ttl ^
  --format turtle

if errorlevel 1 exit /b 1
