# Configuration settings for Douyin Live Stream Comment Processing
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Douyin Live Stream settings
DOUYIN_LIVE_URL = os.getenv('DOUYIN_LIVE_URL', 'https://www.douyin.com/live/1234567890')
DOUYIN_ROOM_ID = os.getenv('DOUYIN_ROOM_ID', '')

# Alibaba Bailian API settings
BAILIAN_API_KEY = os.getenv('BAILIAN_API_KEY', '')
BAILIAN_REGION = os.getenv('BAILIAN_REGION', 'cn-shanghai')
BAILIAN_TEXT_MODEL = os.getenv('BAILIAN_TEXT_MODEL', 'qwen-plus')  # 文本处理模型
BAILIAN_VOICE_MODEL = os.getenv('BAILIAN_VOICE_MODEL', 'qwen-tts')  # 语音合成模型

# Audio settings
AUDIO_VOLUME = float(os.getenv('AUDIO_VOLUME', '0.8'))
AUDIO_SAMPLE_RATE = int(os.getenv('AUDIO_SAMPLE_RATE', '22050'))

# Product introduction settings
PRODUCT_INTRO_TIMEOUT = int(os.getenv('PRODUCT_INTRO_TIMEOUT', '30'))  # seconds
PRODUCT_DATA_FILE = os.getenv('PRODUCT_DATA_FILE', 'product_intro.json')

# Comment processing settings
COMMENT_FILTER_THRESHOLD = float(os.getenv('COMMENT_FILTER_THRESHOLD', '0.5'))
MAX_COMMENT_QUEUE_SIZE = int(os.getenv('MAX_COMMENT_QUEUE_SIZE', '100'))

# Logging settings
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
LOG_FILE = os.getenv('LOG_FILE', 'app.log')

# System settings
MAX_RESPONSE_TIME = int(os.getenv('MAX_RESPONSE_TIME', '3'))  # seconds
API_REQUEST_TIMEOUT = int(os.getenv('API_REQUEST_TIMEOUT', '5'))  # seconds
USE_REAL_API = os.getenv('USE_REAL_API', 'false').lower() == 'true'

# Voice synthesis settings
VOICE_TYPE = os.getenv('VOICE_TYPE', 'zh-CN-YunxiNeural')
VOICE_SPEED = float(os.getenv('VOICE_SPEED', '1.0'))
VOICE_PITCH = float(os.getenv('VOICE_PITCH', '1.0'))