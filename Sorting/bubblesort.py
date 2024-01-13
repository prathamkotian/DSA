# Bubble sort
# Push max value element to right-most position
# chooses two adjacent elements and checks for condition and swaps
# Time Complexity O(N^2)

def bubble_sort(arr):

    # length of arr
    n = len(arr)

    # outer loop runs from index (n-1) till index 1    
    for i in range(n-1,0,-1): 
        for j in range (i):
            if arr[j] > arr[j+1]:   
                # swapping
                arr[j], arr[j+1] = arr[j+1], arr[j] 
    return arr

#Test the function 
arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(arr))