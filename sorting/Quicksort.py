
from typing import List
def partition(arr,low,high):
    i=low
    j=high
    pivot=low
    while i<=j:
        if arr[i]<=arr[pivot]:
            i+=1
        elif arr[j]>arr[pivot]:
            j-=1
        else:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
    
    arr[pivot],arr[j]=arr[j],arr[pivot]
    return j
        





def quickSort (arr: List[int], low: int,high: int):
    if low<high:
        p_index=partition(arr,low,high)
        quickSort(arr,low,p_index-1)
        quickSort(arr,p_index+1,high)
    
