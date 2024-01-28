from __main__ import app
from flask import request, jsonify, session
from pipelines.songGen import gen_songs, gen_prompt
from pipelines.summary import summarize_desc
from pipelines.vision import desc_img
from pipelines.spotify import create_playlist, \
        delete_playlist, get_uri, add_song_to_playlist
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
    imageURI = request.json.get("image")
    token = session["authorization_header"]
    user_id = session["spotify_id"]

    playlist = create_playlist(token, user_id)
    print("PLAYLIST", playlist)
    for song_and_artist in songs.split("\n"):
        result = get_uri(token, song_and_artist)
        if result:
            print("SONG FOUND", result)
            add_song_to_playlist(token, playlist["id"], result)
    ret = {
        "playlist_id": playlist["id"],
        "playlist_link": playlist["external_urls"]["spotify"],
    }
    auth0 = session.get("user")["userinfo"]["sub"] 
    insert_playlist(ret["playlist_id"], "songsnap", imageURI, ret["playlist_link"])
    userdata = get_user(auth0).data
    userdata["playlist_ids"].append(ret["playlist_id"])
    update_user(auth0, "", "", userdata["playlist_ids"])

    return jsonify(ret)

@app.route("/songsnapapi/get-playlists", methods=["GET"])
def get_playlists_endpoint():
    if not session.get("user"):
        return "Not logged in", 400

    auth0 = session.get("user")["userinfo"]["sub"]
    db_user = get_user(auth0)
    if not db_user:
        insert_user(auth0, "", "", [])
        db_user = get_user(auth0)
    db_user = db_user[0]
    return jsonify({"playlist_ids": db_user.data["playlist_ids"]})


@app.route("/songsnapapi/get-playlist", methods=["POST"])
def get_playlist_endpoint():
    playlist_id = request.json.get("playlist_id")
    db_playlist = get_playlist(playlist_id).data
    if not db_playlist:
        return "No playlist found", 400
    return jsonify({
        "image_url": db_playlist["picture_url"],
        "spotify_url": db_playlist["spotify_url"],
        "name": db_playlist["name"]})


