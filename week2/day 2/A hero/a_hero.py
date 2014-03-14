from random import randint


class Entity():
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.__has_weapon = False
        self.__attack = 0
        self.__critical = 1
        global __max_health
        __max_health = health

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def get_health(self):
        return self.health

    def take_damage(self, damage_points):
        self.health -= damage_points
        if self.health < 0:
            self.health = 0

    def take_healing(self, healing_points):
        if self.health == 0:
            return False

        self.health += healing_points

        if self.health > __max_health:
            self.health = __max_health

        return True

    def equip_weapon(self, weapon):
        self.weapon = weapon
        self.__attack = self.weapon.damage
        self.__has_weapon = True

    def has_weapon(self):
        return self.__has_weapon

    def attack(self):
        if self.has_weapon():
            if self.weapon.critical_hit():
                self.__critical = 2
        else:
            self.__critical = 1
        return self.__attack * self.__critical


class Hero(Entity):
    def __init__(self, name, health, nickname):
        super().__init__(name, health)
        self.nickname = nickname

    def known_as(self):
        return self.name + ' ' + self.nickname


class Orc(Entity):
    def __init__(self, name, health, berserk_factor):
        super().__init__(name, health)
        if berserk_factor > 2:
            self.berserk_factor = 2
        elif berserk_factor < 1:
            self.berserk_factor = 1
        else:
            self.berserk_factor = berserk_factor

    def attack(self):
        return Entity.attack(self) * self.berserk_factor


class Weapon():
    def __init__(self, type, damage, critical_strike_percent):
        self.type = type
        self.damage = damage
        self.critical_strike_percent = critical_strike_percent

    def critical_hit(self):
        roll = randint(0, 100)
        if roll <= self.critical_strike_percent * 100:
            return True
        else:
            return False


class Fight():
    def __init__(self, hero, orc):
        self.hero = hero
        self.orc = orc
        self.chance = randint(0, 100)
        self.first = ''
        if self.chance <= 50:
            self.first = 'hero'
        else:
            self.first = 'orc'

    def simulate_fight(self):
        __orc_weapon_damage = self.orc.weapon.damage * self.orc.berserk_factor
        __hero_weapon_damage = self.hero.weapon.damage
        while True:
            if self.first == 'hero':
                self.orc.take_damage(self.hero.attack())
                if self.hero.attack() == 2 * __hero_weapon_damage:
                    print('Critical strike!')
                print('Orc takes ' + str(self.hero.attack()) +
                    ' damage from Hero\n')
                self.first = 'orc'
            else:
                self.hero.take_damage(self.orc.attack())
                if self.orc.attack() == 2 * __orc_weapon_damage:
                    print('Critical strike!')
                print('Hero takes ' + str(self.orc.attack()) +
                    ' damage from orc.\n')
                self.first = 'hero'

            if self.hero.health == 0:
                print('The hero died.')
                break
            elif self.orc.health == 0:
                print('The orc is dead.')
                break


class Dungeon():
    def __init__(self, map):
        self.map = map
        self.dungeon_map = open(self.map, 'r')
        self.map_array = []
        for line in self.dungeon_map.readlines():
            self.map_array.append(line.strip())
        self.map_height = len(self.map_array)
        self.map_width = len(self.map_array[0])
        self.dungeon_map.close()

    def print_map(self):
        print('\n'.join(self.map_array))

    def spawn(self, player_name, entity):
        self.player_name = player_name
        __successful = False
        for i in range(len(self.map_array)):
            if self.map_array[i].count('S') > 0:
                if type(entity) == Hero:
                    self.map_array[i] = self.map_array[i].replace('S', 'H', 1)
                    __successful = True
                    break
                elif type(entity) == Orc:
                    self.map_array[i] = self.map_array[i].replace('S', 'O', 1)
                    __successful = True
                    break
            else:
                __successful = False
        return __successful

    def move(self, player_name, direction):
        self.direction = direction
        for i in range(len(self.map_array)):
            for j in range(len(self.map_array[i])):
                if self.map_array[i][j] == 'H' and self.direction == 'right' and self.map_array[i][j + 1] == '.':
                    self.map_array[i] = self.map_array[i].replace('.', 'H', 1)
                    self.map_array[i] = self.map_array[i].replace('H', '.', 1)
                    return True
                #move left, up, down still to be done
                else:
                    return False
