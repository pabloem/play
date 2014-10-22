def max_subarray_n2(a):
    pass
    max_sum = 0
    max_i = 0
    max_j = 0
    for i in range(len(a)-1):
        this_sum = 0
        for j in range(len(a))[i:]:
            this_sum += a[j]
            print 'I is '+str(i)+' J is'+str(j)+' TS is '+str(this_sum)
            if this_sum > max_sum:
                max_sum = this_sum
                max_i = i
                max_j = j
    return max_i, max_j, max_sum


def max_subarray_nlogn(A,low,high):
    pass
    if high==low:
        return (low,high,A[low])
    else:
        mid = (low+high)/2
        (left_low,left_high,left_sum) = max_subarray_nlogn(A,low,mid)
        (right_low,right_high,right_sum) = max_subarray_nlogn(A,mid+1,high)
        (cross_low,cross_high,cross_sum) = _max_crossing_subarray(A,low,mid,high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low,left_high,left_sum)
        if right_sum >= cross_sum:
            return (right_low,right_high,right_sum)
        return (cross_low,cross_high,cross_sum)
    
def _max_crossing_subarray(A,low,mid,high):
    left_sum = -20000
    max_left = mid
    t_sum = 0
    i = mid
    while i >= low:
        t_sum += A[i]
        if t_sum > left_sum:
            left_sum = t_sum
            max_left = i
        i-=1
    right_sum = -20000
    t_sum = 0
    j = mid+1
    max_right = j
    while j <= high:
        t_sum = t_sum+A[j]
        if t_sum > right_sum:
            right_sum = t_sum
            max_right = j
        j+=1
    return (max_left,max_right,left_sum+right_sum)

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
