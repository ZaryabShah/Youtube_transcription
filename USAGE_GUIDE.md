# YouTube Transcript Extractor - Usage Guide

## 🚀 Quick Start

This project allows you to extract transcripts from YouTube videos and save them as text files.

### 📋 Prerequisites

- Python 3.8 or higher
- Internet connection

### 🔧 Installation

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Or install manually:**
   ```bash
   pip install requests defusedxml
   ```

## 🎯 Usage Options

### Option 1: Simple Transcriber (Recommended for beginners)

```bash
python simple_transcriber.py
```

**Features:**
- Easy interactive interface
- Extract transcripts from YouTube URLs or video IDs
- Save as formatted text files
- Support for different languages

**Example:**
```bash
python simple_transcriber.py https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

### Option 2: Advanced Transcriber (Full features)

```bash
python youtube_transcriber.py
```

**Features:**
- Interactive menu system
- Multiple language support
- Translation capabilities
- Batch processing
- List available transcripts
- Custom output directories

## 📝 Examples

### Extract English transcript:
```python
python simple_transcriber.py
# Enter: https://www.youtube.com/watch?v=VIDEO_ID
# Language: en (or press Enter for default)
```

### Extract German transcript:
```python
python simple_transcriber.py
# Enter: https://www.youtube.com/watch?v=VIDEO_ID
# Language: de
```

### Using video ID directly:
```python
python simple_transcriber.py
# Enter: dQw4w9WgXcQ
```

## 🌍 Supported Languages

Common language codes:
- `en` - English
- `es` - Spanish  
- `fr` - French
- `de` - German
- `it` - Italian
- `pt` - Portuguese
- `ru` - Russian
- `ja` - Japanese
- `ko` - Korean
- `zh` - Chinese
- `ar` - Arabic
- `hi` - Hindi

## 📄 Output Format

The transcript files will be saved as:
- `transcript_VIDEO_ID.txt` (simple version)
- `transcript_TITLE_VIDEO_ID.txt` (advanced version)

Example output format:
```
YouTube Transcript - Video ID: dQw4w9WgXcQ
Language: English (en)
Auto-generated: False
==================================================

[00:00] Never gonna give you up
[00:03] Never gonna let you down
[00:07] Never gonna run around and desert you
...
```

## 🚨 Common Issues & Solutions

### 1. "No transcript available"
- The video might not have subtitles/captions
- Try a different language code
- Some videos have transcripts disabled

### 2. "Request blocked" or "IP blocked"
- YouTube might be blocking your IP
- Try again later
- Consider using a VPN or proxy

### 3. "Invalid URL"
- Make sure you're using a valid YouTube URL
- Supported formats:
  - `https://www.youtube.com/watch?v=VIDEO_ID`
  - `https://youtu.be/VIDEO_ID`
  - Just the video ID: `VIDEO_ID`

### 4. "Module not found"
- Install dependencies: `pip install -r requirements.txt`

## 🔧 Advanced Usage (Python Code)

```python
from youtube_transcript_api import YouTubeTranscriptApi

# Basic usage
api = YouTubeTranscriptApi()
transcript = api.fetch('VIDEO_ID')

# With language preference
transcript = api.fetch('VIDEO_ID', languages=['de', 'en'])

# List available transcripts
transcript_list = api.list('VIDEO_ID')
for t in transcript_list:
    print(f"Language: {t.language}, Generated: {t.is_generated}")
```

## 📊 Features Summary

| Feature | Simple Script | Advanced Script |
|---------|---------------|----------------|
| Extract transcripts | ✅ | ✅ |
| Multiple languages | ✅ | ✅ |
| Translation | ❌ | ✅ |
| Batch processing | ❌ | ✅ |
| Custom output directory | ❌ | ✅ |
| List available transcripts | ❌ | ✅ |
| Interactive menu | ✅ | ✅ |

## 🤝 Need Help?

1. Check this guide first
2. Make sure dependencies are installed
3. Verify the YouTube URL is correct
4. Try with different videos to test

## 📜 License

This project uses the MIT licensed `youtube-transcript-api` library.

---

**Happy transcribing! 🎬📝**
