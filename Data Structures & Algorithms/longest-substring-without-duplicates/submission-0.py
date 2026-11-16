
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        longest = 0
        for right_side in range(len(s)):
            while s[right_side] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right_side])
            longest = max(longest, right_side - left + 1)
        return longest
        
        