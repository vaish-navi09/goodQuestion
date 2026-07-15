# MERGE TWO SORTED LIST
# a = [1,4,6,8]
# b = [2,3,5,7,9]
# c = []
# i = 0
# j = 0
# while i< len(a) and j< len(b):
#    if a[i] < b[j]:
#       c.append(a[i])
#       i+=1
#    else:
#       c.append(b[j])
#       j+=1
# while j < len(b):
#       c.append(b[j])
#       j += 1
# while i < len(a):
#       c.append(a[i])
#       i += 1
# print(c)

# PRIME NO. LIST

nums = [2,5,6,9,11,13,15,17]
prime = []

for i in range (len(nums)):
    if nums[i] == 2:
        prime.append(nums[i])
        continue
    isPrime = True
    for j in range(2,nums[i]):
        if nums[i]% j == 0:
             isPrime= False
             break
    if isPrime:
          prime.append(nums[i])

print(prime)       
