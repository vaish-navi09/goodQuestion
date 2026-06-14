# Arrange  acc to marks

# marks = {"A":85,"B": 95, "C":75}
# data = []
# for name in marks:
#     data.append([marks[name], name]) 
# print(data) 
# data.sort(reverse= True)
# for name,score in data :
#     print(name , score)
tasks = []
def add_task () :
    task = input("enter your task")
    tasks.append(task)
    print("task added")

def view_task():
    for task in tasks:
        print(task)
def remove_task():
     task = input("enter the task to remove")
     if task in tasks:
         tasks.remove(task)
         print("task remove")
     else:
         print("can't have task")

while True:
    print("1. add task")
    print("2.view task")
    print("3. remove task")
    print("4.exit")

    choice = input("enter your choice")
    if choice == "4":
        print("Goodbye!")
        break
    if choice == "1":
        add_task()
    elif  choice == "2":
        view_task()
    elif choice == "3":
        remove_task()
    else:
        print("invalid")