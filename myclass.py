class person:
    def __init__(self, name, nation, age):
        self.name=name
        self.nation=nation
        self.age=age

    def introduce_self(self):
        print("My name is "+self.name)
        print("I am "+self.nation)
        print(self.age)
