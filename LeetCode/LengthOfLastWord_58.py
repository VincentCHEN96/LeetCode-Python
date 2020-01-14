class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        length = 0
        index = len(s) - 1
        while index >= 0 and s[index] == ' ':
            index -= 1
        while index >= 0:
            if s[index] != ' ':
                length += 1
                index -= 1
            else:
                break
        return length
