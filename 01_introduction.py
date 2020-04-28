import random

scale = 10
arr  = [random.randint(0, 9) for _ in range(scale)]

# broot force 1d
def find_peak(arr):
    for index in range(1,len(arr)-1):
        if arr[index-1] <= arr[index] and arr[index] >= arr[index+1]:
            return index,arr[index]

        
# divide & conquer 1d
def find_peak_dq(arr):
    
    half  = len(arr)//2    
    if arr[half-1] <= arr[half] and arr[half] >= arr[half+1]:
        return half, arr[half]
    elif arr[half-1]< arr[half]:
        return find_peak_dq(arr[half::])
    else:
        return find_peak_dq(arr[half::])

arr2 = [[random.randint(0, 9) for _ in range(scale)] for _ in range(scale)]
srow = random.randint(0,len(arr2)-1)
scol = random.randint(0,len(arr2)-1)

def greedy_ascent(arr2,srow,scol):
    if srow > 0 and arr2[srow-1][scol] > arr2[srow][scol]:
        return(greedy_ascent(arr2, srow-1, scol))
    
    elif srow < (len(arr2)-1) and arr2[srow+1][scol] > arr2[srow][scol]:
        return(greedy_ascent(arr2, srow+1, scol))
    
    elif scol > 0 and arr2[srow][scol-1] > arr2[srow][scol]:
        return(greedy_ascent(arr2, srow, scol-1))    
        
    elif scol < (len(arr2)-1) and arr2[srow][scol+1] > arr2[srow][scol]:
        return(greedy_ascent(arr2, srow, scol+1))
    else:
        return (srow,scol)       

     
for i in arr2:
    print(i)
print(greedy_ascent(arr2, srow, scol))      
                
            
            