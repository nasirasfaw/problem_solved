n = int(input())

nums = list(map(int, input().split()))

count = 0
for i in range(1, len(nums)):
    if nums[i] > max(nums[:i]) or nums[i] < min(nums[:i]):
        count += 1

print(count)
