# 01
values = (0, 1, 2)
#create tuple
if any(values): 
    # Try Check if values include True or False Value And Return 
    # We Found False So This if Is Cancelled
    # 0 ==> False So my_var will not be defined
    my_var = 0

my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]
if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):
    # Try Check if my_list includ True or False Value And Return
    # We Found True in all(my_list[:4]) so will print Good
    print("Good")
else:
  print("Bad")

# 02 

v = 40

my_range = list(range(v))

print(sum(my_range, v) + pow(v, v, v))  # 820

# 03
n = 20

l = list(range(n))

if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):

  print("Good")

# 04 
# السؤال دا ادفانسيد وانا بصراحه مكسل أحله بكرا بقي :"D
