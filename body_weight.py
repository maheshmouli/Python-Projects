
def feet_cm():
    print('Input your height:')
    h_ft = int(input('Feet: '))
    h_inch = int(input('Inches: '))

    h_inch += h_ft * 12
    h_cm = round(h_inch * 2.54, 1)

    return h_cm

def BMI_cal():
    height = float(feet_cm())
    weight = float(input('Enter your weight in kgs: '))
    height = height/100
    BMI = weight/(height * height)
    print('Your body mass is: ', BMI)
    if (BMI>0):
        if(BMI<18):
            print('You are under weight')
        elif(BMI>18 or BMI<=24):
            print('You are normal weight')
        elif(BMI>24 or BMI<=30):
            print('You are over weight')
        else:
            print('You are Obese. You need to start working on your weight')
    else:
        print('Please enter valid details...')

if __name__=="__main__":
    BMI_cal()
