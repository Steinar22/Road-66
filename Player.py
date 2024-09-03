class Player(object):
    def __init__(self, name):
        self.name = name  
        

    def details(self):
        print(f"""\n\tWelcome, {self.name} . Road 66 is not just a road; it's a descent into madness.
              Keep your wits about you, for the horrors that await are not for the faint of heart.\t\n""")

    def show_death_messages(self):
        for message in self.deathMessages:
            print(message)

    deathMessages = [
        "The world is unfair.",
        "Maybe it's time to use some brains!",
        "Admit it YOU'RE WEAK!",
        "Do you still believe in Santa?"
    ]


name = input("\n\t\tPlease Enter your name traveller:")


first_player = Player(name)


first_player.details()

