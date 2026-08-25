#longest LENGTH CONTIGUOUS SUBARRAY sum = k 
nums=[10,5,2,7,1,9]
k=15
seen={0:-1}
longest = 0
pref_sum = 0
best_lis=[]
for i in range (len(nums)):
    pref_sum += nums[i]
    if pref_sum-k in seen:
        length = i-seen[pref_sum-k]
        if length > longest:
            longest= length 
            start = seen[pref_sum-k]+1
            best_lis = nums[start: i+1]
    if pref_sum not in seen:
            seen[pref_sum] = i
print(longest)
print(best_lis)


#COUNT SUBARRAY WITH SUM K 
nums = [1,2,3]
k = 3
count = 0
seen ={0:1}
pref_sum=0
for num in nums :
    pref_sum += num
    if pref_sum not in seen:
          seen[pref_sum] = 1
    else:
         seen[pref_sum] += 1
    if pref_sum-k in seen:
         count+= seen[pref_sum-k]

print("count=",count)

#longest consecutive sequence
nums = [100,4,200,1,3,2]
nums =set(nums)
longest= 0
lis=[]
for num in nums:
     if num-1 not in nums:
          curr = num
          length = 1

          while curr+1 in nums:
               curr+=1
               length += 1 
          if length > longest :
            longest = length
            lis= list(range(num, curr+1))
                    
print(longest,"length")
print(lis)

#subarray with equal 0s and 1s
nums= [0,1,0,1,1,0,0]
k= 0
seen={0:-1}
pref_sum = 0
lis =[]
longest = 0
for i in range (len(nums)):
     if nums[i] == 0:
          pref_sum -= 1
     else:
          pref_sum += 1
     if pref_sum in seen:
          length = i - seen[pref_sum]
          if length > longest:
               longest = length
               start = seen[pref_sum] + 1
               lis = nums[start: i+1]
     else:
               seen[pref_sum] = i
print(lis)
print(longest)

#lonegest SUBARRAY WITH EQUAL 0S 1S AND 2s
nums= [0,1,2,0,1,2,1,0]
count0= 0
count1= 0
count2= 0
longest=0
seen={(0,0):-1}
for i in range (len(nums)):
     if nums[i]== 0:
          count0+=1 
     elif nums[i]== 1:
          count1+= 1
     else:
          count2+= 1
     diff1 = count0-count1
     diff2 = count1-count2
     state=(diff1,diff2)
     if state in seen:
          length= i-seen[state]
          if length>longest:
               longest= length
     else:
          seen[state]=i 
print(longest)

#COUNT SUBARRAYS WITH XOR = K 
nums=[4,2,2,6,4]
k= 6
seen={0:1}
pref_xor = 0
count = 0
for num in nums:
     pref_xor ^= num
     if pref_xor not in seen:
          seen[pref_xor] = 1
     else:
          seen[pref_xor] += 1
     if pref_xor ^ k in seen:
          count += seen[pref_xor ^ k]
print(count, "count of xor")

#SUBARRAY MAX XOR
nums =[8,1,2,12,7,6]
max_xor = 0
prefix =[0]
curr_xor = 0
for num in nums:
     curr_xor ^= num
     for prev in prefix:
          sub = curr_xor ^ prev
          if sub > max_xor:
             max_xor = sub
     prefix.append(curr_xor)
print(max_xor,"max_xor")


# MAXIMUM SUBARRAY  SUM WITH ONE DELETION
nums = [1,-2,0,3]
pre_norm= 0
pre_dele = float("-inf")
curr_sum = 0
answer = float("-inf")
for num in nums:
     curr = num
     normal = max(curr_sum,pre_norm +curr)
     deleted = max(pre_norm, pre_dele + curr)

     answer = max(answer,normal, deleted)

     pre_norm = normal
     pre_dele = deleted
print(answer, "max sum with one del")

#maximum sum circular subarray
nums= [5,-3,5]
pre_max = 0
pre_min = 0
total = 0
sec_best= float("inf")
best =  float("-inf")
for num in nums :
     total += num
     curr = num 
     max_sum = max(curr , curr+ pre_max)
     best = max(best , max_sum)
     min_sum = min(curr, curr +pre_min)
     sec_best = min(sec_best, min_sum)

     pre_max = max_sum
     pre_min = min_sum
answer = total - sec_best
answer =max(answer, best)
print(answer)

#max LENGTH SUARRAY WITH SUM DIVISIBLE BY K 
nums = [2,7,6,1,4,5]
k = 3
seen = {0:-1}
pref_sum = 0
longest = 0
for i in range (len(nums)):
     pref_sum+= nums[i]
     if pref_sum % k in seen:
          length = i - seen[pref_sum % k]
          if length > longest:
               longest = length
     else:
          seen[pref_sum % k] = i 
print(longest, "max length divisible by k")


# LONGEST SUBARRAY WITH AT MOST K DISTInCT ELEMENTS
nums = [1,2,1,2,3]
k = 2
right = 0
left = 0
freq = {}
longest = 0

while right < len(nums):
     freq[nums[right]] = freq.get(nums[right],0) + 1
     while len(freq) > k:
          freq[nums[left]] -= 1
          if freq[nums[left]] == 0:
               del freq[nums[left]]
          left+= 1
     length = right-left +1
     if length> longest:
          longest = length
     right += 1
print(longest ,"longest at most k distinct ele")

# count subarrays with exactly k distinct elements
nums = [1,2,1,2,3]

def atmost(k):
     right = 0
     left = 0
     freq = {}
     count = 0
     while right < len(nums):
          freq[nums[right]]= freq.get(nums[right],0)+1
          while len(freq) > k:
               freq[nums[left]] -= 1
               if freq[nums[left]] == 0 :
                    del freq[nums[left]]
               left += 1
          length = right- left +1
          count += length
          right += 1
     return count 
exactly= atmost(2)- atmost(1)
print(exactly, "exactly k dis elem counts")


# MINIMUM WINDOW CONTAINING ALL VALUES
nums = [2,1,2,3,1,2,4]
target = [1,2,3]
right = 0
left = 0
freq = {}
formed = 0
req = len(target)
min_length = float("inf")
while right < len(nums):
     if nums[right] in target:
          freq[nums[right]] = freq.get(nums[right],0) +1
          if freq[nums[right]] == 1:
               formed += 1
               while formed == req :
                    length = right-left+1
                    if length < min_length:
                         min_length= length
                         start = left

                    if nums[left] in freq:
                       freq[nums[left]] -= 1
                       if freq[nums[left]]== 0:
                         del freq[nums[left]]
                         formed -= 1
                    left += 1
     right += 1
answer = nums[start: start+min_length]
print(answer,"mini number contain all ele of target")

#circular next grEATER ELE
nums = [1,2,1]    
answer = [-1,-1,-1]   
stack= []   
n = len(nums)     
for i in range (2*len(nums)):
     index = i% n
     curr = nums[index]
     while stack and curr > nums[stack[-1]]:
          wait_index = stack.pop()
          answer[wait_index] = curr
     if i < len(nums):
          stack.append(index)
print(answer,"circular next great")

#median from data stream-two heap
import heapq
nums = [5,2,8,1,7]
small = []
large = []
for curr in nums:
     if not small:
          heapq.heappush(small,-curr)
     elif curr < -small[-1]:
          heapq.heappush(small, -curr)
     else:
          heapq.heappush(large,curr)
     if len(small) - len(large) > 1:
          value= -heapq.heappop(small)
          heapq.heappush(large, value)
     if len(large) - len(small) > 1:
          value = heapq.heappop(large)
          heapq.heappush(small, value)
     if len(large)==len(small):
          median= (-small[0] + large[0])/2
     if len(large)- len(small) == 1:
          median = large[0]
     if len(small) - len(large) == 1:
          median = -small[0]
print(median,"mid value of random array")


# longest subarray with sum <= k
nums = [2,1,3,2,1]
right = 0
left = 0
total = 0
longest = 0
k = 5
while right < len(nums):
     total += nums[right]
     while total > k :
          total -= nums[left]
          left += 1
     length = right - left + 1
     if length > longest :
          longest = length
     right += 1
print(longest,"len of longest sum less than k")






     
    
    





    