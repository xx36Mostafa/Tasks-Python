# https://elzero.org/python-assignments-lesson-from-38-to-40/
# upper(): returns the string in uppercase
# lower(): returns the string in lowercase
# capitalize(): capitalizes the first letter of the string
# count(): returns the number of occurrences of a substring in the string
# find(): returns the index of the first occurrence of a substring in the string
# replace(): replaces a substring with another substring
# strip(): removes leading and trailing whitespace from the string
# split(): splits the string into a list of substrings based on a specified delimiter

# 01 
name = input('دخل اسمك ياعم: ').strip().capitalize()
print(f"Hello {name}, Happy To See You Here.")

# 02
age = int(input('Your Age: '))
if age < 16:
    print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")
elif age > 16:
    print(f"Hello Your Age Is {age}, All Articles Is Suitable For You")

# 03
first_name = input().strip()
third_name = input().strip()
print(f'Hello {first_name} {third_name}')

# 04
email = input('enter your email: ').strip()
# email = Osama@Nn.Sa
name = email.split('@')
# name[0] == > Osama
# name[1] ===> Nn.Sa
email_ser = name[1].lower().split('.')
# email_ser[0] ==> nn because method lower()
# email_ser[1] ==> ss
print(f'Your Name Is {name[0]}')
print(f'Email Service Provider Is {email_ser[0]}')
print(f'Top Level Domain Is {email_ser[1]}')
