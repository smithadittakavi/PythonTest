def swap( A, x, y ):
    tmp = A[x]
    A[x] = A[y]
    A[y]=tmp


def selectionsort( aList ):
    for i in range( len( aList ) ):
            least = i
            for k in range( i + 1 , len( aList ) ):
                if aList[k] < aList[least]:
                    least = k
 
            swap( aList, least, i )

aList = [3,7,2,1]
selectionsort(aList)
print(aList)
 
 
