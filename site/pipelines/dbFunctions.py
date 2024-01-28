import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

def update_user(id, spotify_client_id, spotify_client_secret, playlist_ids):
    data = supabase.table("user").update({"spotify_client_id": spotify_client_id, "spotify_client_secret": spotify_client_secret, "playlist_ids": playlist_ids}).eq("id", id).execute()

def update_playlist(id, picture_url, spotify_url):
    data = supabase.table("playlist").update({"picture_url": picture_url, "spotify_url": spotify_url}).eq("id", id).execute()

def insert_user(id, spotify_client_id, spotify_client_secret, playlist_ids):
    data = supabase.table("user").insert({"id": id, "spotify_client_id": spotify_client_id, "spotify_client_secret": spotify_client_secret, "playlist_ids": playlist_ids}).execute()

def insert_playlist(id, name, picture_url, spotify_url):
    data = supabase.table("playlist").insert({"id": id, "name": name, "picture_url": picture_url, "spotify_url": spotify_url}).execute()

def get_user(id):
    data = supabase.table("user").select('*').eq('id', id).execute()
    return data


def get_playlist(id):
    data = supabase.table("playlist").select('*').eq('id', id).execute()
    return data

if __name__ == "__main__":
    insert_playlist(13, 'a', "c", 'b')
    insert_user(34, 'a', 'b', [1,2,3])
    update_user(218832132198321, 'a', 'b', [1,2,3])
    update_playlist(218832132198321, 'a', 'b')
    print(get_user(69420))
    print(get_playlist(1283))
