#!/usr/bin/env python3
"""
YouTube Transcript API Examples
===============================

This script demonstrates various ways to use the YouTube Transcript API.
"""

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter, JSONFormatter
import json
import os


def example_basic_usage():
    """Example 1: Basic transcript extraction"""
    print("🔥 Example 1: Basic Transcript Extraction")
    print("-" * 40)
    
    try:
        # Replace with any video ID you want to test
        video_id = "dQw4w9WgXcQ"  # Rick Roll for testing
        
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id)
        
        print(f"📹 Video ID: {transcript.video_id}")
        print(f"🌍 Language: {transcript.language}")
        print(f"🤖 Auto-generated: {transcript.is_generated}")
        print(f"📊 Total snippets: {len(transcript)}")
        print("\n📝 First 3 snippets:")
        
        for i, snippet in enumerate(transcript[:3]):
            print(f"  [{i+1}] {snippet.start:.1f}s: {snippet.text}")
            
    except Exception as e:
        print(f"❌ Error: {e}")


def example_language_selection():
    """Example 2: Language preference"""
    print("\n🌍 Example 2: Language Preference")
    print("-" * 40)
    
    try:
        video_id = "dQw4w9WgXcQ"
        
        api = YouTubeTranscriptApi()
        # Try German first, then English
        transcript = api.fetch(video_id, languages=['de', 'en'])
        
        print(f"📹 Video ID: {transcript.video_id}")
        print(f"🌍 Selected language: {transcript.language}")
        print(f"📊 Snippet count: {len(transcript)}")
        
    except Exception as e:
        print(f"❌ Error: {e}")


def example_list_transcripts():
    """Example 3: List available transcripts"""
    print("\n📋 Example 3: List Available Transcripts")
    print("-" * 40)
    
    try:
        video_id = "dQw4w9WgXcQ"
        
        api = YouTubeTranscriptApi()
        transcript_list = api.list(video_id)
        
        print(f"📹 Video ID: {video_id}")
        print("Available transcripts:")
        
        for transcript in transcript_list:
            print(f"  🌍 {transcript.language} ({transcript.language_code})")
            print(f"     🤖 Auto-generated: {transcript.is_generated}")
            print(f"     🔄 Translatable: {transcript.is_translatable}")
            if transcript.is_translatable:
                print(f"     📝 Translation languages: {len(transcript.translation_languages)}")
            print()
            
    except Exception as e:
        print(f"❌ Error: {e}")


def example_translation():
    """Example 4: Translate transcript"""
    print("\n🔄 Example 4: Translate Transcript")
    print("-" * 40)
    
    try:
        video_id = "dQw4w9WgXcQ"
        
        api = YouTubeTranscriptApi()
        transcript_list = api.list(video_id)
        
        # Get English transcript
        english_transcript = transcript_list.find_transcript(['en'])
        print(f"📍 Original: {english_transcript.language}")
        
        # Translate to Spanish
        spanish_transcript = english_transcript.translate('es')
        translated_data = spanish_transcript.fetch()
        
        print(f"🔄 Translated to: {translated_data.language}")
        print("\n📝 First 2 translated snippets:")
        
        for i, snippet in enumerate(translated_data[:2]):
            print(f"  [{i+1}] {snippet.start:.1f}s: {snippet.text}")
            
    except Exception as e:
        print(f"❌ Error: {e}")


def example_formatters():
    """Example 5: Using formatters"""
    print("\n📄 Example 5: Using Formatters")
    print("-" * 40)
    
    try:
        video_id = "dQw4w9WgXcQ"
        
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id)
        
        # Text formatter
        text_formatter = TextFormatter()
        text_output = text_formatter.format_transcript(transcript)
        
        print("📝 Text Format (first 200 chars):")
        print(text_output[:200] + "...")
        
        # JSON formatter
        json_formatter = JSONFormatter()
        json_output = json_formatter.format_transcript(transcript)
        
        print(f"\n📊 JSON Format (snippet count): {len(json.loads(json_output))}")
        
        # Save formatted outputs
        with open("example_transcript.txt", "w", encoding="utf-8") as f:
            f.write(text_output)
        
        with open("example_transcript.json", "w", encoding="utf-8") as f:
            f.write(json_output)
            
        print("✅ Formatted files saved: example_transcript.txt, example_transcript.json")
        
    except Exception as e:
        print(f"❌ Error: {e}")


def example_batch_processing():
    """Example 6: Process multiple videos"""
    print("\n📚 Example 6: Batch Processing")
    print("-" * 40)
    
    # Example video IDs (replace with your own)
    video_ids = [
        "dQw4w9WgXcQ",  # Rick Roll
        # Add more video IDs here for testing
    ]
    
    api = YouTubeTranscriptApi()
    
    for i, video_id in enumerate(video_ids, 1):
        try:
            print(f"📹 Processing video {i}/{len(video_ids)}: {video_id}")
            transcript = api.fetch(video_id)
            
            # Save each transcript
            filename = f"batch_transcript_{video_id}.txt"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(f"Video ID: {transcript.video_id}\n")
                f.write(f"Language: {transcript.language}\n")
                f.write("=" * 50 + "\n\n")
                
                for snippet in transcript:
                    minutes = int(snippet.start // 60)
                    seconds = int(snippet.start % 60)
                    f.write(f"[{minutes:02d}:{seconds:02d}] {snippet.text}\n")
            
            print(f"✅ Saved: {filename}")
            
        except Exception as e:
            print(f"❌ Failed for {video_id}: {e}")


def example_error_handling():
    """Example 7: Error handling"""
    print("\n🚨 Example 7: Error Handling")
    print("-" * 40)
    
    from youtube_transcript_api._errors import (
        TranscriptsDisabled, 
        NoTranscriptFound, 
        VideoUnavailable
    )
    
    # Test with various scenarios
    test_cases = [
        ("invalid_video_id", "Invalid video ID"),
        ("dQw4w9WgXcQ", "Valid video ID"),
    ]
    
    api = YouTubeTranscriptApi()
    
    for video_id, description in test_cases:
        print(f"🧪 Testing: {description} ({video_id})")
        
        try:
            transcript = api.fetch(video_id)
            print(f"✅ Success: Found {len(transcript)} snippets")
            
        except TranscriptsDisabled:
            print("❌ Transcripts are disabled for this video")
        except NoTranscriptFound:
            print("❌ No transcript found for this video")
        except VideoUnavailable:
            print("❌ Video is unavailable")
        except Exception as e:
            print(f"❌ Other error: {e}")


def main():
    """Run all examples"""
    print("🎬 YouTube Transcript API Examples")
    print("=" * 50)
    
    examples = [
        example_basic_usage,
        example_language_selection,
        example_list_transcripts,
        example_translation,
        example_formatters,
        example_batch_processing,
        example_error_handling,
    ]
    
    for example_func in examples:
        try:
            example_func()
        except KeyboardInterrupt:
            print("\n\n👋 Interrupted by user")
            break
        except Exception as e:
            print(f"\n❌ Example failed: {e}")
        
        input("\nPress Enter to continue to next example...")
    
    print("\n🎉 All examples completed!")
    
    # Clean up example files
    cleanup_files = [
        "example_transcript.txt",
        "example_transcript.json",
    ]
    
    cleanup_files.extend([f"batch_transcript_{vid}.txt" for vid in ["dQw4w9WgXcQ"]])
    
    for file in cleanup_files:
        if os.path.exists(file):
            try:
                os.remove(file)
                print(f"🧹 Cleaned up: {file}")
            except:
                pass


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
