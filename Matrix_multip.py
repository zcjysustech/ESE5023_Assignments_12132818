import random

def Matrix_multip(M1,M2):
    res = [[0]*len(M2[0]) for i in range(len(M1))]
    for i in range(len(res)):
        for j in range(len(res[0])):
            for u in range(len(M1[0])):
                res[i][j] += M1[i][u]*M2[u][j]
    return res

if __name__=="__main__":
    M1 = [[0] * 5 for i in range(10)]
    for i in range(len(M1)):
        for j in range(len(M1[0])):
            M1[i][j] = random.randint(0,50)

    M2 = [[0] * 10 for i in range(5)]
    for i in range(len(M2)):
        for j in range(len(M2[0])):
            M2[i][j] = random.randint(0,50)
    res = Matrix_multip(M1,M2)
    print(M1)
    print(M2)
    print(res)