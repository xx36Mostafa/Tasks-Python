# https://elzero.org/python-assignments-lesson-from-21-to-23/
# append(): adds an element to the end of a list
# extend(): adds multiple elements to the end of a list
# insert(): inserts an element at a specific index in a list
# remove(): removes an element from a list
# pop(): removes and returns the last element from a list (or a specific index if provided)
# index(): returns the index of the first occurrence of an element in a list
# count(): returns the number of occurrences of an element in a list
# sort(): sorts the elements of a list in ascending order
# reverse(): reverses the order of the elements in a list
# copy(): returns a shallow copy of a list

# 01
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(f'{friends[0]} \n{friends[0]} \n{friends[-1]} \n{friends[-1]}') 
# 02
# المطلوب انك تجيب الاسماء اللي الانديكس بتاعها رقم فردي 1 3 5 كدا
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[0::2])
print(friends[1::2]) 
# او
print(friends[0], friends[2], friends[4])
print(friends[1], friends[3])

# 03
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
x = len(friends)
print(friends[1:-1])
print(friends[x-2:x]) # ==> الـ أكس هنا عدد العناصر وممكن نوفر علي نفسنا بـ
print(friends[-2:])

# 04
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
friends[-1] = "Elzero"
friends[-2] = "Elzero"
print(friends)

# 05
friends = ["Osama", "Ahmed", "Sayed"]
friends.insert(0,'Nasser') # ===> 0 دي علشان تتحط فـ الاول 
friends.append('Nasser') # ===> كدا كدا هتتحط فـ الاخر لوحدها
print(friends) 

# 06
friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]
x,y = friends[0],friends[1]
friends[0:2] = [] # ==> دا معناه اننا هنشيلهم زي مـ كنا بنستبدل فوق كدا
friends.pop(-1)
print(friends)

# 07 
friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]
friends.extend(employees) 
friends.extend(school)
print(friends)

# 08
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
friends.sort()
print(friends)
friends.sort(reverse=True)
print(friends)

# 09
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
print(len(friends))

# 10
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]

print(technologies[-1][0]) # ==> يدخل علي اخر انديكس اللي هوا الليست وبعدها هياخد اول انديكس 
print(technologies[-1][-1])