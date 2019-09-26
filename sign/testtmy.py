

def Partition(arr,sta,end):
    int i=low
    int j=high
    int key=arr[low]
    while True:
        while arr[i++]<key:
            if i==j:
                break
        while arr[j--]>key:
            if j==i:
                break
        if i>=j:
            break
        int temp=arr[i]
        arr[i]=arr[j]
        arr[j]=temp
    int temp=arr[0]
    arr[0]=arr[j]
    arr[j]=temp
    Partition(arr,low,j-1)
    Partition(arr,j+1,high)


def Qsort():
    int arr[8]=[49,38,65,97,76,13,27,49]
    Qsort(arr,0,len(arr))

    print (arr)
