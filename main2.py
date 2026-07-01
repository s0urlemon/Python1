from io import BytesIO
import requests
import streamlit as st
from huggingface_hub import InferenceClient
import config

MODEL_ID='stabilityai/stable-diffusion-3-medium-diffusers'
FILTER_API_URL="https://filters-zeta.verce1.app/api/filter"

ENHANCE_SYS=(
    'Imporve prompts ofr text-to-image.Return ONLY the enhanced prompt.'
    "Add subject,style,lighting,camers angle,background,colors.Keep it safe."
)
NEGATIVE="low quality,blurry,distorted,watermark,text,cropped"

img_client=InferenceClient(provider="hf-inference",
                           api_key=config.HF_API_KEY)

def check_prompt_with_filter_api(prompt:str):
    try:
        response=requests.post(
            FILTER_API_URL,
            json={"prompt":prompt},
            timeout=10,
        )
        response.raise_for_status()
        data=response.json()

        if not isinstance(data,dict):
            return{"ok":False,"reason":"Invalid filter API response."}
        return data
    except Exception as e:
        return{
            "ok":False,
            "reason":f"Filter API Error:{str(e)}",
        }
    
def enhance_prompt(raw:str)-> str:
    from hf import generate_response
    out=generate_response(
        f"{ENHANCE_SYS}\nUser prompt:{raw}",
        temperature=0.4,
        max_tokens=250,
    )
    return (out or raw).strip()

def gen_image(prompt:str):
    filter_result=check_prompt_with_filter_api(prompt)
    if not filter_result.get("ok"):
        return None,f"Prompt blocked by safety filter.{filter_result.get("reason","unsafe prompt")}"
    try:
        return img_client.text_to_image(
            prompt=prompt,
            negative_prompt=NEGATIVE,
            model=MODEL_ID,
        ),None
    
    except Exception as e:
        msg=str(e)
        if "negative_prompt" in msg or 'unexpected keyword' in msg:
            try:
                return img_client.text_to_image(
                    prompt=prompt,
                    model=MODEL_ID,
                ),None
            except Exception as e2:
                msg=str(e2)

        if any(x in msg for x in ["402",'Payment Required','pre-paid credits']):
            return None,"Image backened requires credits or model not available on hf-interferance.\n\nRaw error:"+msg