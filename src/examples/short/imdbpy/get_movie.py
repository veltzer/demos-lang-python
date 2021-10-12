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
    print(f"{sys.argv[0]}: usage: {sys.argv[0]} [moviedID]")
    print(f"{sys.argv[0]}: example: {sys.argv[0]} 0120591")
    sys.exit(1)

movieID = sys.argv[1]
i = imdb.IMDb()
out_encoding = sys.stdout.encoding or sys.getdefaultencoding()

try:
    # Get a Movie object with the data about the movie identified by
    # the given movieID.
    movie = i.get_movie(movieID)
except imdb.IMDbError as e:
    print("Probably youre not connected to Internet. Complete error report: {e}")
    sys.exit(3)

print(movie.summary().encode(out_encoding, 'replace'))
print(movie.summary())

for k in movie.keys():
    print(f"=============== {k} ===============")
    print(movie[k])

print(f"==== [{movie['title']}] movieID: [{movieID}] ====")
imdbURL = i.get_imdbURL(movie)
if imdbURL:
    print(f"IMDb URL: [{imdbURL}]")
genres = movie.get('genres')
if genres:
    print(f"Genres: {' '.join(genres)}")
cast = movie.get('cast')
if cast:
    print('Cast: ')
    cast = cast[:5]
    for name in cast:
        print(f"{name['name']} ({name.currentRole})")
rating = movie.get('rating')
if rating:
    print(f"Rating: {rating}")
i.update(movie, info=['trivia'])
trivia = movie.get('trivia')
if trivia:
    rand_trivia = trivia[random.randrange(len(trivia))]
    print(f"Random trivia: {rand_trivia}")

info_runtime = movie.get('runtime')
print(f"Runtime is: {info_runtime}")

info_directors = movie.get('director')
print(info_directors)
for n, d in enumerate(info_directors):
    print(dir(d))
    for k, v in d.items():
        print(k, v)
    print(d.personID)
    print(f"{n}, {d['name']}")
