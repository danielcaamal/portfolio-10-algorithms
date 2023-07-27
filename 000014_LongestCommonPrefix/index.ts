// function longestCommonPrefix(strs: string[]): string {
//   let longestPrefix = strs[0]
//   for (let i = 1; i < strs.length; i++) {
//     for (let j = longestPrefix.length; j >= 0; j--) {
//       if (longestPrefix.slice(0, j) === strs[i].slice(0, j)) {
//         longestPrefix = longestPrefix.slice(0, j)
//         break;
//       }
//     }
//   }
//   return longestPrefix;
// };

function longestCommonPrefix(strs: string[]): string {
    if (!strs.length) return "";

    strs.sort();
    let first = strs[0], last = strs[strs.length - 1];
    let i = 0;

    while (i < first.length && i < last.length && first[i] === last[i]) i++;

    return first.substring(0, i);
}


console.time()
const result1 = longestCommonPrefix(["flower","flow","flight"])
const expected1 = "fl";
console.log({ result1, expected1 })

const result2 = longestCommonPrefix(["dog","racecar","car"])
const expected2 = "";
console.log({ result2, expected2 })
console.timeEnd()

const result3 = longestCommonPrefix(["flower"])
const expected3 = "flower";
console.log({ result3, expected3 })
