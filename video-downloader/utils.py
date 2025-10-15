"""
Utility functions for Video Downloader
"""

import os
import re
from urllib.parse import urlparse
from config import DEFAULT_OUTPUT_PATH


def validate_url(url):
    """
    Validate if the provided URL is valid
    
    Args:
        url (str): URL to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False


def sanitize_filename(filename):
    """
    Remove invalid characters from filename
    
    Args:
        filename (str): Original filename
        
    Returns:
        str: Sanitized filename
    """
    # Remove invalid characters
    filename = re.sub(r'[<>:"/\\|?*]', '', filename)
    # Limit length
    return filename[:200]


def format_size(bytes):
    """
    Convert bytes to human-readable format
    
    Args:
        bytes (int): Size in bytes
        
    Returns:
        str: Formatted size string
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024.0:
            return f"{bytes:.2f} {unit}"
        bytes /= 1024.0


def create_output_directory(path=DEFAULT_OUTPUT_PATH):
    """
    Create output directory if it doesn't exist
    
    Args:
        path (str): Directory path
        
    Returns:
        str: Absolute path of directory
    """
    if not os.path.exists(path):
        os.makedirs(path)
    return os.path.abspath(path)


def get_video_info_display(info):
    """
    Format video information for display
    
    Args:
        info (dict): Video information dictionary
        
    Returns:
        str: Formatted video info
    """
    title = info.get('title', 'Unknown')
    duration = info.get('duration', 0)
    uploader = info.get('uploader', 'Unknown')
    views = info.get('view_count', 0)
    
    minutes = duration // 60
    seconds = duration % 60
    
    return f"""
    Title: {title}
    Duration: {minutes}m {seconds}s
    Uploader: {uploader}
    Views: {views:,}
    """


def progress_hook(d):
    """
    Display download progress
    
    Args:
        d (dict): Progress dictionary from yt-dlp
    """
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', 'N/A')
        speed = d.get('_speed_str', 'N/A')
        eta = d.get('_eta_str', 'N/A')
        print(f"\rDownloading: {percent} | Speed: {speed} | ETA: {eta}", end='')
    elif d['status'] == 'finished':
        print(f"\n✓ Download completed! Now processing...")
