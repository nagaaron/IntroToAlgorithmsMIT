# binary search O(logn), search O(n)

#Insertion Sort O(n^2)

arr = [11,22,33,44,55,5,2,4,6,1,3,8,6,9,0]
def insertion_sort(arr):
    for index in range(len(arr)-1):
        for indexmin in range(len(arr[index::-1])):
            if arr[index+1]<arr[indexmin]:
                arr[indexmin],arr[index+1] = arr[index+1],arr[indexmin]
    return arr


#Insert Sort with binary search O(log(n)n)
def binary_search_sort(arr):
    for index in range(len(arr)-1):
        halfcheck = (index+1)//2
        if arr[index+1] < arr[halfcheck]:
            for indexmin in range(len(arr[halfcheck::-1])):
                if arr[index+1]<arr[indexmin]:
                    arr[indexmin],arr[index+1] = arr[index+1],arr[indexmin]
        if arr[index+1] >= arr[halfcheck]:
            for indexmin in range(len(arr[halfcheck:index:1])):
                if arr[index+1]<arr[indexmin]:
                    arr[indexmin],arr[index+1] = arr[index+1],arr[indexmin]
    return arr
        

#because of auxillary space insertion is preferable over merge sort
#merge sort O(log(n)n)

def merge(arr,leftarr,rightarr):
    
    lenghtl = len(leftarr)
    lenghtr = len(rightarr)
    k,i,j  =0,0,0
    while i < lenghtl and j < lenghtr:
        if leftarr[i] <= rightarr[j]:
            arr[k] = leftarr[i]
            k+=1
            i+=1
        elif leftarr[i] > rightarr[j]:
            arr[k] = rightarr[j]
            k+=1
            j+=1
    while i <lenghtl:
        arr[k] =leftarr[i]
        k+=1
        i+=1
    while j <lenghtr:
        arr[k] = rightarr[j]
        k+=1
        j+=1
    return arr
    
def merge_sort(arr):
    lenght = len(arr)
    if lenght < 2:
        return arr
    mid = lenght//2
    leftarr = arr[:mid]
    rightarr = arr[mid:]
    merge_sort(leftarr)
    merge_sort(rightarr)
    return merge(arr,leftarr,rightarr)


print(insertion_sort(arr))
print(binary_search_sort(arr))
print(merge_sort(arr))




