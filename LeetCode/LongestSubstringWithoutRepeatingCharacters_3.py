class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        start = end = 0

        while end < len(s):
            if s[end] in s[start : end]:
                max_length = max((end - start), max_length)
                start += s[start : end].index(s[end]) + 1
            end += 1

        return max((end - start), max_length)
