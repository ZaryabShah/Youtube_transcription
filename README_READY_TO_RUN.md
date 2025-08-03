# 🎬 YouTube Transcript Extractor - Ready to Run!

A simple, ready-to-use Python project for extracting transcripts from YouTube videos and saving them as text files.

## 🚀 Quick Start (3 Steps!)

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
| `simple_transcriber.py` | 🌟 **Start here!** Easy-to-use transcript extractor |
| `youtube_transcriber.py` | Advanced version with more features |
| `examples.py` | Code examples and demonstrations |
| `run_transcriber.bat` | Windows batch file for one-click execution |
| `requirements.txt` | Dependencies list |
| `USAGE_GUIDE.md` | Detailed usage instructions |

## 🎯 What This Does

✅ **Extracts transcripts** from YouTube videos  
✅ **Saves as text files** with timestamps  
✅ **Supports multiple languages** (English, Spanish, German, etc.)  
✅ **Works with video URLs or IDs**  
✅ **Handles auto-generated and manual subtitles**  
✅ **Translation capabilities** (advanced version)  
✅ **Batch processing** (advanced version)  

## 🔧 Usage Examples

### Basic Usage
```bash
python simple_transcriber.py
# Enter: https://www.youtube.com/watch?v=VIDEO_ID
```

### Command Line Usage
```bash
python simple_transcriber.py https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

### Different Languages
```bash
python simple_transcriber.py
# Enter URL, then language: es (for Spanish)
```

### Windows Users - One Click!
Just double-click: `run_transcriber.bat`

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

1. **Windows users:** Double-click `run_transcriber.bat`
2. **Everyone else:** Run `python simple_transcriber.py`
3. **Developers:** Check out `examples.py` for code samples

**Happy transcribing! 🎬📝**
