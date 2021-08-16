arr = []
ans=0
for _ in range(8):
    arr.append(list(map(str, list(input()))))
    #한줄한줄 받아와서 리스트에 저장!

for i in range(8):
    for j in range(8):
        if (j+i)%2 == 0:
            if arr[j][i] == 'F':
                ans+=1

print(ans)