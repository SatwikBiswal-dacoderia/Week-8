try:
    f=open("todolist.txt", "r")
    r=f.read()
    str=input("Enter the word to be searched: ")
    if str in r:
        print("The word exists in the file.")   
    else:
        print("The word does not exist in the file.")   
except Exception as e:
    print("Error!!! :-\n", e)
    f.close()