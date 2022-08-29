# 创建列表
language = ["python", "java", "c++"]
print(language)
# 删除列表元素
del (language[-1])
print(language)
del (language[-1])
print(language)
# 弹出列表元素
language = ["python", "java", "c++"]
print(language)
l3 = language.pop()
print(l3)
print(language)
l2 = language.pop(1)
print(l2)
print(language)
# 移出列表元素
language = ["python", "java", "c++", "c++"]
print(language)
language.remove("c++")
print(language)
# 排序
language = ["java", "python", "c++"]
print(language)
language.sort()
print(language)
language.sort(reverse=True)
print(language)
# 排序不影响原列表
language = ["java", "python", "c++"]
print(language)
print(sorted(language))
print(language)
# 反转
language = ["java", "python", "c++"]
print(language)
language.reverse()
print(language)
# 遍历
languages = ["python", "java", "c++"]
for language in languages:
    print(language)
print("for in end")

# 1-10的列表
numbers = list(range(1, 11))
print(numbers)
# 1-10奇数的列表
numbers = list(range(1, 11, 2))
print(numbers)
# 1-10数字的平方
numbers = []
for number in range(1, 11):
    numbers.append(number ** 2)
print(numbers)
# 简单统计
numbers = list(range(1, 11))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(sum(numbers) / len(numbers))
# 列表解析
numbers = [number ** 2 for number in range(1, 11)]
print(numbers)
# 切片
languages = ["python", "java", "c++", "php"]
print(languages)
print(languages[1:3])
print(languages[:3])
print(languages[2:])
print(languages[:-3])
print(languages[-2:])
# 切片遍历
for language in languages[:3]:
    print(language)
# 列表复制
languages = ["python", "java", "c++", "php"]
languages_new = languages[:]
print(languages)
print(languages_new)
# 列表赋值
languages = ["python", "java", "c++", "php"]
languages_1 = languages
languages.append("oc")
languages_1.append("js")
print(languages)
print(languages_1)
# 元组
people = ("male", "female")
print(people)
for one in people:
    print(one)

