// this will find the sum of all even numbers in the fibonacci sequence whose 
// values do not exceed 4,000,000
//
//answer: 4613732
//time: 0.090s

function main() {
  var x = 1
  var y = 1
  var z = 0
  var total = 0
  while (y <= 4000000) {
    z = y
    y += x
    if (y % 2 == 0) {
      total += y;
    }
    x = z
  }
  return total
}
console.log(main())
