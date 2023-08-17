s = [int(i) for i in input().split()]
a = [[int(i) for i in input().split()] for j in range(s[0])]
b = [["0" for i in range(s[0])] for j in range(s[1])]
for i in range(s[1]) :
        for j in range(s[0]) :
                b[i][j] = a[j][i]
        print(' '.join([str(i) for i in b[i]]))


