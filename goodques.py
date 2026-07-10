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


nums = [3,1,4,1,5,9,2]
for j in range(len (nums)):
    
    for i in range (j+1,len(nums)):
        if nums[j] + nums[i] == 5 :
            print((nums[j], nums[i]))


