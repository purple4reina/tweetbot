#!/usr/bin/python

import sys

sys.path.append('/homepages/10/d337401589/htdocs/modules/')

with open('/homepages/10/d337401589/htdocs/modules/tweetbot/parts_of_speech_word_files/verbs/31K_verbs.txt', 'r') as verb_list:

    verbs = verb_list.readlines()
    verbs = [v[:-2] for v in verbs]

def cleanbooks():

    with open('/homepages/10/d337401589/htdocs/modules/tweetbot/tweetlines.txt', 'a') as tweets:

        with open('/homepages/10/d337401589/htdocs/modules/tweetbot/booksample.txt', 'r') as books:
        
            for line in books:
                
                output = str()
                capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                write = 'off'
                for c in line:
                    if c in capital and write == 'off':
                        write = 'on'
                    if write == 'on':
                        output += c
                    if c == '.':
                        break

                if len(output) < 20 or len(output) > 40:
                    continue
                elif (output[-1] != '.') or ('\"' in output) or ('(' in output) or (')' in output) or ('\'' in output) or ('_' in output) or (':' in output) or ('Zarathustra' in output) or ('Gutenberg' in output) or ('Mr.' in output) or ('  ' in output) or ('|' in output) or ('=' in output) or ('{' in output) or ('}' in output) or ('Dr.' in output) or ('Mrs.' in output):
                    continue
                elif len(set(verbs) & set(output.split())) == 0:
                    continue
                else:
                    tweets.write('\n' + output)




