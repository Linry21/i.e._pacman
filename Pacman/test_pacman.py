import unittest
from pacman import Pacman

class TestPacman(unittest.TestCase):
    def test_place(self):
        pacman_1 = Pacman(0,0,0)
        pacman_1.place(1,2,"SOUTH")

        self.assertEqual(pacman_1.x, 1)
        self.assertEqual(pacman_1.y, 2)
        self.assertEqual(pacman_1.direction, 2)

    def test_move(self):
        pacman_1 = Pacman(0,0,0)
        pacman_2 = Pacman(6,0,1)

        pacman_1.move()
        pacman_2.move()

        self.assertEqual(pacman_1.x, 0)
        self.assertEqual(pacman_1.y, 1)
        self.assertEqual(pacman_2.x, 6)
        self.assertEqual(pacman_2.y, 0)
        
    def test_left(self):
        pacman_1 = Pacman(0,0,0)
        pacman_2 = Pacman(6,0,1)

        pacman_1.left()
        pacman_2.left()

        self.assertEqual(pacman_1.direction, -1)
        self.assertEqual(pacman_2.direction, 1)

    def test_right(self):
        pacman_1 = Pacman(0,0,0)
        pacman_2 = Pacman(6,0,1)

        pacman_1.right()
        pacman_2.right()

        self.assertEqual(pacman_1.direction, 1)
        self.assertEqual(pacman_2.direction, 1)

if __name__ == '__main__':
    unittest.main()