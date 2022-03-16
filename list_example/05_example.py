# 5: display list element by using positive and negative index
list = [10,20.3,'hello',20]
ind = len(list)
for i in range(0,ind):
    print(f'{list[i]} is in {i} or -{ind} index')
    ind = ind - 1