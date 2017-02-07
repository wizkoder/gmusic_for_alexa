print "starting..."

import sqlite3
import sys

con = sqlite3.connect('gmusic.db')
cur = con.cursor()

cur.execute("SELECT * FROM playlist_song")

rows = cur.fetchall()
for row in rows:
	print row

print "...stopping"