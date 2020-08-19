"""
get_movie.py

Convert this script to imdbpy https://imdbpy.github.io/downloads/

Usage: get_movie 'movieID'

Show some info about the movie with the given movieID (e.g. '0133093'
for 'The Matrix', using 'http' or 'mobile').
Notice that movieID, using 'sql', are not the same IDs used on the web.

NOTES:
- this script is python2 on purpose because the imdb module is currently only available for python2 in ubuntu.
"""

import random
import sys

import imdb

if len(sys.argv) != 2:
    print('{0}: usage: {0} [moviedID]'.format(sys.argv[0]))
    print('{0}: example: {0} 0120591'.format(sys.argv[0]))
    sys.exit(1)

movieID = sys.argv[1]
i = imdb.IMDb()
out_encoding = sys.stdout.encoding or sys.getdefaultencoding()

try:
    # Get a Movie object with the data about the movie identified by
    # the given movieID.
    movie = i.get_movie(movieID)
except imdb.IMDbError as e:
    print('Probably youre not connected to Internet. Complete error report:')
    print(e)
    sys.exit(3)

print(movie.summary().encode(out_encoding, 'replace'))
print(movie.summary())

for k in movie.keys():
    print('=============== {0} ==============='.format(k))
    print(movie[k])

print('==== [{0}] movieID: [{1}] ===='.format(movie['title'], movieID))
imdbURL = i.get_imdbURL(movie)
if imdbURL:
    print('IMDb URL: [{0}]'.format(imdbURL))
genres = movie.get('genres')
if genres:
    print('Genres: %s' % ' '.join(genres))
cast = movie.get('cast')
if cast:
    print('Cast: ')
    cast = cast[:5]
    for name in cast:
        print('%s (%s)' % (name['name'], name.currentRole))
rating = movie.get('rating')
if rating:
    print('Rating: %s' % rating)
i.update(movie, info=['trivia'])
trivia = movie.get('trivia')
if trivia:
    rand_trivia = trivia[random.randrange(len(trivia))]
    print('Random trivia: %s' % rand_trivia)

info_runtime = movie.get('runtime')
print('Runtime is: {info_runtime}'.format(info_runtime=info_runtime))

info_directors = movie.get('director')
print(info_directors)
for n, d in enumerate(info_directors):
    print(dir(d))
    for k, v in d.items():
        print(k, v)
    print(d.personID)
    print('{n}, {d}'.format(n=n, d=d['name']))
