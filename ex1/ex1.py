arr = [0]*10
arr[0] = 10
arr[1] = 20
arr.append(1)
arr.append(2)

print(arr)
for x in arr:
    print(x, end=' ')
print()
for i in range(len(arr)):
    print(arr[i], end=' ')