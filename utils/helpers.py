# Helper functions for Douyin Live Stream Comment Processing
import json
import os
from utils.logger import get_logger

logger = get_logger('helpers')

def load_json_file(file_path):
    """Load JSON file and return its content"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Error loading JSON file {file_path}: {e}")
        return {}

def save_json_file(file_path, data):
    """Save data to JSON file"""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        logger.error(f"Error saving JSON file {file_path}: {e}")
        return False

def sanitize_comment(comment):
    """Sanitize comment text"""
    if not comment:
        return ''
    # Remove special characters, trim whitespace
    return comment.strip().replace('\n', ' ').replace('\r', ' ')

def is_valid_comment(comment, min_length=1, max_length=500):
    """Check if comment is valid"""
    if not comment:
        return False
    comment_length = len(comment)
    return min_length <= comment_length <= max_length

def format_response(text):
    """Format response text for voice synthesis"""
    if not text:
        return ''
    # Remove extra whitespace, ensure proper punctuation
    text = ' '.join(text.split())
    if not text.endswith(('.', '!', '?')):
        text += '.'
    return text

def get_file_path(filename):
    """Get absolute path to file"""
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), filename)