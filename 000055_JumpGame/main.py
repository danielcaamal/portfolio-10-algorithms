class Solution:
    # def canJump(self, nums: int) -> bool:
    #     cur = nums[0]
    #     for i in range(cur, len(nums)):
    #         i += nums[i]
    #         if i > len(nums) - 1:
    #             break
    #     if cur >= len(nums) - 1:
    #         return True
    #     return False
    
    # def r_canJump(self, current, nums):
    #     if current >= len(nums) - 1:
    #         return True
    #     for i in range(nums[current]):
    #         if self.r_canJump(current + i + 1, nums):
    #             return True
    #     return False
    
    # def canJump2(self, nums: int) -> bool:
    #     return self.r_canJump(0, nums)
      
    #     def jump(self, nums: List[int]) -> int:
    #     current_max_reach = 0
    #     next_max_reach = 0
    #     jump_count = 0

    #     for i in range(len(nums) - 1):
    #         next_max_reach = max(next_max_reach, i + nums[i])

    #         if i == current_max_reach:
    #             jump_count += 1
    #             current_max_reach = next_max_reach
        
    #     return jump_count
      
    
    def canJump(self, nums: int) -> bool:
        curr = nums[0]
        for i in range(1, len(nums)):
            if curr == 0:
                return False
            curr -= 1
            print(curr, nums[i])
            curr = max(curr, nums[i])
        return True
  

if __name__ == '__main__':
    solution = Solution()
    
    # solution1 = solution.canJump2([2,3,1,0,0,5])
    # print('Solution1:', solution1)
    
    # solution2 = solution.canJump2([3,2,1,0,4])
    # print('Solution2:', solution2)

    # solution3 = solution.canJump2([2,0,0])
    # print('Solution3:', solution3)
    
    solution4 = solution.canJump2([0])
    print('Solution4:', solution4)
    
    solution5 = solution.canJump2([2,2,0,1,1])
    print('Solution5:', solution5)
    
