class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        if n < 10:
            return n
        str_n = str(n)
        digit_list = []
        for digit in str_n:
            digit_list.append(int(digit))
        
        length = len(digit_list)
        for i in range(length-1, 0, -1):
            if digit_list[i] < digit_list[i-1]:
                digit_list[i-1] -= 1
                digit_list[i:] = [9]*(length-i)
            else:
                pass
        return int("".join([str(d) for d in digit_list]))

