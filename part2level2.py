# # two sum _ sorted array
# nums = [1,2,4,6,8,9,11]
# start= 0
# end = len(nums)-1
# target= 15
# while start<= end:
#      if nums[start]+nums[end]> target:
#           end -= 1
#      elif nums[start]+ nums[end]< target:
#           start += 1
#      else:
#           print(start,end ,"index of sum of target value")
#           break
#      #longest subarray with sum<= k
# nums = [2,1,5,1,3,2]
# k = 7
# right = 0
# left = 0
# longest = 0
# total = 0
# while right < len(nums):
#      total += nums[right]
#      while total > k:
#          total -= nums[left]
#          left += 1
#      length = right-left +1
#      if length > longest:
#           longest = length
#      right += 1
# print(longest, "longest subarray atmost k")

# # longest substring without repeating chaar
# s = "abcabcbb"
# seen = set()
# right = 0
# left = 0
# length = 0
# while right< len(s):
#      while s[right] in seen:
#           seen.remove(s[left])
#           left += 1
#      seen.add(s[right])
#      length = max(length, len(seen))
#      right += 1
# print(length, "with repe longest substring")
# # mini size subarray sum 
# nums = [2,3,1,2,4,3]
# target = 7
# right = 0
# left = 0
# total = 0
# smallest = float('inf')
# while right < len(nums):
#      total += nums[right]
#      while total >= target :
#                length = right - left +1
#                if length < smallest:
#                     smallest = length
#                total -=nums[left]
#                left += 1
#      right += 1
# print(smallest,"mini size subarray")


# #longest sequence consecutive with one deletion


# nums = [1,1,0,1,1,1,0,1]
# right = 0
# left = 0
# maximum = 0
# zeros= 0
# while right < len(nums):
#      if nums[right] == 0:
#           zeros += 1
#           while zeros > 1:
#                if nums[left] == 0:
#                     zeros -= 1
#                left += 1
#      length = right - left + 1
#      if length > maximum :
#           maximum = length
#      right += 1
# print(maximum - 1,"with one del longest consecutive")


# #at most 2 distint values 
# nums = [1,2,1,2,3,2,2]   
# freq = {}         
# right = 0
# left = 0
# longest = 0
# while right < len(nums):
#      freq[nums[right]]  = freq.get(nums[right],0)+ 1
#      while len(freq)> 2:
#           freq[nums[left]] -= 1
#           if freq[nums[left]] == 0:
#                del freq[nums[left]]
#           left += 1
#      length = right-left +1
#      if length > longest:
#            longest = length
#      right += 1
# print(longest,"at most two distint value")

# # maximum points from cards only k card
# cards = [1,2,3,4,5,6,1]
# n = len(cards)
# k = 3
# window = n-k
# total = sum(cards)
# curr = sum(cards[:window])
# minimum = curr
# right = window
# left = 0
# while right < n:
#      curr += cards[right]
#      curr -= cards[left]
#      if curr < minimum:
#           minimum = curr 
#      left += 1
#      right += 1
# print(total - minimum,"max sum of k cards")



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

     





     