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
        pacman_3 = Pacman(0,5,0)
        pacman_4 = Pacman(0,0,1)
        pacman_5 = Pacman(0,0,2)
        pacman_6 = Pacman(0,2,2)
        pacman_7 = Pacman(0,0,3)
        pacman_8 = Pacman(2,0,3)
        

        pacman_1.move()
        pacman_2.move()
        pacman_3.move()
        pacman_4.move()
        pacman_5.move()
        pacman_6.move()
        pacman_7.move()
        pacman_8.move()

        self.assertEqual(pacman_1.y, 1)
        self.assertEqual(pacman_2.x, 6)
        self.assertEqual(pacman_3.y, 5)
        self.assertEqual(pacman_4.x, 1)
        self.assertEqual(pacman_5.y, 0)
        self.assertEqual(pacman_6.y, 1)
        self.assertEqual(pacman_7.x, 0)
        self.assertEqual(pacman_8.x, 1)

        
    def test_left(self):
        pacman_1 = Pacman(0,0,0)
        pacman_2 = Pacman(6,0,1)

        pacman_1.left()
        pacman_2.left()

        self.assertEqual(pacman_1.direction, 3)
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