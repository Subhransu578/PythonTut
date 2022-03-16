list1 = [[[10,20,30],[40,50,60],[70,80,90]],[[100,200,300],[400,500,600],[700,800,900]]]
list2 = [[[101,20,30],[40,50,60],[70,80,90]],[[100,200,300],[400,500,599],[700,800,900]]]
list = []
# for i in range(2):
#     for j in range(3):
#         for k in range(3):
#             list1[i][j][k] = list1[i][j][k] + list2[i][j][k]
#             print(list1[i][j][k])

for i in range(2): # this is number of 2D array 
    list.append([])
    for j in range(3): # this is number of 1D array inside 2D array
        list[i].append([])
        for k in range(3): # this is number of elements inside 1D array
            list[i][j].append(list1[i][j][k] + list2[i][j][k])
            print(f'Sum of {list1[i][j][k]} + {list2[i][j][k]} = {list[i][j][k]}')