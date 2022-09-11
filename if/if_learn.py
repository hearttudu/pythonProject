languages = ["python", "java", "js"]
for language in languages:
    if language == "java":
        print(language.upper())
    else:
        print(language.title())
# 相等和不相等
languages = ["python", "java", "js"]
for language in languages:
    if language != "java":
        print(language.upper())
    else:
        print(language.title())
# 多个条件and
languages = ["python", "java", "js"]
for language in languages:
    if language != "java" and language != "js":
        print(language.upper())
    else:
        print(language.title())
# 多个条件or
languages = ["python", "java", "js"]
for language in languages:
    if language == "java" or language == "js":
        print(language.upper())
    else:
        print(language.title())
# 元素是否在列表中
languages = ["python", "java", "js"]
print("python" in languages)
print("c++" in languages)
print("kotlin" not in languages)

age = 17
if age < 6:
    print("child")
elif age < 18:
    print("teenager")
elif age < 60:
    print("adult")
else:
    print("old people")

languages = ["python", "java", "js"]
if "python" in languages:
    print("python is in")
if "java" in languages:
    print("java is in")
if "js" in languages:
    print("js is in")

letters = ["a", "b"]
if letters:
    print("not none")


