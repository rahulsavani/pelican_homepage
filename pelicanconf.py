# AUTHOR = 'TEST_AUTHOR'
# SITENAME = 'TEST_TITLE'
# SITEURL = ''
AUTHOR = u'Rahul Savani'
SITENAME = u"Rahul Savani"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

###############################################################################
# ADDED BY RAHUL:
PLUGIN_PATHS = ['plugins']
PLUGINS = ['pelican-bibtex']
PUBLICATIONS_SRC = 'content/rs_pubs_web.bib'

DIRECT_TEMPLATES = ['publications']


STATIC_PATHS = ['images']

# turn off automatic display of pages so we can order them ourselves
DISPLAY_PAGES_ON_MENU = False

THEME = 'themes/notmyidea'

MENUITEMS = (
    ('Home',                '/index.html'),
    ('Contact',             '/pages/contact-details.html'),
    ('Bio',                 '/pages/short-bio.html'),
    ('Papers',              '/publications.html'),
    ('Research Activities', '/pages/research-activities.html'),
    ('Teaching',            '/pages/teaching.html'),
    ('Game solvers',        '/pages/game-solvers.html'),
)


###############################################################################

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


###############################################################################
# EDITED BY RAHUL:

# Blogroll
# LINKS = (('Pelican', 'https://getpelican.com/'),
         # ('Python.org', 'https://www.python.org/'),
         # ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         # ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
          # ('Another social link', '#'),)

# Social widget
SOCIAL = (
    ('github', 'https://github.com/rahulsavani'),
    ('bitbucket', 'https://bitbucket.org/rahulsavani'),
    #('stackex', 'http://stackexchange.com/users/280773/rahul-savani'),
    ('dblp', 'http://dblp.uni-trier.de/pers/hy/s/Savani:Rahul'),
    ('scholar', 'https://scholar.google.co.uk/citations?user=bfqfILEAAAAJ&hl=en'), 
    ('linkedin', 'https://www.linkedin.com/in/rahulsavani'),
    ('facebook', 'https://www.facebook.com/rahul.savani'),
    )

#FILES_TO_COPY = (
            #('extra/CNAME', 'CNAME'),
            #)
STATIC_PATHS = [
            'extra/CNAME',
                ]
EXTRA_PATH_METADATA = {
            'extra/CNAME': {'path': 'CNAME'},
                }




DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
