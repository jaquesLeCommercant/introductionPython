print("I can convert temperatures from Celcius to Fahrenheit, and vice versa.\nType 'c' to convert Celcius to Fahrenheit,\nor type 'f' to convert from Fahrenheit to Celcius.")
cof = input()
if cof == "c":
    print("Give me a temperature in Celcius, and I'll convert it to Fahrenheit.")
    temp = float(input())
    print(str(temp)+"°C equals "+ str(temp*1.8+32) +"°F.")
elif cof == "f":
    print("Give me a temperature in Fahrenheit, and I'll convert it to Celcius.")
    temp = float(input())
    print(str(temp)+"°F equals "+ str((temp-32)*(5/9)) +"°C.")
else:
    print("I do not recognize this key.")