class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        tail = length - 1
        round = 1

        while tail >= 0:
            front = 0
            while front <= tail and tail < length:
                temp_str = s[front : (tail + 1)]
                if self.isPalindorme(temp_str):
                    return temp_str
                else:
                    front += 1
                    tail += 1
            round += 1
            tail = length - round
        return ""

    def isPalindorme(self, s : str) -> bool:
        front = 0
        tail = len(s) - 1

        while front < tail:
            if s[front] != s[tail]:
                return False
            front += 1
            tail -= 1
        return True
