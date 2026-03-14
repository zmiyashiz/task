while True:

    a=int(input("1. Show students\n2. Add student\n3. Update student\n4. Delete student\n5. Exit\n\n"))

    if a == 1:
        with open("data.txt", "r") as file:
            print(file.read())

    elif a == 2:
        with open("data.txt", "a") as file:
            id = input("ID: ")
            first_name = input("Name:")
            surname = input("Surname:")
            age = input("Age:")
            email = input("Email: ")
            phone_number = input("Phone number: ")

            file.write(f"{id + "," + first_name + "," + surname +"," + age + "," + email + "," + phone_number}\n")
            

    elif a == 3:
        updated_data=[]

        v = input("Insert the name that you want to change: ")
        
        id1 = input("ID: ")
        first_name1 = input("Name:")
        surname1 = input("Surname:")
        age1 = input("Age:")
        email1 = input("Email: ")
        phone_number1 = input("Phone number: ")

        with open("data.txt", "r") as file:
            lines = file.readlines()

            for line in lines:
                eq = line.strip().split(",")[1]

                if eq == v:
                    updated_data.append(f"{id1 + "," + first_name1 + "," + surname1 +"," + age1 + "," + email1 + "," + phone_number1}\n")
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
                if dn[1] != (nn):
                    file.write(line)

    elif a == 5:
        break
