# Problem name: Special Pythagorean triplet (problem 9)
# Problem url: https://projecteuler.net/problem=9
# Author: Thorvaldur Gautsson

# Question:
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math

def findTriplets(number):
	triplets = []
	for b in range(1, int(number/2)):
		for a in range(1, b):
			if pow(number, 2) - 2*number*math.sqrt(pow(a, 2) + pow(b, 2)) - 2*a*b == 0:
				c = int(math.sqrt(pow(a, 2) + pow(b, 2)))
				triplets.append((a,b,c))
	return triplets


def multiplyTriplets(triplet_list):
	return [triplet[0] * triplet[1] * triplet[2] for triplet in triplet_list]

triplets = findTriplets(1000)

print("The triplets are: " + str(triplets))
print("The multiplies are: " + str(multiplyTriplets(triplets)))