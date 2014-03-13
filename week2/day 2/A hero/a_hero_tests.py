import a_hero
import unittest
import sys


class TestAHero(unittest.TestCase):
    def setUp(self):
        self.h = a_hero.Hero("Bron", 100, "The DragonSlayer")

    def test_hero(self):
        self.assertEqual("Bron", self.h.name)
        self.assertEqual(100, self.h.get_health())
        self.assertEqual("The DragonSlayer", self.h.nickname)

    def test_known_as(self):
        self.assertEqual("Bron The DragonSlayer", self.h.known_as())

    def test_is_alive(self):
        self.assertTrue(self.h.is_alive())

    def test_get_health(self):
        self.assertEqual(100, self.h.get_health())

    def test_take_damage_bigger_than_current_health(self):
        self.h.take_damage(1000.5)
        self.assertEqual(0, self.h.get_health())
        self.assertTrue(not self.h.is_alive())

    def test_take_damage(self):
        self.h.take_damage(13.5)
        self.assertEqual(86.5, self.h.get_health())

    def test_heal_dead_hero(self):
        self.h = a_hero.Hero("Bron", 0, "The DragonSlayer")
        self.assertTrue(not self.h.take_healing(100))
        self.assertEqual(0, self.h.get_health())

    def test_heal_more_than_max_health(self):
        self.assertTrue(self.h.take_healing(100))
        self.assertEqual(100, self.h.get_health())

    def test_has_weapon(self):
        self.assertEqual(False, self.h.has_weapon())

    def test_equip_weapon(self):
        self.assertEqual(False, self.h.has_weapon())
        self.h.equip_weapon(a_hero.Weapon('axe', 11, 1))
        self.assertEqual(True, self.h.has_weapon())

    def test_attack_without_weapon(self):
        self.assertEqual(0, self.h.attack())

    def test_attack_with_weapon(self):
        self.h.equip_weapon(a_hero.Weapon('axe', 11, 1))
        self.assertEqual(11 * 2, self.h.attack())


class TestOrc(unittest.TestCase):
    def setUp(self):
        self.orc = a_hero.Orc("Thrall", 76, 1.3)

    def test_get_health(self):
        self.assertEqual(76, self.orc.get_health())

    def test_is_alive(self):
        self.assertTrue(self.orc.is_alive())

    def test_berserk_factor_larger_than_2(self):
        self.orc = a_hero.Orc("Thrall", 76, 3.3)
        self.assertEqual(2, self.orc.berserk_factor)

    def test_berserk_factor_smaller_than_1(self):
        self.orc = a_hero.Orc("Thrall", 76, 0.2)
        self.assertEqual(1, self.orc.berserk_factor)

    def test_berserk_factor_in_allowed_range(self):
        self.assertEqual(1.3, self.orc.berserk_factor)

    def test_heal_dead_orc(self):
        self.orc = a_hero.Hero("Thrall", 0, 1.3)
        self.assertTrue(not self.orc.take_healing(100))
        self.assertEqual(0, self.orc.get_health())

    def test_heal_more_than_max_health(self):
        self.assertTrue(self.orc.take_healing(76))
        self.assertEqual(76, self.orc.get_health())

    def test_has_weapon(self):
        self.assertEqual(False, self.orc.has_weapon())

    def test_equip_weapon(self):
        self.assertEqual(False, self.orc.has_weapon())
        self.orc.equip_weapon(a_hero.Weapon('axe', 11, 1))
        self.assertEqual(True, self.orc.has_weapon())

    def test_attack_without_weapon(self):
        self.assertEqual(0, self.orc.attack())

    def test_attack_with_weapon(self):
        self.orc.equip_weapon(a_hero.Weapon('axe', 11, 1))
        self.assertEqual(11 * 1.3 * 2, self.orc.attack())


class TestWeaponCritical(unittest.TestCase):
    def setUp(self):
        self.weapon = a_hero.Weapon('axe', 11, 1)

    def test_critical_hit_100_percent(self):
        self.assertEqual(True, self.weapon.critical_hit())

    def test_critical_hit_0_percent(self):
        self.weapon = a_hero.Weapon('axe', 11, 0)
        self.assertEqual(False, self.weapon.critical_hit())


class TestFight(unittest.TestCase):
    def setUp(self):
        self.orc = a_hero.Orc("Thrall", 76, 1.3)
        self.orc.equip_weapon(a_hero.Weapon('axe', 11, 0.1))
        self.h = a_hero.Hero("Bron", 100, "The DragonSlayer")
        self.h.equip_weapon(a_hero.Weapon('Broadsword', 14, 0.1))
        self.fight = a_hero.Fight(self.h, self.orc)

    def test_who_goes_first(self):
        if self.fight.first == 'hero':
            self.assertEqual('hero', self.fight.first)
        else:
            self.assertEqual('orc', self.fight.first)

    def test_fight_simulation(self):
        self.fight.simulate_fight()


class TestMap(unittest.TestCase):
    def setUp(self):
        self.dungeon = a_hero.Dungeon('dungeon_map.txt')
        self.hero = a_hero.Hero("Bron", 100, "The DragonSlayer")
        self.orc = a_hero.Orc("Thrall", 76, 1.3)

    def test_print_map(self):
        self.dungeon.print_map()

    def test_spawn_hero(self):
        self.assertTrue(self.dungeon.spawn('player 1', self.hero))

    def test_spawn_orc(self):
        self.assertTrue(self.dungeon.spawn('player 2', self.orc))

    def test_spawn_hero_and_orc(self):
        self.dungeon.spawn('player 1', self.hero)
        self.assertTrue(self.dungeon.spawn('player 2', self.orc))
        self.dungeon.print_map()

    def test_spawn_more_than_spawn_locations(self):
        self.dungeon.spawn('player 1', self.hero)
        self.dungeon.spawn('player 2', self.orc)
        self.dungeon.spawn('player 1', self.hero)
        self.dungeon.spawn('player 2', self.orc)
        self.assertTrue(not self.dungeon.spawn('player 2', self.orc))


if __name__ == '__main__':
    unittest.main()
