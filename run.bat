@echo off

set PYTHON_PATH=C:\Python39\python.exe
set VENV_NAME=myenv

if not defined %VENV_NAME% (
    echo Creating virtual environment...
    %PYTHON_PATH% -m venv %VENV_NAME%
)

echo Activating virtual environment...
call %VENV_NAME%\Scripts\activate.bat

echo Checking for required packages...
pip freeze | findstr /i /x /c:"package_name" > nul
if %errorlevel% equ 1 (
    echo Installing required packages...
    pip install -r requirements.txt
)

echo Running text2.py...

rem Clear the terminal
cls

python text2.py