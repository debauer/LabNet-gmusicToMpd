#!/usr/bin/python
#
# Autor: David 'debauer' Bauer
# www.debauer.net
# 
# Part of the FabLab Karlsruhe e.V. LabNet (lab automation and integration)
#
# Status: Tested
#


from subprocess import *
import os
import time
from flask import Flask, jsonify
from urllib import quote

app = Flask(__name__)

server = "localhost:9999"
mpd_folder = "/mnt/daten/public/"
playlist_folder = "Musik/temp_playlists/"

def get_by_search(artist,album):
	return "http://" + server + "/get_by_search?type=album&artist=" + artist + "&title=" + album

def get_new_station_by_search(artist,num):
	#http://localhost:9999/get_new_station_by_search?type=artist&artist=Queen&num_tracks=100
	return "http://" + server + "/get_new_station_by_search?type=artist&artist=" + artist + "&num_tracks=" + str(num)

def run_cmd(cmd):
	p = Popen(cmd, shell=True, stdout=PIPE)
	output = p.communicate()[0]
	return output

def save_playlist(m3u,filename):
	text_file = open(mpd_folder + playlist_folder + filename, "w")
	text_file.write(m3u)
	text_file.close()
	return m3u

def random_filename():
	return str(time.time()).replace(".","")  + ".m3u"

@app.route('/play/album/<string:artist>/<string:album>', methods=['get'])
def play_album(artist, album):
	filename = random_filename()
	artist = quote(artist)
	album = quote(album)
	m3u = save_playlist(run_cmd("curl -s '" + get_by_search(artist,album) + "'"),filename)
	run_cmd("mpc clear")
	run_cmd("mpc load Musik/temp_playlists/" + filename)
	run_cmd("mpc play")
	return m3u, 201

@app.route('/add/album/<string:artist>/<string:album>', methods=['get'])
def add_album(artist, album):
	filename = random_filename()
	artist = quote(artist)
	album = quote(album)
	m3u = save_playlist(run_cmd("curl -s '" + get_by_search(artist,album) + "'"),filename)
	#run_cmd("mpc clear")
	run_cmd("mpc load Musik/temp_playlists/" + filename)
	run_cmd("mpc play")
	return m3u, 201

@app.route('/add/radio/<string:artist>', methods=['get'])
def add_radio(artist):
	filename = random_filename()
	artist = quote(artist)
	m3u = save_playlist(run_cmd("curl -s '" + get_new_station_by_search(artist,100) + "'"),filename)
	#run_cmd("mpc clear")
	run_cmd("mpc load Musik/temp_playlists/" + filename)
	run_cmd("mpc play")
	return m3u, 201

@app.route('/play/radio/<string:artist>', methods=['get'])
def play_radio(artist):
	filename = random_filename()
	artist = quote(artist)
	m3u = save_playlist(run_cmd("curl -s '" + get_new_station_by_search(artist,100) + "'"),filename)
	run_cmd("mpc clear")
	run_cmd("mpc load Musik/temp_playlists/" + filename)
	run_cmd("mpc play")
	return m3u, 201

if __name__ == '__main__':
	#app.run(host="192.168.3.184",port=5002,debug=True)
	app.run(host="192.168.1.6",port=5003,debug=True)
	#app.run(port=5002,debug=True)