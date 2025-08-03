#!/usr/bin/env python3
"""
YouTube Transcriber Script
==========================

This script allows you to extract transcripts from YouTube videos and save them as text files.

Usage:
    python youtube_transcriber.py

Features:
- Extract transcripts from YouTube URLs or video IDs
- Save transcripts to .txt files
- Support for multiple languages
- Automatic translation capabilities
- Handle both manual and auto-generated subtitles

Author: Generated for YouTube Transcript API project
"""

import os
import sys
import re
from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    TranscriptsDisabled, 
    NoTranscriptFound, 
    VideoUnavailable,
    RequestBlocked,
    IpBlocked
)


def extract_video_id(url_or_id):
    """
    Extract video ID from YouTube URL or return the ID if it's already a video ID.
    
    Args:
        url_or_id (str): YouTube URL or video ID
        
    Returns:
        str: Video ID
        
    Raises:
        ValueError: If the URL format is invalid
    """
    # If it's already a video ID (11 characters, alphanumeric and some special chars)
    if re.match(r'^[a-zA-Z0-9_-]{11}$', url_or_id):
        return url_or_id
    
    # Parse different YouTube URL formats
    if 'youtube.com' in url_or_id or 'youtu.be' in url_or_id:
        if 'youtu.be/' in url_or_id:
            # Handle youtu.be format
            return url_or_id.split('youtu.be/')[-1].split('?')[0]
        elif 'youtube.com' in url_or_id:
            # Handle youtube.com format
            parsed_url = urlparse(url_or_id)
            if 'watch' in parsed_url.path:
                query_params = parse_qs(parsed_url.query)
                if 'v' in query_params:
                    return query_params['v'][0]
            elif 'embed' in parsed_url.path:
                return parsed_url.path.split('/embed/')[-1]
    
    raise ValueError(f"Invalid YouTube URL or video ID: {url_or_id}")


def get_safe_filename(title, video_id):
    """
    Create a safe filename from video title and ID.
    
    Args:
        title (str): Video title
        video_id (str): Video ID
        
    Returns:
        str: Safe filename
    """
    # Remove invalid characters for filenames
    safe_title = re.sub(r'[<>:"/\\|?*]', '_', title)
    safe_title = safe_title.strip()
    
    # Limit length and add video ID
    if len(safe_title) > 50:
        safe_title = safe_title[:50].strip()
    
    return f"{safe_title}_{video_id}.txt"


def format_transcript(transcript_data):
    """
    Format transcript data into readable text.
    
    Args:
        transcript_data: FetchedTranscript object
        
    Returns:
        str: Formatted transcript text
    """
    formatted_lines = []
    
    for snippet in transcript_data:
        # Format: [MM:SS] Text
        start_time = snippet.start
        minutes = int(start_time // 60)
        seconds = int(start_time % 60)
        time_stamp = f"[{minutes:02d}:{seconds:02d}]"
        
        # Clean up the text
        text = snippet.text.strip()
        if text:
            formatted_lines.append(f"{time_stamp} {text}")
    
    return "\n".join(formatted_lines)


def save_transcript_to_file(transcript_text, filename, video_info):
    """
    Save transcript to a text file with metadata.
    
    Args:
        transcript_text (str): Formatted transcript text
        filename (str): Output filename
        video_info (dict): Video metadata
    """
    with open(filename, 'w', encoding='utf-8') as f:
        # Write header with metadata
        f.write("="*60 + "\n")
        f.write("YOUTUBE VIDEO TRANSCRIPT\n")
        f.write("="*60 + "\n")
        f.write(f"Video ID: {video_info['video_id']}\n")
        f.write(f"Language: {video_info['language']}\n")
        f.write(f"Language Code: {video_info['language_code']}\n")
        f.write(f"Auto-generated: {video_info['is_generated']}\n")
        f.write(f"Total Snippets: {video_info['snippet_count']}\n")
        f.write("="*60 + "\n\n")
        
        # Write transcript
        f.write(transcript_text)
        
        f.write(f"\n\n{'='*60}\n")
        f.write("End of Transcript\n")
        f.write("="*60 + "\n")


def transcribe_video(url_or_id, languages=['en'], output_dir=None, translate_to=None):
    """
    Main function to transcribe a YouTube video.
    
    Args:
        url_or_id (str): YouTube URL or video ID
        languages (list): Preferred languages in order of preference
        output_dir (str): Output directory (default: current directory)
        translate_to (str): Language code to translate to (optional)
        
    Returns:
        bool: Success status
    """
    try:
        # Extract video ID
        video_id = extract_video_id(url_or_id)
        print(f"📹 Processing video ID: {video_id}")
        
        # Initialize API
        api = YouTubeTranscriptApi()
        
        # Get transcript
        print(f"🔍 Fetching transcript in languages: {languages}")
        transcript = api.fetch(video_id, languages=languages)
        
        # Translate if requested
        if translate_to:
            print(f"🌐 Translating to: {translate_to}")
            # First get the transcript list to access translation
            transcript_list = api.list(video_id)
            original_transcript = transcript_list.find_transcript(languages)
            translated_transcript = original_transcript.translate(translate_to)
            transcript = translated_transcript.fetch()
        
        # Format transcript
        transcript_text = format_transcript(transcript)
        
        # Prepare video info
        video_info = {
            'video_id': transcript.video_id,
            'language': transcript.language,
            'language_code': transcript.language_code,
            'is_generated': transcript.is_generated,
            'snippet_count': len(transcript)
        }
        
        # Create filename
        title = f"transcript_{video_id}"
        if translate_to:
            title += f"_translated_to_{translate_to}"
        filename = get_safe_filename(title, video_id)
        
        # Set output directory
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
            filename = os.path.join(output_dir, filename)
        
        # Save to file
        save_transcript_to_file(transcript_text, filename, video_info)
        
        print(f"✅ Transcript saved to: {filename}")
        print(f"📊 Total snippets: {len(transcript)}")
        print(f"🌍 Language: {transcript.language} ({transcript.language_code})")
        print(f"🤖 Auto-generated: {transcript.is_generated}")
        
        return True
        
    except ValueError as e:
        print(f"❌ Error: {e}")
        return False
        
    except (TranscriptsDisabled, NoTranscriptFound) as e:
        print(f"❌ No transcript available for this video: {e}")
        return False
        
    except VideoUnavailable as e:
        print(f"❌ Video is unavailable: {e}")
        return False
        
    except (RequestBlocked, IpBlocked) as e:
        print(f"❌ Request blocked (IP ban): {e}")
        print("💡 Tip: You might need to use a proxy or try again later")
        return False
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False


def list_available_transcripts(url_or_id):
    """
    List all available transcripts for a video.
    
    Args:
        url_or_id (str): YouTube URL or video ID
    """
    try:
        video_id = extract_video_id(url_or_id)
        api = YouTubeTranscriptApi()
        transcript_list = api.list(video_id)
        
        print(f"📋 Available transcripts for video: {video_id}")
        print("-" * 50)
        
        for transcript in transcript_list:
            print(f"🌍 Language: {transcript.language} ({transcript.language_code})")
            print(f"🤖 Auto-generated: {transcript.is_generated}")
            print(f"🔄 Translatable: {transcript.is_translatable}")
            if transcript.is_translatable:
                print(f"📝 Available translations: {len(transcript.translation_languages)} languages")
            print("-" * 30)
            
    except Exception as e:
        print(f"❌ Error listing transcripts: {e}")


def main():
    """Main interactive function."""
    print("🎬 YouTube Transcript Extractor")
    print("=" * 40)
    
    while True:
        print("\nOptions:")
        print("1. Extract transcript from YouTube video")
        print("2. List available transcripts for a video")
        print("3. Extract and translate transcript")
        print("4. Batch process multiple videos")
        print("5. Exit")
        
        choice = input("\nSelect an option (1-5): ").strip()
        
        if choice == '1':
            url_or_id = input("\nEnter YouTube URL or video ID: ").strip()
            if not url_or_id:
                print("❌ Please enter a valid URL or video ID")
                continue
                
            # Ask for language preference
            lang_input = input("Enter preferred languages (comma-separated, default: en): ").strip()
            languages = [lang.strip() for lang in lang_input.split(',')] if lang_input else ['en']
            
            # Ask for output directory
            output_dir = input("Enter output directory (press Enter for current directory): ").strip()
            output_dir = output_dir if output_dir else None
            
            transcribe_video(url_or_id, languages, output_dir)
            
        elif choice == '2':
            url_or_id = input("\nEnter YouTube URL or video ID: ").strip()
            if not url_or_id:
                print("❌ Please enter a valid URL or video ID")
                continue
            list_available_transcripts(url_or_id)
            
        elif choice == '3':
            url_or_id = input("\nEnter YouTube URL or video ID: ").strip()
            if not url_or_id:
                print("❌ Please enter a valid URL or video ID")
                continue
                
            source_lang = input("Enter source language (default: en): ").strip() or 'en'
            target_lang = input("Enter target language for translation (e.g., es, fr, de): ").strip()
            
            if not target_lang:
                print("❌ Please enter a target language")
                continue
                
            output_dir = input("Enter output directory (press Enter for current directory): ").strip()
            output_dir = output_dir if output_dir else None
            
            transcribe_video(url_or_id, [source_lang], output_dir, target_lang)
            
        elif choice == '4':
            print("\n📝 Enter video URLs/IDs (one per line, empty line to finish):")
            videos = []
            while True:
                video = input().strip()
                if not video:
                    break
                videos.append(video)
            
            if not videos:
                print("❌ No videos entered")
                continue
                
            lang_input = input("Enter preferred languages (comma-separated, default: en): ").strip()
            languages = [lang.strip() for lang in lang_input.split(',')] if lang_input else ['en']
            
            output_dir = input("Enter output directory (press Enter for current directory): ").strip()
            output_dir = output_dir if output_dir else None
            
            success_count = 0
            for i, video in enumerate(videos, 1):
                print(f"\n📹 Processing video {i}/{len(videos)}: {video}")
                if transcribe_video(video, languages, output_dir):
                    success_count += 1
                    
            print(f"\n✅ Successfully processed {success_count}/{len(videos)} videos")
            
        elif choice == '5':
            print("👋 Goodbye!")
            break
            
        else:
            print("❌ Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Interrupted by user. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)
