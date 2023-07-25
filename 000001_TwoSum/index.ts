function twoSum(nums: number[], target: number): number[] {
    const hashMap: { [key: string]: number } = {};

    for (let i = 0; i <= nums.length; i++) {
        const diff = target - nums[i];
        console.log(Object.keys(hashMap))
        if ((Object.keys(hashMap)).includes(String(diff))) {
            return [ hashMap[diff], i ];
        } else {
            hashMap[nums[i]] = i;
        }
    }
    throw new Error('No two sum solution');
};

function twoSum2(nums: number[], target: number): number[] {
    const numberMap = new Map();

    for (let i = 0; i <= nums.length; i++) {
        const number = nums[i];
        const diff = target - number;

        if (numberMap.has(diff)) return [numberMap.get(diff), i];

        numberMap.set(number, i);
    }
    throw new Error('No two sum solution');
};


console.time()
const result1 = twoSum2([2,7,11,15],9);
const expected1 = [0,1];
console.log({ result1, expected1 })

const result2 = twoSum2([3,2,4],6);
const expected2 = [1,2];
console.log({ result2, expected2 })

const result3 = twoSum2([3,3],6);
const expected3 = [0,1];
console.log({ result3, expected3 })
console.timeEnd()