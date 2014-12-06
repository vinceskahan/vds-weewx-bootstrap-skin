Minimal bootstrap-based skin for weewx
vinceskahan@gmail.com

This is a minimalist bootstrap-based skin

Installation instructions:

1) run the installer:

setup.py install --extension vds-bootstrap.tgz

2) restart weewx:

sudo /etc/init.d/weewx stop
sudo /etc/init.d/weewx start

This will result in a skin called vds-bootstrap with a 
number of cross-linked web pages based on bootstrap.

The web root will be 'skins/bootstrap' for brevity,
so this obviously would conflict with any other skin
that uses the name 'bootstrap'.

Notes: this skin enables the xsearch.py example extension
 that comes with weewx, which permits the $alltime stats
 to be displayed.  It also enables $seven_day which is 
 not currently used.  See the xsearch.py code for details.
