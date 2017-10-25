from subprocess import *
from urllib import quote

server = "localhost:9999"

def get_qry_raw(raw):
	return "http://" + server + "/"+ raw

def get_qry(t="artist",artist="",album=""):
	s = "http://" + server + "/get_by_search?type="+ t + "&num_tracks=" + str(num)
	if artist:
		s = s + "&artist=" + artist 
	if album:
		s = s + "&album=" + album 
	return s

def get(artist,album):
	return "http://" + server + "/get_by_search?type=album&artist=" + artist + "&title=" + album

def get_artist(artist):
	return "http://" + server + "/get_by_search?type=artist&artist=" + artist

def get_radio(artist,num):
	#http://localhost:9999/get_new_station_by_search?type=artist&artist=Queen&num_tracks=100
	return "http://" + server + "/get_new_station_by_search?type=artist&artist=" + artist + "&num_tracks=" + str(num)