from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()
client.api_key = os.getenv("OPENAI_API_KEY")

def gen_songs(text, modelName='gpt-3.5-turbo'):
    response = client.chat.completions.create(
        model=modelName,
        messages=text,
    )

    return response.choices[0].message.content

def gen_prompt(desc, song_count):
    message_data = [
        {"role": "system", "content": f"Generate {song_count} songs with the songwriter names split by newlines to capture the essence of the image description provided."},
        {"role": "user", "content": desc}
    ]

    return message_data

modelName = 'ft:gpt-3.5-turbo-1106:personal::8lWqsaNg' # fine-tuned model
desc = '''This black and white image features a group of well-dressed individuals, likely from the mid-20th century, given the style of their clothing, which includes hats and tailored suits for men and dresses with hats for women. These fashion choices, combined with the black and white nature of the photograph, suggest a time period from the 1940s or 1950s.\n\nThe setting is unmistakably Parisian, as the Eiffel Tower looms in the background, which identifies the culture as French. The architecture of the iconic tower and its unmistakable silhouette immediately anchor the location.\n\nThe mood of the photo appears to be one of casual observation or tourism, with the individuals seemingly engaged in light conversation or observation. They do not appear to be posing for the photo but are rather captured in a candid moment. The atmosphere seems calm and perhaps a bit reflective, consistent with a foggy or overcast day in Paris, given the muted skyline.'''
song_amount = 10

text = gen_prompt(desc, song_amount)
songs = gen_songs(text, modelName)

print(songs)
