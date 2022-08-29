# 创建列表
people = ["amy", "bob", "cat", "dog"]
print("I invite " + str(people) + " to dinner!")
# 修改元素
print(people[-1] + " cant come.")
people[-1] = "ella"
print("I invite " + str(people) + " to dinner!")
# 添加元素
print("I find a bigger table.")
people.insert(0, "start")
people.insert(2, "middle")
people.append("last")
print("I invite " + str(people) + " to dinner!")
# 删除元素
print("I can only invite 2 people to dinner.")
p1 = people.pop()
print("I cant invite you to dinner," + p1)
p2 = people.pop()
print("I cant invite you to dinner," + p2)
p3 = people.pop()
print("I cant invite you to dinner," + p3)
p4 = people.pop()
print("I cant invite you to dinner," + p4)
p5 = people.pop()
print("I cant invite you to dinner," + p5)
print(str(people) + " are still in list.")
del (people[-1])
del (people[-1])
print(people)
