def convert():
    f = float(input('Enter the temperature in Fahrenheit: '))
    c = (f - 32) * 5/9
    print('Temperature in Celsius is: ', round(c))

if __name__=="__main__":
    convert()