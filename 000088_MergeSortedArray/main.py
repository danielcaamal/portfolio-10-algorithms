class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        write_cursor = len(nums1) - 1
        while m > 0 and n > 0:
            print("m:", m)
            print("n:", n)
            if nums1[m - 1] > nums2[n - 1]:
                nums1[write_cursor] = nums1[m-1]
                m -= 1
            else:
                nums1[write_cursor] = nums2[n-1]
                n -= 1
            write_cursor -= 1
        
        while m > 0:
            nums1[write_cursor] = nums1[m-1]
            m -= 1
            write_cursor -= 1
        
        while n > 0:
            nums1[write_cursor] = nums2[n-1]
            n -= 1
            write_cursor -= 1



if __name__ == '__main__':
    solution = Solution()
    
    solution1 = [1,2,3,0,0,0]
    solution.merge(solution1,3,[2,5,6],3)
    print('Solution1:', solution1)
    
    solution2 = [1]
    solution.merge(solution2,1,[],0)
    print('Solution2:', solution2)
    
    solution3 = [0]
    solution.merge(solution3,0,[1],1)
    print('Solution3:', solution3)


