people_0 = {"name": "aaa", "age": 18}
print(people_0)
print(people_0["name"])
print(people_0["age"])

people_0["sex"] = "man"
print(people_0)
people_0["age"] = 19
print(people_0)

del people_0["age"]
print(people_0)

name = people_0.pop("name")
print(people_0)
print(name)

people_0 = {"name": "aaa", "age": 18, "sex": "man"}
for key in people_0.keys():
    print(key)
for key in sorted(people_0.keys()):
    print(key)
for value in people_0.values():
    print(value)
for key, value in people_0.items():
    print(key + ":" + str(value))

person_0 = {"name": "aaa", "age": 18}
person_1 = {"name": "bbb", "age": 19}
person_2 = {"name": "ccc", "age": 20}
people = [person_0, person_1, person_2]
for person in people:
    print(person)
eat = ["fish", "meat"]
language = ["English", "Chinese"]
sport = ["football", "basketball"]
person_3 = {"eat": eat, "language": language, "sport": sport}
for key, values in person_3.items():
    print(key + ":")
    for value in values:
        print(value)
person_0 = {"name": "aaa", "age": 18}
person_1 = {"name": "bbb", "age": 19}
person_2 = {"name": "ccc", "age": 20}
people = {"person0": person_0, "person1": person_1, "person2": person_2}
for key, values in people.items():
    print("name" + ":" + values["name"])
    print("age" + ":" + str(values["age"]))

