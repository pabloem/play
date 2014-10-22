from random import randrange
def quicksort(A):
    if len(A) <= 1:
        return A
    pivot = A[randrange(len(A))]
    #print 'quicksort - Enter - piv:'+str(pivot)+' A:'+str(A)
    L = list()
    R = list()
    pivot_list = list()
    for a in A:
        if a == pivot:
            pivot_list.append(a)
        elif a < pivot:
            L.append(a)
        else:
            R.append(a)
    L = quicksort(L)
    R = quicksort(R)
    return L+pivot_list+R
    
a = [randrange(1000) for _ in range(100)]
quicksort(a)
