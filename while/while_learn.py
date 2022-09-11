num = 0
while num < 10:
    num += 1
    print(num)

num = 1
while num <= 10:
    print(num)
    num += 1

# message = "You can input message and I will repeat it back to you.Enter 'quit' to end."
# result = ""
# while result != "quit":
#    result = input(message)
#    if result != "quit":
#       print(result)

# message = "You can input message and I will repeat it back to you.Enter 'quit' to end."
# flag = True
# while flag:
# result = input(message)

# if result == "quit":
# flag = False
# else:
# print(result)
# message = "You can input message and I will repeat it back to you.Enter 'quit' to end."
# flag = True
# while flag:
# result = input(message)

# if result == "quit":
# break
# else:
# print(result)
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        break
    else:
        print(num)
languages = ["python", "java", "c++"]
languages1 = []
while languages:
    print(languages)
    language = languages.pop()
    languages1.append(language)
    print(languages1)

languages = ["python", "java", "python", "c++", "python"]
print(languages)
while "python" in languages:
    languages.remove("python")
print(languages)
