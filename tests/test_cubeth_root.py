import unittest


from tasks.cubeth_root import find_cube_root


class TestCubeRoot(unittest.TestCase):
    def test_cube_root(self):
        self.assertEqual(find_cube_root(27), 3)
        
    def test_cube_root_3(self):
        self.assertEqual(find_cube_root(8), 2)
        
    def test_cube_root_4(self):
        self.assertEqual(find_cube_root(1), 1)


if __name__ == "__main__":
    unittest.main()