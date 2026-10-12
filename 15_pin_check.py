pin = "7482"
answer = None
attemptsLeft = int(3)
while answer != pin :
    if attemptsLeft > 0 :
        answer = input(f"{attemptsLeft} attempts left.\nEnter PIN code : ")
        if answer == pin :
            print("PIN code correct.")
            break
        else:
            attemptsLeft -= 1
            print("PIN code incorrect.")
            continue
    else:
        print("Too many attempts. Payment refused.")
        break

