# Product introduction module for automatic product presentations
import time
import threading
from utils.logger import get_logger
from utils.helpers import load_json_file, get_file_path
from config.config import PRODUCT_DATA_FILE

logger = get_logger('product_intro')

class ProductIntroduction:
    def __init__(self):
        self.products = self._load_products()
        self.current_product_index = 0
        self.last_intro_time = 0
    
    def _load_products(self):
        """Load product data from file"""
        try:
            product_file = get_file_path(PRODUCT_DATA_FILE)
            products = load_json_file(product_file)
            if products:
                logger.info(f"Loaded {len(products)} products")
                return products
            else:
                # Default product data if file not found
                logger.warning("No product data found, using default")
                return [
                    {
                        "name": "智能手表",
                        "description": "多功能智能手表，支持心率监测、运动追踪、消息提醒等功能",
                        "price": "仅售299元"
                    },
                    {
                        "name": "无线耳机",
                        "description": "高品质无线蓝牙耳机，主动降噪，续航长达24小时",
                        "price": "优惠价199元"
                    },
                    {
                        "name": "充电宝",
                        "description": "大容量充电宝，支持快充，兼容多种设备",
                        "price": "特惠价99元"
                    }
                ]
        except Exception as e:
            logger.error(f"Error loading product data: {e}")
            # Return default product data
            return [
                {
                    "name": "智能手表",
                    "description": "多功能智能手表，支持心率监测、运动追踪、消息提醒等功能",
                    "price": "仅售299元"
                }
            ]
    
    def get_next_product(self):
        """Get next product for introduction"""
        if not self.products:
            logger.warning("No products available")
            return None
        
        # Get current product
        product = self.products[self.current_product_index]
        
        # Update index for next time
        self.current_product_index = (self.current_product_index + 1) % len(self.products)
        
        logger.debug(f"Selected product: {product['name']}")
        return product
    
    def should_introduce(self, last_comment_time, timeout):
        """Check if product introduction should be triggered"""
        current_time = time.time()
        time_since_last_comment = current_time - last_comment_time
        time_since_last_intro = current_time - self.last_intro_time
        
        # Trigger introduction if no comment for timeout seconds
        # and at least 30 seconds since last introduction
        if time_since_last_comment >= timeout and time_since_last_intro >= 30:
            self.last_intro_time = current_time
            return True
        return False
    
    def refresh_products(self):
        """Refresh product data from file"""
        try:
            new_products = self._load_products()
            if new_products:
                self.products = new_products
                self.current_product_index = 0
                logger.info("Product data refreshed")
                return True
            return False
        except Exception as e:
            logger.error(f"Error refreshing product data: {e}")
            return False