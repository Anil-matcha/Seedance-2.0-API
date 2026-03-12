# Seedance 2.0 API: The Ultimate AI Text-to-Video & Image-to-Video Generator

[![GitHub stars](https://img.shields.io/github/stars/Anil-matcha/Seedance-2.0-API.svg)](https://github.com/Anil-matcha/Seedance-2.0-API/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

The most comprehensive Python wrapper for the **Seedance 2.0 API** (by ByteDance), delivered via [muapi.ai](https://muapi.ai). Create cinematic, high-fidelity AI videos from text prompts and images with the world's leading video generation model.

## 🚀 Why Seedance 2.0 API?
Seedance 2.0 is the industry-leading **Sora alternative** developed by ByteDance. It offers:
- **Cinematic Quality**: Generate 2K resolution videos with realistic physics and lighting.
- **Superior Motion**: Advanced "Director-level" camera control and character consistency.
- **Multimodal Inputs**: Supports Text-to-Video (T2V), Image-to-Video (I2V), and Video Extension.
- **Fast Processing**: Get high-quality results in seconds via the MuAPI infrastructure.

## 🌟 Key Features
- ✅ **Text-to-Video (T2V)**: Transform complex prompts into stunning 15s video clips.
- ✅ **Image-to-Video (I2V)**: Animate static images with precise motion control using `images_list`.
- ✅ **Video Extension**: Seamlessly extend existing clips while maintaining style and character consistency.
- ✅ **Customizable Resolution**: Choose between `basic` and `high` (2K) quality settings.
- ✅ **Flexible Aspect Ratios**: Supports `16:9`, `9:16`, `4:3`, and `3:4` for YouTube Shorts, TikTok, and Reels.

---

## 🛠 Installation

```bash
# Clone the Seedance 2.0 API repository
git clone https://github.com/Anil-matcha/Seedance-2.0-API.git
cd Seedance-2.0-API

# Install required dependencies
pip install -r requirements.txt
```

### Configuration
Create a `.env` file in the root directory and add your [MuAPI](https://muapi.ai) API key:
```env
MUAPI_API_KEY=your_muapi_api_key_here
```

---

## 💻 Quick Start (Python)

```python
from seedance_api import SeedanceAPI

# Initialize the Seedance 2.0 client
api = SeedanceAPI()

# 1. Generate Video from Text (T2V)
print("Generating AI Video...")
submission = api.text_to_video(
    prompt="A cinematic slow-motion shot of a cyberpunk city in the rain, neon lights reflecting on puddles, 8k resolution",
    aspect_ratio="16:9",
    duration=5,
    quality="high"
)

# 2. Wait for the magic to happen
result = api.wait_for_completion(submission['request_id'])
print(f"Success! View your AI video here: {result['url']}")
```

---

## 📡 API Endpoints & cURL Examples

### 1. Text-to-Video (T2V)
**Endpoint**: `POST https://api.muapi.ai/api/v1/seedance-v2.0-t2v`
```bash
curl --location --request POST "https://api.muapi.ai/api/v1/seedance-v2.0-t2v" \
  --header "Content-Type: application/json" \
  --header "x-api-key: YOUR_API_KEY" \
  --data-raw '{
      "prompt": "A majestic eagle soaring over the snow-capped Himalayas",
      "aspect_ratio": "16:9",
      "duration": 5,
      "quality": "high"
  }'
```

### 2. Image-to-Video (I2V)
**Endpoint**: `POST https://api.muapi.ai/api/v1/seedance-v2.0-i2v`
```bash
curl --location --request POST "https://api.muapi.ai/api/v1/seedance-v2.0-i2v" \
  --header "Content-Type: application/json" \
  --header "x-api-key: YOUR_API_KEY" \
  --data-raw '{
      "prompt": "Make the clouds move slowly across the sky",
      "images_list": ["https://example.com/mountain.jpg"],
      "aspect_ratio": "16:9",
      "duration": 5,
      "quality": "basic"
  }'
```

### 3. Video Extension
**Endpoint**: `POST https://api.muapi.ai/api/v1/seedance-v2.0-extend`
```bash
curl --location --request POST "https://api.muapi.ai/api/v1/seedance-v2.0-extend" \
  --header "Content-Type: application/json" \
  --header "x-api-key: YOUR_API_KEY" \
  --data-raw '{
      "request_id": "YOUR_PREVIOUS_REQUEST_ID",
      "prompt": "The camera pans right to reveal a hidden valley",
      "duration": 5,
      "quality": "high"
  }'
```

---

## 📖 API Documentation Reference

| Method | Parameters | Description |
| :--- | :--- | :--- |
| `text_to_video` | `prompt`, `aspect_ratio`, `duration`, `quality` | Generate video from text prompts. |
| `image_to_video` | `prompt`, `images_list`, `aspect_ratio`, `duration`, `quality` | Animate images from a URL list. |
| `extend_video` | `request_id`, `prompt`, `duration`, `quality` | Extend a previously generated video segment. |
| `get_result` | `request_id` | Check the status of a generation task. |
| `wait_for_completion` | `request_id`, `poll_interval`, `timeout` | Blocking helper to wait for the final URL. |

---

## 🔗 Related Resources
- **Playground**: [Seedance 2.0 I2V Playground](https://muapi.ai/playground/seedance-v2.0-i2v)
- **Extension Tool**: [Seedance 2.0 Extend Playground](https://muapi.ai/playground/seedance-v2.0-extend)
- **API Provider**: [MuAPI.ai](https://muapi.ai)

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Keywords**: Seedance 2.0 API, ByteDance Seedance, Text-to-Video AI, Image-to-Video API, AI Video Generator, MuAPI, Sora Alternative, Python AI Video, Video Generation API.
