# Problem name: Sum square difference (problem 6)
# Problem url: https://projecteuler.net/problem=6
# Author: Thorvaldur Gautsson

def sum_of_squares(n):
	sum = 0
	for i in range(1, n+1):
		sum += pow(i, 2)
	return sum

def square_of_sum(n):
	sum = 0
	for i in range(1, n+1):
		sum += i
	return pow(sum, 2)

answer = square_of_sum(100) - sum_of_squares(100)
print(answer)