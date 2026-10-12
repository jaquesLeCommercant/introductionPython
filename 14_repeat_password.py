password = input("Set new password : ")
answer = None
while answer != password :
    answer = input("Confirm new password : ")
    if answer == password :
        break
    else:
        print("The password does not match !")
        continue

print("Your password has been updated !")