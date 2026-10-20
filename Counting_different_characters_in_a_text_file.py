try:
    with open("todolist.txt", "r") as f:
        v=0
        u=0
        l=0
        v=0
        s=0
        d=0
        r=f.read()
        for i in r:
            if i.isupper():
                u+=1
            elif i.islower():
                l+=1
            elif i.isdigit():
                d+=1
            elif i.isspace():
                s+=1
            else:
                v+=1
    print("The number of uppercase letters is:", u)
    print("The number of lowercase letters is:", l)
    print("The number of digits is:", d)
    print("The number of spaces is:", s)
    print("The number of other characters is:", v)
except Exception as e:
    print("Error!!! :-\n", e)