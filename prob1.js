// Problem name: Multiples of 3 and 5 (problem 1)
// Problem url: https://projecteuler.net/problem=1
// Author: Thorvaldur Gautsson

function multiplierSum(n) {
	var sum = 0;
	for (var i = 0; i < n; i++) {
		if (i % 3 == 0 || i % 5 == 0)
			sum += i
	}
	return sum
}

console.log(multiplierSum(1000))