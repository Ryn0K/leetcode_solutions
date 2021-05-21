nums = [0,2,3,5,6]
target = 11
for i in range(0,len(nums)):
    for j in range(0,len(nums)):
        if(nums[i]+nums[j] == target and (j>i)):
            print(f"[{i},{j}]")
            break