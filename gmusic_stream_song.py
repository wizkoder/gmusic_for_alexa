print "starting..."

from gmusicapi import Mobileclient
import sys
import login_credentials

api = Mobileclient()
api.login(login_credentials.google_email, login_credentials.google_password, Mobileclient.FROM_MAC_ADDRESS)

print "url: " + api.get_stream_url('59b55acc-09c2-3048-9463-40cf50d34d16')

print "...stopping"