# An identity matrix is defined as a square matrix with 1s running from the top left of the square to the bottom right. The rest are 0s. The identity matrix has applications ranging from machine learning to the general theory of relativity.

# Create a function that takes an integer n and returns the identity matrix of n x n dimensions. For this challenge, if the integer is negative, return the mirror image of the identity matrix of n x n dimensions.. It does not matter if the mirror image is left-right or top-bottom.

# https://edabit.com/challenge/QN4RMpAnktNvMCWwg

def id_mtrx(n):
    if isinstance(n, int):
        matrix=[]
        ps=n
        n=abs(n)
        
        for i in range(n):
            row=[0]*n
            row[i]=1
            matrix.append(row)
        if ps>0:        
            return matrix
        return matrix[::-1]
    
    return "Error"

print(id_mtrx(-2))