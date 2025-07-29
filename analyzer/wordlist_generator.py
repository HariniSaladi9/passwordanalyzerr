def generate_variants(word):
    return [
        word,
        word + "123",
        word.replace('a', '@').replace('e', '3') + "2025"
    ]

def generate_wordlist(inputs):
    wordlist = []
    for item in inputs:
        wordlist += generate_variants(item)
    return set(wordlist)

import os

def save_wordlist(words, filename="wordlists/custom_wordlist.txt"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)  # ensures folder exists
    with open(filename, "w") as f:
        for word in words:
            f.write(word + "\n")
