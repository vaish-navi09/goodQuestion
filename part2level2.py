# two sum _ sorted array
nums = [1,2,4,6,8,9,11]
start= 0
end = len(nums)-1
target= 15
while start<= end:
     if nums[start]+nums[end]> target:
          end -= 1
     elif nums[start]+ nums[end]< target:
          start += 1
     else:
          print(start,end ,"index of sum of target value")
          break
     #longest subarray with sum<= k
nums = [2,1,5,1,3,2]
k = 7
right = 0
left = 0
longest = 0
total = 0
while right < len(nums):
     total += nums[right]
     while total > k:
         total -= nums[left]
         left += 1
     length = right-left +1
     if length > longest:
          longest = length
     right += 1
print(longest)

# longest substring without repeating chaar
s = "abcabcbb"
seen = set()
right = 0
left = 0
length = 0
while right< len(s):
     while s[right] in seen:
          seen.remove(s[left])
          left += 1
     seen.add(s[right])
     length = max(length, len(seen))
     right += 1
print(length)
# mini size subarray sum 
nums = [2,3,1,2,4,3]
target = 7
right = 0
left = 0
total = 0
smallest = float('inf')
while right < len(nums):
     total += nums[right]
     while total >= target :
               length = right - left +1
               if length < smallest:
                    smallest = length
               total -=nums[left]
               left += 1
     right += 1
print(smallest)
     

     





     