print "starting..."

import sqlite3
import sys

con = sqlite3.connect('gmusic.db')
con.execute ("CREATE TABLE playlist (playlistid text, name text, lastmodified number)")
con.execute ("CREATE TABLE playlist_song (trackid text, playlistid text, absoluteposition number, lastmodified number)")
con.execute ("CREATE TABLE song (trackid number, title text, albumId text, album text, albumArtist text, year number, tracknumber number, genre text)")

print "...stopping"
