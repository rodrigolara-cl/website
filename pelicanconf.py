from datetime import datetime

AUTHOR = 'Rodrigo Lara'
SITENAME = 'Ingeniería y Data Science'
SITESUBTITLE = "Un archivo de mis proyectos"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Santiago'
PROFILEPIC = 'profile_pic.jpg'
DEFAULT_LANG = 'es'
COMMENTBOX = '5676459674828800-proj'
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
THEME = "future-imperfect"
# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),)

# Social widget
SOCIAL = (('Linkedin', 'https://www.linkedin.com/in/rodrigo--lara/'),
          ('Github', 'https://github.com/rodrigolara-cl'),)

#DISPLAY_CATEGORIES_ON_MENU = False
#DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
    ('Inicio', '/'),
    #('Archivos', '/archivos.html'),
    #('Tags', '/tags.html'),
    ('Blog', '/category/blog.html'),
    ('Acerca de', '/pages/acerca-de.html'),
)
CONTACTS = [
    ("Twitter", "twitter", "https://twitter.com/lesterxileno"),
    ("Instagram", "instagram", "https://www.instagram.com/lesterxileno/"),
    ("Github", "github", "https://github.com/rodrigolara-cl"),
    ("Linkedin", "linkedin", "https://www.linkedin.com/in/rodrigo--lara/")
]
DEFAULT_PAGINATION = 5
LOAD_CONTENT_CACHE = False
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
now = datetime.now()
current_datetime = now.strftime("%Y-%m-%d %H:%M")
#DEFAULT_METADATA = {
  #  'status': 'draft',
    #'date': current_datetime
#}
PLUGINS = []
