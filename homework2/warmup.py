# This is homework 2.
import random
from Crypto.Cipher import AES
import math


def change(cents):
    if cents < 0:
        raise ValueError('amount cannot be negative')
    coins_list = []
    remaining = cents

    def find_coin_number(coin_value):
        coins_list.append(math.floor(remaining/coin_value))
	    remaining %= coin_value

    for value in [25, 10, 5, 1]:
        find_coin_number(value)


def make_crypto_functions(key, initialization_vector):
    local_key = key
    local_initialization_vector = initialization_vector
<<<<<<< HEAD
    def encrypt(text):
        cipher = AES.new(local_key, AES.MODE_CBC, local_initialization_vector)
        return cipher.encrypt(text)
    def decrypt(text):
        cipher = AES.new(local_key, AES.MODE_CBC, local_initialization_vector)
        return cipher.decrypt(text)
        

    return (encrypt, decrypt)
=======

    def encrypt(text):
		cipher = AES.new(local_key, AES.MODE_CBC, local_initialization_vector)
		return cipher.encrypt(text)

	def decrypt(text):
		cipher = AES.new(local_key, AES.MODE_CBC, local_initialization_vector)
		return cipher.decrypt(text)


	return (encrypt, decrypt)
>>>>>>> 674a6eabd4649172f263de5f2af724a590d39a87

"""  5 triples."""
def triples(upper_value):
    result = []
    for a in range(1, upper_value+ 1):
        for b in range(1, upper_value+ 1):
            for c in range(1, upper_value+ 1):
                if a**2 + b**2 == c**2 and a < b  and b < c: 
                    result.append((a, b, c))
    return result


def scramble(words):
    permuted_words = random.sample(words, len(words))
    new_words = ''.join(permuted_words)
    return new_words

# print(scramble(""))

def powers(base, max1):
    if (max1 == 0):
        return 0
    number = 0
    exponent = 0
    while number <= max1:
        yield base ** exponent
        exponent += 1
        number = base ** exponent

def interleave(first, *second):
<<<<<<< HEAD
    one_length = len(first)
    two_length = len(second)
    max_num = max(len(first), len(second))
    result = []
    for x in range(0, max_num):
        if (x < len(first)):
            result.append(first[x])
        if (x < len(second)):
            result.append(second[x])
    return result


def change(cents):
    if cents < 0:
        raise ValueError('amount cannot be negative')
    coins_list = []
    remaining = cents
    def find_coin_number(coin_value):
        coins_list.append(math.floor(remaining/coin_value))
        remaining = remaining % coin_value
    for value in [25, 10, 5, 1]:
        find_coin_number(value)
    return tuple(coins_list)


def strip_quotes(str):
    return re.sub("\"|\'", "", str)

def say(word):
    if word == None:
        return ""
    def phrase(new_word):
        if new_word == None:
            return word
        return say( word + " " + other)
    return phrase(new_word)

=======
	one_length = len(first)
	two_length = len(second)
	max_num = math.max(len(first), len(second))
	result = []
	for x in range(0, max_num):
		if (x < len(first)):
			result.append(first[x])
		if (x < len(second)):
			result.append(second[x])
	return result


def strip_quotes():
	print("hi")


def say():
	print ("hi")
>>>>>>> 674a6eabd4649172f263de5f2af724a590d39a87


def Cylinder():
    print("hi")


def random_name():
    print("hi")




# if __name__ == "__main__":
#   e, d = make_crypto_functions('zombie devops feynman123', '0000000000000000')
#   print(e)
#   print(d)
