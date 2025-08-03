#!/usr/bin/env python3
"""
Simple YouTube Transcriber
==========================

Quick script to extract YouTube video transcripts and save them as text files.

Usage:
    python simple_transcriber.py
    
Or run directly with a video:
    python simple_transcriber.py https://www.youtube.com/watch?v=VIDEO_ID
"""

import sys
import os
import re
from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi


def extract_video_id(url_or_id):
    """Extract video ID from YouTube URL or return the ID if it's already a video ID."""
    # If it's already a video ID (11 characters)
    if re.match(r'^[a-zA-Z0-9_-]{11}$', url_or_id):
        return url_or_id
    
    # Extract from different YouTube URL formats
    if 'youtu.be/' in url_or_id:
        return url_or_id.split('youtu.be/')[-1].split('?')[0]
    elif 'youtube.com' in url_or_id:
        parsed_url = urlparse(url_or_id)
        if 'watch' in parsed_url.path:
            query_params = parse_qs(parsed_url.query)
            if 'v' in query_params:
                return query_params['v'][0]
        elif 'embed' in parsed_url.path:
            return parsed_url.path.split('/embed/')[-1]
    
    raise ValueError(f"Invalid YouTube URL: {url_or_id}")


def download_transcript(video_url_or_id, language='en'):
    """Download transcript for a YouTube video and save it as a text file."""
    try:
        # Extract video ID
        video_id = extract_video_id(video_url_or_id)
        print(f"📹 Video ID: {video_id}")
        
        # Get transcript
        print(f"🔍 Fetching transcript...")
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id, languages=[language])
        
        # Format transcript
        transcript_lines = []
        for snippet in transcript:
            start_time = snippet.start
            minutes = int(start_time // 60)
            seconds = int(start_time % 60)
            time_stamp = f"[{minutes:02d}:{seconds:02d}]"
            text = snippet.text.strip()
            if text:
                transcript_lines.append(f"{time_stamp} {text}")
        
        # Save to file
        filename = f"transcript_{video_id}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"YouTube Transcript - Video ID: {video_id}\n")
            f.write(f"Language: {transcript.language} ({transcript.language_code})\n")
            f.write(f"Auto-generated: {transcript.is_generated}\n")
            f.write("=" * 50 + "\n\n")
            f.write("\n".join(transcript_lines))
            f.write(f"\n\n" + "=" * 50)
            f.write(f"\nTotal snippets: {len(transcript)}")
        
        print(f"✅ Transcript saved to: {filename}")
        print(f"📊 Total snippets: {len(transcript)}")
        print(f"🌍 Language: {transcript.language}")
        print(f"🤖 Auto-generated: {transcript.is_generated}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def main():
    """Main function."""
    print("🎬 Simple YouTube Transcript Downloader")
    print("=" * 40)
    
    # Check if URL was provided as command line argument
    if len(sys.argv) > 1:
        video_url = sys.argv[1]
        download_transcript(video_url)
        return
    
    # Interactive mode
    while True:
        video_url = input("\n🔗 Enter YouTube URL or video ID (or 'quit' to exit): ").strip()
        
        if video_url.lower() in ['quit', 'exit', 'q']:
            print("👋 Goodbye!")
            break
            
        if not video_url:
            print("❌ Please enter a valid URL or video ID")
            continue
            
        # Optional language selection
        language = input("🌍 Enter language code (default: en): ").strip() or 'en'
        
        success = download_transcript(video_url, language)
        
        if success:
            print("\n✅ Transcript downloaded successfully!")
        else:
            print("\n❌ Failed to download transcript. Try another video.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Interrupted by user. Goodbye!")
