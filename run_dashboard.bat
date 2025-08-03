@echo off
echo 🌐 Starting YouTube Transcript Extractor Dashboard
echo ================================================
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
python -c "import streamlit, youtube_transcript_api" >nul 2>&1
if errorlevel 1 (
    echo 📦 Installing required dependencies...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ❌ Failed to install dependencies
        pause
        exit /b 1
    )
)

echo ✅ All dependencies are ready!
echo.
echo 🚀 Starting Streamlit dashboard...
echo 🌐 The dashboard will open in your default browser
echo 📍 Default URL: http://localhost:8501
echo.
echo Press Ctrl+C to stop the server
echo.

REM Start Streamlit
streamlit run streamlit_dashboard.py --server.port 8501 --server.address localhost

pause
