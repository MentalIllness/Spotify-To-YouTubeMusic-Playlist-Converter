import spotipy
from spotipy.oauth2 import SpotifyOAuth
from ytmusicapi import YTMusic
import time

# ---------- SPOTIFY AUTH ----------
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="YOUR CLIENT ID",
    client_secret="YOUR CLIENT SECRET",
    redirect_uri="https://example.com/callback",
    scope="playlist-read-private"
))

# Spotify Playlist ID
playlist_id = "YOUR PLAYLIST ID"

print("Fetching tracks from Spotify...")

results = sp.playlist_items(playlist_id)
tracks = results["items"]

songs = []
for item in tracks:
    track = item.get("track")

    if track is None:
        print("Skipped deleted track.")
        continue

    if track.get("is_local"):
        print("Skipped local file:", track.get("name"))
        continue

    title = track.get("name")
    artists = track.get("artists", [])

    if not title or not artists:
        print("Skipped invalid track metadata.")
        continue

    artist = artists[0]["name"]
    songs.append(f"{title} {artist}")

print(f"Found {len(songs)} valid songs.")

# Save them to a file so you SEE them
with open("spotify_songs.txt", "w", encoding="utf-8") as f:
    for s in songs:
        f.write(s + "\n")

print("Saved songs to spotify_songs.txt")

# ---------- YT MUSIC AUTH ----------
yt = YTMusic("headers_auth.json")

new_playlist_id = yt.create_playlist(
    title="mess (shuffled)",
    description="Converted playlist"
)

print("Created YT Music playlist:", new_playlist_id)

# Add songs
for i, song in enumerate(songs):
    print(f"Processing song {i+1}/{len(songs)} → {song}")

    results = yt.search(song, filter="songs")
    if not results:
        print(f"  Not found: {song}")
        continue

    video_id = results[0]["videoId"]

    try:
        yt.add_playlist_items(new_playlist_id, [video_id])
        print(f"  Added: {song}")
    except Exception as e:
        if "409" in str(e):
            print(f"  Skipped (409 conflict, probably duplicate): {song}")
        else:
            print("  Error adding:", e)

    time.sleep(0.3)


print("Conversion finished.")


