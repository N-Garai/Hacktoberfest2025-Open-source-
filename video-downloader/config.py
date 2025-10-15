"""
Configuration settings for Video Downloader
"""

# Download settings
DEFAULT_OUTPUT_PATH = "downloads"
DEFAULT_FORMAT = "best"
DEFAULT_QUALITY = "1080p"

# Supported video qualities
VIDEO_QUALITIES = {
    '144p': 'worst',
    '240p': 'worstvideo+worstaudio',
    '360p': '18',
    '480p': '135+140',
    '720p': '136+140',
    '1080p': '137+140',
    'best': 'bestvideo+bestaudio/best'
}

# File naming template
OUTPUT_TEMPLATE = '%(title)s.%(ext)s'

# Connection settings
TIMEOUT = 30
RETRIES = 3

# Supported platforms
SUPPORTED_PLATFORMS = [
    'YouTube',
    'Vimeo',
    'Dailymotion',
    'Facebook',
    'Instagram',
    'Twitter',
    'TikTok'
]
