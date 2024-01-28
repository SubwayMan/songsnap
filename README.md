# Songsnap
Turn your photo memories into musical blasts from the past! 🎵📷

[![YouTube Video](https://www.youtube.com/watch?v=4eT1EpgSBOE)
[![uofthacksPhoto](https://github.com/SubwayMan/songsnap/assets/62809012/15f5c19c-1130-4095-8400-fec6ebe3ffd9)](https://www.youtube.com/watch?v=4eT1EpgSBOE)


## What it Does
Songsnap utilizes GPT-4 Vision to extract detailed information from images such as time period, mood, cultural elements, and location. This data is then summarized using Cohere into concise bullet points. Users can upload photos to the platform, which then generates a curated playlist based on the image description using a fine-tuned GPT-3.5 model. The generated playlists can be accessed and played directly through the website thanks to integration with the Spotify API. Additionally, users can manage and access their playlists through a library page powered by Supabase, a PostgreSQL database API. We also have an Auth0 login system set up.

## How to Use
1. Clone repository: `git clone https://github.com/SubwayMan/songsnap.git`
2. Install requirements: `pip install -r requirements.txt`
3. Create a `.env` and add the following API keys into it: `OPENAI_API_KEY, CO_API_KEY, KINTONE_TOKEN, AUTH0_CLIENT_ID, AUTH0_CLIENT_SECRET, AUTH0_DOMAIN, APP_SECRET_KEY, SUPABASE_URL, SUPABASE_KEY`
