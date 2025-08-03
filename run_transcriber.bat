@echo off
echo 🎬 YouTube Transcript Extractor
echo ================================
echo.
echo This script will help you extract transcripts from YouTube videos.
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python 3.8 or higher first
    pause
    exit /b 1
)

REM Check if required modules are available
python -c "import youtube_transcript_api" >nul 2>&1
if errorlevel 1 (
    echo 📦 Installing required dependencies...
    pip install requests defusedxml
    if errorlevel 1 (
        echo ❌ Failed to install dependencies
        pause
        exit /b 1
    )
)

echo ✅ All dependencies are ready!
echo.

REM Run the transcriber
python simple_transcriber.py

pause
