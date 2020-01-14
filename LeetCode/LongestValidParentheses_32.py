class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [] # dp[i]表示以s[i]结尾的最长有效括号的长度
        dp.append(0)

        for i in range(1, len(s)):
            if s[i] == '(': # "...("
                dp.append(0)
            elif s[i - 1] == '(':   # "...()"
                dp.append((dp[i - 2] if i - 2 >= 0 else 0) + 2)
            elif (i - dp[i - 1] - 1) >= 0 and s[i - dp[i - 1] - 1] == '(':   # "...(...))"
                dp.append(dp[i - 1] + 2 + (dp[i - 2 - dp[i - 1]] if (i - 2 - dp[i - 1]) >= 0 else 0))
            else:   # "...)...))"
                dp.append(0)

        return max(dp)
