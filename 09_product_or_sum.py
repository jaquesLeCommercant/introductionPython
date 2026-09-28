print("Enter an integer here:")
n1 = int(input())
print("Enter another integer here:")
n2 = int(input())
prod = int(n1*n2)
summ = int(n1+n2)

if prod<1000:
    print(f"The product of {n1} and {n2} is {prod}.")
else:
    print(f"The sum of {n1} and {n2} is {summ}.")