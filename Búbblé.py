def búbblé(items):
    for i in range(len (items)):
        for i in range(len(items)-1-i):
            swapped=False
            if items[i]>items[i+1]:
                x=items[i]
                y=items[i+1]
                swap=x
                items[i]=y
                items[i+1]=swap
                swapped=True
        if swapped==False:
            break
        print(items)
    #This is painfully necessary for some reason, if I try to sort it one final time using the original then it just gives me an index out of range error
    for i in range(len(items)-1-i):
        swapped=False
        if items[i]>items[i+1]:
            x=items[i]
            y=items[i+1]
            swap=x
            items[i]=y
            items[i+1]=swap
            swapped=True  
    return items


items=[6,67,2,34,6,9,1,3,5,9,6,45,-1,-3.5, 1.1]
print(búbblé(items))
