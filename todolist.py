try:
    f = open("todolist.txt", "w")

    n = int(input("Enter the number of inputs: "))

    for i in range(n):
        el = input(f"{i + 1}. Enter the work: ")
        f.write(el + "\n")

    print("All the works have been written!")

    f.close()

except Exception as e:
    print("Error!!! :-\n", e)
    f.close()


try:
    f = open("todolist.txt", "r")

    result = f.readlines()

    print("Your Entries:")

    print(result)

    f.close()

except Exception as e:
    print("Error!!! :-\n", e)