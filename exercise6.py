A = [1, 2, 2, 3, 4]
B = [2, 4]
sortedA = sorted(A)
sortedB = sorted(B)

def presInAHash(A, B):
    C = {}
    for i in range(len(A)):
        if ():
            C = A[i]

def presInAArray(A, B):
    C = noDuplicates(sortedA)
    for i in range(len(B)):
        for j in (i + 1, len(B) - 1):
            if (C[i] == B[j]):
                C.remove(C[i])

def noDuplicates(A):
    C = []
    for i in range(len(A)):
        for j in (i + 1, len(A) - 1):
            if A[i] == A[j]:
                continue
            C.append(A[i])
    return C
                



print(presInAArray(sortedA, sortedB))
