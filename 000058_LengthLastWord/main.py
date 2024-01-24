class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])

if __name__ == '__main__':
    solution = Solution()
    
    solution1 = solution.lengthOfLastWord("Hello World")
    print('Solution1:', solution1)
    
    solution2 = solution.lengthOfLastWord("   fly me   to   the moon  ")
    print('Solution2:', solution2)
    
    solution3 = solution.lengthOfLastWord("luffy is still joyboy")
    print('Solution3:', solution3)
