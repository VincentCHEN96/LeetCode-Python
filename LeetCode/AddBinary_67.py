class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = [] # 结果串列表
        i = len(a) - 1  # a的尾指针
        j = len(b) - 1  # b的尾指针
        carry = 0   # 进位数

        while i >= 0 or j >= 0:
            operand_1 = operand_2 = 0
            if i >= 0:
                operand_1 = int(a[i])
            if j >= 0:
                operand_2 = int(b[j])
            bit_sum = operand_1 + operand_2 + carry
            carry = int(bit_sum / 2)
            result.insert(0, str(bit_sum % 2))
            i -= 1
            j -= 1
        # 最后的进位数非0则加到最前面
        if carry == 1:
            result.insert(0, '1')

        return "".join(result)
