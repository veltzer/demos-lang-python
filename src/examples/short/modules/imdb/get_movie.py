"""
get_movie.py

Convert this script to imdbpy https://imdbpy.github.io/downloads/

Usage: get_movie "movie_id"

Show some info about the movie with the given movie_id (e.g. "0133093"
for "The Matrix", using "http" or "mobile").
Notice that movie_id, using "sql", are not the same IDs used on the web.

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

movie_id = sys.argv[1]
i = imdb.IMDb()
out_encoding = sys.stdout.encoding or sys.getdefaultencoding()

try:
    # Get a Movie object with the data about the movie identified by
    # the given movie_id.
    movie = i.get_movie(movie_id)
except imdb.IMDbError as e:
    print(f"Probably youre not connected to Internet. Complete error report: {e}")
    sys.exit(3)

print(movie.summary().encode(out_encoding, "replace"))
print(movie.summary())

for k, v in movie.items():
    print(f"=============== {k} ===============")
    print(v)

title = movie["title"]
print(f"==== [{title}] movie_id: [{movie_id}] ====")
imdb_url = i.get_imdbURL(movie)
if imdb_url:
    print(f"IMDb URL: [{imdb_url}]")
genres = movie.get("genres")
if genres:
    print(f"Genres: {genres}")
cast = movie.get("cast")
if cast:
    print("Cast: ")
    cast = cast[:5]
    for person in cast:
        name = person["name"]
        print(f"{name} ({name.currentRole})")
rating = movie.get("rating")
if rating:
    print(f"Rating: {rating}")
i.update(movie, info=["trivia"])
trivia = movie.get("trivia")
if trivia:
    rand_trivia = trivia[random.randrange(len(trivia))]
    print(f"Random trivia: {rand_trivia}")

info_runtime = movie.get("runtime")
print(f"Runtime is: {info_runtime}")

info_directors = movie.get("director")
print(info_directors)
for n, d in enumerate(info_directors):
    print(dir(d))
    for k, v in d.items():
        print(k, v)
    print(d.personID)
    name = d["name"]
    print(f"{n}, {name}")
