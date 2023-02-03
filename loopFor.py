# https://elzero.org/python-assignments-lesson-from-51-to-55/

# 01
my_nums = [15, 81, 5, 17, 20, 21, 13]
y = 0
for i in my_nums:
    if i % 5 == 0:
        y += 1
        print(f'{y} ==> {i}')
print("All Numbers Printed")

# 02
for i in range(1,21):
    if i < 10:
        print(f'0{i}')
    else:
        print(i)
print("All Numbers Printed")

# 03
my_ranks = {
  'Math': 'A',
  "Science": 'B',
  'Drawing': 'A',
  'Sports': 'C'}
total = 0
for i in my_ranks:
    if my_ranks[i] == 'A':
        print(f'My Rank in {i} Is A And This Equal 100 Points')
        total += 100
    elif my_ranks[i] == 'B':
        print(f'My Rank in {i} Is B And This Equal 80 Points')
        total += 80
    elif my_ranks[i] == 'C':
        print(f'My Rank in {i} Is C And This Equal 40 Points')
        total += 40
print(f'Total Points Is {total}')

# 04
students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": { 
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}
for name in students: 
    print(f'''
"------------------------------"
"-- Student Name => {name}"
"------------------------------"
''')
    for subjects in students[name]:
        x = 0
        if students[name][subjects]== 'A':
            x = 100
        elif students[name][subjects]=='B':
            x = 80
        elif students[name][subjects]== 'C':
            x = 40
        elif students[name][subjects]== 'D':
            x = 20
        print('- '+subjects+'=>',x)