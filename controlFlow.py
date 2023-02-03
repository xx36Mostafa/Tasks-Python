# https://elzero.org/python-assignments-lesson-from-41-to-46/
# اربع حاجات مفروض تكون عارفهم انما الباقي انت عارفه :D 
# == بتقارن حاجتين ببعض 
# != بتشوف هل الحاجة دي لا تساوي الحاجه التانية
# % بيرجعلك باقي القسمه
# in علشان نشوف هل الحاجة دي موجوده فـ الليست او الاسترينج او كدا ولا لا 

# 01
num1,num2 = int(input('Enter first Number: ')),int(input('Enter secod Number: '))
operation = input('Choose "+" Or "-" Or "*" Or "/" ')
if operation == '+':
    res = num1 + num2
    print(res)
elif operation == '-':
    res = num1 - num2
    print(res)
elif operation == '*':
    res = num1 * num2
    print(res)
elif operation == '/':
    res = num1 / num2
    print(res)

# 02
age = int(input('Enter age: '))
if age > 6:
    print('App Is Suitable For You')
elif age < 16:
    print('App Is Not Suitable For You')

# 03
age = int(input('Enter age: '))
if age > 10 and age < 100:
    print(f'Your age in months is {age*12}')
    print(f'Your age in weeks  is {age*52}')
    print(f'Your age in days  is {age*365}')
    print(f'Your age in hours  is {age*365*24}')
    print(f'Your age in minutes is {age*365*24*60}')
    print(f'Your age in seconds is {age*365*24*60*60}')
else:
    print('Age is out of range')

# 04
country = input("Input Your Country: ").capitalize()
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30

if country in countries:
    print(f'Your Country Eligible For Discount And The Price After Discount Is {price-discount}$')
else:
    print('Your Country Not Eligible For Discount And The Price Is $100')