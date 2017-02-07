# Problem name: Largest prime factor (problem 3)
# Problem url: https://projecteuler.net/problem=3
# Author: Thorvaldur Gautsson

def find_factors(n):
	factors = []
	i = 2
	while n > 1:
		if n % i == 0:
			factors.append(i)
			n = n/i
			i = 2
		else:
			i += 1
	return max(factors)

print(find_factors(600851475143))