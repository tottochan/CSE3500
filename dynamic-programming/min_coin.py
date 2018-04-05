def min_coin(D, n):
    
    C = [ 0 for i in range(n+1)]

    C[0] = 0

    for i in range(1, n+1):
        
        C[i] = -1

        for j in range(len(D)):
            
            if i >= D[j] and C[i - D[j]] >= 0:

                if C[i] == -1:
                    
                    C[i] = C[i - D[j]] + 1
                    
                elif C[i] >=0 and C[i] > C[i - D[j]] + 1:
                    
                    C[i] = C[i - D[j]] + 1
                    
                    
    return C[n]

D = [1, 2, 5, 7]

n = 100

m = min_coin(D,n)

print(m)
