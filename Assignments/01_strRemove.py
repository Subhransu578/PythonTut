# Str remove by using recursion
def StrRemove(s,i):
    print(s[i])
    s.pop(i)
    if s == []:
        return
    return StrRemove(s,i)
lst = ['a','b','c']
StrRemove(lst,0)
print(lst)