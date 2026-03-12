# Seedance 2.0 API: Official Python Wrapper for ByteDance's AI Video Generator

[![GitHub stars](https://img.shields.io/github/stars/Anil-matcha/Seedance-2.0-API.svg)](https://github.com/Anil-matcha/Seedance-2.0-API/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

The most comprehensive and official Python wrapper for the **Seedance 2.0 API** (developed by ByteDance), delivered via [muapi.ai](https://muapi.ai). Generate cinematic, high-fidelity AI videos from text prompts and static images with the world's most advanced video generation model.

## 🚀 Why Use Seedance 2.0 API?

Seedance 2.0 is the industry-leading **Sora alternative** developed by ByteDance, offering unparalleled video quality and motion consistency.

- **Cinematic Quality**: Generate 2K resolution AI videos with realistic physics and lighting.
- **Superior Motion Control**: Advanced camera movement and character consistency for professional results.
- **Multimodal API**: Supports Text-to-Video (T2V), Image-to-Video (I2V), and Video Extension.
- **Developer-First**: Fast processing via the MuAPI infrastructure with a simple Python SDK.

## 🌟 Key Features of Seedance 2.0 API

- ✅ **Seedance 2.0 Text-to-Video (T2V)**: Transform complex descriptive prompts into stunning 15s AI video clips.
- ✅ **Seedance 2.0 Image-to-Video (I2V)**: Animate any static image with precise motion control using `images_list`.
- ✅ **Video Extension**: Seamlessly extend existing clips while maintaining consistent style and characters.
- ✅ **High-Resolution Output**: Support for `basic` and `high` (2K) quality settings.
- ✅ **Flexible Aspect Ratios**: Optimized for `16:9`, `9:16` (TikTok/Reels), `4:3`, and `3:4`.

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

## 💻 Quick Start with Seedance 2.0 API (Python)

```python
from seedance_api import SeedanceAPI

# Initialize the Seedance 2.0 client
api = SeedanceAPI()

# 1. Generate Video from Text (T2V) using Seedance 2.0 API
print("Generating AI Video using Seedance 2.0...")
submission = api.text_to_video(
    prompt="A cinematic slow-motion shot of a cyberpunk city in the rain, neon lights reflecting on puddles, 8k resolution",
    aspect_ratio="16:9",
    duration=5,
    quality="high"
)

# 2. Wait for completion
result = api.wait_for_completion(submission['request_id'])
print(f"Success! View your Seedance 2.0 video here: {result['url']}")
```

---

## 📡 API Endpoints & Reference

### 1. Seedance 2.0 Text-to-Video (T2V)
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

### 2. Seedance 2.0 Image-to-Video (I2V)
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

---

## 📖 Documentation & Guides

For a comprehensive walkthrough, check out the **[Seedance 2.0 API: Complete Developer Guide](https://medium.com/@anilmatcha/seedance-2-0-api-complete-developer-guide-text-to-video-image-to-video-python-sdk-1479f5e5491f)** on Medium. This guide covers advanced use cases, prompt engineering, and best practices for high-quality video generation.

| Method | Parameters | Description |
| :--- | :--- | :--- |
| `text_to_video` | `prompt`, `aspect_ratio`, `duration`, `quality` | Generate video from text prompts using Seedance 2.0. |
| `image_to_video` | `prompt`, `images_list`, `aspect_ratio`, `duration`, `quality` | Animate images using the Seedance 2.0 I2V model. |
| `extend_video` | `request_id`, `prompt`, `duration`, `quality` | Extend an existing Seedance video segment. |
| `get_result` | `request_id` | Check task status for the Seedance API. |
| `wait_for_completion` | `request_id`, `poll_interval`, `timeout` | Blocking helper for Seedance generation tasks. |

---

## 🔗 Official Resources
- **Developer Guide**: [Seedance 2.0 API: Complete Tutorial](https://medium.com/@anilmatcha/seedance-2-0-api-complete-developer-guide-text-to-video-image-to-video-python-sdk-1479f5e5491f)
- **Playground**: [Seedance 2.0 I2V Playground](https://muapi.ai/playground/seedance-v2.0-i2v)
- **Extension Tool**: [Seedance 2.0 Extend Playground](https://muapi.ai/playground/seedance-v2.0-extend)
- **API Provider**: [MuAPI.ai](https://muapi.ai)

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Keywords**: Seedance 2.0 API, ByteDance Seedance, AI Video Generator, Text-to-Video AI, Image-to-Video API, Seedance Python SDK, Seedance V2 API, Sora Alternative, MuAPI, Video Generation API, Cinematic AI Video, AI Video Creation, ByteDance Video AI, Seedance API Documentation, Seedance I2V, Seedance T2V, AI Movie Generator, AI Animation API, Python Video API, Seedance 2.0 Tutorial.
