print("This program will calculate your average score.\nPress 'q' to end the operation and get your average.")
answer = 0
result = 0
running_program = True
times_ran = 0
while running_program :
    answer = input("Enter a number : ")
    
    if not answer.isnumeric():
        if answer == "q":
            break
        else :
            continue
    times_ran += 1
    result = round((result + int(answer))/times_ran, 1)
    
print(f"The average is {result}/20.")
    