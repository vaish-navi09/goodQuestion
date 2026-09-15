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
print(longest, "longest subarray atmost k")

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
print(length, "with repe longest substring")
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
print(smallest,"mini size subarray")


#longest sequence consecutive with one deletion


nums = [1,1,0,1,1,1,0,1]
right = 0
left = 0
maximum = 0
zeros= 0
while right < len(nums):
     if nums[right] == 0:
          zeros += 1
          while zeros > 1:
               if nums[left] == 0:
                    zeros -= 1
               left += 1
     length = right - left + 1
     if length > maximum :
          maximum = length
     right += 1
print(maximum - 1,"with one del longest consecutive")


#at most 2 distint values 
nums = [1,2,1,2,3,2,2]   
freq = {}         
right = 0
left = 0
longest = 0
while right < len(nums):
     freq[nums[right]]  = freq.get(nums[right],0)+ 1
     while len(freq)> 2:
          freq[nums[left]] -= 1
          if freq[nums[left]] == 0:
               del freq[nums[left]]
          left += 1
     length = right-left +1
     if length > longest:
           longest = length
     right += 1
print(longest,"at most two distint value")

# maximum points from cards only k card
cards = [1,2,3,4,5,6,1]
n = len(cards)
k = 3
window = n-k
total = sum(cards)
curr = sum(cards[:window])
minimum = curr
right = window
left = 0
while right < n:
     curr += cards[right]
     curr -= cards[left]
     if curr < minimum:
          minimum = curr 
     left += 1
     right += 1
print(total - minimum,"max sum of k cards")



# INTERVAL PROBLEMS
interval = [[1,3],[2,6],[8,10],[9,12]]
interval = sorted(interval)
merge = []
merge.append(interval[0])
for i in range(1,len(interval)):
    if merge[-1][1] >= interval[i][0]:
        merge[-1][1] = max(interval[i][1],merge[-1][1])
    else:
        merge.append(interval[i])
print(merge)
        
interval = [[1,3],[6,9]]
newInterval = [2,5]
interval = sorted(interval)
for i in range (len(interval)):
    if interval[i][1]>newInterval[0]:
        interval[i][1] = max(interval[i][1],newInterval[1])
print(interval)

interval =[[1,2],[2,3],[3,4],[1,3]]
interval =sorted(interval)
last_end= interval[0][1]
count = 0
for i in range(1,len(interval)):
    if last_end > interval[i][0]:
        count += 1
        if last_end > interval[i][1]:
            last_end= interval[i][1]
print(count,"interval to remove")

interval = [[0,30],[5,10],[15,20]]
start_time =[]
end_time =[]
for i in range (len(interval)):
    start_time.append(interval[i][0])
    end_time.append(interval[i][1])
start_time.sort()
end_time.sort()
room = 0
end = 0
start= 0
maxiroom = 0
while start <len(start_time) and end < len(end_time):
    if start_time[start]<end_time[end]:
        room +=1
        start += 1
        if maxiroom< room:
            maxiroom = room
            
    else:
        room -= 1
        end += 1
print(room,"maximum room")



#stack problem

#valid parenthese
s = "({[]})"  
lis =[]
value = True
for i in range (len(s)):
    if s[i] in "({[":
        lis.append(s[i])
    else:
        if not lis :
            value = False
        x = lis.pop()
        if (x =="["and s[i] == "]") or (x =="{"and s[i] =="}")or (x =="("and s[i]==")"):
      
          continue
        else:
          value = False
        if lis:
           value = False
print(value)
# remove adjavent duplicate
s= "abbaca"
lis = []
for i in range(len(s)):
    if not lis:
       lis.append(s[i])
    elif lis[-1] != s[i]:
       lis.append(s[i])
    else:
       lis.pop()
print("".join(lis))
# greater number from in right
nums = [2,1,5,3,4]
answer = [-1]*len(nums)
stack = []
for i in range (len(nums)):
   while stack and nums[stack[-1]] < nums[i]:
      index = stack.pop()
      answer[index] = nums[i]
   stack.append(i)
print(answer)
   
#days we get max temprature
temp = [73,74,75,71,69,72,76,73]
stack = []
answer = [0]*len(temp)
for i in range (len(temp)):
   while stack and temp[stack[-1]] < temp[i]:
      index = stack.pop()
      answer[index] = i - index
   stack.append(i)
print(answer)

           
# koko eating bananas minimum eating speed
piles = [3,6,7,11]
h = 8 
i = 1
j = max(piles)

while i <= j  :
   mid = (i+j)// 2   
   hour = 0
   for pile in piles:
      hour += (pile+ mid -1)// mid
   if hour<= h:
      j = mid -1
   else:
      i = mid +1
print(i,"mini speed koko eat bananas")


# ship package within D days
weights =[1,2,3,4,5,6,7,8,9,10]
days = 5
left = max(weights) # 10
right = sum(weights) # 55
while left <= right :
   mid = (left+right)// 2
   day = 1
   total =0
   for weight in weights:
      if total +weight <= mid:
         total+= weight
      else:
         day += 1
         total = weight
      if day < days:
         right = mid - 1
      else:
         left = mid+ 1
print(left)
      


stalls = [1,2,4,8,9]
k = 3
left = 1
right = max(stalls)-min(stalls)
while left<= right:
   mid = (left+right)// 2 
   count = 1
   last = stalls[0]
   for stall in stalls[1:]:
      if stall-last >= mid:
         count += 1
         last = stall
   if count >= k:
         left = mid +1
   else:
         right = mid -1
print(right)  

heights =[2,1,5,6,2,3]
heights.append(0)
stack =[] # greater length heights index
max_area = 0
for i in range(len(heights)):
     while stack and heights[stack[-1]] > heights[i]:
         index = stack.pop()
         height = heights[index]
         if stack:
             width = i - stack[-1] -1
         else:
             width = i
         area = height * width
         max_area = max(area, max_area)
     stack.append(i)
print(max_area,"max rectangle ")
   
 # pair with given difference          
nums =[1,3,5,8,12] 
k = 7
left = 0
right = len(nums)-1
while left< right:
    if nums[right]-nums[left]>k:
        right -= 1
    elif nums[right]-nums[left]<k:
        left += 1
    else:
        print(True) 
        break
else:
    print(False)     

# container with most water
height= [1,8,6,2,5,4,8,3,7]
left = 0
max_water = 0
right = len(height)-1
while left<right:
    if height[left]<height[right]:
        heigh = height[left]
        width = right-left
        water = heigh*width
        left += 1
    else:
        heigh = height[right]
        width = right-left
        water = heigh * width
        right -= 1
    if water > max_water:
        max_water = water
print(max_water,"most water contain")

# 3Sum equal zero
nums =[-1,0,1,2,-1,-4]
nums = sorted(nums)   # -4,-1,-1,0,1,2
result = []
for fixed in range(len(nums)-2):
    left = fixed+1
    right = len(nums)-1
    if fixed > 0 and nums[fixed] == nums[fixed-1]:
        continue
    while left<right:
        if nums[fixed]+nums[left]+nums[right]> 0:
            right -= 1
        elif  nums[fixed]+nums[left]+nums[right]< 0:
            left += 1
        else:
             result.append([nums[right],nums[left],nums[fixed]])
             left += 1
             right -= 1
             while left < right and nums[left]==nums[left-1]:
                 left += 1
             while left< right and nums[right] == nums[right+1]:
                 right -= 1

print(result)

# Trapping rain water
height = [0,1,0,2,1,0,1,3,2,1,2,1]
left = 0
right = len(height)-1
max_left = height[left]
max_right = height[right]
water = 0
while left< right:
    if height[left]< height[right]:
        max_left = max(max_left,height[left])
        water +=  max_left-height[left]
        left += 1
    else:
        max_right = max(max_right, height[right])
        water += max_right-height[right]
        right -= 1
print(water)
         

nums = [100,4,200,1,3,2]
nums = sorted(nums)
max_length = 0
for num in nums :
    if num-1 not in nums:
        curr = num
        length = 1
        while curr+1 in nums:
            length += 1
            curr += 1
        if max_length< length:
            max_length = length
print(max_length,"longest consecutive seq")

# product of array except itself
nums =[1,2,3,4]
pre =[]

num =[]
pre.append(1)
pro = 1
for i in range(len(nums)-1):
    pro = nums[i]*pre[-1]
    pre.append(pro)
pro = 1
suff =[]
for i in range(len(nums)-1,-1,-1):
    suff.append(pro)
    pro = pro*nums[i]
suff.reverse()
for i in range(len(nums)):
    num.append(pre[i]*suff[i])
print(num,"product of array except itself")

# find dublicate number:
nums =[1,3,4,2,2]
slow = nums[0]
fast = nums[0]
while True:
    slow = nums[slow]
    fast = nums[nums[fast]]
    if slow == fast:
        break
slow =nums[0]
while slow!= fast:
        slow = nums[slow]
        fast = nums[fast]
print(slow,"duplicate")

# rotate array
nums =[1,2,3,4,5,6,7]
k = 3
def rotate_part(nums,left,right):
    while left < right:
        nums[left] , nums[right] = nums[right],nums[left]
        left += 1
        right -= 1
rotate_part(nums,0,len(nums)-1)
rotate_part(nums,0,k-1)
rotate_part(nums,k,len(nums)-1)
print(nums) 

    
         

   






     