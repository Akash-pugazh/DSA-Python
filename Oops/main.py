class Person:
    def __init__(self, name, pwd):
        self.name = name
        self.__pwd = pwd

    def get_pwd(self):
        return self.__pwd

    def set_pwd(self, pwd):
        self.__pwd = pwd

    def get_details(self):
        return {"name": self.name, "pass": self.get_pwd()}


akash = Person("Akash", "1234")
print(akash.get_details())
