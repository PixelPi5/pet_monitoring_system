import requests
import os
from serpapi import GoogleSearch

# API Key from SerpAPI
API_KEY = "your_serpapi_api_key"

# Search Parameters
params = {
    "q": "cat walking",
    "tbm": "isch",  # Image search
    "ijn": "0",
    "api_key": API_KEY,
}

# Output Directory
output_dir = "dataset/cat_walking"
os.makedirs(output_dir, exist_ok=True)

# Perform Search
search = GoogleSearch(params)
results = search.get_dict()

# Download Images
count = 0
for image_result in results.get("images_results", []):
    try:
        # Timeout added here
        img_data = requests.get(image_result["original"], timeout=10).content
        with open(f"{output_dir}/image_{count}.jpg", "wb") as handler:
            handler.write(img_data)
        count += 1
        print(f"Downloaded {count} images")
        if count >= 100:  # Limit to 100 images
            break
    except Exception as e:
        print(f"Could not download image {count}: {e}")

print(f"Downloaded {count} images to {output_dir}")
