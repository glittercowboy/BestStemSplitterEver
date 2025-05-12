import os
from pathlib import Path
import gdown

def main():
    MODEL_DIR = Path("drumsep/model")
    MODEL_FILE = MODEL_DIR / "49469ca8.th"
    GDRIVE_ID = "1-Dm666ScPkg8Gt2-lK3Ua0xOudWHZBGC"

    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    if not MODEL_FILE.exists():
        print("Downloading drum separation model...")
        gdown.download(id=GDRIVE_ID, output=str(MODEL_FILE), quiet=False)
        print("Model downloaded.")
    else:
        print("Model already exists.")

if __name__ == "__main__":
    main()
