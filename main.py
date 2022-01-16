from ytmusicapi import YTMusic
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import re
import sys
import random
import string

# SPOTIFY VARIABLES
SPOTIFY_USER_ID =
CLIENT_ID =
CLIENT_SECRET = 
REDIRECT_URI =

# YT MUSIC VARIABLES
YT_USER_ID =


def create_spotify():
    scope = ["playlist-modify-public", "user-library-modify", "user-library-read"]
    auth_manager = SpotifyOAuth(scope=scope, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI)
    return spotipy.Spotify(auth_manager=auth_manager)


def create_youtube():
    return YTMusic("headers_auth.json", YT_USER_ID)


if __name__ == '__main__':

    # Initialize our youtube music object
    ytmusic = create_youtube()

    # Initialize our spotify object
    sp = create_spotify()

    # Get our liked songs from youtube music
    get_liked = ytmusic.get_liked_songs(limit=9999)
    get_liked = [(x["title"], x["artists"][0]["name"]) for x in get_liked["tracks"]]

    # Create a new album in spotify
    new_playlist = sp.user_playlist_create(SPOTIFY_USER_ID, "Youtube Liked")

    # Go through every liked song
    not_found = 0
    for i, (song, artist) in enumerate(get_liked):

        # Print progress
        sys.stdout.write("\r{}/{}".format(i + 1, len(get_liked)))

        # Take out (music video) or [music video]
        song = re.sub("(\(.*\)|\[.*\])", "", song).strip()

        # Take out artist - song in title
        song = song.split("-")[-1]

        # Search for the song
        # query = sp.search(q=f"artist:{artist} track:{song}")
        query = sp.search(q=f"{song} {artist}")

        # If the query returned something
        if query["tracks"]["items"]:

            # Add it to the playlist
            sp.playlist_add_items(playlist_id=new_playlist["id"], items=[query["tracks"]["items"][0]["id"]])

        # If the query doesn't return anything
        else:

            # Track how many we couldn't find
            not_found += 1

    # Print how many we lost
    print(f"\nCould not find {not_found} out of {len(get_liked)} tracks")

