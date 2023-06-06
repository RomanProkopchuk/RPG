import random
import time


class Player:
    def __init__(self, player_name, player_hp, player_damage):
        self.name = player_name
        self.hp = player_hp
        self.damage = player_damage
        self.lvl = 1
        self.exp = 0

    def level_up(self):
        self.lvl += 1
        self.exp = 0
        self.hp += self.lvl * 15
        self.damage += self.lvl * 8
        print(f"Поздравляем! У вас новый уроень: {self.lvl}\n")

    @staticmethod
    def create_weapon():
        weapons = ['меч', 'лук', 'книга']
        weapons_rare = {
            1: 'обычный',
            2: 'редкий',
            3: 'очень редкий'
        }
        random_weapon = random.choice(weapons)
        random_rare = random.choice(list(weapons_rare.keys()))
        if random_weapon == weapons[0]:
            hero.damage += 10 * random_rare
        elif random_weapon == weapons[1]:
            hero.damage += 20 * random_rare
        elif random_weapon == weapons[2]:
            hero.damage += 30 * random_rare
        return random_weapon, weapons_rare[random_rare]

    @staticmethod
    def create_point():
        point_rare = {
            50: 'маленькая',
            85: 'средняя',
            100: 'большая'
        }
        random_rare = random.choice(list(point_rare.keys()))
        hero.hp += random_rare
        return point_rare[random_rare]

    def attack(self, victim):
        victim.hp -= self.damage
        print(f"Ваш урон: {self.damage}")
        if victim.hp <= 0:
            rand_exp = self.lvl * 20
            print(f"Поздравляем! {victim.name} повержен! +{rand_exp} опыта!")
            item = random.randint(1, 3)
            if item == 1:
                weapon = self.create_weapon()
                print(f'у вас новое оружие {weapon[0]}, с редкостью: {weapon[1]}\n'
                      f'ваш урон {self.damage}')
            elif item == 2:
                point = self.create_point()
                print(f'вам выпала {point} фляшка с зельем \n'
                      f'ваши жизни {hero.hp}')
            elif item == 3:
                print('вам нечего не выпало')
            time.sleep(1)
            self.exp += rand_exp
            max_exp = self.lvl * 55

            # Проверка на повышение уровня
            if self.exp >= max_exp:
                self.level_up()
                max_exp = self.lvl * 55
                time.sleep(.7)
                print(f"До следующего уровня: {max_exp} опыта!\n")
                time.sleep(.7)
            time.sleep(.7)
            return False
        else:
            print(f"{victim.name}, осталось {victim.hp} здоровья")
            time.sleep(.7)
            return True

    @staticmethod
    def create_player(player_name, player_race, player_class):
        hp = 0
        damage = 0
        player_name = player_name
        if player_race == races_list[0]:
            hp = 140
            damage = 100
        elif player_race == races_list[1]:
            hp = 175
            damage = 140
        elif player_race == races_list[2]:
            hp = 130
            damage = 95
        elif player_race == races_list[3]:
            hp = 100
            damage = 100
        else:
            print("Ошибка!\n"
                  "Неизвестная раса!")
            quit()

        if player_class == class_list[0]:
            hp += 20
            damage += 50
        elif player_class == class_list[1]:
            hp += 50
            damage += 20
        elif player_class == class_list[2]:
            hp += 40
            damage += 40

        else:
            print("Ошибка!\n"
                  "Неизвестный класс!")
            quit()

        return Player(player_name, hp, damage)


class Enemy:
    def __init__(self, enemy_name, enemy_hp, enemy_damage):
        self.name = enemy_name
        self.hp = enemy_hp
        self.damage = enemy_damage

    def attack(self, victim):
        victim.hp -= self.damage
        print(f"{self.name}. Урон: {self.damage}")
        time.sleep(.3)
        if victim.hp <= 0:
            print(f"Вы повержены! Игра окончена!")
            quit()
        else:
            print(f"Ваше здоровье: {victim.hp}")
            time.sleep(.7)

    @staticmethod
    def create_enemy():
        enemy_names = ["Вампир", "Скелет", "Орк"]
        enemy_name = random.choice(enemy_names)
        enemy_hp = random.randint(110, 150) + 5 * hero.lvl
        enemy_damage = random.randint(80, 115) + 7 * hero.lvl
        return Enemy(enemy_name, enemy_hp, enemy_damage)


races_list = ["эльф", "гном", "хоббит", "человек"]
class_list = ["лучник", "рыцарь", 'маг']

print("Здравствуйте, как вас зовут?")
name = input()
print("К какой расе вы относитесь?")
for race in races_list:
    print(race, end=" ")
print()
race = input().lower()

print("К какому классу вы относитесь?")
for class_player in class_list:
    print(class_player, end=" ")
print()
class_player = input().lower()

hero = Player.create_player(name, race, class_player)

print(
    f"Персонаж создан!\n"
    f"Имя: {hero.name}\n"
    f"Здоровье: {hero.hp}\n"
    f"Урон: {hero.damage}\n"
)
time.sleep(.7)


def fight_choice():
    answer = int(input("Атаковать или бежать? (1 или 2) "))
    if answer == 1:
        result_attack = hero.attack(enemy)
        if result_attack:
            enemy.attack(hero)
            fight_choice()
    elif answer == 2:
        plan = random.randint(0, 1)
        if plan == 0:
            print("Вы сбежали от монстра!")
            time.sleep(.7)
        elif plan == 1:
            print("Вас поймали!")
            time.sleep(.5)
            enemy.attack(hero)
            time.sleep(.3)
            fight_choice()
    else:
        print("Неверное действие!")
        fight_choice()


while True:
    event = random.randint(0, 1)
    if event == 0:
        print("Вам никто не встретился, идём дальше...")
        time.sleep(.7)
    elif event == 1:
        enemy = Enemy.create_enemy()
        print(f"Вас заметил {enemy.name}\n"
              f"Здоровье -> {enemy.hp}\n"
              f"Урон -> {enemy.damage}")
        fight_choice()