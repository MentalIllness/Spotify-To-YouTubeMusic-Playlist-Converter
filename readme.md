Spotify to YouTube Music Playlist Converter

This Python script allows you to convert a Spotify playlist into a YouTube Music playlist. It fetches all tracks from a Spotify playlist and adds them to a new playlist on YouTube Music.

Features

Fetch tracks from any private or public Spotify playlist.

Skip local files, deleted tracks, or tracks with missing metadata.

Automatically create a new playlist on YouTube Music.

Search and add tracks to YouTube Music.

Handle duplicates and conflicts gracefully.

Requirements

Python 3.8+

Spotipy
 (pip install spotipy)

ytmusicapi
 (pip install ytmusicapi)

Setup
1. Spotify

Create a Spotify Developer App
 to get client_id and client_secret.

Set the redirect URI (e.g., https://example.com/callback).

Update the script with your credentials:

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    redirect_uri="YOUR_REDIRECT_URI",
    scope="playlist-read-private"
))


Replace playlist_id with the ID of the playlist you want to convert.
Example: playlist_id = "6bI8NNLvfXFXETy8zGx6RW"

2. YouTube Music

Install YTMusicAPI
.

Export your YouTube Music authentication headers:

ytmusicapi --cookies <path_to_your_browser_cookies>


Save the resulting headers_auth.json in the same folder as the script.

Usage

Run the script:

python playlist_converter.py


The script will:

Fetch all valid songs from the Spotify playlist.

Save them to spotify_songs.txt (for reference).

Create a new playlist on YouTube Music.

Add all found tracks to the new playlist.

Track progress is printed to the console. Skipped songs (local or not found) will also be indicated.

Notes

Only the first artist of each track is used for searching on YouTube Music.

Some songs may not be found due to different naming conventions on YouTube Music.

Be mindful of rate limits; the script uses a small delay (time.sleep(0.3)) between API calls.

License

This project is licensed under the MIT License.