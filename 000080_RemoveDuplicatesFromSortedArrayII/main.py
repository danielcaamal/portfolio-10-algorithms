class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        write_cursor = 1
        count_repeated = 0
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                count_repeated += 1
            else:
                count_repeated = 0
                
            if count_repeated < 2:
                nums[write_cursor] = nums[i]
                write_cursor += 1

        return write_cursor


      


if __name__ == '__main__':
    solution = Solution()
    
    test1 = [1,1,1,2,2,3]
    test2 = [0,0,1,1,1,1,2,3,3]
    
    solution1 = solution.removeDuplicates(test1)
    print('Solution1:', solution1)
    solution2 = solution.removeDuplicates(test2)
    print('Solution2:', solution2)