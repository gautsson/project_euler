// Problem name: 10001st prime (problem 7)
// Problem url: https://projecteuler.net/problem=7
// Author: Thorvaldur Gautsson

// Question: 
// By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
// What is the 10 001st prime number?

function findPrimes(n) {
    var primes = [];
    var primesLength = 0;
    var candidate = 2;
    while (primesLength < n) {
        if (isPrime(candidate)) {
            primes.push(candidate);
            primesLength += 1
        }
        candidate += 1;
    }
    return primes[n-1];
}

function isPrime(candidate) {
    if (candidate === 2) return true;
    if (candidate % 2 == 0) return false;
    for (var i = 2; i <= Math.sqrt(candidate); i++) {
        if (candidate % i === 0) {
            return false
        }
    }
    return true;
}

console.log(findPrimes(10001));
