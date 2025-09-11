import requests
import hashlib
import os
import sys
sys.path.append('..')  # Go up one level to find config.py
from config import DATASET_URL, DATASET_FILE
from datetime import datetime

def download_file(url):
    """Download file content from URL"""
    response = requests.get(url)
    response.raise_for_status()
    return response.content

def compute_hash(content):
    """Compute SHA256 hash of content"""
    sha256 = hashlib.sha256()
    sha256.update(content)
    return sha256.hexdigest()

def check_and_download():
    """Check if file is updated and download if necessary"""
    try:
        # Download the latest file content
        print(f"Checking for updates at {datetime.now()}")
        content = download_file(DATASET_URL)
        current_hash = compute_hash(content)

        # Check if file exists and compare hash
        if os.path.exists(DATASET_FILE):
            with open(DATASET_URL, 'rb') as f:
                old_content = f.read()
            old_hash = compute_hash(old_content)

            if old_hash == current_hash:
                print("✓ File is already up-to-date.")
                return False
            else:
                print("📥 New version detected! Downloading...")
        else:
            print("📥 File doesn't exist. Downloading for the first time...")

        # Save the new content
        with open(DATASET_FILE, 'wb') as f:
            f.write(content)
        print(f"✓ Download complete: {DATASET_FILE}")
        return True

    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    check_and_download()
