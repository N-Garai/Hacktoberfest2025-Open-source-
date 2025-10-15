"""
Main entry point for Video Downloader
"""

import sys
from downloader import VideoDownloader
from utils import get_video_info_display
from config import VIDEO_QUALITIES, SUPPORTED_PLATFORMS


def print_banner():
    """Print application banner"""
    banner = """
    ╔════════════════════════════════════════╗
    ║     VIDEO DOWNLOADER v1.0              ║
    ║     Download videos from any platform  ║
    ╚════════════════════════════════════════╝
    """
    print(banner)


def print_menu():
    """Print main menu"""
    print("\n" + "="*50)
    print("MENU")
    print("="*50)
    print("1. Download Single Video")
    print("2. Download Audio Only")
    print("3. Download Playlist")
    print("4. Get Video Information")
    print("5. View Supported Platforms")
    print("6. Exit")
    print("="*50)


def get_quality_choice():
    """Get quality preference from user"""
    print("\nAvailable Qualities:")
    for idx, quality in enumerate(VIDEO_QUALITIES.keys(), 1):
        print(f"{idx}. {quality}")
    
    try:
        choice = int(input("\nSelect quality (1-{}): ".format(len(VIDEO_QUALITIES))))
        qualities = list(VIDEO_QUALITIES.keys())
        if 1 <= choice <= len(qualities):
            return qualities[choice - 1]
    except:
        pass
    
    print("Invalid choice. Using 'best' quality.")
    return 'best'


def main():
    """Main function"""
    print_banner()
    
    # Initialize downloader
    downloader = VideoDownloader()
    
    while True:
        print_menu()
        
        try:
            choice = input("\nEnter your choice (1-6): ").strip()
            
            if choice == '1':
                # Download single video
                url = input("\nEnter video URL: ").strip()
                quality = get_quality_choice()
                
                try:
                    downloader.download_video(url, quality=quality)
                except Exception as e:
                    print(f"\n❌ Error: {e}")
            
            elif choice == '2':
                # Download audio only
                url = input("\nEnter video URL: ").strip()
                
                try:
                    downloader.download_video(url, audio_only=True)
                except Exception as e:
                    print(f"\n❌ Error: {e}")
            
            elif choice == '3':
                # Download playlist
                url = input("\nEnter playlist URL: ").strip()
                quality = get_quality_choice()
                
                try:
                    downloader.download_playlist(url, quality=quality)
                except Exception as e:
                    print(f"\n❌ Error: {e}")
            
            elif choice == '4':
                # Get video information
                url = input("\nEnter video URL: ").strip()
                
                try:
                    info = downloader.get_video_info(url)
                    print("\n" + "="*50)
                    print("VIDEO INFORMATION")
                    print("="*50)
                    print(get_video_info_display(info))
                    print("="*50)
                except Exception as e:
                    print(f"\n❌ Error: {e}")
            
            elif choice == '5':
                # View supported platforms
                print("\n" + "="*50)
                print("SUPPORTED PLATFORMS")
                print("="*50)
                for platform in SUPPORTED_PLATFORMS:
                    print(f"✓ {platform}")
                print("="*50)
                print("\nNote: Works with 1000+ websites!")
            
            elif choice == '6':
                # Exit
                print("\n👋 Thank you for using Video Downloader!")
                print("="*50)
                sys.exit(0)
            
            else:
                print("\n❌ Invalid choice! Please enter 1-6.")
        
        except KeyboardInterrupt:
            print("\n\n👋 Exiting...")
            sys.exit(0)
        except Exception as e:
            print(f"\n❌ Unexpected error: {e}")


if __name__ == "__main__":
    main()
