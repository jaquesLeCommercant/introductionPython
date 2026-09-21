print("Give me a timespan in seconds.")
seconds=int(input())
print(str(seconds//3600) + " hours, "+ str((seconds%3600)//60) + " minutes, and " +str(((seconds%3600)//60)%60) + " seconds.")