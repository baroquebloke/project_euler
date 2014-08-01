//A palindromic number reads the same both ways. The largest palindrome made 
//from the product of two 2-digit numbers is 9009 = 91 × 99.
//Find the largest palindrome made from the product of two 3-digit numbers.
//
//answer: 906609
//time: 0.345s
//  

function reverse(s) {
  return s.split('').reverse().join('');
}

function palind_num() {
  var is_pal = 0
  for (var x = 999; x > 99; x--) {
    for (var y = x; y > 99; y--) {
      var num = x * y;
      if (num.toString() === reverse(num.toString())) {
        if (is_pal < num) {
          is_pal = num;
        }
      }
    }
  }
  return is_pal
}

console.log(palind_num())
