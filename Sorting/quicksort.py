# Quick Sort 
# Picks the pivot and places it in correct place
# smaller elements on left side and larger on right
# i = left pointer and j = right pointer
# i finds first element greater than pivot 
# j finds first element smaller than pivot
# Time Complexity O(N^2) for WORST and O(Nlog(N)) for Average

def partition(arr,low,high):
    
    p=arr[low]
    i=low
    j=high

    while i<j:
        
        while arr[i]<=p and i<=high-1:
            i+=1
        while arr[j]>p and j>=low+1:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    
    arr[low],arr[j] = arr[j],arr[low]

    return j


def Quick_sort(arr,low,high):
    if low < high:
        pivot=partition(arr,low,high)
        Quick_sort(arr,low,pivot-1)
        Quick_sort(arr,pivot+1,high)
    return arr

#Test the function 
arr = [64, 34, 25, 12, 22, 11, 90]
print(Quick_sort(arr,0,len(arr)-1))