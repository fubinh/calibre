#!/usr/bin/env python2
# vim:fileencoding=utf-8
from __future__ import absolute_import, division, print_function, unicode_literals

__license__ = 'GPL v3'
__copyright__ = '2014, Kovid Goyal <kovid at kovidgoyal.net>'

from threading import Lock

from calibre.utils.icu import _icu
from calibre.utils.localization import lang_as_iso639_1

_iterators = {}
_lock = Lock()


def split_into_words(text, lang='en'):
    with _lock:
        it = _iterators.get(lang, None)
        if it is None:
            it = _iterators[lang] = _icu.BreakIterator(_icu.UBRK_WORD, lang_as_iso639_1(lang) or lang)
        it.set_text(text)
        return [text[p:p+s] for p, s in it.split2()]


def split_into_words_and_positions(text, lang='en'):
    with _lock:
        it = _iterators.get(lang, None)
        if it is None:
            it = _iterators[lang] = _icu.BreakIterator(_icu.UBRK_WORD, lang_as_iso639_1(lang) or lang)
        it.set_text(text)
        return it.split2()


def index_of(needle, haystack, lang='en'):
    with _lock:
        it = _iterators.get(lang, None)
        if it is None:
            it = _iterators[lang] = _icu.BreakIterator(_icu.UBRK_WORD, lang_as_iso639_1(lang) or lang)
        it.set_text(haystack)
        return it.index(needle)


def count_words(text, lang='en'):
    with _lock:
        it = _iterators.get(lang, None)
        if it is None:
            it = _iterators[lang] = _icu.BreakIterator(_icu.UBRK_WORD, lang_as_iso639_1(lang) or lang)
        it.set_text(text)
        return len(it.split2())
