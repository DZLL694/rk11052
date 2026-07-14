tasks = []

while True:
    print("\n1. 添加任务")
    print("2. 查看任务")
    print("3. 删除任务")
    print("4. 退出程序")

    choice = input("请选择功能：")

    if choice == "1":
        task = input("请输入任务内容：")
        tasks.append(task)
        print("任务添加成功")

    elif choice == "2":
        if len(tasks) == 0:
            print("当前没有任务")
        else:
            for index, task in enumerate(tasks, start=1):
                print(index, task)

    elif choice == "3":
        for index, task in enumerate(tasks, start=1):
            print(index, task)

        number = int(input("请输入要删除的任务编号："))

        if 1 <= number <= len(tasks):
            tasks.pop(number - 1)
            print("任务删除成功")
        else:
            print("任务编号不存在")

    elif choice == "4":
        print("程序已退出")
        break

    else:
        print("输入错误，请重新选择")