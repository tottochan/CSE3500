def max_length(A):    
    C = [ -1 for i in range(len(A))]
    for i in range(len(A)):
        max1 = 0
        for j in range(i):
            if A[j] <= A[i] and C[j] > max1:
                max1 = C[j]
        C[i] = max1 + 1
    max2 = 0
    for i in range(len(A)):
        if C[i] > max2:
            max2 = C[i]
    return max2
T = [2,3,5,7,2,9,1,9,3,27,36]
x = max_length(T)
print(x)
