print("Welcome!\nSet -1 as index to stop the program.")
list = [1, 2, 3, 4, 5]
index = 0
newVal = 0

while True :
    index = int(input("Index: "))
    newVal = int(input("New value: "))
    if index > 4 :
        print("Please select an index between 0 and 4 included only.\nSet -1 as index to stop the program.")
        continue
    elif index < 0:
        break
    else:
        list[index] = int(newVal)
        print(list)