Rahul Savani's academic homepage
================================

This home page uses pelican:

http://getpelican.com/

To produce the publication list it adapts

https://github.com/vene/pelican-bibtex

which in turn uses pybtex

http://pybtex.sourceforge.net/

One one minor change is made to pybtex, the addition of an extra
symbol for a line break in the html backend. In detail, the following line

.. code-block:: python

    'br': u'<BR/>',

is added to

pybtex/backends/html.py

as in the following:

.. code-block:: python

    class Backend(BaseBackend):
        default_suffix = '.html'
        symbols = {
            'ndash': u'&ndash;',
            'newblock': u'\n',
            'nbsp': u'&nbsp;',
            'br': u'<BR/>'
        }

This change is not contained in this repo. The adaptation of pelican-bibtex is
included (in plugns/pelican-bibtex/pelican-bibtex.py) along with a new pybtex style (in
plugins/pelican-bibtex/rahul_style.py).
