import os

#write file
a = open('main.txt', 'a', encoding = 'utf-8')
a.write('noi dung file')
a.close()

with open('main.txt', 'a') as f:
    f.write('noi dung file')
    
#create folder
os.mkdir("learn")

#rename file
os.rename('main.txt', 'xulyfile.txt')

#remove folder
os.remove('xulyfile.txt')

#remove folder
# import shutil
# shutil.rmtree('Code_tool/learn')

#read folder
diachi = os.listdir('Code_tool/learn')
# D = os.listdir('E:\\tool\\lap trinh tool python\\bai 2\\Duong ha) 
print(diachi)

