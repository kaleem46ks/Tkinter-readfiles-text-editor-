# readfile
# open function
# read method ------> read file
# seek method ------> change cursor position
# tell method ------> tell cursor position
# readline method ------> read only one line
# readlines method ------> gives list containing line by line
# close method

f = open('file1.txt')
# print(f"cursor position {f.tell()}")
# print(f.read())
# print(f.readline(), end="")
# print(f.readline(), end="")
# print(f.readline(), end="")
# f.seek(0)
# print(f"cursor position {f.tell()}")
# print(f.read())

lines = f.readlines()   #-----> gives list 
print(lines)
print(len(lines))
for i in lines:
    print(i, end= '')

#------- name , closed ---------
print(f.name)  #--------> output name of file
print(f.closed) #-------> true or false
f.close()
print(f.closed)


# python escape sequence---> \ n , \ t
# windows - \
# linux, mac - /

# f = open(r"D:\Ms office2021Activation.txt")
# print(f.read())

# for line in f.readlines()[:2]:  # printing only two lines
#     print(line,end='')

# print(f.closed)
# f.close()
# print(f.closed)

#------------with block------------

# f = open('filel.txt')
# f.read()
# f.close()

# with block ---------> you don't have to close file
# context manager
with open('file1.txt')as f:
    data = f.read()
    print(data)

#------------write file-------------
 
# w ----> write
# a -----> append 
# r+ ------> (read and write) it does't create file itself

# with open('file2.txt', 'w') as f:     # w ---> overrite file and delets all old data
#     f.write('Hello there')

# with open('file.txt', 'a') as f:        # a --->  'w' and 'a' also create new file 
#     f.write('Hello there\n')            # with escap sequence cursor moves to next line

with open('file.txt', 'r+') as f:
    f.seek(len(f.read()))
    f.write('\nThis is new line 4')

#-----------write file data to another file -----------

with open('file1.txt','r') as rf:
    with open('file.txt','w') as wf:
        wf.write(rf.read())                 # it read data of file1.txt and write to file.txt