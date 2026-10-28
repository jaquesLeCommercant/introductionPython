myList = []
choice = None 
answer = None
index = 0

while True :
    choice = input("What operation do you want to do in your list ?\nA: Adding an element,\nD: Deleting an element,\nM: Modifying an element,\nQ: Quit\nYour choice: ")
    
    if choice == "A" :
        answer = input("New element: ")
        myList.append(answer)
        print(myList)

    elif choice == "D":
        index = int(input("Index of the element to delete: "))

        # system to force user into chosing valid index
        # negative index values aren't accepted
        
        if 0 <= index <= (len(myList) -1) :
            del myList[index]
            print(myList)
        else :
            print("Please select a valid index. Negative values aren't accepted.")

    elif choice == "M":
        answer = input("New value: ")
        index = int(input("Index of the element to modify: "))

        if 0 <= index <= (len(myList) -1) :
            myList[index] = answer
            print(myList)
        else :
            print("Please select a valid index. Negative values aren't accepted.")

    elif choice == "Q" :
        print(f"Final list: {myList}")
        break

    else :
        print("Character not recognized. Don't forget to type in uppercase!")
        continue
