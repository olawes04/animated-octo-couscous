import random



def merge(list_a, list_b):
    i=0
    j=0
    merged_list=[]
    while len(merged_list)<len(list_a)+len(list_b):
        if list_a[i]<list_b[j]:
            merged_list.append(list_a[i])
            i+=1
        else:
            merged_list.append(list_b[j])
            j+=1
        if i==len(list_a):
            y=j
            for x in range(j,len(list_b)):
                merged_list.append(list_b[y])
                y+=1
            break
        elif i==len(list_b):
            y=i
            for x in range(i,len(list_a)):
                merged_list.append(list_a[y])
                y+=1
            break
    return merged_list

#print(merge([1,2],[1,4,7]))
#assert(merge([1,2],[1,4,7])==[1,1,2,4,7])
list_a=[]
list_b=[]  

for i in range(10):
    list_a=list_a.append(random.randint(1,100))
for i in range(15):
    list_b=list_b.append(random.randint(1,100))

print(merge(list_a,list_b))

