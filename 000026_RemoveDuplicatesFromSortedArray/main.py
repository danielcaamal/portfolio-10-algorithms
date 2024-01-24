class Solution:
    def removeDuplicates(self, nums: [int]):
        read_cursor = write_cursor = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[write_cursor] = nums[read_cursor]
                write_cursor += 1
            
            read_cursor += 1

        return write_cursor


if __name__ == '__main__':
    solution = Solution()
    
    test1 = [1,1,2]
    test2 = [0,0,1,1,1,2,2,3,3,4]
    
    solution1 = solution.removeDuplicates(test1)
    print('Solution1:', solution1)
    solution2 = solution.removeDuplicates(test2)
    print('Solution2:', solution2)