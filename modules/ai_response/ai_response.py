# AI response module using Alibaba Bailian platform API
import time
import threading
import requests
from utils.logger import get_logger
from config.config import (
    BAILIAN_API_KEY, BAILIAN_REGION, 
    BAILIAN_TEXT_MODEL, API_REQUEST_TIMEOUT, USE_REAL_API
)

logger = get_logger('ai_response')

class AIResponse:
    def __init__(self):
        self.api_key = BAILIAN_API_KEY
        self.region = BAILIAN_REGION
        self.model = BAILIAN_TEXT_MODEL
        self.base_url = f"https://bailian.{self.region}.aliyuncs.com"
        self.use_real_api = USE_REAL_API
    
    def generate_response(self, comment):
        """Generate AI response to comment"""
        try:
            # Prepare request data
            comment_text = comment.get('text', '')
            user_name = comment.get('user', 'Unknown')
            
            # Create prompt
            prompt = f"用户{user_name}说: {comment_text}\n请给出一个友好、专业的回应，适合在直播中使用。"
            
            # Call Bailian API
            response = self._call_bailian_api(prompt)
            
            if response:
                logger.debug(f"Generated response for comment: {comment_text}")
                return response
            else:
                logger.error("Failed to generate response")
                return "感谢您的评论！"
        except Exception as e:
            logger.error(f"Error generating AI response: {e}")
            return "感谢您的评论！"
    
    def _call_bailian_api(self, prompt):
        """Call Bailian API to generate response"""
        try:
            if self.use_real_api and self.api_key:
                # Real API call implementation
                logger.info("Using real Bailian API")
                headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self._get_access_token()}"
                }
                data = {
                    "model": self.model,
                    "prompt": prompt,
                    "max_tokens": 100,
                    "temperature": 0.7
                }
                response = requests.post(
                    f"{self.base_url}/api/text/generation",
                    headers=headers,
                    json=data,
                    timeout=API_REQUEST_TIMEOUT
                )
                response.raise_for_status()
                return response.json().get("result", "")
            else:
                # Mock response for demonstration
                logger.info("Using mock API response")
                time.sleep(0.5)  # Simulate API latency
                mock_responses = [
                    "感谢您的支持，我们会继续努力！",
                    "很高兴您喜欢我们的产品，有什么可以帮助您的吗？",
                    "您的建议很有价值，我们会认真考虑的。",
                    "谢谢关注，我们会持续为大家带来优质内容。",
                    "非常感谢您的评论，祝您生活愉快！"
                ]
                
                # Return a random mock response
                import random
                return random.choice(mock_responses)
            
        except Exception as e:
            logger.error(f"Error calling Bailian API: {e}")
            return None
    
    def _get_access_token(self):
        """Get access token for Bailian API"""
        # Implement access token retrieval logic
        # This would typically involve calling Alibaba Cloud STS or IAM API
        return "mock_access_token"
    
    def generate_product_intro(self, product_data):
        """Generate product introduction"""
        try:
            # Prepare product information
            product_name = product_data.get('name', '产品')
            product_description = product_data.get('description', '这是一款优质产品')
            product_price = product_data.get('price', '价格优惠')
            
            # Create prompt
            prompt = f"请为{product_name}生成一段吸引人的产品介绍，包括{product_description}和{product_price}。"
            
            # Call Bailian API
            response = self._call_bailian_api(prompt)
            
            if response:
                logger.debug(f"Generated product introduction for: {product_name}")
                return response
            else:
                logger.error("Failed to generate product introduction")
                return f"欢迎了解我们的{product_name}，{product_description}，{product_price}。"
        except Exception as e:
            logger.error(f"Error generating product introduction: {e}")
            return "欢迎了解我们的产品，品质保证，价格优惠。"