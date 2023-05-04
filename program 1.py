'''
1. create an array with positive and negative numbers then move all
the negative numbers towards starting of the array and print the final output.
[10,1,5,-5,-9]
'''
def sort_negative(arr, n ):
    j = 0
    for i in range(0, n) :
        if (arr[i] < 0) :
            temp = arr[i]
            arr[i] = arr[j]
            arr[j]= temp
            j = j + 1
    print(arr)
arr = [10,1,5,-5,-9]
n = len(arr)
sort_negative(arr, n)
