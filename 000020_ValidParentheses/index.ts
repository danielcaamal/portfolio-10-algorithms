function isValid(s: string): boolean {
  const map = new Map([
    ['(', ')'],
    ['[', ']'],
    ['{', '}'],
  ])

  const stack: string[] = [];

  for (let i = 0; i <= s.length - 1; i++) {
    const current = map.get(s[i])
    if (current) {
      stack.push(current);
    }
    else if (stack.pop() !== s[i]) {
      return false;
    }
  }
  return stack.length === 0;
}

console.time()
const result1 = isValid("()");
const expected1 = true;
console.log({ result1, expected1 })

const result2 = isValid("()[]{}");
const expected2 = true;
console.log({ result2, expected2 })

const result3 = isValid("(]");
const expected3 = false;
console.log({ result3, expected3 })
console.timeEnd()