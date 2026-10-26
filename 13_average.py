print("This program will calculate your average score.\nPress 'q' to end the operation and get your average.")

counter = 0
summ = 0

while True :
    answer = input("Enter a score: ")
    if answer.isnumeric() and 0 <= int(answer) <= 20 :
        summ += int(answer)
        counter += 1
    elif answer == "q" :
        break
    else :
        print("Invalid value.")


if counter > 0 :
    result = round(summ / counter , 1)
    print(f"The average is {result}/20.")
else :
    print("No scores were entered.")