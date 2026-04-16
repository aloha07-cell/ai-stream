# Douyin live stream comment capture module
import time
import threading
import queue
import re
from utils.logger import get_logger
from utils.helpers import sanitize_comment, is_valid_comment
from config.config import DOUYIN_LIVE_URL, DOUYIN_ROOM_ID, MAX_COMMENT_QUEUE_SIZE
from modules.comment_capture.live_man import DouyinLiveWebFetcher

logger = get_logger('comment_capture')


class CommentCapture:
    def __init__(self, comment_queue):
        self.comment_queue = comment_queue
        self.fetcher = None
        self.running = False
        self.thread = None
    
    def start(self):
        """Start capturing comments"""
        try:
            logger.info(f"Starting comment capture with URL: {DOUYIN_LIVE_URL}")
            
            # Extract live_id from URL
            live_id = self._extract_live_id()
            if not live_id:
                logger.error("Could not extract live_id from URL")
                return False
            
            logger.info(f"Extracted live_id: {live_id}")
            
            # Initialize and start DouyinLiveWebFetcher
            self.fetcher = DouyinLiveWebFetcher(live_id, comment_queue=self.comment_queue, save_comments=True, save_file='comments.json')
            self.running = True
            
            # Start fetcher in a separate thread
            self.thread = threading.Thread(target=self._run_fetcher)
            self.thread.daemon = True
            self.thread.start()
            
            logger.info("Comment capture started successfully")
            return True
        except Exception as e:
            logger.error(f"Error starting comment capture: {e}")
            return False
    
    def stop(self):
        """Stop capturing comments"""
        try:
            self.running = False
            if self.fetcher:
                self.fetcher.stop()
            if self.thread:
                self.thread.join(timeout=5)
            logger.info("Comment capture stopped")
        except Exception as e:
            logger.error(f"Error stopping comment capture: {e}")
    
    def _extract_live_id(self):
        """Extract live_id from URL"""
        if DOUYIN_ROOM_ID:
            return DOUYIN_ROOM_ID
        
        if DOUYIN_LIVE_URL:
            # Extract live_id from URL
            match = re.search(r'live\.douyin\.com/(\d+)', DOUYIN_LIVE_URL)
            if match:
                return match.group(1)
        
        return None
    
    def _run_fetcher(self):
        """Run the fetcher in a separate thread"""
        try:
            self.fetcher.start()
        except Exception as e:
            logger.error(f"Error running fetcher: {e}")

