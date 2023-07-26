function isPalindrome(x: number): boolean {
  let aux_x = x;
  let reversed_x = 0;

  while (aux_x > 0) {
    const last_digit = aux_x % 10;
    aux_x = aux_x / 10 >> 0;
    reversed_x = reversed_x * 10 + last_digit;
  }

  return reversed_x === x;
};

// function isPalindrome(x: number): boolean {
//   const xString = x.toString();
//   const xReversed = xString.split('').reverse().join('');
//   return xString === xReversed;
// };

console.time()
const result1 = isPalindrome(121)
const expected1 = true;
console.log({ result1, expected1 })

const result2 = isPalindrome(-121)
const expected2 = false;
console.log({ result2, expected2 })

const result3 = isPalindrome(10)
const expected3 = false;
console.log({ result3, expected3 })
console.timeEnd()