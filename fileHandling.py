# https://elzero.org/python-assignments-lesson-from-65-to-68/
# مش عليك فـ منهجك اول سؤال دا
# 01
import os

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
path_folder = os.path.join(desktop, "Python")
path_file = os.path.join(desktop, "Python","assign.py")
os.mkdir(path_folder)
os.mkdir(path_file)

# هيعمل الـ 50 ملف تيكست خلي بالك بقي
for i in range(1, 51):
    file_path = os.path.join(path_folder, f"txt{i}.txt")
    with open(file_path, "w") as file:
        file.write(f"Elzero Web School => {i}")

special_file_path = os.path.join(path_folder, "txt25.txt")
os.rename(special_file_path, os.path.join(path_folder, "special-text.txt"))
special_file = open(os.path.join(path_folder, "special-text.txt"),'w')
special_file.write('')
special_file.close()

print(f'"Current working directory:" {os.getcwd()}')
print(f'"Current file path:" {__file__}')
print(f'"Current file name:" {os.path.basename(__file__)}')
print(f'"Total number of files in the Python folder:", {len(os.listdir(path_folder))}')

# 02
txt1 = os.path.join(path_folder, "txt1.txt")
with open(txt1,'a') as f:
    for i in range(50):
        f.write('Appended => Elzero Web School'+'\n')
    
# # 03
number_of_words = 0

txt1 = os.path.join(path_folder, "txt1.txt")
with open(txt1,'r') as f:
    lines = f.readlines()
    data = f.read().split()
    print(f'Number Of Lines Is => {len(lines)}')
    print(f'Number Of Words  Is => {len(data)}')
    print(f'Number Of Chars  Is => {len(f.read())}')
    print(f'Number Of "l" Is => {f.read().count("l")}')
