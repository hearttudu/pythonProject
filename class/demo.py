class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.country = "China"

    def get_name(self):
        print(self.name)

    def get_age(self):
        print(self.age)

    def get_country(self):
        print(self.country)

    def set_name(self, name):
        self.name = name


people1 = People("Amy", "18")
# 调用方法
people1.get_name()
people1.get_age()
people1.get_country()

people2 = People("Tom", "19")
people2.country = "Japan"
# 调用方法
people2.get_name()
people2.get_age()
people2.get_country()
people2.set_name("Bob")
people2.get_name()


class Chinese(People):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.province = "shandong"

    def print_province(self):
        print(self.province)


people3 = Chinese("Ming", "20")
people3.get_name()
people3.get_age()
people3.get_country()
people3.print_province()
