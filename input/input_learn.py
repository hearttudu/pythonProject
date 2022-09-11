message = input("Please input your name:")
print("Hello, " + message)
age = input("How old are you?")
if int(age) < 13:
    print("You are a child.")
elif int(age) < 18:
    print("Your are a teenager.")
else:
    print("Your are an adult")