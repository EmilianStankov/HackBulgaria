import unittest
import timer


class TimerTests(unittest.TestCase):

    def test_started_timer(self):
        self.assertEqual(False, timer.start_timer())


if __name__ == '__main__':
    unittest.main()
