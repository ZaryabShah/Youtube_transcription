# 🌐 YouTube Transcript Extractor - Streamlit Dashboard

A beautiful, interactive web dashboard for extracting YouTube video transcripts with advanced features and real-time preview.

## 🚀 Quick Start

### Method 1: Windows One-Click (Recommended)
Double-click: **`run_dashboard.bat`** or **`run_dashboard.ps1`**

### Method 2: Command Line
```bash
streamlit run streamlit_dashboard.py
```

### Method 3: Custom Port
```bash
streamlit run streamlit_dashboard.py --server.port 8080
```

## 🌟 Dashboard Features

### ✨ **Core Features**
- **🔗 URL Input**: Paste any YouTube URL or video ID
- **👁️ Live Preview**: See transcript immediately on the dashboard  
- **⏰ Timestamp Toggle**: Switch between with/without timestamps in real-time
- **🌍 Multi-Language**: Support for 12+ languages
- **🔄 Translation**: Translate transcripts to different languages
- **📱 Responsive**: Works on desktop, tablet, and mobile
- **🎬 Video Embed**: Preview the video directly in the dashboard

### 💾 **Download Options**
- **📝 With Timestamps**: `[00:15] Text content here`
- **📄 Without Timestamps**: `Clean text content`
- **📊 JSON Format**: Raw data with timing information
- **🎨 Multiple Formats**: TXT, JSON with metadata headers

### 🎛️ **Advanced Options**
- **🌐 Language Selection**: Choose preferred transcript language
- **🔄 Auto-Translation**: Translate to target language
- **📋 Available Transcripts**: See all languages for any video
- **🤖 Transcript Types**: Manual vs auto-generated indicators
- **📊 Statistics**: Snippet count, video info, processing time

## 🖥️ Dashboard Interface

### 📱 **Main Layout**
```
┌─────────────────────────────────────────────────────────┐
│                    🎬 YouTube Transcript Extractor      │
├─────────────────────────────┬───────────────────────────┤
│         📝 Extract          │       ℹ️ Video Info       │
│                             │                           │
│  🔗 URL Input               │  📹 Video ID              │
│  🌍 Language Options        │  🎬 Video Embed           │
│  ⏰ Timestamp Toggle        │  📊 Quick Stats           │
│  🔄 Translation Settings    │                           │
│  🚀 Extract Button          │                           │
├─────────────────────────────┴───────────────────────────┤
│                     📄 Transcript Display               │
│  👁️ Display Format Toggle  📊 Snippet Count            │
│  📝 Live Transcript Preview (Scrollable)                │
├─────────────────────────────────────────────────────────┤
│                    💾 Download Section                  │
│  📥 With Timestamps  📄 Without Timestamps  📊 JSON     │
├─────────────────────────────────────────────────────────┤
│             📋 Available Transcripts (Expandable)       │
│  🌍 All languages, types, and translation options       │
└─────────────────────────────────────────────────────────┘
```

### 🎛️ **Sidebar Features**
- **📚 Quick Guide**: Step-by-step instructions
- **✨ Features List**: All available capabilities
- **🔧 System Info**: Current server time
- **📊 Session Info**: Current video and transcript status
- **🔄 Clear Data**: Reset all session data

## 🎯 How to Use

### 1️⃣ **Basic Usage**
1. **Start Dashboard**: Double-click `run_dashboard.bat`
2. **Enter URL**: Paste YouTube URL in the input field
3. **Set Options**: Choose language and timestamp preference
4. **Extract**: Click "🚀 Extract Transcript"
5. **View**: See transcript instantly on the dashboard
6. **Download**: Choose your preferred format and download

### 2️⃣ **Advanced Usage**
1. **Translation**: Enable "🔄 Enable Translation" and select target language
2. **Language Selection**: Choose from 12+ supported languages
3. **Format Toggle**: Switch between with/without timestamps anytime
4. **Multiple Downloads**: Download in all formats as needed
5. **Video Preview**: Watch the video embedded in the dashboard

### 3️⃣ **Batch Workflow**
1. Extract transcript from first video
2. Download in preferred format
3. Click "🔄 Clear All Data" in sidebar
4. Enter next video URL
5. Repeat process

## 🌍 Supported Languages

| Display Name | Code | Display Name | Code |
|--------------|------|--------------|------|
| English      | `en` | Spanish      | `es` |
| French       | `fr` | German       | `de` |
| Italian      | `it` | Portuguese   | `pt` |
| Russian      | `ru` | Japanese     | `ja` |
| Korean       | `ko` | Chinese      | `zh` |
| Arabic       | `ar` | Hindi        | `hi` |

## 📋 Supported URL Formats

✅ **Full YouTube URLs**
- `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
- `https://youtube.com/watch?v=dQw4w9WgXcQ`

✅ **Short URLs**
- `https://youtu.be/dQw4w9WgXcQ`

✅ **Embed URLs**
- `https://www.youtube.com/embed/dQw4w9WgXcQ`

✅ **Video IDs Only**
- `dQw4w9WgXcQ`

## 💡 Pro Tips

### ⚡ **Performance Tips**
- Dashboard loads instantly after first use
- Transcripts are cached during session
- Use "Clear Data" button to free memory
- Multiple formats download instantly

### 🎯 **Best Practices**
- Test with well-known videos first (like the Rick Roll example)
- Check "Available Transcripts" section for language options
- Use translation feature for content in foreign languages
- Download both timestamp versions for different use cases

### 🔧 **Troubleshooting**
- **Slow loading**: Check internet connection
- **No transcript**: Try different language or check if video has captions
- **Translation error**: Ensure source transcript supports translation
- **Download issues**: Try different browser or disable ad blockers

## 🌐 Network Configuration

### 🏠 **Local Access** (Default)
- **URL**: `http://localhost:8501`
- **Access**: Only from your computer

### 🌍 **Network Access** (Advanced)
To make dashboard accessible from other devices on your network:

1. **Find your IP**: `ipconfig` (Windows) or `ifconfig` (Mac/Linux)
2. **Run with network access**:
   ```bash
   streamlit run streamlit_dashboard.py --server.address 0.0.0.0 --server.port 8501
   ```
3. **Access from other devices**: `http://YOUR_IP:8501`

### 🔒 **Security Note**
- Dashboard runs locally by default (secure)
- Network access exposes dashboard to local network
- Don't expose to internet without proper security measures

## 🎨 Dashboard Themes

The dashboard automatically adapts to your system theme:
- **🌞 Light Mode**: Clean, professional appearance
- **🌙 Dark Mode**: Easy on the eyes for long sessions
- **📱 Mobile**: Responsive design for all screen sizes

## 🔧 Customization

### 🎨 **UI Customization**
The dashboard includes custom CSS for:
- Beautiful gradient headers
- Color-coded status messages
- Responsive layout design
- Professional styling

### ⚙️ **Configuration**
Settings can be modified in `.streamlit/config.toml`:
- Default port (8501)
- Browser auto-open
- Performance settings
- CORS settings for network access

## 📊 Technical Details

### 🔧 **Technology Stack**
- **Frontend**: Streamlit (Python web framework)
- **Backend**: YouTube Transcript API
- **UI**: Custom CSS + Streamlit components
- **Data**: JSON, TXT export formats

### ⚡ **Performance**
- **Startup**: ~2-3 seconds
- **Transcript Extraction**: ~2-5 seconds per video
- **Memory Usage**: Low (~50MB typical)
- **Concurrent Users**: Supports multiple browser tabs

### 🌐 **Browser Support**
- ✅ Chrome (Recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ✅ Mobile browsers

## 🚨 Error Handling

The dashboard gracefully handles:
- **Invalid URLs**: Clear error messages
- **No transcripts**: Suggests alternatives
- **Network issues**: Retry suggestions
- **IP blocking**: VPN recommendations
- **Translation errors**: Fallback options

## 📱 Mobile Experience

The dashboard is fully responsive:
- **📱 Mobile**: Touch-friendly interface
- **📟 Tablet**: Optimized layout
- **💻 Desktop**: Full feature set
- **🖥️ Large screens**: Expanded layout

## 🎉 Ready to Start?

1. **Quick Start**: Double-click `run_dashboard.bat`
2. **Open Browser**: Go to `http://localhost:8501`
3. **Start Transcribing**: Paste any YouTube URL and extract!

**The dashboard will be running at: `http://localhost:8501`**

---

**🎬 Happy transcribing with your new dashboard! 🚀**
