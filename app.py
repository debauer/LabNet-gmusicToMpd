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
from urllib import quote
import gmusic

from flask import Flask, jsonify, render_template, flash, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *
from flask_socketio import SocketIO, emit

nav = Nav()

topbar = Navbar('',
    View('Home', 'index'),
    View('Your Account', 'index'),
)

nav.register_element('top', topbar)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

nav.init_app(app)
Bootstrap(app)

server = "localhost:9999"
mpd_folder = "/srv/public/Nutzer/"
playlist_folder = "David_Bauer/temp_playlist/"

def cmd_run(cmd):
	p = Popen(cmd, shell=True, stdout=PIPE)
	output = p.communicate()[0]
	return output

def playlist_safe(m3u,filename):
	text_file = open(mpd_folder + playlist_folder + filename, "w")
	text_file.write(m3u)
	text_file.close()
	return m3u

def filename_random():
	return str(time.time()).replace(".","")  + ".m3u"

def mpc_helper(fn,clear=True):
	if clear == True:
		cmd_run("mpc clear")
	cmd_run("mpc load " + playlist_folder + fn)
	cmd_run("mpc play")
	return 201

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/play/album/<string:artist>/<string:album>', methods=['get'])
def play_album(artist, album):
	filename = "album_" + artist + "_" + album + "_" + filename_random()
	filename = filename.replace(" ", "")
	m3u = playlist_safe(cmd_run("curl -s '" + gmusic.get(quote(artist),quote(album)) + "'"),filename)
	return m3u, mpc_helper(filename)

@app.route('/add/album/<string:artist>/<string:album>', methods=['get'])
def add_album(artist, album):
	filename = "album_" + artist + "_" + album + "_" + filename_random()
	filename = filename.replace(" ", "")
	m3u = playlist_safe(cmd_run("curl -s '" + gmusic.get(quote(artist),quote(album)) + "'"),filename)
	return m3u, mpc_helper(filename,False)

@app.route('/add/artist/<string:artist>', methods=['get'])
def add_artist(artist):
	filename = "artist_" + artist + "_" + filename_random()
	filename = filename.replace(" ", "")
	m3u = playlist_safe(cmd_run("curl -s '" + gmusic.get_artist(quote(artist)) + "'"),filename)
	return m3u, mpc_helper(filename,False)

@app.route('/play/artist/<string:artist>', methods=['get'])
def play_artist(artist):
	filename = "artist_" + artist + "_" + filename_random()
	filename = filename.replace(" ", "")
	m3u = playlist_safe(cmd_run("curl -s '" + gmusic.get_artist(quote(artist)) + "'"),filename)
	return m3u, mpc_helper(filename)

@app.route('/add/radio/<string:artist>', methods=['get'])
def add_radio(artist):
	filename = "radio_" + artist + "_" + filename_random()
	filename = filename.replace(" ", "")
	m3u = playlist_safe(cmd_run("curl -s '" + gmusic.get_radio(quote(artist),100) + "'"),filename)
	return m3u, mpc_helper(filename,False)

@app.route('/play/radio/<string:artist>', methods=['get'])
def play_radio(artist):
	filename = "radio_" + artist + "_" +filename_random()
	filename = filename.replace(" ", "")
	m3u = playlist_safe(cmd_run("curl -s '" + gmusic.get_radio(quote(artist),100) + "'"),filename)
	return m3u, mpc_helper(filename)

if __name__ == '__main__':
	#app.run(host="192.168.3.184",port=5002,debug=True)
	#socketio.run(app)
	app.run(host="192.168.1.6",port=5003,debug=True)
	#app.run(port=5002,debug=True)
