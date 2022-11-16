def hello():
    print("Hello")


hello()


def hello(name):
    print("Hello, " + name)


hello("Tom")


def show_name_and_age(name, age):
    print("Your name is " + name)
    print("You are " + str(age) + " years old")


show_name_and_age("Tom", 18)


def show_name_and_age(name, age):
    print("Your name is " + name)
    print("You are " + str(age) + " years old")


show_name_and_age(name="Tom", age=18)


def show_name_and_age(name="Sam", age="19"):
    print("Your name is " + name)
    print("You are " + str(age) + " years old")


show_name_and_age(name="Tom", age=18)
show_name_and_age()


def show_name_and_age(name, age="19"):
    print("Your name is " + name)
    print("You are " + str(age) + " years old")


show_name_and_age(name="Tom", age=18)


def process_person_info(name, age):
    info = {"name": name, "age": age}
    return info


print(process_person_info("Tom", "19"))


def process_person_info(name, age, country="China"):
    info = {"name": name, "age": age, "country": country}
    return info


print(process_person_info("Tom", "19"))
print(process_person_info("Bob", "18", "America"))


def hello(people):
    for person in people:
        print("Hello, " + person)


hello(["Tom", "Bob"])


def move(fruits1, fruits2):
    while fruits1:
        fruit = fruits1.pop()
        fruits2.append(fruit)


fruits11 = ["Apple", "Peach", "Pair"]
fruits22 = []
move(fruits11, fruits22)
print(fruits11)
print(fruits22)


def copy(fruits3, fruits4):
    while fruits3:
        fruit = fruits3.pop()
        fruits4.append(fruit)


fruits33 = ["Apple", "Peach", "Pair"]
fruits44 = []
copy(fruits33[:], fruits44)
print(fruits33)
print(fruits44)


def process_person_info(*item):
    print(item)


process_person_info("Tom", 19, "China")
process_person_info("Sam")
process_person_info("Amy", "America")


def process_person_info(name, *item):
    print(name + str(item))


process_person_info("Tom", 19, "China")
process_person_info("Sam", 18)
process_person_info("Amy", "America")


def process_person_info(name, **item):
    print(name + str(item))


process_person_info("Tom", age=19, country="China")
process_person_info("Sam", age=18)
process_person_info("Amy", country="America")
