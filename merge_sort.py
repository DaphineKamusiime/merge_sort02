def merge_sort(a,b):
    sorted_arr=[]
    x=0
    y=0
    len_a=len(a)
    len_b=len(b)
    while x<len_a and y<len_b:
        if a[x]<=b[y]:
            sorted_arr.append(a[x])
            x+=1
        else:
            sorted_arr.append(b[y])
            y+=1
##the next 2 while loops apply for unequal arrays 
    while x<len_a:
        sorted_arr.append(a[x])
        x+=1
    while y<len_b:
        sorted_arr.append(b[y])
        y+=1
    return sorted_arr
A=[2,100,1000]
B=[1,699,1000000,1000001]
C=[99,300,501,10003]
D=[99,300]


print(merge_sort(A,B))
print(merge_sort(C,D))
#big o complexity=5+n