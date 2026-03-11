while True:

    a=int(input("1. Show students\n2. Add student\n3. Update student\n4. Delete student\n5. Exit\n\n"))

    if a == 1:
        with open("data.txt", "r") as file:
            print(file.read())

    elif a == 2:
        with open("data.txt", "a") as file:
            name = input("Name:")
            age = input("Age:")
            file.write(f"{name + "," + age}\n")
            

    elif a == 3:
        updated_data=[]

        v = input("Isert the name that you want to change: ")
        c=input("Name: " )
        age=input("Age: ")

        with open("data.txt", "r") as file:
            lines = file.readlines()

            for line in lines:
                eq = line.strip().split(",")[0]

                if eq == v:
                    updated_data.append(f"{c +","+ age}\n")
                else:
                    updated_data.append(line)
        
        with open("data.txt", "w") as file:
            file.writelines(updated_data)

    elif a == 4:

        nn=input("Who do you want to delete: ")

        with open("data.txt", "r") as file:
            lines=file.readlines()
            

        with open("data.txt", "w") as file:
            for line in lines:
                dn = line.strip().split(",")
                if dn[0] != (nn):
                    file.write(line)

    elif a == 5:
        break
