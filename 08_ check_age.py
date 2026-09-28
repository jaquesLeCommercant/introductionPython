print("Hi. In which year are you born ?")
date = int(input())
age = 2026-date
print("By the end of 2026, you'll be "+str(age)+" years old !")
if age < 12:
    print("You are currently a child.")
elif age < 18:
    print("You're a teenager.")
elif age < 70:
    print("You're an adult.")
elif age < 3000:
    print("You're somewhat old now...")
else:
    print("WHAAAA...? How is bro even ALIVE !??")
