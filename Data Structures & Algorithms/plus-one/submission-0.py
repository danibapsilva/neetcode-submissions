class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        digits[-1] += 1
        for i in range(len(digits) - 1, -1, -1):
            digit_val = digits[i] + carry
            carry = digit_val // 10
            remaining = digit_val % 10
            digits[i] = remaining
        
        if carry:
            return [carry] + digits
        return digits