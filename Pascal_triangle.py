
def Pascal_triangle(k):

    res = [[1 for j in range(i + 1)] for i in range(k + 1)]
    for i in range(2, k + 1):
        for j in range(1, i):
            res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
    print(res[-1])

if __name__=="__main__":
    k = 200
    Pascal_triangle(k)
