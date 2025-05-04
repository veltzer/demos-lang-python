"""
simple example of itertools.groupby
"""


from itertools import groupby

# Sample data - a list of words
words = ["ant", "cat", "banana", "bat", "car", "apple"]

# Group words by their first letter
grouped_words = {}
for key, group in groupby(sorted(words), key=lambda x: x[0]):
    grouped_words[key] = list(group)

# Print the results
for letter, words_list in grouped_words.items():
    print(f"Words starting with '{letter}': {words_list}")
