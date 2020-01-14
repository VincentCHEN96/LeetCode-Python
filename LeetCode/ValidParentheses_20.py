class Solution:
    stack = ""  # 模拟一个栈
    index = -1  # 模拟栈顶指针指向当前栈顶元素

    def isValid(self, s: str) -> bool:
        for i in range(0, len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                self.stack += s[i]  # 入栈
                self.index += 1 # 栈顶指针+1
            elif s[i] == ')' and not self.isMatch('('):
                return False
            elif s[i] == ']' and not self.isMatch('['):
                return False
            elif s[i] == '}' and not self.isMatch('{'):
                return False
        # 遍历完成后栈空则成功，栈非空则失败
        if self.index < 0:
            return True
        else:
            return False

    def isMatch(self, bracket: str) -> bool:
        if self.index >= 0 and self.stack[self.index] == bracket:
            self.stack = self.stack[:-1]    # 出栈
            self.index -= 1 # 栈顶指针-1
            return True
        else:
            return False
