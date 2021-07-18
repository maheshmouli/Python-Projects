import random
import string

pwd_len = int(input('Enter the length of password: '))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols 

if pwd_len<8:
    print('Set the bar atleast as 8 character..')
else:
    temp = random.sample(all, pwd_len)
    password = "".join(temp)
    print(password)