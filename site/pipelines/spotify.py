from dotenv import load_dotenv
import os
import base64
from requests import post, get, delete
import json

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
user_id = os.getenv("USER_ID")

def get_token(): 
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def get_link(token, name_and_artist):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={name_and_artist}&type=track&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["tracks"]["items"][0]["external_urls"]["spotify"]

    if len(json_result) == 0:
        print("No song with this description exists D:")
        return None
    
    return json_result

def get_uri(token, name_and_artist):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={name_and_artist}&type=track&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["tracks"]["items"][0]["uri"]

    if len(json_result) == 0:
        print("No song with this description exists D:")
        return None
    
    return json_result

def add_song_to_playlist(token, playlist_id, uri):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    headers = get_auth_header(token)
    query = f"?uris={uri}"

    query_url = url + query
    result = post(query_url, headers=headers)
    json_result = json.loads(result.content)
    return json_result

def create_playlist(token, user_id):
    url = f"https://api.spotify.com/v1/users/{user_id}/playlists"
    headers = get_auth_header(token)
    result = post(url, headers=headers)
    json_result = json.loads(result.content)
    return json_result

def delete_playlist(token, playlist_id):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/followers"
    headers = get_auth_header(token)
    result = delete(url, headers=headers)
    json_result = json.loads(result.content)
    return json_result


token = get_token()

playlist = create_playlist(token, "31oiujwbiwvgqqhz2tavenyxqgey")
# - playlist["external_urls"]["spotify"]
# - playlist["id"]

print(playlist)

# song_link = get_link(token, "Safety Dance by Men Without Hats")
# song_uri = get_uri(token, "Safety Dance by Men Without Hats")

# print(song_link)
# print(song_uri)

# result = search_for_artist(token, "ACDC")
# print(result)
# artist_id = result["id"]
# print(artist_id)
# songs = get_songs_by_artist(token, artist_id)
# print(songs)

# for idx, song in enumerate(songs):
#     print(f"{idx + 1}. {song['name']}")
