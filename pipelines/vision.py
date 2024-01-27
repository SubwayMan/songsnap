from openai import OpenAI
import os

client = OpenAI()
openai.api_key = os.getenv("OPENAI_API_KEY")

def describe_image(filePath):
    return 0

current_dir = os.getcwd()
img_folder = os.path.join(current_dir, "Images")
img_path = os.path.join(img_folder, "img1.jpg")

image_desc = describe_image(img_path)

print(image_desc)
