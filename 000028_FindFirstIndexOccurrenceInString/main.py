class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if i + len(needle) > len(haystack):
                    return -1
                current = 0
                for j in range(len(needle)):
                    if haystack[i + j] != needle[j]:
                        break
                    current = j
                if current == len(needle) - 1:
                    return i
        return -1





if __name__ == '__main__':
    solution = Solution()
    
    solution1 = solution.strStr("sadbutsad", "sad")
    print('Solution1:', solution1)
    
    solution2 = solution.strStr("leetcode", "leeto")
    print('Solution2:', solution2)