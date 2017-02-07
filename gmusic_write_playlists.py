print "starting..."

from gmusicapi import Mobileclient
import sqlite3
import sys
import login_credentials

api = Mobileclient()
api.login(login_credentials.google_email, login_credentials.google_password, Mobileclient.FROM_MAC_ADDRESS)

con = sqlite3.connect('gmusic.db')
cur = con.cursor()

print "playlists ..."
playlists = api.get_all_user_playlist_contents()
cur.execute("DELETE FROM playlist")
cur.execute("DELETE FROM playlist_song")
for playlist in playlists:
	sql = "INSERT INTO playlist (playlistid, name, lastmodified) VALUES(" + "'" + playlist['tracks'][0]['playlistId'] + "','" + playlist['name'] + "'," + playlist['lastModifiedTimestamp'] + ")"
	cur.execute(sql)
	for track in playlist['tracks']:
		sql = "INSERT INTO playlist_song (trackid, playlistid, absoluteposition, lastmodified) VALUES(" + "'" + track['trackId'] + "','" + track['playlistId'] + "'," + str(track['absolutePosition']) + ',' + playlist['lastModifiedTimestamp'] + ")"
		cur.execute(sql)

con.commit()
con.close()

print "...stopping"
