import random
import time

class Character:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0

    def heal(self, amount):
        self.hp += amount
        if self.hp > 100:
            self.hp = 100

    def __str__(self):
        return f"{self.name} (HP: {self.hp})"


class Player(Character):
    def __init__(self, name):
        super().__init__(name, 100, 10)
        self.inventory = []
        self.level = 1
        self.experience = 0

    def add_item(self, item):
        self.inventory.append(item)

    def show_inventory(self):
        if len(self.inventory) == 0:
            print("Inventory is empty.")
        else:
            print("Inventory:")
            for item in self.inventory:
                print(f"- {item}")


class Monster(Character):
    def __init__(self, name, hp, attack):
        super().__init__(name, hp, attack)


class Item:
    def __init__(self, name, heal_amount):
        self.name = name
        self.heal_amount = heal_amount

    def __str__(self):
        return f"{self.name} (Heals: {self.heal_amount})"


def create_monster():
    monsters = ["Goblin", "Orc", "Troll", "Skeleton", "Zombie"]
    name = random.choice(monsters)
    hp = random.randint(20, 50)
    attack = random.randint(5, 15)
    return Monster(name, hp, attack)

def battle(player, monster):
    print(f"A wild {monster.name} appears!")
    while player.is_alive() and monster.is_alive():
        action = input("Do you want to (a)ttack or (r)un? ")
        if action == "a":
            monster.take_damage(player.attack)
            print(f"You attacked {monster.name} for {player.attack} damage!")
            if monster.is_alive():
                player.take_damage(monster.attack)
                print(f"{monster.name} attacked you for {monster.attack} damage!")
        elif action == "r":
            print("You ran away!")
            break
        else:
            print("Invalid action!")
    if not monster.is_alive():
        print(f"You defeated {monster.name}!")
        loot = random.choice([Item("Health Potion", 20), None])
        if loot:
            player.add_item(loot)
            print(f"You found a {loot.name}!")



def explore(player):
    """Explore the dungeon and encounter monsters or items."""
    print("You are exploring the dungeon...")
    while player.is_alive():
        encounter = random.choice(["monster", "item", "nothing"])
        if encounter == "monster":
            monster = create_monster()
            battle(player, monster)
        elif encounter == "item":
            item = Item("Health Potion", 20)
            print(f"You found a {item.name}!")
            take_item = input("Do you want to take it? (y/n) ")
            if take_item == "y":
                player.add_item(item)
        else:
            print("You found nothing.")

def main():
    """Main function to start the game."""
    print("Welcome to the Dungeon Explorer!")
    player_name = input("Enter your character's name: ")
    player = Player(player_name)
    while player.is_alive():
        action = input("Do you want to (e)xplore or (i)nventory? ")
        if action == "e":
            explore(player)
        elif action == "i":
            player.show_inventory()
        else:
            print("Invalid action!")
    print("Game Over!")



# Дальнейшее расширение кода
class CustomMonster(Monster):
    def __init__(self, name, hp, attack):
        super().__init__(name, hp, attack)
        self.special_attack = random.randint(5, 20)

    def use_special(self, player):
        print(f"{self.name} uses a special attack!")
        player.take_damage(self.special_attack)


def create_custom_monster():
    names = ["Dragon", "Vampire", "Werewolf", "Giant"]
    name = random.choice(names)
    hp = random.randint(50, 100)
    attack = random.randint(10, 25)
    return CustomMonster(name, hp, attack)


def battle_with_custom(player, monster):
    print(f"A wild {monster.name} appears!")
    while player.is_alive() and monster.is_alive():
        action = input("Do you want to (a)ttack, (r)un, or (s)pecial? ")
        if action == "a":
            monster.take_damage(player.attack)
            print(f"You attacked {monster.name} for {player.attack} damage!")
            if monster.is_alive():
                player.take_damage(monster.attack)
                print(f"{monster.name} attacked you for {monster.attack} damage!")
        elif action == "r":
            print("You ran away!")
            break
        elif action == "s":
            player.attack += 5
            print("You powered up your attack!")
        else:
            print("Invalid action!")
    if not monster.is_alive():
        print(f"You defeated {monster.name}!")
        loot = random.choice([Item("Health Potion", 20), None])
        if loot:
            player.add_item(loot)
            print(f"You found a {loot.name}!")


# Добавление новых функций для улучшения игры
def save_game(player):
    """Save the player's game state to a file."""
    with open(f"{player.name}_save.txt", "w") as f:
        f.write(f"{player.name}\n{player.hp}\n{player.level}\n{player.experience}\n")
        for item in player.inventory:
            f.write(f"{item.name}\n")

def load_game():
    """Load the player's game state from a file."""
    name = input("Enter your character's name to load: ")
    try:
        with open(f"{name}_save.txt", "r") as f:
            player_name = f.readline().strip()
            hp = int(f.readline().strip())
            level = int(f.readline().strip())
            experience = int(f.readline().strip())
            player = Player(player_name)
            player.hp = hp
            player.level = level
            player.experience = experience
            items = f.readlines()
            for item_name in items:
                player.add_item(Item(item_name.strip(), 20))
            print("Game loaded successfully!")
            return player
    except FileNotFoundError:
        print("Save file not found.")
        return None



def main_menu():
    """Display the main menu and handle user choice."""
    print("1. New Game")
    print("2. Load Game")
    choice = input("Choose an option: ")
    if choice == "1":
        main()
    elif choice == "2":
        player = load_game()
        if player:
            explore(player)

if __name__ == "__main__":
    main_menu()