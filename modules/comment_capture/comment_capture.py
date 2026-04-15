# Douyin live stream comment capture module
import time
import threading
import random
from utils.logger import get_logger
from utils.helpers import sanitize_comment, is_valid_comment
from config.config import DOUYIN_LIVE_URL, DOUYIN_ROOM_ID, MAX_COMMENT_QUEUE_SIZE

logger = get_logger('comment_capture')

class CommentCapture:
    def __init__(self, comment_queue):
        self.comment_queue = comment_queue
        self.client = None
        self.running = False
        self.thread = None
        self.mock_comments = [
            "这个产品怎么样？",
            "价格是多少？",
            "有什么优惠活动吗？",
            "质量如何？",
            "能便宜点吗？",
            "支持退换货吗？",
            "什么时候发货？",
            "有什么颜色可选？",
            "尺寸合适吗？",
            "使用方法是什么？"
        ]
        self.mock_users = ["用户1", "用户2", "用户3", "用户4", "用户5"]
    
    def start(self):
        """Start capturing comments"""
        try:
            # Try to import DouyinLiveClient
            try:
                from douyin_live_sdk import DouyinLiveClient
                # Initialize Douyin live client
                if DOUYIN_ROOM_ID:
                    self.client = DouyinLiveClient(room_id=DOUYIN_ROOM_ID)
                else:
                    self.client = DouyinLiveClient(url=DOUYIN_LIVE_URL)
                
                # Register comment callback
                self.client.on_comment(self._on_comment)
                
                # Start client
                self.client.start()
                logger.info("Using real Douyin live comment capture")
            except ImportError:
                # Mock implementation for demonstration
                logger.warning("douyin_live_sdk not available, using mock implementation")
            
            self.running = True
            
            # Start monitoring thread
            self.thread = threading.Thread(target=self._monitor)
            self.thread.daemon = True
            self.thread.start()
            
            # Start mock comment generator if using mock implementation
            if not self.client:
                mock_thread = threading.Thread(target=self._generate_mock_comments)
                mock_thread.daemon = True
                mock_thread.start()
            
            logger.info("Comment capture started")
            return True
        except Exception as e:
            logger.error(f"Error starting comment capture: {e}")
            return False
    
    def stop(self):
        """Stop capturing comments"""
        try:
            self.running = False
            if self.client:
                try:
                    self.client.stop()
                except Exception as e:
                    logger.error(f"Error stopping Douyin client: {e}")
            if self.thread:
                self.thread.join(timeout=5)
            logger.info("Comment capture stopped")
        except Exception as e:
            logger.error(f"Error stopping comment capture: {e}")
    
    def _on_comment(self, comment):
        """Handle new comment"""
        try:
            # Extract comment content
            comment_text = comment.get('content', '')
            user_name = comment.get('user_name', 'Unknown')
            
            # Sanitize and validate comment
            sanitized_comment = sanitize_comment(comment_text)
            if not is_valid_comment(sanitized_comment):
                return
            
            # Create comment object
            comment_data = {
                'text': sanitized_comment,
                'user': user_name,
                'timestamp': time.time()
            }
            
            # Add to queue if not full
            if self.comment_queue.qsize() < MAX_COMMENT_QUEUE_SIZE:
                self.comment_queue.put(comment_data)
                logger.debug(f"Captured comment from {user_name}: {sanitized_comment}")
            else:
                logger.warning("Comment queue full, discarding new comment")
        except Exception as e:
            logger.error(f"Error processing comment: {e}")
    
    def _generate_mock_comments(self):
        """Generate mock comments for demonstration"""
        while self.running:
            try:
                # Generate random comment
                comment_text = random.choice(self.mock_comments)
                user_name = random.choice(self.mock_users)
                
                # Create comment object
                comment_data = {
                    'text': comment_text,
                    'user': user_name,
                    'timestamp': time.time()
                }
                
                # Add to queue if not full
                if self.comment_queue.qsize() < MAX_COMMENT_QUEUE_SIZE:
                    self.comment_queue.put(comment_data)
                    logger.info(f"Generated mock comment from {user_name}: {comment_text}")
                
                # Wait random time between 5-15 seconds
                time.sleep(random.randint(5, 15))
            except Exception as e:
                logger.error(f"Error generating mock comments: {e}")
                time.sleep(1)
    
    def _monitor(self):
        """Monitor comment capture status"""
        while self.running:
            try:
                time.sleep(1)
            except Exception as e:
                logger.error(f"Error in comment capture monitor: {e}")
                break