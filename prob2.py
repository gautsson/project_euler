# Problem name: Even Fibonacci numbers (problem 2)
# Problem url: https://projecteuler.net/problem=2
# Author: Thorvaldur Gautsson

def fibs(n):
	sum = 0
	num1 = 1
	num2 = 2
	while num2 < n:
		if num2 % 2 == 0:
			sum += num2
		tmp = num1 + num2
		num1 = num2
		num2 = tmp
	return(sum)

print(fibs(4000000))