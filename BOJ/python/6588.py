import math
import sys

N=10**6
is_prime=[True]*(N+1)
is_prime[0],is_prime[1]=False,False
prime_list=[]

i=2
while i*i<=N:
    if is_prime[i]:
        # i의 배수는 is_prime[]=False
        for mul in range(i*i,N+1,i):
            is_prime[mul]=False
    i+=1

for x in range(2,N+1):
    if is_prime[x]:
        prime_list.append(x)

def guess(n):
    for x in prime_list:
        if is_prime[n-x]:
            return f'{n} = {x} + {n-x}'
        if x > n//2:
            return "Goldbach's conjecture is wrong."

ans=[]
while True:
    x=int(sys.stdin.readline())
    if x==0:
        break
    ans.append(guess(x))

sys.stdout.write("\n".join(ans)+'\n')