# size = int(input("enter the size: "))
# dic={}
# for i in range(size):
#     id=int(input('Enter student id: '))
#     name=input('Enter student name: ')
#     age=int(input('Enter student age: '))
#     course=input('Enter student course: ')
#     stu=[id,name,age,course]
#     dic[i]=stu
# search=int(input('search id: '))
# for i in range(size):
#     if dic[i][0]==search:
#         print('****** Student Information *****')
#         print('student id: ',dic[i][0])
#         print('student name: ',dic[i][1])
#         print('student age: ',dic[i][2])
#         print('student course: ',dic[i][3])
# add=input('Do you want to record more yes or no: ')
# if add == 'yes':
#     id=int(input('Enter student id: '))
#     name=input('Enter student name: ')
#     age=int(input('Enter student age: '))
#     course=input('Enter student course: ')
#     stu=[id,name,age,course]
#     dic[i]=stu
# else:
#     print('Ok fine')


dic={}
while True:
    id=int(input('Enter student id: '))
    name=input('Enter student name: ')
    age=int(input('Enter student age: '))
    course=input('Enter student course: ')
    stu=[id,name,age,course]
    dic[id]=stu
    add=input('Do you want add more record yes or no: ')
    if add == 'yes':
        continue
    else:
        search=int(input('Enter search id: '))
        if search in dic:
            print('****** Student Information *****')
            print('student id: ',dic[search][0])
            print('student name: ',dic[search][1])
            print('student age: ',dic[search][2])
            print('student course: ',dic[search][3])
            break
        else:
            print('Sry!! Student id is not found.')
            break