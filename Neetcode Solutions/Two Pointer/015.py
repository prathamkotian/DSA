class Solutions:
    def triplet(n: int, arr: [int]) -> [[int]]:

        ans=[]
        arr.sort()

        for i in range(n):
            # ignoring duplicates:
            if i != 0 and arr[i] == arr[i - 1]:
                continue

    
            j=i+1
            k=n-1

            while (j<k):
                total_sum=arr[i]+arr[j]+arr[k]
                if total_sum>0:
                    k-=1
                elif total_sum<0:
                    j+=1
                else:
                    temp=[arr[i],arr[j],arr[k]]
                    ans.append(temp)
                    j+=1
                    k-=1
                    # ignoring dublicates 
                    while j < k and arr[j] == arr[j - 1]:
                        j += 1
                    while j < k and arr[k] == arr[k + 1]:
                        k -= 1

            
        return ans


nums = [-1,0,1,2,-1,-4]
print(Solutions.triplet(len(nums),nums))