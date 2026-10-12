print("This program will calculate your average score.\nPress 'q' to end the operation and get your average.")
answer = 0
summ = 0
result = 0
running_program = True
times_ran = 0
while running_program :
    answer = input("Enter a number : ")
    
    
    if not answer.isnumeric():
        if answer == "q":
            break
        else :
            times_ran += 1
            summ += int(answer)
            continue
    result = round((result + int(summ))/times_ran, 1)
    
print(f"The average is {result}/20.")
    