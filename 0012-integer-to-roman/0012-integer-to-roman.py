class Solution:
    def intToRoman(self, num: int) -> str:
        # Map of integer values to their corresponding Roman numerals
        value_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        
        # Initialize an empty result string
        roman = []
        
        # Iterate over the value_map, checking each value-symbol pair
        for value, symbol in value_map:
            # While the current num is greater than or equal to the value, append the symbol
            while num >= value:
                roman.append(symbol)
                num -= value
        
        # Join the list into a final string and return it
        return ''.join(roman)
