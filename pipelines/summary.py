import cohere
import os
from dotenv import load_dotenv

load_dotenv()

co_api_key = os.getenv("CO_API_KEY")
co = cohere.Client(co_api_key)

def summarize_desc(desc):
    response = co.summarize(text=desc, length='short', format='bullets')

    return response.summary

desc = '''This black and white image features a group of well-dressed individuals, likely from the mid-20th century, given the style of their clothing, which includes hats and tailored suits for men and dresses with hats for women. These fashion choices, combined with the black and white nature of the photograph, suggest a time period from the 1940s or 1950s.\n\nThe setting is unmistakably Parisian, as the Eiffel Tower looms in the background, which identifies the culture as French. The architecture of the iconic tower and its unmistakable silhouette immediately anchor the location.\n\nThe mood of the photo appears to be one of casual observation or tourism, with the individuals seemingly engaged in light conversation or observation. They do not appear to be posing for the photo but are rather captured in a candid moment. The atmosphere seems calm and perhaps a bit reflective, consistent with a foggy or overcast day in Paris, given the muted skyline.'''

summary = summarize_desc(desc)

print(summary)
