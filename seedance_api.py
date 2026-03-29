import os
import requests
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class SeedanceAPI:
    def __init__(self, api_key=None):
        """
        Initialize the Seedance 2.0 API client.
        :param api_key: Your MuAPI.ai API key. Defaults to MUAPI_API_KEY environment variable.
        """
        self.api_key = api_key or os.getenv("MUAPI_API_KEY")
        if not self.api_key:
            raise ValueError("API Key is required. Set MUAPI_API_KEY in .env or pass it to the constructor.")
        
        self.base_url = "https://api.muapi.ai/api/v1"
        self.headers = {
            "x-api-key": self.api_key,
            "Content-Type": "application/json"
        }

    def text_to_video(self, prompt, aspect_ratio="16:9", duration=5, quality="basic"):
        """
        Submits a Seedance 2.0 Text-to-Video (T2V) generation task.

        :param prompt: The text prompt describing the video. To use a fictional character,
                       reference it inline with @character:<id> where <id> is the request_id
                       from a completed create_character() call. Multiple characters supported.
                       Example: "@character:ab539e5f-... walks on the beach at sunset"
        :param aspect_ratio: Video aspect ratio (e.g., '16:9', '9:16').
        :param duration: Video duration in seconds.
        :param quality: Output quality ('basic' or 'high').
        :return: JSON response from the Seedance 2.0 API.
        """
        endpoint = f"{self.base_url}/seedance-v2.0-t2v"
        payload = {
            "prompt": prompt,
            "aspect_ratio": aspect_ratio,
            "duration": duration,
            "quality": quality
        }
        return self._post_request(endpoint, payload)

    def image_to_video(self, prompt, images_list, aspect_ratio="16:9", duration=5, quality="basic"):
        """
        Submits a Seedance 2.0 Image-to-Video (I2V) generation task.

        :param prompt: Text prompt to guide the animation. Reference images in the list with
                       @image1, @image2, etc. To inject a character from create_character(),
                       use @character:<id> inline — e.g. "@image1 shows the scene, @character:ab539e5f-... is the hero".
                       Characters are appended after images_list entries automatically.
        :param images_list: A list of image URLs to animate.
        :param aspect_ratio: Video aspect ratio.
        :param duration: Video duration.
        :param quality: Output quality.
        :return: JSON response from the Seedance 2.0 API.
        """
        endpoint = f"{self.base_url}/seedance-v2.0-i2v"
        payload = {
            "prompt": prompt,
            "images_list": images_list,
            "aspect_ratio": aspect_ratio,
            "duration": duration,
            "quality": quality
        }
        return self._post_request(endpoint, payload)

    def omni_reference(self, prompt, aspect_ratio="16:9", duration=5,
                        images_list=None, video_files=None, audio_files=None):
        """
        Submits a Seedance 2.0 Omni-Reference generation task.

        Omni-Reference lets you condition a video on any combination of image, video,
        and audio references — all in a single request. Use @character:<id> inline in
        the prompt to inject a fictional character created via create_character().

        :param prompt: Text prompt describing the video. Supports @character:<id> syntax.
        :param aspect_ratio: Video aspect ratio (e.g., '16:9', '9:16').
        :param duration: Video duration in seconds (minimum 4 s for video references).
        :param images_list: Optional list of image URLs to condition on.
        :param video_files: Optional list of video URLs to condition on.
        :param audio_files: Optional list of audio URLs to condition on.
        :return: JSON response with request_id.
        """
        endpoint = f"{self.base_url}/seedance-2.0-omni-reference"
        payload = {
            "prompt": prompt,
            "aspect_ratio": aspect_ratio,
            "duration": duration,
        }
        if images_list:
            payload["images_list"] = images_list
        if video_files:
            payload["video_files"] = video_files
        if audio_files:
            payload["audio_files"] = audio_files
        return self._post_request(endpoint, payload)

    def create_character(self, images_list, outfit_description, character_name=None):
        """
        Creates a reusable fictional character sheet from reference photos.

        Upload 1–5 images of a real person along with an outfit/style description.
        The API returns a request_id — once completed, the character can be referenced
        inline in any T2V, I2V, or Omni-Reference prompt using @character:<request_id>.

        :param images_list: List of image URLs showing the reference person (1–5 images).
        :param outfit_description: Description of the desired outfit/style for the character.
        :param character_name: Optional display name for the character.
        :return: JSON response with request_id. Poll wait_for_completion() and use
                 the returned request_id as @character:<id> in future prompts.

        Example workflow::

            # Step 1 — create the character
            char = api.create_character(
                images_list=["https://example.com/person.jpg"],
                outfit_description="cyberpunk jacket with neon accents",
                character_name="Nova"
            )
            char_id = char["request_id"]
            api.wait_for_completion(char_id)   # wait for sheet to render

            # Step 2 — use the character in a video
            video = api.text_to_video(
                prompt=f"@character:{char_id} rides a motorcycle through a neon-lit city at night",
                aspect_ratio="16:9",
                duration=5,
            )
            result = api.wait_for_completion(video["request_id"])
            print(result["url"])
        """
        endpoint = f"{self.base_url}/seedance-2-character"
        payload = {
            "images_list": images_list,
            "outfit_description": outfit_description,
        }
        if character_name:
            payload["character_name"] = character_name
        return self._post_request(endpoint, payload)

    def extend_video(self, request_id, prompt="", duration=5, quality="basic"):
        """
        Extends a previously generated Seedance 2.0 video.
        
        :param request_id: The ID of the video segment to extend.
        :param prompt: Optional text prompt for the extension.
        :return: JSON response from the Seedance 2.0 API.
        """
        endpoint = f"{self.base_url}/seedance-v2.0-extend"
        payload = {
            "request_id": request_id,
            "prompt": prompt,
            "duration": duration,
            "quality": quality
        }
        return self._post_request(endpoint, payload)

    def video_edit(self, prompt, video_urls, images_list=None, aspect_ratio="16:9", quality="basic", remove_watermark=False):
        """
        Submits a Seedance 2.0 Video-Edit generation task.
        
        :param prompt: The text prompt describing the edit.
        :param video_urls: A list of video URLs to edit.
        :param images_list: Optional list of image URLs.
        :param aspect_ratio: Video aspect ratio.
        :param quality: Output quality.
        :param remove_watermark: Whether to remove watermark.
        :return: JSON response from the Seedance 2.0 API.
        """
        endpoint = f"{self.base_url}/seedance-v2.0-video-edit"
        payload = {
            "prompt": prompt,
            "video_urls": video_urls,
            "images_list": images_list or [],
            "aspect_ratio": aspect_ratio,
            "quality": quality,
            "remove_watermark": remove_watermark
        }
        return self._post_request(endpoint, payload)

    def _post_request(self, endpoint, payload):
        response = requests.post(endpoint, json=payload, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_result(self, request_id):
        """
        Polls for the result of a generation task.
        """
        endpoint = f"{self.base_url}/predictions/{request_id}/result"
        response = requests.get(endpoint, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def wait_for_completion(self, request_id, poll_interval=5, timeout=600):
        """
        Waits for the video generation to complete and returns the result.
        """
        start_time = time.time()
        while time.time() - start_time < timeout:
            result = self.get_result(request_id)
            status = result.get("status")
            
            if status == "completed":
                return result
            elif status == "failed":
                raise Exception(f"Video generation failed: {result.get('error')}")
            
            print(f"Status: {status}. Waiting {poll_interval} seconds...")
            time.sleep(poll_interval)
        
        raise TimeoutError("Timed out waiting for video generation to complete.")

if __name__ == "__main__":
    # Example usage for T2V
    try:
        api = SeedanceAPI()
        prompt = "A cinematic shot of a futuristic city with neon lights, 8k resolution"
        
        print(f"Submitting T2V task with prompt: {prompt}")
        submission = api.text_to_video(prompt=prompt, duration=5)
        request_id = submission.get("request_id")
        print(f"Task submitted. Request ID: {request_id}")
        
        print("Waiting for completion...")
        result = api.wait_for_completion(request_id)
        print(f"Generation completed! Video URL: {result.get('url')}")
        
    except Exception as e:
        print(f"Error: {e}")
