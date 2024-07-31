arr = [3, 1, 5, 6, 2, 8, 4, 7]
n = len(arr)

for i in range(1, n):
    curr = arr[i]
    j = i

    while j > 0 and arr[j - 1] > curr:
        arr[j] = arr[j - 1]
        j -= 1
    arr[j] = curr

print(arr)
    
    
