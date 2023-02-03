# https://elzero.org/python-assignments-lesson-from-90-to-94/
# 01 
NUM = input("Add Your Number ")
if len(NUM) != 1:
    raise IndexError('Only One Character Allowed')
elif NUM.isdigit():
    print(f'The Number Is {NUM}')
elif NUM == 0:
    raise ValueError('Only One Character Allowed')
elif NUM.isalpha():
    raise Exception('Only Numbers Allowed')

# 02
LETTER = input("Add Letter From A to Z: ")
try:
    if len(NUM) != 1: 
        raise TypeError('You Must Write One Character Only') # ==> بنخليه ينزل علي ال إكسيبت اجباري ومعاه المسدج دي

    elif not 'A' <= LETTER <= 'Z':
        raise TypeError('The Letter Not In A - Z')

    else:
        print("You Typed " + LETTER)

except Exception as x: # ==> خزننا المسدج فـ فاريبيل اسمه x علشان نقدر نعمله برينت
    print(x) 

# 03
def calculate(num1: int, num2: int) -> int:
    return num1 + num2

print(calculate(20, 30))
