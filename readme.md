# Spotify To YouTube Music Converter

A simple and efficient tool to transfer your playlists from Spotify to YouTube Music using proper API authentication.

## Features

- Convert Spotify playlists to YouTube Music playlists
- Maintain track order and metadata
- Support for private and public playlists
- Fast and reliable API-based transfer using headers-based authentication for YT Music

## Requirements

- Python 3.10+
- `spotipy` library for Spotify API
- `ytmusicapi` library for YouTube Music API

## Installation

1. Install dependencies:

`pip install spotipy ytmusicapi`

2. Configure your API credentials:

- **Spotify:** Use `SpotifyOAuth` with your Client ID, Client Secret, Redirect URI, and `playlist-read-private` scope. Via the Spotify's Developer  Dashboard!!
- **YouTube Music:** Use `headers_auth.json` exported from your YT Music session for authentication.

## How to Get `headers_auth.json` for YouTube Music

1. **Open YouTube Music in Google Chrome or Firefox**:

   - Go to [https://music.youtube.com](https://music.youtube.com)
   - Log in with your Google account.

2. **Open Developer Tools**:

   - Chrome: `Ctrl+Shift+I` (Windows) / `Cmd+Option+I` (Mac)
   - Firefox: `Ctrl+Shift+I` (Windows) / `Cmd+Option+I` (Mac)

3. **Go to the Network tab**:

   - Reload the page to capture requests.
   - Filter requests by `browse` or `xhr`.

4. **Find a request to `browse` endpoint**:

   - Click on any request to `https://music.youtube.com/youtubei/v1/browse`
   - Go to the `Headers` section.
   - Copy all request headers, including:

     - `Authorization` (if present)
     - `x-goog-authuser`
     - `x-origin`
     - `User-Agent`
     - `Cookie` (most important: contains `SAPISID`, `SID`, `HSID`, etc.)

5. **Save headers to `headers_auth.json`**:

   - Create a new file called `headers_auth.json`
   - Format the headers as JSON, for example:

```json
{
    "accept": "application/json",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/json",
    "cookie": "SAPISID=xxxx; SID=xxxx; HSID=xxxx; ...",
    "user-agent": "Your browser user agent string",
    "x-goog-authuser": "0",
    "x-origin": "https://music.youtube.com"
}
```
6. Place headers_auth.json in the same folder as the script.
