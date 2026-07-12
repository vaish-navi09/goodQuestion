# text = input("enter the txt:")
# word = text[: : -1]
# if word == text :
#     print("palindrom")
# else:
#     print("not a palindrom")

# import random
# secret = random.randint(1,50)
# count = 0
# while True:
#     guess = int(input("enter the num:"))
#     count += 1
#     if guess > secret:
#         print("too high")
#     elif guess < secret:
#         print("too low")
#     else:
#         print("correct")
        
#         print(count)
#         break
#     if count <= 5:
#         print("excelent")
#     elif count > 5 and count<10:
#         print("good")
#     else:
#         print("keep trying")


# nums = [12,45,7,34,89,56]
# lar = nums[0]
# sec_lar = nums[0]
# for val in nums [1:]:
#     if lar < val:
#         sec_lar = lar
#         lar = val
#     elif sec_lar < val :
#         sec_lar = val
# print("second largest" ,sec_lar)

# nums = [10,20,30,40,50]
# temp = nums[0]
# for i in range(len(nums)-1):
#     nums[i] = nums[i+1]
# nums[-1] = temp
# print(nums)


# nums = [3,1,4,1,5,9,2]
# for j in range(len (nums)):
    
#     for i in range (j+1,len(nums)):
#         if nums[j] + nums[i] == 5 :
#             print((nums[j], nums[i]))

# nums = [10 ,5,8,7,8]
# # nums = (list(set(nums)))   another method 
# print(nums)
# lar = float("-inf")
# sec_lar = float("-inf")
# for num in nums:
#     if num > lar :
#         sec_lar = lar
#         lar  = num
#     elif num > sec_lar and sec_lar != lar  :
#         sec_lar = num
    
# print("second_lar:", sec_lar)


# text = "python programming is very interesting"
# length = float("-inf")
# longest = " "
# longest_word = []

# words = text.split()
# for word in words:
#     if len(word) > length:
#         length = len(word)
#         longest_word = []
#         longest_word.append(word)
#     elif len(word) == length:
#         longest_word.append(word)
# print(longest_word)



# nums = [2,3,4,5]
# new_num = []

# for i in range(len(nums)) :
#     pro = 1
#     for j in range(len(nums)):
#       if i == j :
#          continue
#       pro = pro * nums[j]
#     new_num.append(pro)
# print(new_num)   


nums = [1,2,3,7,8,10,11,12,13]
max_length = 1       
length = 1        
for i in range (len(nums)-1):
  if  nums[i+1]- nums[i] == 1:
    length+= 1
  else:
      length = 1
  if length> max_length:
   max_length = length 
print("longest consecutive sequence",max_length)



    
