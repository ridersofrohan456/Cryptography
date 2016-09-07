from __future__ import print_function

def crypto(encoded):
	for i in range(0,25):
		for c in encoded:
			# Takes each of the letters in the encrypted code, and shifts
			# by one. 
			temp = ord(c)+i
			if (temp > 90):
				temp = temp - 26
			print(chr(temp),end="") # It prints each of the letters
		print("") # Just prints a new line

# This code prints 26 lines, each with letters shifted one from before. I go through 
# the 26 lines and find the one that makes the most sense

crypto("ZETIVUZSCPDZCZKRIPLJRXVFWKYVTRVJRITZGYVITFEKZELVUZEKFKYVKNVEKZVEKYTVEKLIP")

