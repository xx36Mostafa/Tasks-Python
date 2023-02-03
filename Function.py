# https://elzero.org/python-assignments-lesson-from-56-to-59/
# 01 
def calculate(num1,num2,opreator='add'):
   if opreator.lower() == 'add' or opreator.upper() == 'A':
      return num1+num2
   elif opreator.lower() == 'subtract' or opreator.upper() == 'S':
      return num1-num2
   elif opreator.lower() == 'multiply' or opreator.upper() == 'M':
      return num1*num2
   else:
      print('[!] Error')
print(calculate(10, 20)) # 30
print(calculate(10, 20, "AdD")) # 30
print(calculate(10, 20, "a")) # 30
print(calculate(10, 20, "A")) # 30
print(calculate(10, 20, "S")) # -10
print(calculate(10, 20, "subTRACT")) # -10
print(calculate(10, 20, "Multiply")) # 200
print(calculate(10, 20, "m")) # 200

# 02 
def addition(*n):
    x = 0
    for i in n:
        if i != 10:
            if i == 5:
                x -= 5
            else:
                x += i
    return x
print(addition(10, 20, 30, 10, 15)) 
print(addition(10, 20, 30, 10, 15, 5, 100))

# 03
def show_skills(name,*skills):
    print(f'Hello {name} Your Skills Is')
    if len(skills) == 0:
        print(f'Hello {name} You Have No Skills To Show')
    else:
        for i in skills:
            print(f'- {i}')
    
show_skills("Osama", "HTML", "CSS", "JS", "Python")
show_skills("Ahmed")

# 04
def say_hello(name='Unknown',age='Unknown',country='Unknown'):
    return f'Hello {name} Your Age Is {age} And You Live In {country}'
print(say_hello("Osama", 38, "Egypt"))
print(say_hello())
