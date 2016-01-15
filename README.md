# photowall

Photowall is a very simple Python script which takes a directory of images, 
inserts them into a Sqlite database & spits out a mobile friendly 'social wall' of these images.

It allows the user to add relevant links to each image by editing the sqlite database 
(I sugest using [DB Browser for SQLite for editing](https://github.com/sqlitebrowser/sqlitebrowser) until something more 
substantial is built. 

## Configuration / Options
* The script can be configured to refresh its database every x minutes as more data is added
* The script can be exposed as an upstart service (linux) so it runs merrily in the background


# [Demo](http://wall.shebangs.co)
Associated [blog post](https://karmacomputing.co.uk/blog/our-news-1/post/photo-wall-8)

![alt text](http://i61.tinypic.com/2wp6qub.png "Example")

## Future dreams & aspirations
* Twitter / Instagram / (insert social platform here) integration 
* A better admin interface for photowall, probably using the Flask based 
[Sqlite browser] (https://pypi.python.org/pypi/sqlite-browser/0.1.1) or similar*

*A very viable solution to editing the sqlite database remotly is to use [sshfs](fuse.sourceforge.net/sshfs.html) 
to mount the remote directory storing your photowall database and then use sqlitebrowser to edit it as though its stored locally.
[Digital Ocean] (https://www.digitalocean.com/community/tutorials/how-to-use-sshfs-to-mount-remote-file-systems-over-ssh)
 has a good tutorial on how to do this.
