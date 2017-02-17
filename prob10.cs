//Problem name: Summation of primes (problem 10)
//Problem url: https://projecteuler.net/problem=10
//Author: Thorvaldur Gautsson

//Question:
// The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
// Find the sum of all the primes below two million.

using System;
using System.Collections.Generic;
using System.Linq;

namespace ProjectEuler
{
    class Problem10
    {
        static void Main(string[] args)
        {
            Console.WriteLine(FindPrimes(2000000));
            Console.ReadKey();
        }

        private static long FindPrimes(long n)
        {
            var primes = new List<long>();
            for (var i = 2; i < n; i++) {
                if (IsPrime(i))
                {
                    primes.Add(i);
                }
            }
            return primes.Sum();
        }

        private static bool IsPrime(long number)
        {
            if (number == 2) return true;
            else if (number%2 == 0) return false;
            else
            {
                for (var i = 3; i <= Math.Sqrt(number); i++)
                {
                    if (number%i == 0) return false;
                }
                return true;
            }
        }
    }
}
