try:
    f= open("todolist.txt", "r")
    r=f.readlines()
    for i in range(len(r)):
        print(f"{i+1}. {r[i].strip()}")
        f.close()
except Exception as e:
    print("Error!!! :-\n", e)
    f.close()