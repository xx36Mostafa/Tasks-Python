# https://elzero.org/python-assignments-lesson-from-24-to-25/

# + ==> علشان نضيف 2 مع بعض او اكتر 
# * ==> علشان نكرر العناصر اللي موجوده
# count ==> علشان نعرف عدد عنصر معين 
# index()  ==> بيخليك تعرف الاندكس بتاع رقم او اي حاجه عموما يعني
# destruct ودي شوفها فـ الحل رقم 5 لاني مش هعرف اشرحها بصراحه

# 01 
name = 'BoDa',
print(name[0])
print(type(name))

# 02

friends = ("Osama", "Ahmed", "Sayed")
friends = ("Elzero",) + friends[1:]  # وممكن نعمله بـ طريقه تانيه وهي اننا نحوله لـ ليست ونرجعه تاني
print(friends)
print(type(friends))
print(f'{len(friends)} Elements')

# 03

nums = (1, 2, 3)
letters = ("A", "B", "C")
nums_and_letters_one = nums + letters
print(nums_and_letters_one)
print(f'{len(nums_and_letters_one)} Elements')

# 04
my_tuple = (1, 2, 3, 4)
x,y,w,z = my_tuple

print(x)
print(y)
print(z)