try:
    with open("todolist.txt", "r") as f:
        r=f.read()
        result=len(r)
        print("The number of words in the file is:", result)
except Exception as e:  
    print("Error!!! :-\n", e)