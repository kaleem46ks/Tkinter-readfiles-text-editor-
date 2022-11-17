import os
# os.getcwd()
print(os.getcwd())
# os.mkdir('movies')
if os.path.exists('movies'):
    print('already exits')
else:
    os.mkdir('movies')

# os.chdir(r'd:\stuff')
# open('jabba.txt','a').close() #---------> to create file
# print(os.listdir())
# print(os.listdir(r'D:\Old Pictures\old oictures\image'))     #-----> list of all cwd

# for item in os.listdir():
#     path = os.path.join(os.getcwd(),item)
#     print(path)     # printing all file path in cwd

fileiter = os.walk(r'D:\Excel  Data and Test sheet')
# print(fileiter)
for current_path,folder_name,file_name in fileiter:
    print(f"current path: {current_path}")
    print(f"folder name: {folder_name}")
    print(f"file name: {file_name}")

# os.rmdir('new')   #-------> only delets empty folder
# os.makedirs('new/movies')     #------> create folder inside folder

import shutil

# shutil.rmtree('songs')  #----------> permanently delets folder
# shutil.copytree('new','documents/new')      #-------->  ('folder to copy','path/'folder name')
# shutil.copy('new.txt','documents/new.txt')   #-------->  ('file to copy','path/'file name')
# shutil.move('file.txt','new/file2.txt')        #-------->  ('file to move', 'path/rename or file name')
# shutil.move('new','documents/new2') 