from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()
client.api_key = os.getenv("OPENAI_API_KEY")

def desc_img(img_url):
    response = client.chat.completions.create(
                    model="gpt-4-vision-preview",
                    messages=[
                        {
                          "role": "user",
                          "content": [
                            {"type": "text", "text": "Describe this image. Make sure to include what timeframe and culture it looks like its from, as well as the mood of the image overall image"},
                            {
                              "type": "image_url",
                              "image_url": {
                                "url": img_url,
                              },
                            },
                          ],
                        }
                    ],
                    max_tokens=300,
    )

    return response.choices[0].message.content

img_url = 'https://www.trumanlibrary.gov/sites/default/files/styles/tiff_conversion/public/photographs/2016/2016-266.tif.jpg?itok=75tRRJY5'
image_desc = desc_img(img_url)

print(image_desc)
