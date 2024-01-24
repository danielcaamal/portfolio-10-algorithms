class Solution:
  
    # def _swap(self, nums, index1, index2):
    #     nums[index1], nums[index2] = nums[index2], nums[index1]
  
    def removeElement(self, nums, val):
      
        if not nums:
            return 0

        write_cursor = 0
        
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[write_cursor] = nums[i]
                write_cursor += 1

        return write_cursor

if __name__ == '__main__':
    solution = Solution()
    
    test1 = [3,2,2,3]
    test2 = [0,1,2,2,3,0,4,2]
    
    solution1 = solution.removeElement(test1, 3)
    print('Solution1:', solution1)
    solution2 = solution.removeElement(test2, 2)
    print('Solution2:', solution2)