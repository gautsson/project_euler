function findLargestPalindrome() {
	var palindromes = [];
	var num1 = 999;
	var num2 = 999;

	while (num2 > 800) {
		var tmp = num1 * num2;
		if (isPalindrome(tmp)) {
			palindromes.push(tmp)
		}
		if (num1 < 800) {
			num1 = 999;
			num2 -= 1
		}
		else {
			num1 -= 1;
		}
	}
	return getMaxOfArray(palindromes);
}

function isPalindrome(number) {
	return number.toString() === reverse(number.toString())
}

function reverse(string) {
    return string.split("").reverse().join("")
}

function getMaxOfArray(numArray) {
	return Math.max.apply(null, numArray)
}

console.log(findLargestPalindrome())