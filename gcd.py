from fractions import gcd
def calculateGCD(y):
	for x in range(0, y):
		if (gcd(x, y)==1):
			print(x)


calculateGCD(29)
