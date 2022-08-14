# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
# SITEURL = ''
SITEURL = 'https://cgi.csc.liv.ac.uk/~rahul'
RELATIVE_URLS = False

# FEED_ALL_ATOM = 'feeds/all.atom.xml'
# CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None 

DELETE_OUTPUT_DIRECTORY = True

# fix the menu items -- taken from old publishconf.py
MENUITEMS = tuple([(a,SITEURL+b) for a,b in MENUITEMS])

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
