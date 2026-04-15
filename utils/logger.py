# Logger utility for Douyin Live Stream Comment Processing
import logging
import os
from config.config import LOG_LEVEL, LOG_FILE

# Create logger instance
logger = logging.getLogger('douyin-live-comment-voice')
logger.setLevel(getattr(logging, LOG_LEVEL))
logger.propagate = False  # Prevent duplicate logging

# Set up console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(getattr(logging, LOG_LEVEL))
console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)

# Add file handler if LOG_FILE is specified
if LOG_FILE:
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setLevel(getattr(logging, LOG_LEVEL))
    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

def get_logger(name=None):
    """Get a logger with the specified name"""
    if name:
        return logger.getChild(name)
    return logger