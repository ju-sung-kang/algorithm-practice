n=int(input())
nums=list(map(int, input().split()))

max_sum = nums[0]
cur_sum = nums[0]
for i in range(1,n):
    cur_sum = max(cur_sum+nums[i], nums[i])
    max_sum = max(max_sum, cur_sum)
print(max_sum)
