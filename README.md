# Douyin Live Stream Comment Processing with Voice Response

This project is a Python-based system that captures Douyin (TikTok) live stream bullet comments, processes them through Alibaba's Bailian platform API for voice responses, and automatically provides product introductions when there are no comments.

## Features

- **Real-time comment capture**: Uses third-party open-source tool to capture Douyin live stream bullet comments
- **AI-powered responses**: Generates intelligent responses using Alibaba's Bailian platform API
- **Voice synthesis**: Converts text responses to speech
- **Audio output**: Plays synthesized speech through computer speakers
- **Automatic product introductions**: Provides product information when no comments are received

## System Architecture

```
douyin-live-comment-voice/
├── config/              # Configuration settings
├── modules/             # Core functionality modules
│   ├── comment_capture/ # Douyin comment capture
│   ├── ai_response/     # Bailian API integration
│   ├── voice_synthesis/ # Text-to-speech
│   ├── audio_output/    # Audio playback
│   └── product_intro/   # Product introduction content
├── utils/               # Utility functions
├── main.py              # Main script
├── requirements.txt     # Dependencies
└── README.md            # Documentation
```

## Prerequisites

- Python 3.8 or higher
- Douyin live stream URL or room ID
- Alibaba Bailian platform API credentials (optional for demonstration)
- Internet connection
- Speakers or audio output device

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd douyin-live-comment-voice
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your configuration:

```env
# Douyin Live Stream settings
DOUYIN_LIVE_URL=https://www.douyin.com/live/1234567890
DOUYIN_ROOM_ID=

# Alibaba Bailian API settings
BAILIAN_API_KEY=your_api_key
BAILIAN_SECRET_KEY=your_secret_key
BAILIAN_REGION=cn-shanghai
BAILIAN_MODEL=qwen-plus

# Audio settings
AUDIO_VOLUME=0.8

# Product introduction settings
PRODUCT_INTRO_TIMEOUT=30
PRODUCT_DATA_FILE=product_intro.json
```

## Usage

1. Start the system:

```bash
python main.py
```

2. The system will:
   - Connect to the Douyin live stream
   - Capture bullet comments in real-time
   - Generate AI responses to comments
   - Convert responses to speech and play through speakers
   - Provide product introductions when no comments are received

3. To stop the system, press Ctrl+C

## Configuration

### Douyin Live Stream Settings
- `DOUYIN_LIVE_URL`: URL of the Douyin live stream
- `DOUYIN_ROOM_ID`: Room ID of the Douyin live stream (alternative to URL)

### Alibaba Bailian API Settings
- `BAILIAN_API_KEY`: Your Bailian API key
- `BAILIAN_SECRET_KEY`: Your Bailian secret key
- `BAILIAN_REGION`: Bailian API region (e.g., cn-shanghai)
- `BAILIAN_MODEL`: Bailian model to use (e.g., qwen-plus)

### Audio Settings
- `AUDIO_VOLUME`: Audio volume (0.0 to 1.0)

### Product Introduction Settings
- `PRODUCT_INTRO_TIMEOUT`: Time in seconds before product introduction is triggered
- `PRODUCT_DATA_FILE`: Path to product data JSON file

## Product Data Format

Create a `product_intro.json` file with your product information:

```json
[
    {
        "name": "智能手表",
        "description": "多功能智能手表，支持心率监测、运动追踪、消息提醒等功能",
        "price": "仅售299元"
    },
    {
        "name": "无线耳机",
        "description": "高品质无线蓝牙耳机，主动降噪，续航长达24小时",
        "price": "优惠价199元"
    }
]
```

## Notes

- This system uses mock implementations for demonstration purposes
- In production, you'll need to implement actual API calls to Alibaba's Bailian platform
- The Douyin comment capture functionality requires a third-party library
- Ensure you have the necessary permissions to capture comments from Douyin live streams

## Troubleshooting

- **Comment capture issues**: Check your internet connection and Douyin live stream URL
- **API errors**: Verify your Bailian API credentials
- **Audio issues**: Ensure your speakers are properly connected and configured
- **Performance issues**: Adjust the `MAX_COMMENT_QUEUE_SIZE` and `PRODUCT_INTRO_TIMEOUT` settings

## License

[MIT License](LICENSE)