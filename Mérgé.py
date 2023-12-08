import random



def merge(list_a, list_b):
    i = 0
    j = 0
    merged_list = []
    while i < len(list_a) and j < len(list_b):
        if list_a[i] < list_b[j]:
            merged_list.append(list_a[i])
            i += 1
        else:
            merged_list.append(list_b[j])
            j += 1
    while i < len(list_a):
        merged_list.append(list_a[i])
        i += 1
    while j < len(list_b):
        merged_list.append(list_b[j])
        j += 1
    return merged_list

#print(merge([1,2],[1,4,7]))
#assert(merge([1,2],[1,4,7])==[1,1,2,4,7])

list_c=[19,1,2,42,3,5,4,5,3,9]


def merge_sort(list_c):
    if len(list_c) <= 1:
        return list_c
    middle = len(list_c) // 2
    left_list = list_c[:middle]
    right_list = list_c[middle:]
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return merge(left_list, right_list)

print(merge_sort([19, 1, 2, 42, 3, 5, 4, 5, 3, 9]))
