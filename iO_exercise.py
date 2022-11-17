# Harshit's salary is 100
# Mohit's salary is 50
#-------------------exercise 1-----------------

with open('salary.txt','r') as rf:
    with open('output.txt','w') as wf:
        for line in rf.readlines():
            name,salary = line.split(',')
            wf.write(f'{name}\'s salary is {salary}')



#-------------------exercise 2-----------------

# with open('index.html','r') as webpage :
#     with open('output2.txt','a') as wf:
#         for line in webpage.readlines():
#            if '<a href=' in line:
#                pos = line.find('<a href=')
#                first_quote = line.find('\"',pos)
#                second_quote = line.find('\"',first_quote+1)
#                url = line[first_quote+1:second_quote]
#                wf.write(url+'\n')

#----------better solution------------

with open('index.html','r') as webpage :
    with open('output2.txt','a') as wf:
        page = webpage.read()
        link_exist = True
        while link_exist:
            pos = page.find('<a href=')
            if pos == -1:
                link_exist = False
            else:
                first_quote = page.find('\"',pos)
                second_quote = page.find('\"',first_quote+1)
                url = page[first_quote+1:second_quote]
                wf.write(url+'\n')
                page = page[second_quote:]


#-------------read file with emojis--------------

# with open('love_story.txt','r',encoding='utf-8') as f:
#     print(f.encoding)
#     data= f.read()
#     print(data)


#--------------read large file---------------

# with open('file.txt','r') as f:
#     data = f.read(100)
#     while len(data)>0:          # to read very large file use while loop to be memory efficient
#         print(data)
#         data = f.read(100)