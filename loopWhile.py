# https://elzero.org/python-assignments-lesson-from-47-to-50/
# 01
num = int(input())
x = 0
if num > 0:
    while num > 0 :
        num -= 1
        if num != 6 and num != 0:
            print(num)
            x += 1
    print(f'{x} Numbers Printed Successfully.')
else:
    print('The number is less than zero')

# 02
friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
y = 0
count = 0 
while y < len(friends):
    if friends[y][0].isupper():
        print(friends[y])
    else:
        count += 1    
    y += 1
print(f'Friends Printed And Ignored Names Count Is {count}')

# 03
skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]

while skills:
    print("\n".join(skills));break
# 04

my_friends = []
count = 4 
while count > 0:
    friend = input('Enter Name Of Friend: ')
    if friend.isupper():
        print("Invalid Name")
    elif friend.islower():
        friends.append(friend[0].capitalize())
        count -= 1 
        print(f'"Friend {friend} Added => 1st Letter Become Capital"')
        print(f'"Names Left in List Is {count}"')
    elif friend[0].isupper():
        count -= 1 
        print(f'"Friend {friend} Added => 1st Letter Become Capital"')
        print(f'"Names Left in List Is {count}"')
