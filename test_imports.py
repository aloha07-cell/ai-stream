# Test script to verify all modules import correctly
import sys
import os

# Add the current directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("Testing imports...")

try:
    from config.config import *
    print("✓ config.config imported successfully")
except Exception as e:
    print(f"✗ Error importing config.config: {e}")

try:
    from utils.logger import get_logger
    print("✓ utils.logger imported successfully")
except Exception as e:
    print(f"✗ Error importing utils.logger: {e}")

try:
    from utils.helpers import *
    print("✓ utils.helpers imported successfully")
except Exception as e:
    print(f"✗ Error importing utils.helpers: {e}")

try:
    from modules.comment_capture.comment_capture import CommentCapture
    print("✓ modules.comment_capture imported successfully")
except Exception as e:
    print(f"✗ Error importing modules.comment_capture: {e}")

try:
    from modules.ai_response.ai_response import AIResponse
    print("✓ modules.ai_response imported successfully")
except Exception as e:
    print(f"✗ Error importing modules.ai_response: {e}")

try:
    from modules.voice_synthesis.voice_synthesis import VoiceSynthesis
    print("✓ modules.voice_synthesis imported successfully")
except Exception as e:
    print(f"✗ Error importing modules.voice_synthesis: {e}")

try:
    from modules.audio_output.audio_output import AudioOutput
    print("✓ modules.audio_output imported successfully")
except Exception as e:
    print(f"✗ Error importing modules.audio_output: {e}")

try:
    from modules.product_intro.product_intro import ProductIntroduction
    print("✓ modules.product_intro imported successfully")
except Exception as e:
    print(f"✗ Error importing modules.product_intro: {e}")

print("\nImport test complete!")
