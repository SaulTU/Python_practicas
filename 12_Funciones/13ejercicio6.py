def media(*nums):
    a=1
    for i in nums:
        a+=i
    b=float(a/len(nums))
    return b

print(media(2,3,4,10,20))
