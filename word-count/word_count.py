import re

from collections import Counter


WORDS = re.compile("[a-z0-9]+(['][a-z]+)?")


def count_words(sentence):
    return Counter(word.group(0) for word in WORDS.finditer(sentence.lower()))
