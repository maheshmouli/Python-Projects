class roman_decimal:
    def roman_to_decimal(self,s):
        roman_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        
        for i in range(len(s)):
            if i > 0 and roman_val[s[i]] > roman_val[s[i-1]]:
                int_val += roman_val[s[i]] - 2 * roman_val[s[i - 1]]
            else:
                int_val += roman_val[s[i]]
        return int_val

if __name__=="__main__":
    #roman = print('Enter the Roman Number: ')
    print(roman_decimal().roman_to_decimal('MMMCMLXXXVI'))