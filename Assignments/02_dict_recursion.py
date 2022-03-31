# dictionary key with value
dic={1:'a',7:'b',3:'c'}
lst=list(dic.items())
j=0
k=0
def display(d,lst,j,k):
    if j not in range(len(lst)):
        return
    print(f'{lst[j][k]}: {lst[j][k+1]}{lst[j][k]}')
    j+=1
    return display(d,lst,j,k)
display(dic,lst,j,k)