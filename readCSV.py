from csv import reader

# output--> list
with open('file.csv','r') as f:
    csv_reader = reader(f)
    # iterator 
    next(csv_reader)
    for row in csv_reader:
        print(row)

from csv import DictReader
# order dict
with open('file.csv','r') as f:
    csv_reader = DictReader(f, delimiter= '|')
    for row in csv_reader:
        print(row['Email'])

#--------------write csv file---------------
# 1 - writer , 

# from csv import writer

# with open('file2.csv','w',newline='') as f:
#     csv_writer = writer(f)
#     # # methods--> writerow , writerows
#     csv_writer.writerow(['Name','Country'])
#     csv_writer.writerow(['mohit','INDIA'])
#     csv_writer.writerow(['harshit','INDIA'])
   
    # csv_writer.writerows([['name','country'],['mohit','INDIA'],['harshit','INDIA']])

#---------------2-DictWriter--------------

from csv import DictWriter
with open('final.csv','w',newline='') as f:
    csv_writer = DictWriter(f,fieldnames=['firstname','lastname','age'])
    csv_writer.writeheader()
    #writerow , writerows
    # csv_writer.writerow({
    #     'firstname' : 'harshit',
    #     'lastname' : 'vashistha',
    #     'age' : 500
    # })
    # csv_writer.writerow({
    #     'firstname' : 'kaleem',
    #     'lastname' : 'shaikh',
    #     'age' : 500
    # })
    # csv_writer.writerow({
    #     'firstname' : 'irfan',
    #     'lastname' : 'beg',
    #     'age' : 500
    # })
     

    # writerows > [dict, dict, dict ]
    csv_writer.writerows([
        {'firstname' :'harshit', 'lastname':'vashistha', 'age':500},
        {'firstname' :'harshit', 'lastname':'vashistha', 'age':500},
        {'firstname' :'harshit', 'lastname':'vashistha', 'age':500}
        ])

#------------------------- read and write from csv file---------------------------------

# from csv import DictReader , DictWriter

# with open('read.csv','r') as rf:
#     with open('write.csv','w',newline='') as wf:
#         csv_reader = DictReader(rf)
#         csv_writer = DictWriter(wf,fieldnames=['first_name','last_name','age'])
#         csv_writer.writeheader()
#         for row in csv_reader:
#             fname,lname,age = row['firstname'],row['lastname'],row['age']     # extracting from ordered dictionary
#             csv_writer.writerow({
#                 'firstname':fname.upper(),
#                 'lastname':lname.upper(),
#                 'age':age
#             })
