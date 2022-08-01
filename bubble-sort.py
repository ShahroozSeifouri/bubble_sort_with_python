def bubble_sort(arr):
    n = len(arr)
    for i in range (n):
        for j in range (0,n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
arr=[400,999,15,87,687,489,3245,1598,3394,184,1213,8,85,1,2,6,87]
bubble_sort(arr)
print('Sorted: ', arr)