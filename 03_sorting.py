# binary search O(logn), search O(n)

#Insertion Sort 

arr = [5,2,4,6,1,3,8,6,9,0]

for index in range(len(arr)-1):
    for indexmin in range(len(arr[index::-1])):
        if arr[index+1]<arr[indexmin]:
            arr[indexmin],arr[index+1] = arr[index+1],arr[indexmin]
print(arr)

#Insert Sort with binary search
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
        
        
print(binary_search_sort(arr))  