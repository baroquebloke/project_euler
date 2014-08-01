// The prime factors of 13195 are 5, 7, 13, and 29.
// What is the largest prime factor of the number 600851475143
//
// Answer: 
// time: 

function primeFactors(n) {
  factors = [];
  d = 2;
  while (n > 1) {
    while (n % d === 0) {
      factors.push(d);
      n /= d;
    }
    d += 1;
    if (d * d > n) {
      if (n > 1) {
        factors.push(n);
        break
      }
    }
  }
  return factors
}

function main(n) {
  var pfs = primeFactors(n);
  var largestPrimeFactor = Math.max(pfs);
  return largestPrimeFactor;
}

console.log(main(600851475143))
