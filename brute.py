import itertools

DNA = ["cctgatagacgctatctggctatccaggtacttaggtcctctgtgcgaatctatgcgtttccaaccat",
       "agtactggtgtacatttgatccatacgtacaccggcaacctgaaacaaacgctcagaaccagaagtgc",
       "aaacgttagtgcaccctctttcttcgtggctctggccaacgagggctgatgtataagacgaaaatttt",

       ]


t = 3
n = 68
l = 8



def score(DNA, s):
    diffArray = ['a', 'c', 'g', 't']
    array = []
    k = 0
    for d in DNA:
        tempArray = []
        for w in d[s[k]:s[k] + l]:
            tempArray.append(w)

        k += 1
        array.append(tempArray)
    i = 0
    mat = []

    i1 = 0
    while i1 < len(diffArray):
        j1 = 0
        arr1 = []
        while j1 < l:
            arr1.append(0)
            j1 += 1
        mat.append(arr1)
        i1 += 1
    while i < len(diffArray):
        j = 0
        while j < l:
            k = 0
            while k < t:
                if diffArray[i] == array[k][j]:
                    mat[i][j] += 1
                k += 1
            j += 1
        i += 1

        x = 0
        sum = 0
        while x < l:
            y = 0
            max = 0
            while y < len(mat):
                if mat[y][x] > max:
                    max = mat[y][x]
                y += 1
            sum += max
            x += 1
    return sum



def bruteForce(DNA, t, n, l):
    data = itertools.product(range(n - l), repeat=t)
    bestScore = 0
    bestMotif = []
    for s in data:
        sco = score(DNA, s)
        if sco > bestScore:
            bestMotif = s
            bestScore = sco

    print("Best Score: ", bestScore)
    print("Best Motif: ", bestMotif)

    return bestMotif


bruteForce(DNA, t, n, l)
