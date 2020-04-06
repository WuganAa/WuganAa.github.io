#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = 'Xᴜɢᴀɴ Cʜᴇɴ'
SITEURL = 'http://localhost:8000'
SITENAME = 'Xᴜɢᴀɴ Cʜᴇɴ'
SITETITLE = 'Xᴜɢᴀɴ Cʜᴇɴ'
SITELOGO = '/images/myself.jpg'
SITESUBTITLE = 'Mathematics and Finance, <br>School of Mathematical Sciences, <br>Chu Kochen Honors College, <br>Zhejiang University'
SITEDESCRIPTION = 'Xugan Chen - Mathematics and Finance. '
FAVICON = '/images/earth1.ico'


# file
PATH = 'content'

# theme
THEME = "./pelican-themes/Flex"

TIMEZONE = 'UTC' # Asia/Shanghai, America/New_York

I18N_TEMPLATES_LANG = 'en'
DEFAULT_LANG = 'en'
OG_LOCALE = 'en_US'
LOCALE = 'en_US'

DATE_FORMATS = {
    'en': '%B %d, %Y',
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_PAGES_ON_MENU = False
LINKS_IN_NEW_TAB = False
USE_FOLDER_AS_CATEGORY = True
HOME_HIDE_TAGS = False

SUMMARY_MAX_LENGTH = '-1'

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
ARTICLE_URL = 'articles/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{slug}.html'

# Blogroll
LINKS = (
    ('About', '/'),
    ('Curriculum Vitae', '/download/xuganchen_cv.pdf'),
    ('Blog', '/category/blog.html'),
)

# Social widget
SOCIAL = (
    ('github', 'https://github.com/wuganaa'),
    ('envelope', 'mailto:chenxg014@gmail.com'),
    ('linkedin', 'https://www.linkedin.com/in/xuganchen/'),
)


MENUITEMS = (
    ('Blog', '/category/blog.html'),
    ('Archives', '/archives.html'),
    ('Tags', '/tags.html'),
    ('About', '/hello.html'),
)

STATIC_PATHS = ['images', 'download', 'favicon.ico']


DEFAULT_PAGINATION = False

# COPYRIGHT_NAME = 'Xugan Chen <a href="https://github.com/wuganaa" title="GitHub → https://github.com/wuganaa" rel="noopener" target="_blank"><i class="fab fa-github"></i></a>   <a href="mailto:chenxg014@gmail.com" title="E-Mail → mailto:chenxg014@gmail.com" rel="noopener" target="_blank"><i class="fas fa-envelope"></i></a>'
COPYRIGHT_NAME = 'Xugan Chen'
COPYRIGHT_YEAR = '2018 - %d' % datetime.now().year


# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True


