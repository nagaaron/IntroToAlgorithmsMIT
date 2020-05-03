# heaps and heap sort

# heaps: nearly completed binary tree

# max heap is particulary important

# heapsort
# (1) create an max heap array out of a random array
# (2) find max element A[i]
# (3) Swap elements A [n] with A[i]

arr = [1,14,10,8,7,9,3,2,4,16,2]

def heap_sort(arr):
    lenght = len(arr)
    build_max_heap(arr,lenght)
    for i in range(lenght-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        max_heapify(arr, i, 0)
    return arr
def build_max_heap(arr,lenght):
    
    for i in range(lenght,-1,-1):
        max_heapify(arr,lenght, i)
    
def max_heapify(arr,l,pos):
    largest = pos
    lpos = 2*pos+1
    rpos = 2*pos+2
    if  lpos < l and arr[pos] < arr[lpos]:
        largest = lpos
    if rpos < l and arr[largest] < arr[rpos]:
        largest = rpos
    
    if largest != pos:
        arr[largest],arr[pos] = arr[pos],arr[largest]
        max_heapify(arr,l,largest)
            

print(heap_sort(arr))