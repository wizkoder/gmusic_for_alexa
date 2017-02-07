print "starting..."

from gmusicapi import Mobileclient
import sqlite3
import sys
import login_credentials

api = Mobileclient()
api.login(login_credentials.google_email, login_credentials.google_password, Mobileclient.FROM_MAC_ADDRESS)

con = sqlite3.connect('gmusic.db')
cur = con.cursor()

print "songs ..."
songs = api.get_all_songs(incremental=False, include_deleted=False)
cur.execute("DELETE FROM song")
for song in songs:
	if hasattr(song,'year'):
		year = song['year']
	else:
		year = 1900
	cur.execute("INSERT INTO song (trackid, title, album, albumArtist, year, tracknumber, genre) VALUES (?,?,?,?,?,?,?)", (song['id'],song['title'],song['album'],song['albumArtist'],year,song['trackNumber'],song['genre']))

con.commit()
con.close()

print "...stopping"
