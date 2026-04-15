# 抖音直播弹幕语音回复系统 - 部署指南

## 项目介绍

这是一个基于Python的系统，可以：
1. 抓取抖音直播的弹幕内容
2. 通过阿里百炼平台的API调用大模型进行语音自动回复
3. 当没有弹幕输入时，自动进行商品介绍
4. 通过电脑扬声器输出语音

## 系统架构

```
douyin-live-comment-voice/
├── config/              # 配置设置
├── modules/             # 核心功能模块
│   ├── comment_capture/ # 抖音弹幕抓取
│   ├── ai_response/     # 百炼API集成
│   ├── voice_synthesis/ # 语音合成
│   ├── audio_output/    # 音频输出
│   └── product_intro/   # 商品介绍内容
├── utils/               # 工具函数
├── main.py              # 主脚本
├── requirements.txt     # 依赖包
├── product_intro.json   # 商品数据
└── .env                 # 环境配置
```

## 准备工作

### 硬件要求
- 电脑一台（Windows、Mac、Linux均可）
- 网络连接
- 扬声器或耳机

### 软件要求
- Python 3.8 或更高版本
- pip 包管理器

## 部署步骤

### 步骤1：下载项目

1. 如果你有Git：
   ```bash
   git clone <仓库地址>
   cd douyin-live-comment-voice
   ```

2. 如果你没有Git：
   - 下载项目压缩包
   - 解压到本地
   - 进入解压后的文件夹

### 步骤2：创建虚拟环境

**Windows用户：**
```cmd
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux用户：**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 步骤3：安装依赖

```bash
pip install -r requirements.txt
```

### 步骤4：配置环境变量

1. 打开 `.env` 文件
2. 根据你的实际情况修改以下配置：

```env
# 抖音直播设置
DOUYIN_LIVE_URL=https://www.douyin.com/live/1234567890  # 替换为你的抖音直播间URL
DOUYIN_ROOM_ID=  # 或者填写直播间ID

# 阿里百炼API设置（可选，不填则使用模拟数据）
BAILIAN_API_KEY=  # 请在此处填写你的百炼API Key
BAILIAN_REGION=cn-shanghai
BAILIAN_TEXT_MODEL=qwen-plus  # 文本处理模型
BAILIAN_VOICE_MODEL=qwen-tts  # 语音合成模型

# 音频设置
AUDIO_VOLUME=0.8  # 音量大小（0.0-1.0）

# 商品介绍设置
PRODUCT_INTRO_TIMEOUT=30  # 无弹幕时多久开始商品介绍（秒）
PRODUCT_DATA_FILE=product_intro.json  # 商品数据文件

# 系统设置
USE_REAL_API=false  # 设置为true使用真实API，false使用模拟数据
```

### 步骤5：配置商品数据

1. 打开 `product_intro.json` 文件
2. 修改为你自己的商品信息：

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
    // 可以添加更多商品
]
```

### 步骤6：运行系统

**Windows用户：**
```cmd
python main.py
```

**Mac/Linux用户：**
```bash
python3 main.py
```

### 步骤7：系统运行

系统启动后，会：
1. 连接到抖音直播间
2. 实时抓取弹幕
3. 对弹幕生成AI回复
4. 将回复转换为语音并播放
5. 当没有弹幕时，自动播放商品介绍

### 步骤8：停止系统

按 `Ctrl+C` 停止系统运行。

## 常见问题解决

### 问题1：无法连接抖音直播间
- 检查网络连接
- 确认直播间URL正确
- 确认直播间处于直播状态

### 问题2：没有语音输出
- 检查扬声器是否正常工作
- 检查音量设置
- 检查 `.env` 文件中的 `AUDIO_VOLUME` 设置

### 问题3：商品介绍不触发
- 检查 `PRODUCT_INTRO_TIMEOUT` 设置
- 确保直播间确实没有弹幕输入

### 问题4：依赖安装失败
- 确认Python版本为3.8或更高
- 尝试更新pip：`pip install --upgrade pip`
- 检查网络连接

## 高级配置

### 自定义回复模板

在 `modules/ai_response/ai_response.py` 文件中，可以修改回复模板，调整AI回复的风格。

### 自定义语音设置

在 `.env` 文件中，可以调整以下语音设置：
- `VOICE_TYPE`：语音类型
- `VOICE_SPEED`：语速
- `VOICE_PITCH`：音调

### 调整弹幕处理

在 `.env` 文件中，可以调整以下设置：
- `MAX_COMMENT_QUEUE_SIZE`：弹幕队列大小
- `COMMENT_FILTER_THRESHOLD`：弹幕过滤阈值

## 生产环境部署

### 1. 使用真实的百炼API

1. 注册阿里百炼平台账号
2. 获取API Key
3. 在 `.env` 文件中填写真实的API Key
4. 将 `USE_REAL_API` 设置为 `true`

**注意：** 百炼平台只需要API Key，不需要Secret Key

### 2. 使用真实的抖音弹幕抓取

1. 安装抖音弹幕抓取库
2. 在 `modules/comment_capture/comment_capture.py` 中使用真实的弹幕抓取功能

### 3. 部署为服务

可以使用 `systemd`（Linux）或 `nssm`（Windows）将系统部署为后台服务，实现开机自启。

## 注意事项

1. 本系统默认使用模拟数据进行演示，实际使用需要配置真实的API
2. 请确保你有抓取抖音直播间弹幕的权限
3. 合理使用API，避免超出配额
4. 系统运行时会占用一定的系统资源，请确保电脑性能足够

## 技术支持

如果遇到问题，请检查日志文件 `app.log` 获取详细信息，或联系技术支持。

---

**部署完成！** 现在你可以开始使用抖音直播弹幕语音回复系统了。