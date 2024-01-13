# Merge Sort
# Divide and Merge policy
# Time Complexity O(Nlog(N))
# Space Complexity O(N) because of temperory variables

def maerge(arr,low,mid,high):
    temp=[]     # temporary array
    left=low    # starting index of left half of arr
    right=mid+1 # starting index of right half of arr

    while left<=mid and right<=high :
        if arr[left]<=arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
    
    # elements on left are still remaining
    while left<=mid:
        temp.append(arr[left])
        left+=1
    
    # elements on right are still remaining
    while right<=high:
        temp.append(arr[right])
        right+=1

    # transferring all the elements from temporary to arr
    for i in range(low,high+1):
        arr[i]=temp[i-low]


def mergesort(arr,low,high):
    if low<high:
        mid=(high+low)//2
        mergesort(arr,low,mid) # left half
        mergesort(arr,mid+1,high) # right half
        maerge(arr,low,mid,high) # merging both halves
    return arr

#Test the function 
arr = [64, 34, 25, 12, 22, 11, 90]
print(mergesort(arr,0,len(arr)-1))
