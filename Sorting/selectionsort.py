# selection sort
# smallest element is shifted to left-most index
# Time complexity O(N^2)

def selection_sort(arr):
    
    n=len(arr)

    # outer loop runs till index (n-2)
    
    for i in range(n-1):
        min_idx = i

        # inner loop runs from ith index till (n-1)
        for j in range(i,n):
    
            if arr[j] < arr[min_idx]:
                min_idx = j
    
        arr[min_idx],arr[i]=arr[i],arr[min_idx]
    
    return arr

#Test the function 
arr = [64, 34, 25, 12, 22, 11, 90]
print(selection_sort(arr))