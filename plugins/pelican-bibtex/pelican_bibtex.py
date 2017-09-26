"""
Pelican BibTeX
==============

A Pelican plugin that populates the context with a list of formatted
citations, loaded from a BibTeX file at a configurable path.

The use case for now is to generate a ``Publications'' page for academic
websites.
"""
# Author: Vlad Niculae <vlad@vene.ro>
# Unlicense (see UNLICENSE for details)

import logging
logger = logging.getLogger(__name__)

from pelican import signals

__version__ = '0.2.1'


def add_publications(generator):
    """
    Populates context with a list of BibTeX publications.

    Configuration
    -------------
    generator.settings['PUBLICATIONS_SRC']:
        local path to the BibTeX file to read.

    Output
    ------
    generator.context['publications']:
        List of tuples (key, year, text, bibtex, pdf, slides, poster).
        See Readme.md for more details.
    """
    if 'PUBLICATIONS_SRC' not in generator.settings:
        return
    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO
    try:
        from pybtex.database.input.bibtex import Parser
        from pybtex.database.output.bibtex import Writer
        from pybtex.database import BibliographyData, PybtexError
        from pybtex.backends import html
        #from pybtex.style.formatting import plain
        from rahul_style import Style as RahulStyle

    except ImportError:
        logger.warn('`pelican_bibtex` failed to load dependency `pybtex`')
        return

    refs_file = generator.settings['PUBLICATIONS_SRC']
    try:
        bibdata_all = Parser().parse_file(refs_file)
    except PybtexError as e:
        logger.warn('`pelican_bibtex` failed to parse file %s: %s' % (
            refs_file,
            str(e)))
        return

    publications = []

    # format entries
    plain_style = RahulStyle()
    #plain_style = plain.Style()
    html_backend = html.Backend()

    html_backend.symbols['br'] = u'<BR/>'
            
    all_entries = bibdata_all.entries.values()

    # remove URL field if DOI is present
    for entry in all_entries:
        if "doi" in entry.fields.keys():
            entry.fields._dict["url"] = ""

    formatted_entries = plain_style.format_entries(all_entries)
    for formatted_entry in formatted_entries:
        key = formatted_entry.key
        entry = bibdata_all.entries[key]
        pub_type = entry.type
        year = entry.fields.get('year')
        # This shouldn't really stay in the field dict
        # but new versions of pybtex don't support pop
        pdf = entry.fields.get('pdf', None)
        #slides = entry.fields.get('slides', None)
        #poster = entry.fields.get('poster', None)
        doi = entry.fields.get('doi', None)
        url = entry.fields.get('url', None)
        arxiv = entry.fields.get('arxiv', None)

        #render the bibtex string for the entry
        bib_buf = StringIO()
        bibdata_this = BibliographyData(entries={key: entry})
        Writer().write_stream(bibdata_this, bib_buf)

        text = formatted_entry.text.render(html_backend)

        # prettify entries
        # remove BibTeX's {}
        text = text.replace("\{", "")
        text = text.replace("{", "")
        text = text.replace("\}", "")
        text = text.replace("}", "")
        # remove textbf used for cv
        text = text.replace("\\textbf ", "")
        # remove \ that comes after Proc.
        text = text.replace("\\", "")

        publications.append((pub_type,
                             key,
                             year,
                             text,
                             bib_buf.getvalue(),
                             pdf,
                             doi,
                             url,
                             arxiv))

    generator.context['publications'] = publications


def register():
    signals.generator_init.connect(add_publications)
