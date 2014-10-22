from math import log
def radixSort(inList, base = 2):
    maxexp = int(round(log(max(inList),base))+1)
    print 'Maxexp is: '+str(maxexp)
    for i in range(maxexp):
        zeros = list()
        ones = list()
        for j in inList:
            if (j/base**i)%base == 1:
                ones.append(j)
            else:
                zeros.append(j)
        inList = zeros+ones
    return inList
