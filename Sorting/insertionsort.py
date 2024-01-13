# Insertion Sort
# Takes an element and places in its right position
# Time Complexity O(N^2)
# Best case O(N)

def insertion_sort(arr):
    n=len(arr)
    
    for i in range(n):
        j=i
        while (j>0 and arr[j-1]>arr[j]):
            arr[j], arr[j-1]=arr[j-1], arr[j]
            j-=1
    return arr

#Test the function 
arr = [64, 34, 25, 12, 22, 11, 90]
print(insertion_sort(arr))