class GameCharacter:
    game_title = "Shadow Realms"

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def __str__(self):
        return f"{self.name} (HP: {self.health}) - {self.game_title}"


hero = GameCharacter("Kael", 100)
mage = GameCharacter("Lyra", 80)

print("Scenario 1: reading shared class attribute")
print(hero.game_title)
print(mage.game_title)

print("Scenario 2: changing class attribute at class level")
GameCharacter.game_title = "Shadow Realms II"
print(hero.game_title)
print(mage.game_title)

print("Scenario 3: overriding attribute on one instance")
hero.game_title = "Kael's Custom Edition"
print(hero.game_title)
print(mage.game_title)

print(hero)
print(mage)
