import random

class Person:
    def __init__(self,name,health, damage, armor):
        self.name=name
        self.health = health
        self.damage = damage
        self.armor = armor
    def hp(self, damage):
        self.health -= damage - self.armor
        if self.health<=0:
            print(f"{self.name} получил {damage - self.armor} урона. У {self.name} не осталось здоровья")
        else:
            print(f"{self.name} получил {damage - self.armor} урона. Осталось здоровья: {self.health}")

class Player(Person):
    def __init__(self,name,health,damage, armor, weapon):
        super().__init__(name,health,damage,armor)
        self.weapon=weapon
        self.damage=self.damage+self.weapon
    def attack (self, enemy):
        enemy.hp(self.damage)

class Enemy(Person):
    def __init__(self,name, health,damage, armor):
        super().__init__(name,health,damage,armor)
    def attack(self, player):
        player.hp(self.damage)

class Fight:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def Battle(self):
        turn = 0
        while self.player.health>0 and self.enemy.health>0:
            if turn == 0:
                self.player.attack(self.enemy)
                turn = 1
            else:
                self.enemy.attack(self.player)
                turn = 0

        if self.enemy.health<=0:
            print(f"{self.player.name} победил")
        else:
            print(f"{self.enemy.name} победил")

player = Player(name="Игрок", health=100,damage=20, armor=5,weapon=1)
enemy = Enemy(name="Враг", health=80, damage=15, armor=3)

game = Fight(player, enemy)
game.Battle()


