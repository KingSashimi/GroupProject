import random

moves = {"overheat": range(18, 26),
         "virus": range(10, 36),
         "download": range(10, 20)}


class Computerman:
    def __init__(self, health):
        self.health = health

    def attack(self, other):
        raise NotImplementedError


class Player(Computerman):
    def __init__(self, health=100):
        super().__init__(health)

    def attack(self, other):
        while True:
            choice = str.lower(input("\nWhat move would you like to make? (Overheat, Virus, or Download)"))

            if choice == "download":
                self.health += int(random.choice(moves[choice]))
                print("\nYour health is now {0.health}.".format(self))
                break
            if choice == "overheat" or choice == "virus":
                damage = int(random.choice(moves[choice]))
                other.health -= damage
                print("\nYou attack with {0}, dealing {1} damage.".format(choice, damage))
                break
            else:
                print("Not a valid move, try again!")


class Printerman(Computerman):
    def __init__(self, health=100):
        super().__init__(health)

    def attack(self, other):
        if self.health <= 35:
            moves_1 = ["overheat", "virus", "download", "download", "dwonload", "download", "download"]
            cpu_choice = random.choice(moves_1)
        else:
            cpu_choice = random.choice(list(moves))
        if cpu_choice == "virus" or cpu_choice == "overheat":
            damage = int(random.choice(moves[cpu_choice]))
            other.health -= damage
            print("\nThe Printerman attacks with {0}, dealing {1} damage.".format(cpu_choice, damage))
        if cpu_choice == "download":
            self.health += int(random.choice(moves[cpu_choice]))
            print("\n Printerman uses download and its health is now {0.health}.".format(self))


def battle(player, Printerman):
    print("Printerman enters...")
    while player.health > 0 and Printerman.health > 0:
        player.attack(Printerman)
        if Printerman.health <= 0:
            break
        print("\nThe health of Printerman is now {0.health}.".format(Printerman))
        Printerman.attack(player)
        if player.health <= 0:
            break
        print("\nYour health is now {0.health}.".format(player))
    if player.health > 0:
        print("You defeated Printerman")
    if Printerman.health > 0:
        print("You were defeated by Printerman")

if __name__ == '__main__':
    battle(Player(), Printerman())
