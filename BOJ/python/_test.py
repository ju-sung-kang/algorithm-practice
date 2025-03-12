n = list(map(int, input().split()))
k=0
for j in n:
  if j>k:
    k=j
i=n.index(k)
print("*",k)
print("*",i+1)