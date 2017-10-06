# This is homework 2.

import re
import random
import math
from Crypto.Cipher import AES
import requests


def change(cents):
    if cents < 0:
        raise ValueError('amount cannot be negative')
    coins_list = []
    remaining = cents

    def find_coin_number(coin_value, remaining):
        coins_list.append(math.floor(remaining/coin_value))
        return remaining % coin_value
    for value in [25, 10, 5, 1]:
        remaining = find_coin_number(value, remaining)
    return tuple(coins_list)


def strip_quotes(str):
    return re.sub("\"|\'", "", str)


def scramble(words):
    permuted_words = random.sample(words, len(words))
    new_words = ''.join(permuted_words)
    return new_words


def powers(base, max1):
    if (max1 == 0):
        raise StopIteration
    number = 0
    exponent = 0
    while number <= max1:
        yield base ** exponent
        exponent += 1
        number = base ** exponent


def triples(upper_value):
    result = []
    for a in range(1, upper_value+1):
        for b in range(1, upper_value+1):
            for c in range(1, upper_value+1):
                if a ** 2 + b ** 2 == c ** 2 and a < b and b < c:
                    result.append((a, b, c))
    return result


def say(word=None):
    if word is None:
        return ""

    def phrase(new_word=None):
        if new_word is None:
            return word
        return say(word + " " + new_word)
    return phrase


def interleave(first, *second):
    max_num = max(len(first), len(second))
    result = []
    for x in range(0, max_num):
        if (x < len(first)):
            result.append(first[x])
        if (x < len(second)):
            result.append(second[x])
    return result


class Cylinder:
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    @property
    def volume(self):
        return math.pi * (self.radius ** 2) * self.height

    @property
    def surface_area(self):
        return 2 * math.pi * ((self.radius * self.height) + (self.radius ** 2))

    def widen(self, factor):
        self.radius *= factor
        return self

    def stretch(self, factor):
        self.height *= factor
        return self


def make_crypto_functions(key, initialization_vector):
    local_key = key
    local_initialization_vector = initialization_vector

    def encrypt(text):
        cipher = AES.new(local_key, AES.MODE_CBC, local_initialization_vector)
        return cipher.encrypt(text)

    def decrypt(text):
        cipher = AES.new(local_key, AES.MODE_CBC, local_initialization_vector)
        return cipher.decrypt(text)

    return (encrypt, decrypt)


def random_name(gender, region):
    response = requests.get('https://uinames.com/api/',
                            params={'gender': gender,
                                    'region': region,
                                    'amount': 1})
    if 'error' in response.json():
        raise ValueError(response.text)
    return '{}, {}'.format(response.json()['surname'], response.json()['name'])
