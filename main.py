#merge sort/divide & conquer algorithm
#recursion is when you call a function inside its own.
def mergesort(array):
    if len(array)>1:
        m=len(array)//2

        L=array[:m]
        R=array[m:]

        mergesort(L)
        mergesort(R)

        i=j=k=0
        #i is the left element of the left array
        #j us the left element of the right array
        #k is the merged array index

        while i <len(L) and j < len(R):
            if L[i]  < R[j]:
                array[k] = L[i]
                i+=1
            else:
                array[k] = R[j]
                j+=1
            k+=1
        while i < len(L):
            array[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            array[k]= R[j]
            j+=1
            k+=1

def printList(array):
    for i in range (len(array)):
        print(array[i],end=" ")

array=[2,5,9,1,3,4]
print("Before sorting: {}".format(array))
mergesort(array)
print("After sorting:")
printList(array)
