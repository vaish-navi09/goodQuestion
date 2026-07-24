# student={"A":[80,75,90],
#          "B":[60,85,70],
#          "C":[95,92,88]
#          }
# lis ={}
# for name , marks in student.items():
#     sum = 0
#     for mark in marks:
#         sum = sum + mark
#     avrg= sum / len(marks)
#     lis[name] = avrg

#     print(name,"=",avrg)
# max_avrg = max(lis, key=lis.get)
# print("highest avrg student:",max_avrg,"-",lis[max_avrg])

# text = "aabbcdee"
# freq = {}
# for ch in text:
#           if ch  in freq:
#                  freq[ch] += 1
#           else:
#                  freq[ch] = 1
# found = False                 
# for char,value in freq.items():
#       if value == 1:
#             print(char,":first unique char")
#             found = True
#             break
# if  not found:
#             print("no unique char")

# nums = [3,0,1,4,5,6,7,9,2]
# n = len(nums)
# def n_sum(n):
#     return n*(n+1)/2
# total = 0
# for i in range(len(nums)):
#     total = total+ nums[i]
# print(n_sum(n)-total, ":missing NO")

# nums = [1,4,20,3,10,5]
# lis = []
# sum = 33
# total = 0 
# best_lis = []
# length = 0
# for i in range(len(nums)) :
#     total = total+nums[i]
#     lis.append(nums[i])

#     while total > sum:
#         total= total -lis[0]
#         lis.pop(0)
    

#     if total == sum:
#         if len(lis) > length:
#             length = max(length, len(lis))
#             best_lis= lis.copy()
# print(length)
# print(best_lis)

# nums = [16,17,4,3,5,2]
# lis = []
# lis.append(nums[-1])
# for i in range(len(nums)-2,-1,-1):
    
#     if max(lis) < nums[i]:
#         lis.append(nums[i])
        

# print(lis)

# nums = [2,2,1,1,1,2,2]
# n = len(nums)/2
# freq = {}
# for ch in nums:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] = 1
# for chrs , value in freq.items():
#      if value > n :
#          print(chrs ,":majority element")

# nums = [2,3,-2,4]
# max_pro = nums[0]
# lis = []
# for i in range (len(nums)) :
#     pro = 1
#     for j in range(i,len(nums)):
#         pro = pro* nums[j]

#         if max_pro< pro:
#          max_pro = pro
#          lis = nums[i:j+1].copy()
# print(max_pro)
# print(lis)

          
# nums=[0,1,0,3,12,0,5] 
# point= 0
# for i in range(point,len(nums)):
#     if nums[i]!= 0 :
#         nums[point]= nums[i]
#         point +=1
# for i in range(point,len(nums)):
#       nums[i]= 0
# print(nums)

# interval = [[1,3],[2,6],[8,10],[9,12]]
# interval = sorted(interval)
# lis =[]
# merge=[]
# merge.append(interval[0])
# for j in range(1,len(interval)):
#           if merge[-1][1] > interval[j][0]:
#                merge[-1][1]= max(merge[-1][1],interval[j][1])
              
#           else:
#                merge.append(interval[j])
# lis.append(merge)
# print(lis)          


nums = [0,1,0,0,1,1,0]
prefix_sum = 0
length = 0
lis =[]
seen= {0:-1}
for i in range (len(nums)):
       if nums[i]== 0:
              prefix_sum -= 1
       else:
              prefix_sum += 1
       if prefix_sum in seen:
              length = max (length , i-seen[prefix_sum])
       else:
              seen[prefix_sum] = 1
print(length)
       
       



    

  

   

    




