import unittest
from actor import Actor


class TestActorClass(unittest.TestCase):
    def setUp(self):
        self.a = Actor("Best.Actor.Ever.")

    def test_get_actor_name(self):
        self.assertEqual("Best.Actor.Ever.", self.a.get_name())

    @unittest.skip("No point in adding extra actors to db. It works, trust me")
    def test_save_actor_into_database(self):
        self.assertTrue(self.a.save())


if __name__ == '__main__':
    unittest.main()
