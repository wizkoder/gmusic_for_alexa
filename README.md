# gmusic_for_alexa
Make Google Music Accessible by Alexa (Raspberry Pie) needed!

1. You need: Python, Sqlite
2. Install the gmusicapi: pip install gmusicapi
3. Create Database and Tables: python create_database.py
4. Read in your playlists from Google Music: python gmusic_write_playlists.py
5. Read in your songs from Google Music: python gmusic_write_songs.py
6. Get Url of a song: python gmusic_stream_song.py (You need to enter a TrackId that exists in your Library)
7. Todo: search Upnp Renderer
8. Todo: Stream to this device