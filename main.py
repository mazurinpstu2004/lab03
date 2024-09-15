def bubble_sort(sort_array):
    for i in range(len(sort_array)):
        for j in range(len(sort_array)):
            if sort_array[i] < sort_array[j]:
                temp = sort_array[i]
                sort_array[i] = sort_array[j]
                sort_array[j] = temp
    return sort_array


n = (int(input()))
arr = []
for i in range(n):
    elem = int(input())
    arr.append(elem)

bubble_sort(arr)

print(arr)