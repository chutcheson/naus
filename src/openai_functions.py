import json

from openai_client import client

def chat(prompt):
    return client.chat.completions.create(
        model="gpt-4-turbo-preview",
        response_format={"type": "json_object"}, 
        messages=[{"role": "user", "content": prompt}]
    ).choices[0].message.content

def vision(prompt, images):
    messages = [{"role": "user", "content": [{"type": "text", "text": prompt}]}]
    
    for image in images:
        messages[0]["content"].append(
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image.downsampled_image_base64}"}}
        )
        
    return client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=messages
    ).choices[0].message.content
