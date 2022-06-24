AUTHOR = 'Rodrigo Lara'
SITENAME = 'Ingeniería y Data Science'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Santiago'

DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Plugins
PLUGINS = [
    'minchin.pelican.plugins.nojekyll'
]

#Theme
THEME = "/home/rodrigo/pelican-themes/built-texts"
# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),)

# Social widget
SOCIAL = (('Linkedin', 'https://www.linkedin.com/in/rodrigo--lara/'),
          ('Github', 'https://github.com/rodrigolara-cl'),
          ('Gmail', 'rodrigoalberto.lara@gmail.com'))

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
