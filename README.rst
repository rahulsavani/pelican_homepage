Rahul Savani's academic homepage
================================

This home page uses pelican:

http://getpelican.com/

To produce the publication list it adapts

https://github.com/vene/pelican-bibtex

which in turn uses pybtex

http://pybtex.sourceforge.net/

One one minor change is made to pybtex, the addition of an extra
tag for bold in the html backend. In detail, the following line

.. code-block:: python

    'bold': u'strong',

is added to

pybtex/backends/html.py

as in the following:

.. code-block:: python

    class Backend(BaseBackend):
        default_suffix = '.html'
        symbols = {
            'ndash': u'&ndash;',
            'newblock': u'\n',
            'nbsp': u'&nbsp;'
        }
        tags = {
            'emph': u'em',
            'bold': u'strong',
        }

This change is not contained in this repo. The adaptation of pelican-bibtex is
included (in plugns/pelican-bibtex) along with a new pybtex style (in
rahul_style.py also in plugins/pelican-bibtex).
