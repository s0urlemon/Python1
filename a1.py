# --------------------------
# 1. Import required libraries
#    - OS, IO, requests, time
#    - datetime for timestamps
#    - Pillow for image handling (Image, ImageDraw, ImageFont)
#    - HF_API_KEY from config
# --------------------------

# --------------------------
# 2. Define constants
#    - MODEL name (facebook/detr-resnet-50)
#    - API endpoint URL
# --------------------------

# --------------------------
# 3. Function: ask_image()
#    - Prompt user for image path
#    - Validate if file exists
#    - Open file as bytes
#    - Return path + bytes
# --------------------------

# --------------------------
# 4. Function: infer()
#    - Send image bytes to Hugging Face API (POST request)
#    - Include Authorization header with API key
#    - Retry if model is warming up (status 503)
#    - Return detections as JSON response
# --------------------------

# --------------------------
# 5. Function: draw()
#    - Take image + detections
#    - For each detection:
#         - Check confidence score threshold
#         - Extract bounding box coordinates
#         - Draw rectangle on image
#         - Write label + confidence above box
#    - Return annotated image
# --------------------------

# --------------------------
# 6. Function: main()
#    - Call ask_image() to get path + bytes
#    - Call infer() to get detections
#    - Open image in Pillow
#    - Call draw() to annotate
#    - Save annotated image with timestamp
#    - Print confirmation / error messages
# --------------------------

# --------------------------
# 7. Entry point
#    - Run main() only if script is executed directly
# --------------------------
import os, io, time, random, requests, mimetypes
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from config import HF_API_KEY
MODEL = "facebook/detr-resnet-101"
API = f"https://router.huggingface.co/hf-inference/models/{MODEL}"
ALLOWED, MAX_MB = {".jpg",".jpeg",".png",".bmp",".gif",".webp",".tiff"}, 8
EMOJI = {"person":"🧍","car":"🚗","truck":"🚚","bus":"🚌","bicycle":"🚲","motorcycle":"🏍️","dog":"🐶","cat":"🐱",
"bird":"🐦","horse":"🐴","sheep":"🐑","cow":"🐮","bear":"🐻","giraffe":"🦒","zebra":"🦓","banana":"🍌",
"apple":"🍎","orange":"🍊","pizza":"🍕","broccoli":"🥦","book":"📘","laptop":"💻","tv":"📺","bottle":"🧴","cup":"🥤"}

def font(sz=18):
    for f in ("DejaVuSans.ttf","Arial.ttf"):
        try:return ImageFont.truetype(f,sz)
        except:pass
    return ImageFont.load__default()

def ask_image():
    print("\nPick an image(JPG/PNG/WebP/BMP/TIFF<8MB) from this folder.")
    while True:
        p=input("Image path:").strip().strip('"').strip("'")
        if not p or not os.path.isfile(p):print("Not Found!");continue
        if os.path.splitext(p)[1].lower() not in ALLOWED:print("Unsupported type!");continue
        if os.path.getsize(p)/(1024*1024)>MAX_MB:print("Too big(>8MB)");continue
        try:Image.open(p).verify()
        except:print("Corrupted image.");continue
        return p
    
def infer(path,img_bytes,tries=8):
    mime,_=mimetypes.guess_type(path)
    for _ in range(tries):
        if mime and mime.startswith("image/"):
            r=requests.post(API,
                            headers={"Authorization":f"Bearer {HF_API_KEY}","Content-Type":mime},
                            data=img_bytes,timeout=60)
        else:
            r=requests.post(API,
                            headers={"Authorization":f"Bearer {HF_API_KEY}"},
                            files=)