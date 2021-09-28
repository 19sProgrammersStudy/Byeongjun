r,c,k=map(int,input().split())
r,c=r-1,c-1
board=[list(map(int,input().split())) for _ in range(3)]
t=0
row,col=3,3
while t<101 :
    if r<row and c<col and board[r][c]==k : break
    max=0
    if row>=col :
        temp_all=[]
        for i in range(row) :
            check,temp=[],[]
            for j in range(col) :

                if [board[i][j]] not in check and board[i][j]!=0 :
                    check.append([board[i][j]])
            for j in range(len(check)) :
                check[j].append(board[i].count(check[j][0]))
            check.sort(key=lambda x : (x[1],x[0]))
            for j in range(len(check)) :
                temp.append(check[j][0])
                temp.append(check[j][1])
            if len(temp) >100 : temp=temp[:100]
            if max<len(temp) : max=len(temp)
            temp_all.append(temp)
        board=[[0]*max for _ in range(len(board))]

        for i in range(len(temp_all)) :
            for j in range(len(temp_all[i])) :
                board[i][j]=temp_all[i][j]
        col=max
    else :
        temp_all = []
        for i in range(col):
            check, temp_col = [], []
            for j in range(row):

                if [board[j][i]] not in check and board[j][i]!=0:
                    check.append([board[j][i]])
                temp_col.append(board[j][i])
            for j in range(len(check)):
                check[j].append(temp_col.count(check[j][0]))
            check.sort(key=lambda x: (x[1], x[0]))
            temp=[]
            for j in range(len(check)):
                temp.append(check[j][0])
                temp.append(check[j][1])
            if len(temp) > 100: temp = temp[:100]
            if max < len(temp): max = len(temp)
            temp_all.append(temp)
        board = [[0] * len(board[0]) for _ in range(max)]

        for i in range(len(temp_all)):
            for j in range(len(temp_all[i])):
                board[j][i] = temp_all[i][j]
        row = max
    t+=1

if t==101 : t=-1
print(t)


