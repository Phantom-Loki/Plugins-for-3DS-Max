@echo off


SET PERMANENT_PATH=C:\My3dsMaxPlugins\
SET SCRIPTS_PATH=%PERMANENT_PATH%scripts\
SET MACROS_PATH=%PERMANENT_PATH%macroscripts\


echo Script Path: %SCRIPTS_PATH%
echo Macros Path: %MACROS_PATH%


if not exist "%SCRIPTS_PATH%" mkdir "%SCRIPTS_PATH%"
if not exist "%MACROS_PATH%" mkdir "%MACROS_PATH%"


if exist "scripts\BrickPatternGenerator.py" (
    echo "Found BrickPatternGenerator.py"
) else (
    echo "Error: BrickPatternGenerator.py not found in the scripts folder."
    pause
    exit /b
)


if exist "macroscripts\BrickPatternGenerator.mcr" (
    echo "Found BrickPatternGenerator.mcr"
) else (
    echo "Error: BrickPatternGenerator.mcr not found in the macroscripts folder."
    pause
    exit /b
)


copy "scripts\BrickPatternGenerator.py" "%SCRIPTS_PATH%"
if %ERRORLEVEL% neq 0 (
    echo "Error: Failed to copy BrickPatternGenerator.py"
    pause
    exit /b
)


copy "macroscripts\BrickPatternGenerator.mcr" "%MACROS_PATH%"
if %ERRORLEVEL% neq 0 (
    echo "Error: Failed to copy BrickPatternGenerator.mcr"
    pause
    exit /b
)


echo Plugin installed successfully to %PERMANENT_PATH%.
pause
