# text = input("enter the txt:")
# word = text[: : -1]
# if word == text :
#     print("palindrom")
# else:
#     print("not a palindrom")

import random
secret = random.randint(1,50)
count = 0
while True:
    guess = int(input("enter the num:"))
    count += 1
    if guess > secret:
        print("too high")
    elif guess < secret:
        print("too low")
    else:
        print("correct")
        break
    print(count)
    if count <= 5:
        print("excelent")
    elif count > 5 and count<10:
        print("good")
    else:
        print("keep trying")
    


