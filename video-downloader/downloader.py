"""
Core video downloader module using yt-dlp
"""

import yt_dlp
from utils import (
    validate_url, 
    create_output_directory, 
    progress_hook,
    get_video_info_display
)
from config import (
    DEFAULT_OUTPUT_PATH, 
    VIDEO_QUALITIES,
    OUTPUT_TEMPLATE,
    TIMEOUT,
    RETRIES
)


class VideoDownloader:
    """
    Video downloader class using yt-dlp
    """
    
    def __init__(self, output_path=DEFAULT_OUTPUT_PATH):
        """
        Initialize downloader
        
        Args:
            output_path (str): Path to save downloaded videos
        """
        self.output_path = create_output_directory(output_path)
        
    def get_video_info(self, url):
        """
        Get video information without downloading
        
        Args:
            url (str): Video URL
            
        Returns:
            dict: Video information
        """
        if not validate_url(url):
            raise ValueError("Invalid URL provided")
        
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                return info
        except Exception as e:
            raise Exception(f"Failed to get video info: {str(e)}")
    
    def download_video(self, url, quality='best', audio_only=False):
        """
        Download video from URL
        
        Args:
            url (str): Video URL
            quality (str): Video quality (best, 1080p, 720p, etc.)
            audio_only (bool): Download audio only
            
        Returns:
            str: Path to downloaded file
        """
        if not validate_url(url):
            raise ValueError("Invalid URL provided")
        
        # Configure download options
        ydl_opts = {
            'format': VIDEO_QUALITIES.get(quality, 'best'),
            'outtmpl': f'{self.output_path}/{OUTPUT_TEMPLATE}',
            'progress_hooks': [progress_hook],
            'retries': RETRIES,
            'socket_timeout': TIMEOUT,
            'nocheckcertificate': True,
        }
        
        # Audio only settings
        if audio_only:
            ydl_opts['format'] = 'bestaudio/best'
            ydl_opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                print(f"\n📥 Starting download from: {url}")
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)
                print(f"\n✅ Successfully downloaded: {info.get('title')}")
                print(f"📁 Saved to: {filename}")
                return filename
        except Exception as e:
            raise Exception(f"Download failed: {str(e)}")
    
    def download_playlist(self, url, quality='best'):
        """
        Download entire playlist
        
        Args:
            url (str): Playlist URL
            quality (str): Video quality
            
        Returns:
            list: List of downloaded files
        """
        ydl_opts = {
            'format': VIDEO_QUALITIES.get(quality, 'best'),
            'outtmpl': f'{self.output_path}/%(playlist)s/%(title)s.%(ext)s',
            'progress_hooks': [progress_hook],
            'retries': RETRIES,
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                print(f"\n📥 Downloading playlist from: {url}")
                ydl.download([url])
                print(f"\n✅ Playlist download completed!")
        except Exception as e:
            raise Exception(f"Playlist download failed: {str(e)}")
