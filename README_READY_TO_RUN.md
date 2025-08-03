# 🎬 YouTube Transcript Extractor - Ready to Run!

A simple, ready-to-use Python project for extracting transcripts from YouTube videos and saving them as text files.

## 🚀 Quick Start (3 Steps!)

### 🌟 **Option A: Web Dashboard (Recommended)**

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Start the Dashboard
```bash
# Windows: Double-click this file
run_dashboard.bat

# Or use command line
streamlit run streamlit_dashboard.py
```

### 3️⃣ Use the Web Interface
- Open your browser to `http://localhost:8501`
- Paste any YouTube URL
- Get instant transcript with live preview!
- Toggle timestamps on/off
- Download in multiple formats

---

### **Option B: Command Line**

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Run the Simple Transcriber
```bash
python simple_transcriber.py
```

### 3️⃣ Enter a YouTube URL
```
🔗 Enter YouTube URL or video ID: https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

**That's it!** Your transcript will be saved as a `.txt` file.

## 📁 Project Files

| File | Description |
|------|-------------|
| `streamlit_dashboard.py` | 🌟 **NEW!** Beautiful web dashboard (recommended) |
| `run_dashboard.bat` | 🖱️ One-click dashboard launcher for Windows |
| `simple_transcriber.py` | 🌟 Easy-to-use command-line transcript extractor |
| `youtube_transcriber.py` | Advanced command-line version with more features |
| `examples.py` | Code examples and demonstrations |
| `run_transcriber.bat` | Windows batch file for command-line version |
| `requirements.txt` | Dependencies list |
| `USAGE_GUIDE.md` | Detailed command-line usage instructions |
| `DASHBOARD_GUIDE.md` | Complete dashboard usage guide |

## 🎯 What This Does

✅ **🌐 Beautiful Web Dashboard** - Interactive interface with live preview  
✅ **Extracts transcripts** from YouTube videos  
✅ **Saves as text files** with timestamps  
✅ **Toggle timestamps** on/off in real-time  
✅ **Supports multiple languages** (English, Spanish, German, etc.)  
✅ **Works with video URLs or IDs**  
✅ **Handles auto-generated and manual subtitles**  
✅ **Translation capabilities** - Translate to different languages  
✅ **Multiple download formats** - TXT, JSON  
✅ **Batch processing** (command-line version)  
✅ **Video embedding** - Preview videos in dashboard  
✅ **Mobile responsive** - Works on all devices  

## 🔧 Usage Examples

### 🌟 **Web Dashboard (Recommended)**
```bash
# Windows - Double click
run_dashboard.bat

# Command line
streamlit run streamlit_dashboard.py

# Custom port
streamlit run streamlit_dashboard.py --server.port 8080
```

### **Command Line Usage**
```bash
python simple_transcriber.py
# Enter: https://www.youtube.com/watch?v=VIDEO_ID
```

### **Direct Command Line**
```bash
python simple_transcriber.py https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

### **Different Languages**
```bash
python simple_transcriber.py
# Enter URL, then language: es (for Spanish)
```

### **Windows Users - One Click!**
- **Dashboard**: Double-click `run_dashboard.bat`
- **Command Line**: Double-click `run_transcriber.bat`

## 📄 Output Example

```
YouTube Transcript - Video ID: dQw4w9WgXcQ
Language: English (en)
Auto-generated: False
==================================================

[00:18] ♪ We're no strangers to love ♪
[00:22] ♪ You know the rules and so do I ♪
[00:27] ♪ A full commitment's what I'm thinking of ♪
[00:31] ♪ You wouldn't get this from any other guy ♪
...
```

## 🌍 Supported Languages

| Code | Language | Code | Language |
|------|----------|------|----------|
| `en` | English | `es` | Spanish |
| `fr` | French | `de` | German |
| `it` | Italian | `pt` | Portuguese |
| `ru` | Russian | `ja` | Japanese |
| `ko` | Korean | `zh` | Chinese |
| `ar` | Arabic | `hi` | Hindi |

## 🚨 Troubleshooting

### Problem: "Module not found"
**Solution:** Install dependencies
```bash
pip install requests defusedxml
```

### Problem: "No transcript available"
**Solutions:**
- Try different language: `es`, `de`, `fr`
- Video might not have subtitles
- Try another video

### Problem: "Request blocked"
**Solutions:**
- YouTube might be blocking your IP
- Try again later
- Use a VPN

### Problem: "Invalid URL"
**Supported formats:**
- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- `VIDEO_ID` (just the 11-character ID)

## 🎛️ Advanced Features

For more features, use `youtube_transcriber.py`:

- **🔄 Translation:** Translate transcripts to different languages
- **📚 Batch processing:** Process multiple videos at once
- **📋 List transcripts:** See all available languages for a video
- **📁 Custom directories:** Save files to specific folders
- **🎨 Different formats:** JSON, SRT, WebVTT support

## 💻 API Usage

```python
from youtube_transcript_api import YouTubeTranscriptApi

# Basic usage
api = YouTubeTranscriptApi()
transcript = api.fetch('VIDEO_ID')

# Print transcript
for snippet in transcript:
    print(f"[{snippet.start:.1f}s] {snippet.text}")
```

## 🛠️ System Requirements

- **Python:** 3.8 or higher
- **OS:** Windows, macOS, Linux
- **Internet:** Required for downloading transcripts
- **Dependencies:** `requests`, `defusedxml` (auto-installed)

## 🎯 Use Cases

- **🎓 Education:** Extract lecture transcripts
- **📝 Content creation:** Get video content for articles
- **♿ Accessibility:** Create text versions of videos
- **🔍 Research:** Analyze video content
- **📚 Note-taking:** Save important video information
- **🌐 Translation:** Convert videos to different languages

## ⚡ Performance

- **Speed:** ~2-5 seconds per video
- **File size:** Text files are typically 1-10 KB
- **Memory:** Low memory usage
- **Rate limits:** YouTube may limit requests

## 🤝 Contributing

This project is based on the excellent [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api) library.

## 📜 License

MIT License - Use freely for personal and commercial projects.

## ⭐ Star This Project

If this helps you, please give it a star! It helps others find this tool.

---

## 🚀 Ready to Start?

### 🌟 **Recommended: Web Dashboard**
1. **Windows users:** Double-click `run_dashboard.bat`
2. **Command line:** Run `streamlit run streamlit_dashboard.py`
3. **Open browser:** Go to `http://localhost:8501`
4. **Start transcribing:** Paste YouTube URLs and extract!

### 💻 **Alternative: Command Line**
1. **Windows users:** Double-click `run_transcriber.bat`
2. **Everyone else:** Run `python simple_transcriber.py`
3. **Developers:** Check out `examples.py` for code samples

### 📚 **Need Help?**
- **Dashboard Guide:** See `DASHBOARD_GUIDE.md`
- **Command Line Guide:** See `USAGE_GUIDE.md`

**Happy transcribing! 🎬📝**
