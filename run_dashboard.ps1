# YouTube Transcript Extractor Dashboard Launcher
# PowerShell Script to start the Streamlit dashboard

Write-Host "🌐 YouTube Transcript Extractor Dashboard" -ForegroundColor Cyan
Write-Host "=" * 50 -ForegroundColor Cyan
Write-Host ""

# Check if Python is available
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Python 3.8 or higher first" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Check if required modules are available
Write-Host "🔍 Checking dependencies..." -ForegroundColor Yellow

try {
    python -c "import streamlit, youtube_transcript_api" 2>$null
    Write-Host "✅ All dependencies are ready!" -ForegroundColor Green
} catch {
    Write-Host "📦 Installing required dependencies..." -ForegroundColor Yellow
    pip install -r requirements.txt
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ Failed to install dependencies" -ForegroundColor Red
        Read-Host "Press Enter to exit"
        exit 1
    }
    Write-Host "✅ Dependencies installed successfully!" -ForegroundColor Green
}

Write-Host ""
Write-Host "🚀 Starting Streamlit dashboard..." -ForegroundColor Green
Write-Host "🌐 The dashboard will open in your default browser" -ForegroundColor Cyan
Write-Host "📍 Dashboard URL: http://localhost:8501" -ForegroundColor Cyan
Write-Host ""
Write-Host "⚡ Features available:" -ForegroundColor Magenta
Write-Host "   • Extract transcripts from YouTube URLs" -ForegroundColor White
Write-Host "   • Toggle timestamps on/off" -ForegroundColor White
Write-Host "   • Multiple language support" -ForegroundColor White
Write-Host "   • Translation capabilities" -ForegroundColor White
Write-Host "   • Download in multiple formats" -ForegroundColor White
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host ""

# Start Streamlit
streamlit run streamlit_dashboard.py --server.port 8501 --server.address localhost

Write-Host ""
Write-Host "👋 Dashboard stopped. Press Enter to exit." -ForegroundColor Yellow
Read-Host
