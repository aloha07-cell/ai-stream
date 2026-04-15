#!/usr/bin/env python3
# Main script for Douyin Live Stream Comment Processing with Voice Response
import time
import threading
import queue
from utils.logger import get_logger
from config.config import PRODUCT_INTRO_TIMEOUT
from modules.comment_capture.comment_capture import CommentCapture
from modules.ai_response.ai_response import AIResponse
from modules.voice_synthesis.voice_synthesis import VoiceSynthesis
from modules.audio_output.audio_output import AudioOutput
from modules.product_intro.product_intro import ProductIntroduction

logger = get_logger('main')

class DouyinLiveCommentVoice:
    def __init__(self):
        # Create comment queue
        self.comment_queue = queue.Queue()
        
        # Initialize modules
        self.comment_capture = CommentCapture(self.comment_queue)
        self.ai_response = AIResponse()
        self.voice_synthesis = VoiceSynthesis()
        self.audio_output = AudioOutput()
        self.product_intro = ProductIntroduction()
        
        # State variables
        self.running = False
        self.last_comment_time = time.time()
        self.thread = None
    
    def start(self):
        """Start the system"""
        try:
            logger.info("Starting Douyin Live Comment Voice system")
            
            # Start comment capture
            if not self.comment_capture.start():
                logger.error("Failed to start comment capture")
                return False
            
            # Start main processing thread
            self.running = True
            self.thread = threading.Thread(target=self._process)
            self.thread.daemon = True
            self.thread.start()
            
            logger.info("System started successfully")
            return True
        except Exception as e:
            logger.error(f"Error starting system: {e}")
            return False
    
    def stop(self):
        """Stop the system"""
        try:
            logger.info("Stopping Douyin Live Comment Voice system")
            
            self.running = False
            
            # Stop comment capture
            self.comment_capture.stop()
            
            # Wait for processing thread to finish
            if self.thread:
                self.thread.join(timeout=5)
            
            logger.info("System stopped successfully")
        except Exception as e:
            logger.error(f"Error stopping system: {e}")
    
    def _process(self):
        """Main processing loop"""
        while self.running:
            try:
                # Check for new comments
                if not self.comment_queue.empty():
                    # Get comment
                    comment = self.comment_queue.get(block=False)
                    self.last_comment_time = time.time()
                    
                    # Process comment
                    self._process_comment(comment)
                else:
                    # Check if product introduction is needed
                    if self.product_intro.should_introduce(self.last_comment_time, PRODUCT_INTRO_TIMEOUT):
                        self._process_product_intro()
                    
                    # Sleep to reduce CPU usage
                    time.sleep(0.1)
            except queue.Empty:
                # No comment in queue, continue
                pass
            except Exception as e:
                logger.error(f"Error in processing loop: {e}")
                # Continue processing
                time.sleep(1)
    
    def _process_comment(self, comment):
        """Process a single comment"""
        try:
            logger.info(f"Processing comment: {comment['text']}")
            
            # Generate AI response
            response_text = self.ai_response.generate_response(comment)
            logger.info(f"Generated response: {response_text}")
            
            # Synthesize speech
            audio_data = self.voice_synthesis.synthesize(response_text)
            
            # Play audio
            if audio_data:
                self.audio_output.play(audio_data)
        except Exception as e:
            logger.error(f"Error processing comment: {e}")
    
    def _process_product_intro(self):
        """Process product introduction"""
        try:
            logger.info("Triggering product introduction")
            
            # Get next product
            product = self.product_intro.get_next_product()
            if not product:
                logger.warning("No product available for introduction")
                return
            
            # Generate product introduction
            intro_text = self.ai_response.generate_product_intro(product)
            logger.info(f"Generated product introduction: {intro_text}")
            
            # Synthesize speech
            audio_data = self.voice_synthesis.synthesize(intro_text)
            
            # Play audio
            if audio_data:
                self.audio_output.play(audio_data)
        except Exception as e:
            logger.error(f"Error processing product introduction: {e}")

def main():
    """Main function"""
    system = DouyinLiveCommentVoice()
    
    try:
        # Start system
        if system.start():
            logger.info("System is running. Press Ctrl+C to stop.")
            
            # Keep main thread alive
            while True:
                time.sleep(1)
    except KeyboardInterrupt:
        logger.info("Received keyboard interrupt")
    finally:
        # Stop system
        system.stop()

if __name__ == "__main__":
    main()