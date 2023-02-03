# https://elzero.org/python-assignments-lesson-from-26-to-32/

# add() - adds an element to the set
# clear() - removes all elements from the set
# copy() - creates a shallow copy of the set
# difference() - returns the difference between two sets as a new set
# difference_update() - removes all elements of another set from this set
# discard() - removes an element from the set if it is present
# intersection() - returns the intersection of two sets as a new set
# intersection_update() - removes all elements from this set that are not present in another, specified set
# isdisjoint() - returns whether two sets have an intersection or not
# issubset() - returns whether another set contains this set or not
# issuperset() - returns whether this set contains another set or not
# pop() - removes and returns an arbitrary set element. Raises KeyError if the set is empty
# remove() - removes an element from the set. Raises KeyError if element not in set
# symmetric_difference() - returns the symmetric difference of two sets as a new set
# symmetric_difference_update() - inserts the symmetric differences from this set and another
# union() - returns the union of sets in a new set
# update() - update the set with the union of this set and others

# 01
my_list = [1, 2, 3, 3, 4, 5, 1]
unique_list = list(set(my_list))
# اللاين رقم 4 دا احنا عارفين ان الـ set مش بتسمح بـ تكرار الارقام فيها 
# فـ احنا جينا حولنا الـ الليست لـ set
# ورجعناها list تاني زي كدا بظبط
unique_list = set(my_list)
unique_list = list(unique_list)
#اللاينين دول هما هما لاين رقم 4 
print(unique_list)
print(type(unique_list))
print(unique_list[:-1])

# 02
nums = {1, 2, 3}
letters = {"A", "B", "C"}
first = nums | letters # ==> union operator 
second = nums.union(letters) # ==> زي اللي فوق بظبط بس دا بـ اوبريتور و دا بـ فانكشن
third = nums.copy()
third.update(letters) 

print(first)
print(second)
print(third)

# 03 
my_set = {1, 2, 3}
letters = {"A", "B", "C"}
print(my_set)
my_set.clear()
print(my_set)
my_set.add('A')
my_set.add('B')
print(my_set)

# 04
set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}

print(set_one.issubset(set_two))

# 05 
dic = {'HTML':'0.9',
        'CSS': '0.8',
        'Python':'0.3%',
        'Ai':'0.2'}

print("HTML Progress Is ", dic["HTML"])
print("CSS Progress Is ", dic["CSS"])
print("Python Progress Is ", dic["Python"])
print("AI Progress Is ", dic["Ai"])

dic["Nodejs"] = '95%'
print("Nodejs Progress Is ", dic["Nodejs"])