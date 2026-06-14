# text = " racecar"
# word = text.split()
# new_text = []
# for wor in word:
#     y = wor[: : -1]
#     new_text.append(y)
# print (" " .join(new_text))


# CALCULATOR 
# def add(a,b) :
#     return a+b
# def sub(a,b):
#     return a-b
# def mulp(a,b):
#     return(a*b)
# def divide(a,b):
#     return a/b
# def power(a,b):
#     return a**b

# while True:
#     print("1. add")
#     print("2. sub")
#     print("3. mulp")
#     print("4. divide")
#     print("5. power")
#     print("6. exit")


#     choice = input("entre your choice")
#     if choice == "6":
#      break
#     a = int(input("entre the number"))
#     b = int(input("entre the 2nd number"))

#     if choice == "1":
#         print(add(a,b))
#     elif choice == "2":
#         print(sub(a,b))
#     elif choice == "3":
#         print(mulp(a,b))
#     elif choice == "4":
#         if b == 0:
#             print("can't divide by zero")
#         else:
#           print(divide(a,b))
#     elif choice == "5":
#         print(power(a,b))
#     else:
#         print("invalid choice")


# nums = [1,2,2,3,4,4,5]
# y = set(nums)
# z = list(y)
#print(z)

# x= (input("enter the number:"))
# print(len(x))

# val = [10, 5, 50, 20, 25]
# val.sort()
# print(val)
# print(val[len(val)-1])
 
# text = "Hello World"
# upper = 0
# lower = 0
# for ch in text :
#    if ch.isupper():
#     upper += 1
#    elif ch.islower():
#      lower += 1
# print(upper)
# print(lower)

# sent = "Python is very easy to learn"   
# freq = {}
# data = sent.split()
# for val in data:
#     length = len(val)
#     if length in freq :
#         freq[length] += 1
#     else:
#         freq[length] = 1
# print(freq)

# with open ("notes.txt", "w") as f:
#     f.write("Hello , Vaish \n welcome to the world")
# with open ("notes.txt","r") as f:
#     data = f.read()
#     print(data)

