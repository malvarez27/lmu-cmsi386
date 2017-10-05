# This is homework 2.
import random
from Crypto.Cipher import AES


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

    def encrypt(text):
		cipher = AES.new(local_key, AES.MODE_CBC, local_initialization_vector)
		return cipher.encrypt(text)

	def decrypt(text):
		cipher = AES.new(local_key, AES.MODE_CBC, local_initialization_vector)
		return cipher.decrypt(text)


	return (encrypt, decrypt)

"""  5 triples."""
def triples():
   for c in range(1, 100):
     for b in range(1, c):
       for a in range(1, b):
         if a * a + b * b == c * c:
           print('({},{},{})'.format(a, b, c))


def scramble(words):
	permuted_words = random.sample(words, len(words))
	new_words = ''.join(permuted_words)
	return new_words

# print(scramble(""))

def powers(power):
	num = 0
	while num < power:
		yield num
		num += 1


def interleave(first, *second):
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


def Cylinder():
	print("hi")


def random_name():
	print("hi")




# if __name__ == "__main__":
# 	e, d = make_crypto_functions('zombie devops feynman123', '0000000000000000')
# 	print(e)
# 	print(d)
