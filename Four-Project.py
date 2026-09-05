Tasks=[]
print("📃Welcome to the To_Do List App! ")

while True:
    print("--------------------")
    print("Choose an option: ")
    print("1: Add Task ")
    print("2: View Tasks ")
    print("3: Delete Task ")
    print("4: Exit ")
    print("--------------------")

    choice = input("Enter your choice (1-4) : ")

    if choice == "1":
        # نطلب من المستخدم انه يدخل مهمة
        value = input("Enter a task : ")
        Tasks.append(value)    
        print("✔ Task Added")

    # عرض كل المهام
    elif choice == "2":    
        # لو القائمة فاضية
        if not Tasks:
            print("No tasks yet ")
        else:    
            # 1 task1
            # 2 task2
            # 3 task3
            print("Your tasks ")
            i = 1
            for data in Tasks:
                print(i,data)
                i+=1
    # delete task
    elif choice == "3":
        # أولا:نتحقق اذا كان في مهام أصلا 
        if not Tasks:
            print("No Tasks to delete : ")
        else:
         # عرض المهام بالارقام عشان يختار منها
            i = 1
            print("Your tasks : ")
            for data in Tasks:
                print(i, data)
                i+=1    
             # نطلب من المستخدم يكتب رقم المهمة اللي عايز يحذفها            
            task_number=int(input("Enter Task number to delete : "))

        if task_number>=1 and task_number<=len(Tasks):
           deleted = Tasks.pop(task_number-1)
           print(f"deleted Task is {deleted}") 
        else:
            print("Invalid Value ")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice : Try again ")    