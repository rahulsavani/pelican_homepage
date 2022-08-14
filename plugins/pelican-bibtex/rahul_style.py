from __future__ import unicode_literals

from pybtex.style.formatting.plain import Style
from pybtex.richtext import Symbol, Text
from pybtex.style.formatting import BaseStyle, toplevel
from pybtex.style.template import (
    field, first_of, href, join, names, optional, optional_field, sentence,
    tag, together, words
)

# pages = field('pages', apply_func=dashify)
pages = field('pages', apply_func=None)
date = words [optional_field('month'), field('year')]

class RahulStyle(Style):

    def get_inproceedings_template(self, e):

        # print("PRINT: Using Rahul's format_inproceedings")

        template = toplevel [
            tag('b') [self.format_title(e, 'title')],
            Symbol('br'),
            self.format_names('author'),
            Symbol('br'),
            words [
                # 'In',
                # optional[ self.format_editor(e, as_sentence=False) ],
                # tag('conference') [self.format_btitle(e, 'booktitle', as_sentence=False)],
                tag('conference') [self.format_btitle(e, 'shorttitle', as_sentence=False)],
                # self.format_volume_and_series(e, as_sentence=False),
                # optional[ words [pages] ], 
                # optional[ field('pages') ],
                # optional_field('pages',apply_func=dashify) # ABC ERROR
                #self.format_address_organization_publisher_date(e),
                Symbol('br'),
            ],
            optional [
                words [
                    field('note'),
                    Symbol('br')  
                ]
            ],
            #self.format_web_refs(e),
        ]
        # print field('pages',apply_func=dashify) # ABC error

        # return template.format_data(e)
        return template


    def get_unpublished_template(self, e):
        template = toplevel [
            self.format_title(e, 'title'),
            Symbol('br'),
            self.format_names('author'),
            Symbol('br'),
            field('note'),
                #optional[ date ]
            #Symbol('br'),
            #self.format_web_refs(e),
        ]
        # return template.format_data(e)
        return template


    def get_inbook_template(self, e):
        template = toplevel [
            tag('pubtitle') [tag('b') [field('title')]],
            Symbol('br'),
            sentence [self.format_names('author')],
            self.format_volume_and_series(e),
            Symbol('br'),
            words [
                sentence(capfirst=True) [
                    self.format_chapter_and_pages(e),
                    #optional[ self.format_editor(e, as_sentence=False) ],
                    self.format_btitle(e, 'booktitle', as_sentence=False),
                    #self.format_volume_and_series(e, as_sentence=False),
                    #self.format_chapter_and_pages(e),
                ],
            Symbol('br'),
            sentence [
                field('publisher'),
                optional_field('address'),
                optional [
                    words [field('edition'), 'edition']
                ],
                #date,
                #Symbol('br'),
                #optional_field('note'),
                ],
            ],
            Symbol('br'),
            sentence [
                optional_field('note'),
            ],
            Symbol('br'),
            #self.format_web_refs(e),
        ]
        # return template.format_data(e)
        return template


    def get_techreport_template(self, e):
        template = toplevel [
            self.format_title(e, 'title'),
            Symbol('br'),
            sentence [self.format_names('author')],
            Symbol('br'),
            sentence [
                words[
                    first_of [
                        optional_field('type'),
                        'Technical Report:',
                    ],
                    optional_field('number')
                ],
                #Symbol('br'),
                #field('institution'),
                #optional_field('address'),
                #date,
            ],
            Symbol('br'),
            sentence(capfirst=False) [ optional_field('note') ],
            #self.format_web_refs(e),
        ]
        # return template.format_data(e)
        return template

    def get_article_template(self, e):
        volume_and_pages = first_of [
            # volume and pages, with optional issue number
            optional [
                join [
                    field('volume'),
                    optional['(', field('number'),')'],
                    ':', pages
                ],
            ],
            # pages only
            words ['pages', pages],
        ]
        template = toplevel [
            self.format_title(e, 'title'),
            Symbol('br'),
            self.format_names('author'),
            Symbol('br'),
            tag('journal') [tag('b') [field('journal')]],
            optional[ volume_and_pages ], 
            Symbol('br'),
            optional [
                words [
                    field('note'),
                    Symbol('br')  
                ]
            ],
            #self.format_web_refs(e),
            #sentence(capfirst=False) [ optional_field('note') ],
        ]
        # return template.format_data(e)
        return template

    def get_phdthesis_template(self, e):
        template = toplevel [
            tag('pubtitle') [self.format_btitle(e, 'title')],
            Symbol('br'),
            sentence [self.format_names('author')],
            Symbol('br'),
            sentence[
                'PhD thesis',
                field('school'),
                optional_field('address'),
                date,
            ],
            sentence(capfirst=False) [ optional_field('note') ],
            Symbol('br'),
            #self.format_web_refs(e),
        ]
        # return template.format_data(e)
        return template

    def get_proceedings_template(self, e):
        template = toplevel [
            first_of [
                # there are editors
                optional [
                    join(' ')[
                        sentence(capfirst=True) [tag('b') [self.format_title(e, 'title')]],
                        Symbol('br'),
                        self.format_editor(e),
                        #self.format_btitle(e, 'title', as_sentence=False),
                        Symbol('br'),
                        self.format_volume_and_series(e, as_sentence=False),
                        self.format_address_organization_publisher_date(e),
                        Symbol('br'),
                    ],
                ],
                # there is no editor
                optional_field('organization'),
                sentence [
                    self.format_btitle(e, 'title', as_sentence=False),
                    self.format_volume_and_series(e, as_sentence=False),
                    #self.format_address_organization_publisher_date(e, include_organization=False),
                ],
            ],
            #sentence(capfirst=False) [ optional_field('note') ],
            #self.format_web_refs(e),
        ]
        # return template.format_data(e)
        return template

    def get_misc_template(self, e):
        template = toplevel [
            tag('pubtitle') [tag('b') [field('title')]],
            Symbol('br'),
            optional[ sentence [self.format_names('author')] ],
            Symbol('br'),
            optional [
                words [
                    sentence [ field('note')],
                    Symbol('br')  
                ]
            ],
            #sentence[
                #optional[ field('howpublished') ],
                #optional[ date ],
            #],
            #sentence(capfirst=False) [ optional_field('note') ],
            #self.format_web_refs(e),
        ]
        # return template.format_data(e)
        return template

###############################################################################
# END OF GET TEMPLATES FUNCTIONS
###############################################################################

###############################################################################
# START OF FORMATTING FUNCTIONS
###############################################################################

    def format_title(self, e, which_field, as_sentence=False):

        def protected_capitalize(x):
            """Capitalize string, but protect {...} parts."""
            result = ""
            level = 0
            for pos, c in enumerate(x):
                if c == '{':
                    level += 1
                elif c == '}':
                    level -= 1
                elif pos == 0:
                    c = c.upper()
                elif level <= 0:
                    c = c.lower()
                result += c
            return result

        # formatted_title = field(which_field)

        formatted_title = tag('pubtitle') [ tag('b') [field(which_field)]]

        # formatted_title = field(  ABC ERROR
            # which_field, apply_func=protected_capitalize)

        if as_sentence:
            return sentence(capfirst=False) [tag('b') [ formatted_title ]]
        else:
            return formatted_title

    # fixes e.g., PhD thesis (from non-bold and with a fullstop)
    #       and short conference names
    def format_btitle(self, e, which_field, as_sentence=False):
        formatted_title = tag('b') [ field(which_field) ]
        if as_sentence:
            return sentence[ formatted_title ]
        else:
            return formatted_title
###############################################################################
###############################################################################
###############################################################################
###############################################################################

class Tmp():


    def format_names(self, role, as_sentence=False):
        formatted_names = names(role, sep=', ', sep2 = ' and ', last_sep=', and ')
        if as_sentence:
            return sentence(capfirst=False) [formatted_names]
        else:
            return formatted_names



    def format_author_or_editor(self, e):
        return first_of [
            optional[ self.format_names('author') ],
            self.format_editor(e),
        ]

    def format_editor(self, e, as_sentence=False):
        editors = self.format_names('editor', as_sentence=False)
        if 'editor' not in e.persons:
            # when parsing the template, a FieldIsMissing exception
            # will be thrown anyway; no need to do anything now,
            # just return the template that will throw the exception
            return editors
        if len(e.persons['editor']) > 1:
            word = 'editors'
        else:
            word = 'editor'
        result = join(sep=', ') [editors, word]
        if as_sentence:
            return sentence(capfirst=False) [result]
        else:
            return result
    
    def format_volume_and_series(self, e, as_sentence=False):
        volume_and_series = optional [
            words [
                'volume', field('volume'), optional [
                    words ['of', field('series')]
                ]
            ]
        ]
        number_and_series = optional [
            words [
                join(sep=Symbol('nbsp')) ['number', field('number')],
                optional [
                    words ['in', field('series')]
                ]
            ]
        ]
        series = optional_field('series')
        result = first_of [
                volume_and_series,
                number_and_series,
                series,
            ]
        if as_sentence:
            return sentence(capfirst=False) [result]
        else:
            return result
    
    def format_chapter_and_pages(self, e):
        return join(sep=', ') [
            optional [words ['chapter', field('chapter')]],
            optional [words ['pages', pages]],
        ]

    def format_edition(self, e):
        return optional [
            words [
                field('edition', apply_func=lambda x: x.lower()),
                'edition',
            ]
        ]

    def format_address_organization_publisher_date(
        self, e, include_organization=True):
        """Format address, organization, publisher, and date.
        Everything is optional, except the date.
        """
        # small difference from unsrt.bst here: unsrt.bst
        # starts a new sentence only if the address is missing;
        # for simplicity here we always start a new sentence
        if include_organization:
            organization = optional_field('organization')
        else:
            organization = None
        return first_of[
            # this will be rendered if there is an address
            optional [
                join(sep=' ') [
                    sentence[
                        field('address'),
                        date,
                    ],
                    sentence[
                        organization,
                        optional_field('publisher'),
                    ],
                ],
            ],
            # if there is no address then we have this
            sentence[
                organization,
                optional_field('publisher'),
                date,
            ],
        ]

    def format_book(self, e):
        template = toplevel [
            self.format_author_or_editor(e),
            self.format_btitle(e, 'title'),
            self.format_volume_and_series(e),
            sentence [
                field('publisher'),
                optional_field('address'),
                self.format_edition(e),
                date
            ],
            sentence(capfirst=False) [ optional_field('note') ],
            self.format_web_refs(e),
        ]
        return template.format_data(e)

    def format_booklet(self, e):
        template = toplevel [
            self.format_names('author'),
            self.format_title(e, 'title'),
            sentence [
                optional_field('howpublished'),
                optional_field('address'),
                date,
                optional_field('note'),
            ],
            self.format_web_refs(e),
        ]
        return template.format_data(e)



    def format_incollection(self, e):
        template = toplevel [
            self.format_title(e, 'title'),
            sentence [self.format_names('author')],
            words [
                'In',
                sentence(capfirst=False) [
                    optional[ self.format_editor(e, as_sentence=False) ],
                    self.format_btitle(e, 'booktitle', as_sentence=False),
                    self.format_volume_and_series(e, as_sentence=False),
                    self.format_chapter_and_pages(e),
                ],
            ],
            sentence [
                optional_field('publisher'),
                optional_field('address'),
                self.format_edition(e),
                date,
            ],
            self.format_web_refs(e),
        ]
        return template.format_data(e)

    def format_manual(self, e):
        # TODO this only corresponds to the bst style if author is non-empty
        # for empty author we should put the organization first
        template = toplevel [
            optional [ sentence [ self.format_names('author') ] ],
            self.format_btitle(e, 'title'),
            sentence [
                optional_field('organization'),
                optional_field('address'),
                self.format_edition(e),
                optional[ date ],
            ],
            sentence(capfirst=False) [ optional_field('note') ],
            self.format_web_refs(e),
        ]
        return template.format_data(e)

    def format_web_refs(self, e):
        # based on urlbst output.web.refs
        return sentence(capfirst=False) [
            optional [ self.format_url(e) ],
            optional [ self.format_eprint(e) ],
            optional [ self.format_pubmed(e) ],
            optional [ self.format_doi(e) ],
            ]

    def format_url(self, e):
        # based on urlbst format.url
        return href [
            field('url'),
            join(' ') [
                'URL:',
                field('url')
                ]
            ]

    def format_pubmed(self, e):
        # based on urlbst format.pubmed
        return href [
            join [
                'http://www.ncbi.nlm.nih.gov/pubmed/',
                field('pubmed')
                ],
            join [
                'PMID:',
                field('pubmed')
                ]
            ]

    def format_doi(self, e):
        # based on urlbst format.doi
        return href [
            join [
                'https://doi.org/',
                field('doi')
                ],
            join [
                'doi:',
                field('doi')
                ]
            ]

    def format_eprint(self, e):
        # based on urlbst format.eprint
        return href [
            join [
                'http://arxiv.org/abs/',
                field('eprint')
                ],
            join [
                'arXiv:',
                field('eprint')
                ]
            ]
