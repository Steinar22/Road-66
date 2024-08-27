class Player(object):
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality

    def details(self):
        print(f"You are {self.name}, {self.age} years old, and are {self.nationality}.")

    messages = {
        "Death Message": "The world is unfair!"
    }


