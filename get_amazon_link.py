#!/usr/bin/python

import amazonproduct
import random


def get_amazon_link():
    assoc_id = 'clacatblo-20'
    random_word = get_random_word()

    api = amazonproduct.API(locale='us')
    try:
        items = api.item_search('Books', Keywords=random_word)
    except amazonproduct.errors.NoExactMatchesFound:
        # if the random word search yields no results, try again
        print 'Match not found, trying again'
        return get_amazon_link()

    book = get_random_book(items)
    asin = book.ASIN

    link = 'http://www.amazon.com/gp/product/{}/?&tag={}'.format(
        asin, assoc_id)

    return link


def get_random_word():
    file_path = (
        '/homepages/10/d337401589/htdocs'
        '/modules/tweetbot/parts_of_speech_word_files'
        '/nouns/2syllablenouns.txt'
    )
    with open(file_path) as nouns:
        # slice of the \n at the end of the found noun
        return random.choice(nouns.readlines())[:-2]


def get_random_book(items):
    # total items returned by the search
    len_items = items.results

    # we only have access to up to 100 at this time, if the actual length is
    # greater than this, set the len to 100
    if len_items > 100:
        len_items = 100

    # get random index
    rand_item_index = random.randrange(len_items)

    i = 0
    for book in items:
        if i == rand_item_index:
            break
        i += 1
    return book
