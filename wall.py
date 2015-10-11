import os
import threading
from os import path
import datetime, time
import sqlite3
import SimpleHTTPServer
import SocketServer
import sched


#Every 5 mins update wall
REFRESH_RATE =  60 * 1 # e.g. 60 * 5 is every 5 mins.

schedule = sched.scheduler(time.time, time.sleep)

def build_wall(sc):
	print "Called"
	#Create database
	conn = sqlite3.connect('shebangswall.db')
	c = conn.cursor()
	files = [x for x in os.listdir('./') if path.isfile('./'+os.sep+x)]

	assets = ['index.html', 'styles.css', 'wall.py', '.wall.py.swp', 'shebangswall.db']


	f = open('index.html', 'w')
	f.write('<section id="photos">')
	f.write('<link rel="stylesheet" href="styles.css"></link>')

	#Get all media items from db
	for row in c.execute('SELECT * FROM media'):
		pic = str(row[2])
		if row[3]:
			link = str(row[3])
		else:
			link = 'http://www.shebangs.co/escapeblog/'

		f.write('<a href="' + link + '"><img src="' + pic + '" /></a>')


	f.write('</section>')
	f.close()
	conn.close()

	#Schedule recall
	sc.enter(REFRESH_RATE, 1, build_wall, (sc,))

	#Create images table
	#c.execute('''CREATE TABLE media
	#		(date text, description text, filepath text, link text) ''')

	#Insert all image paths into directory

	''' for pic in files:
		if pic not in assets:
			now = datetime.datetime.now()
			c.execute("INSERT INTO media (date, filepath) values (?, ?)",
				  (now, pic))
			conn.commit()
	conn.close()
	'''

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
threading.Thread(target=httpd.serve_forever).start()

schedule.enter(1, 1, build_wall, (schedule,)) #Zero seccond delay for initial run
schedule.run()

