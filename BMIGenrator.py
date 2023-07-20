hight = float(input('enter your hight in m: \n'))
weight = float(input('enter your weight in kg: \n'))

bmi = round(weight/hight ** 2)
print(f'your BMI is {bmi}')

if bmi < 18.5:
    print('Great you are underweight')
elif bmi > 18.5 and bmi < 120:
    print('Great you are Normal weight')
