a=int(input("1. Show students\n2. Add student\n3. Update student\n4. Delete student\n5. Exit\n\n"))

if a == 1:
    with open("data.txt", "r") as file:
        print(file.read())

elif a == 2:
    with open("data.txt", "a") as file:
        name = input("Name:")
        age = input("Age:")
        file.write(f"\n{name + " " + age}")
        

elif a == 3:
    updated_data=[]

    v = input("Isert the name that you want to change: ")
    c=input("Name: " )
    age=input("Age: ")

    with open("data.txt", "r") as file:
        lines = file.readlines()

        for line in lines:
            name= line.split()[0]

            if name == v:
                updated_data.append(c +" "+ age)
            else:
                updated_data.append(line)
    
    with open("data.txt", "w") as file:
        file.writelines(updated_data)



