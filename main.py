a = list(input())
ans=0
a.remove(" ")
for i in a:
    ans+=int(i)

print(ans)