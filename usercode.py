path = input("Enter CSV path: ")


print("1. Register")
print("2. Login")
choice = input("Enter choice: ")


file = open(path, 'r')
lines = file.readlines()
file.close()

key = lines[0].strip().split(',')
print("Keys:", key)

users = []

for l in lines[1:]:
    value = l.strip().split(',')
    rowd = {}

    for i in range(len(key)):
        rowd[key[i]] = value[i]

    users.append(rowd)


if choice == "1":
    new_user = input("Enter new username: ")
    new_pass = input("Enter new password: ")

    
    for u in users:
        if u["Name"] == new_user:
            print("Username already exists")
            exit()

   
    file = open(path, 'a')
    file.write(f"\n{new_user},{new_pass},1")
    file.close()

    print("Registration successful! User added as active.")


elif choice == "2":
    uname = input("Enter username: ")
    pwd = input("Enter password: ")

    user_found = False

    for u in users:
        if u["Name"] == uname:
            user_found = True

            if u["Password"] != pwd:
                print("Invalid password")
                break

            if u["Status"] == "0":
                print("User is inactive")
                break

            if u["Status"] == "1":
                print("Login successful! User is active.")
                break

    if not user_found:
        print("Invalid username")

else:
    print("Invalid choice")
