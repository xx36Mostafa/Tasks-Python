# https://elzero.org/python-assignments-lesson-from-11-to-18/
# upper(): returns the string in uppercase
# lower(): returns the string in lowercase
# capitalize(): capitalizes the first letter of the string
# count(): returns the number of occurrences of a substring in the string
# find(): returns the index of the first occurrence of a substring in the string
# replace(): replaces a substring with another substring
# strip(): removes leading and trailing whitespace from the string
# split(): splits the string into a list of substrings based on a specified delimiter


# 01 
name = input('Enter Your Name: ')
age = int(input('Your Age: '))
count = input('Your Country: ')
print(f'''
"Hello '{name}', How You Doing \ """ Your Age Is "{age}"" + And Your Country Is: {age}
''')
# # ==> حطينا الـ ثري كوتيشن علشان نقدر نحطها ب الشكل اللي هوا عايزه 

# 02
print(f'''"Hello '{name}', How You Doing \ \n""" Your Age Is "{age}"" + \nAnd Your Country Is: {age}''')

# 03
name = 'Elzero'
print(name[1]) #Second Letter Is "l"
print(name[2]) # Third Letter Is "z"
print(name[-1]) # Last Letter Is "o"

# 04
print(name[1:4])# "lze"
print(name[0]+name[2]+name[4])#"Ezr"
print(name[-2]+name[2]+name[0])# "rzE"

# 05
# دي حليتها بـ replace وفي ميثود تاني مش فاكرها بصراحه
name = "#@#@Elzero#@#@"
name = name.replace('#@#@','')
print(name)

#06 
num = "9"
print(num.zfill(4))
num = "15"
print(num.zfill(4))
num = "130"
print(num.zfill(4))
num = "950"
print(num.zfill(4))
num = "1500"
print(num.zfill(4))

# 07
name1 = "Osama"
name2 = "Osama_Elzero"

name_1 = name1.rjust(20, "@")
name_ = name2.rjust(20, "@")
print(name_1)
print(name_)

# 08
name_one = "OSamA"
name_two = "osaMA"
print(name_one.swapcase()) # بتبدل لو هوا lower بيبقي upper وهكذا
print(name_two.swapcase()) 

# 09
msg = "I Love Python And Although Love Elzero Web School"

print(msg.count('Love'))

# 10
name = "Elzero"

print(name.index('z'))

# 11 
msg = "I <3 Python And Although <3 Elzero Web School"
msg = msg.replace('<3','love',1) # ==> 1 دي يعني بقوله غيرها مره واحدة او اول اندكس هيجي قدامك اللي هيتغير
print(msg)

# 12
name = "Osama"
age = 38
country = "Egypt"
print(f'My Name Is {name}, And My Age Is {age}, And My Country Is {country}')