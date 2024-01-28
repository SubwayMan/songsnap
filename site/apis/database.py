import os
import requests
from dotenv import find_dotenv, load_dotenv

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

KINTONE_API = os.environ.get("KINTONE_TOKEN")
KINTONE_URL = "https://songsnap.kintone.com"
"""
Function to add a user to the database.
"""
def create_database_user(user_id):

    pass

"""
Retrieves user from database.
Parameters: user Auth0 unique ID.
Returns: dict in following format:
{
    "spotify-token": "SPOTIFY_TOKEN",
    "playlists": {
        "playlist_id": "PLAYLIST_ID",
        ...
    }

}
"""
def get_database_user_info(user_id):
    pass

"""

"""
def create_database_playlist(user_id):
    pass

def get_database_playlist(playlist_id):
    pass


