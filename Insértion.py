def insertion(data):
    for i in range(1,len(data)):
        current_item=data[i]
        j=i
        while j>0 and data[j-1]>current_item:
            data[j]=data[j-1]
            j=j-1
        data[j]=current_item
    return data
data=[1,2,3,6,2,52,5253546,71,12,734,124,674,8463,12345564,12454]
print(insertion(data))