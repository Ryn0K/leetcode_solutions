
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen={}
        start = 0
        max_len = 0
        for i in range(len(s)):
            val = s[i]
            if val in seen:
                start = max(start,seen[val]+1)
            seen[val]= i 
            max_len = max(max_len,i - start + 1)          
        return max_len

if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
