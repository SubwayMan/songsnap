from dotenv import load_dotenv
import os
import base64
from requests import post, get, delete
import json

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
user_id = os.getenv("USER_ID")


def get_auth_header(token):
    print("CALL FOR TOKEN", token, "\n\n\n")
    if type(token) == "str":
        return eval("{" + token + "}")["Auth"]
    return token

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

    json_result = json.loads(result.content)
    if len(json_result) == 0:
        print("No song with this description exists D:")
        return None
    if "error" in json_result:
        return None

    json_result = json_result["tracks"]["items"][0]["uri"]
    
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
    result = post(url, headers=headers, json={"name": "SongSnap"})
    json_result = json.loads(result.content)
    return json_result

def delete_playlist(token, playlist_id):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/followers"
    headers = get_auth_header(token)
    result = delete(url, headers=headers)
    json_result = json.loads(result.content)
    return json_result

def get_user_id(token):
    url = "https://api.spotify.com/v1/me"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["id"]
    return json_result


# - playlist["external_urls"]["spotify"]
# - playlist["id"]


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
