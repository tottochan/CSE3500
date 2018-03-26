def split_number(n):
    C = [[ -1 for i in range(n+1)] for j in range(n+1)]
    C[0][0] = 1

    for i in range(1, n+1):
    	C[0][i] = 0

    for i in range(1, n+1):
    	for j in range(n+1):
	    if j >= i:
	       C[i][j] = C[i-1][j] + C[i][j-i]
	    else:
		C[i][j] = C[i-1][j]

    return C[n][n]

print(split_number(6))
