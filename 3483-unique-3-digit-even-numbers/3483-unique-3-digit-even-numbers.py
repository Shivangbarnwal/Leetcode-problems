from itertools import permutations
class Solution(object):
    def totalNumbers(self, digits):
        even_digits = [d for d in digits if d % 2 == 0]
        count = 0
        unique_numbers = set()
        
        for last in even_digits:
            remaining_digits = list(digits)
            remaining_digits.remove(last)
            
            for p in permutations(remaining_digits, 2):
                if p[0] != 0:
                    number = p[0] * 100 + p[1] * 10 + last
                    unique_numbers.add(number)
        
        return len(unique_numbers)
        