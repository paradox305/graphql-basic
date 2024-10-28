import unittest
from geometry import calculate_bounding_box, rotate_mesh, move_mesh, is_polygon_convex

class TestGeometry(unittest.TestCase):
    def test_bounding_box(self):
        points = [{"x": 0, "y": 0, "z": 0}, {"x": 1, "y": 1, "z": 1}]
        result = calculate_bounding_box(points)
        expected = {"minPoint": {"x": 0, "y": 0, "z": 0}, "maxPoint": {"x": 1, "y": 1, "z": 1}}
        self.assertEqual(result, expected)

    def test_rotate_mesh(self):
        mesh = [{"x": 1, "y": 0, "z": 0}]
        result = rotate_mesh(mesh, 90, "Z")
        expected = [{"x": 0, "y": 1, "z": 0}]
        self.assertAlmostEqual(result[0]["x"], expected[0]["x"], places=5)

    def test_move_mesh(self):
        mesh = [{"x": 1, "y": 1, "z": 1}]
        result = move_mesh(mesh, 1, 1, 1)
        expected = [{"x": 2, "y": 2, "z": 2}]
        self.assertEqual(result, expected)

    def test_is_convex(self):
        points = [{"x": 0, "y": 0, "z": 0}, {"x": 1, "y": 0, "z": 0}, {"x": 0, "y": 1, "z": 0}]
        self.assertTrue(is_polygon_convex(points))

if __name__ == '__main__':
    unittest.main()
