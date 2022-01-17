# YTMusicLikedToSpotify

This application will transfer all your liked videos/songs in YouTube Music (given there is a valid match) to a playlist in Spotify.

Authentication is a little messy.

To authenticate YT Music, you must input the POST request headers and follow these directions to create the headers file: https://ytmusicapi.readthedocs.io/en/latest/setup.html#authenticated-requests

To authenticate Spotify, you must register the app (google spotify developer register app) then change the global variables in the app CLIENT_ID, CLIENT_SECRET, and REDIRECT_URI to match what was inputted.

Finally, all that is left is to press run, copy the URL over when prompted, and wait.
