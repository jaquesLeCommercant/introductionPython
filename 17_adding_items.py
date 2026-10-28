myList = []
counter = None
counter = int(input("How many items do you want to add to the list ?: "))
while counter > 0 :
    value = input("Enter a value: ")
    myList.append(value)
    counter -= 1
print(myList)
