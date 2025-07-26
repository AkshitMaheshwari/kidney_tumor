"""
Download the kidney classification model from cloud storage
"""
import os
import requests
from tqdm import tqdm

def download_model():
    # Replace with your actual download URL (Google Drive, Hugging Face, etc.)
    model_url = "YOUR_CLOUD_STORAGE_URL_HERE"
    model_path = "kidney_classification.h5"
    
    if os.path.exists(model_path):
        print(f"✅ Model already exists: {model_path}")
        return
    
    print("📥 Downloading kidney classification model...")
    
    try:
        response = requests.get(model_url, stream=True)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        
        with open(model_path, 'wb') as file, tqdm(
            desc="Downloading",
            total=total_size,
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
        ) as pbar:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
                    pbar.update(len(chunk))
        
        print(f"✅ Model downloaded successfully: {model_path}")
        
    except Exception as e:
        print(f"❌ Error downloading model: {e}")
        print("Please download the model manually and place it in this directory.")

if __name__ == "__main__":
    download_model()
