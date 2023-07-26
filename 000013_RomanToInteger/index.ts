function romanToInt(s: string): number {
  const symbols = new Map([
    ["I", 1],
    ["V", 5],
    ["X", 10],
    ["L", 50],
    ["C", 100],
    ["D", 500],
    ["M", 1000,]
  ]);

  return s
    .replace('IV', 'IIII')
    .replace('IX', 'VIIII')
    .replace('XL', 'XXXX')
    .replace('XC', 'LXXXX')
    .replace('CD', 'CCCC')
    .replace('CM', 'DCCCC')
    .split('')
    .reduce((acc, current) => acc += symbols.get(current)!, 0);
};


console.time()
const result1 = romanToInt("III")
const expected1 = 3;
console.log({ result1, expected1 })

const result2 = romanToInt("LVIII")
const expected2 = 58;
console.log({ result2, expected2 })

const result3 = romanToInt("MCMXCIV")
const expected3 = 1994;
console.log({ result3, expected3 })
console.timeEnd()