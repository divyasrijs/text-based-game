class Character:
    def __init__(self, name, char_class):
        self.name = name
        self.char_class = char_class
        self.inventory = []
        self.health = 100

    def display_status(self):
        print(f"Name: {self.name}")
        print(f"Class: {self.char_class}")
        print(f"Health: {self.health}")
        print(f"Inventory: {', '.join(self.inventory) if self.inventory else 'Empty'}")


class Game:
    def __init__(self):
        self.character = None
        self.game_over = False

    def start(self):
        print("Welcome to the Text-Based Adventure Game!")
        self.create_character()
        while not self.game_over:
            self.display_choices()
    
    def create_character(self):
        name = input("Enter your character's name: ")
        char_class = input("Choose your character (Warrior/Monster): ")
        self.character = Character(name, char_class)
        print("Character created successfully!")

    def display_choices(self):
        print("\nWhat would you like to do?")
        print("1. Explore the forest\n2. Check inventory\n3. Rest\n4. Quit game")
        choice = input("Enter your choice: ")
        self.handle_choice(choice)

    def handle_choice(self, choice):
        if choice == "1":
            self.explore_forest()
        elif choice == "2":
            self.character.display_status()
        elif choice == "3":
            self.rest()
        elif choice == "4":
            self.quit_game()
        else:
            print("Invalid choice. Try again.")

    def explore_forest(self):
        print("Hurray! You venture into the forest and encounter a wild beast!")
        action = input("Do you want to Fight or Run? ")
        if action.lower() == "fight":
            self.fight()
        else:
            print("You ran back to safer side.")

    def fight(self):
        print("You engage in combat!")
        # Simple fight logic (can be expanded)
        if self.character.char_class == "Warrior":
            print("You swing your sword and defeat the beast!")
            self.character.inventory.append("Beast Hide")
        elif self.character.char_class == "Monster":
            print("You use your agility to defeat the beast!")
            self.character.inventory.append("Beast Claw")
        else:
            print("You fight valiantly but defeated.")
            self.character.health -= 20
        self.check_game_over()

    def rest(self):
        print("You take a rest and recover some health.")
        self.character.health = min(100, self.character.health + 10)

    def check_game_over(self):
        if self.character.health <= 0:
            print("OOPS! Your health has dropped to zero. Game over!")
            self.game_over = True

    def quit_game(self):
        print("Thank you for playing! See you Later!")
        self.game_over = True


if __name__ == "__main__":
    game = Game()
    game.start()
