class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = len(s)
        window = set()
        ans, i, j = 0, 0, 0
        
        while i < chars and j < chars:
            if s[j] not in window:
                window.add(s[j])
                j += 1
                ans = max(ans, j-i)
            else:
                window.remove(s[i])
                i += 1
        
        return ans