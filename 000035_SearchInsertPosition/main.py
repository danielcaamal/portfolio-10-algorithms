class Solution:
    def searchInsert2(self, nums, target) -> int:
        for index, num in enumerate(nums):
            if num >= target:
                return index
        return len(nums)

    def searchInsert(self, nums, target) -> int:
        l, r = 0, len(nums)
        
        while l < r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            else:
                r = m
        return l

if __name__ == '__main__':
    solution = Solution()
    
    solution1 = solution.searchInsert([1,3,5,6], 5)
    print('Solution1:', solution1)
    
    solution2 = solution.searchInsert([1,3,5,6], 2)
    print('Solution2:', solution2)
    
    solution3 = solution.searchInsert([1,3,5,6], 7)
    print('Solution3:', solution3)
