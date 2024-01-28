from __main__ import app
from flask import request, jsonify, session
from pipelines.songGen import gen_songs, gen_prompt
from pipelines.summary import summarize_desc
from pipelines.vision import desc_img
from pipelines.spotify import create_playlist, \
        delete_playlist, get_token, get_uri, add_song_to_playlist
from pipelines.dbFunctions import *

@app.route("/songsnapapi/analyse-image", methods=["POST"])
def analyse_image_endpoint():
    # print(request.json)
    url = request.json.get("img_url")
    if url: 
        result = desc_img(url)
        return jsonify({
            "data": result
        })
    return "No provided image URL", 400


@app.route("/songsnapapi/summarise", methods=["POST"])
def summarise_endpoint():
    # print(request.json)
    desc = request.json.get("content")
    if desc:
        result = summarize_desc(desc)
        return jsonify({
            "data": result,
            "description": desc
        })
    return "No provided description", 400

    
@app.route("/songsnapapi/generate-prompt", methods=["POST"])
def generate_prompt_endpoint():
    text = request.json.get("content")
    songs = request.json.get("songs")
    if text and songs:
        result = gen_prompt(text, songs)
        return jsonify({
            "data": result
        })
    return "No provided text", 400

@app.route("/songsnapapi/generate-songs", methods=["POST"])
def generate_songs_endpoint():
    desc = request.json.get("content")
    if desc:
        result = gen_songs(desc)
        return jsonify({
            "data": result
        })
    return "No provided text", 400

@app.route("/songsnapapi/create-playlist", methods=["POST"])
def create_playlist_endpoint():
    songs = request.json.get("content")
    token = get_token()

    playlist = create_playlist(token)
    print(playlist)
    for song_and_artist in songs.split("\n"):
        result = get_uri(token, song_and_artist)
        if result:
            add_song_to_playlist(token, playlist["id"], result)
    ret = {
        "playlist_id": playlist["id"],
        "playlist_link": playlist["external_urls"]["spotify"],
    }
    return jsonify(ret)

@app.route("/songsnapapi/get-playlist", methods=["GET"])
def get_playlist_endpoint():
    if session.get("user"):
        print(session.get("user")["userinfo"]["sub"]) # get auth0 id
    return jsonify({"placeholder": "urmom"})
    desc = request.json.get("content")
    if desc:
        result = gen_songs(desc)
        return jsonify({
            "data": result
        })
    return "No provided text", 400

