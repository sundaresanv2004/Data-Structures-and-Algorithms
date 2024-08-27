arr = [5, 6, 2, 9, 1, 3, 7]
n = len(arr)

for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if arr[min_index] > arr[j]:
           min_index = j
    
    arr.insert(i, arr.pop(min_index))
    
print("Selection Sort")
print(arr)
