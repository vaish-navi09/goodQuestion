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

# nums = [2,5,6,9,11,13,15,17]
# prime = []

# for i in range (len(nums)):
#     if nums[i] == 2:
#         prime.append(nums[i])
#         continue
#     isPrime = True
#     for j in range(2,nums[i]):
#         if nums[i]% j == 0:
#              isPrime= False
#              break
#     if isPrime:
#           prime.append(nums[i])

# print(prime)       

# word = ["eat","tea","tan","ate","nat","bat"]
# new_word = []
# visited = []
# for i in range(len(word)):
#     if word[i] not in visited:
#         lis = []
#         lis.append(word[i])
#         for j in range(i+1,len(word)):
#             if sorted (word[i]) ==sorted (word[j]):
#                 lis.append(word[j])
#                 visited.append(word[i])
#                 visited.append(word[j])
            
#         if lis :
#             new_word.append(lis)       

# print(new_word)


# interval = [[1,3],[2,6],[8,10],[15,18]]
# new_interval = sorted(interval)
# merge= []    #[1,3]     [1,6]
# merge.append(new_interval[0])
# for i in range(1,len(new_interval)):
#     if merge[-1][1] >= new_interval[i][0]:
#         merge[-1][1] =max(merge[-1][1],new_interval[i][1])
#     else:
#         merge.append(new_interval[i])
    
# print(merge)

# str = "abcbcde"
# max_len = 0
# lis = []
# for ch in str:
#     if ch not in lis:
#         lis.append(ch)
#     else:
#         while ch in lis:
#             lis.pop(0)
#         lis.append(ch)
#     max_len = max(max_len,len(lis))
# print(max_len)
    
#second most frequent word 

# text = "apple banana apple mango banana apple mango"
# text = text.split()
# text = list(text)
# freq ={}
# for ch in text:
#     if ch in freq :
#         freq[ch] += 1
#     else:
#         freq[ch] = 1

# print(freq)
# new_text = sorted(freq.items(), key= lambda item : item[1])

# for i in range(len(new_text)):
#    if new_text[i][1] == new_text[-2][1]:
#     print(new_text[i][0],",", new_text[-2][0])
#     break

#    else:
#       print(new_text[-2][0])


      # LONGEST SEQUENCE USING SET
# nums = [100,4,200,5,6,7,8]
# nums = set(nums)
# longest = 0
# for num in nums:
#     if num -1 not in nums:
#         current = num
#         length = 1
#         while current+1 in nums:
#             current += 1
#             length += 1
#         longest = max(longest,length)
# print(longest)


# text = "programming"
# freq = {}
# for ch in text:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] = 1

# new_text = sorted(freq.items(),key = lambda iteam : iteam[1] , reverse= True)
# print(new_text)

# new = []
# for i in range(len(new_text)):
#     for j in range(new_text[i][1]):
#         new.append(new_text[i][0])
     
# print("".join(new))
    
# nums = [1,1,1,2,2,3,3,3,4]
# freq= {}
# for num in nums:
#     if num in freq:
#         freq[num] += 1
#     else:
#         freq[num] = 1
# new_num = sorted(freq.items(),key= lambda iteam : iteam[1], reverse = True)

# numx =[]
# for i in range(2):
#     numx.append(new_num[i][0])
# print(numx)
    
# nums = [4,5,2,10,8]
# new_num= []

# for i in range(len(nums)):
#     found = False
#     for j in range(i+1,len(nums)):
#         if nums[i]< nums[j]:
#             found = True
#             new_num.append(nums[j])
#             break
#     if not found:
#             new_num.append(-1)
# print(new_num)


# nums = [1,2,2,4,5,6]
# freq= {}
# for num in nums:
#     if num in freq:
#         freq[num] += 1
#     else:
#         freq[num] = 1

# for key ,value in freq.items():
#     if value > 1:
#         print("duplicate:", key)

# for numx in range(1,len(nums)+1):
#     if numx not in freq: 
#         print("missing:", numx)
    

nums = [10,5,2,7,1,9]
total= 15
length = 0
new_sum = 0
lis =[]
best_lis =[]
for i in range(len(nums)):
    new_sum = new_sum + nums[i]
    lis .append(nums[i])
    while new_sum > total:
       new_sum = new_sum-lis[0]
       lis.pop(0)
    
    if new_sum == total:
        if len(lis) > length:
            length = len(lis)
            best_lis = lis.copy()
print(length)
print(best_lis)
  
    
    











