user_input = str(input('Enter the Phrase: '))
txt = user_input.split()
#print(txt)
a = ' '
for i in txt:
    a = a + str(i[0]).upper()
print(a)