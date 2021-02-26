import unittest
import Solution

class UnitTest(unittest.TestCase):
    def validate(self,actual,expted):
        print(actual)
        for location, count in actual.items():
            self.assertEqual(count,expted[location])

    def test_findStoreCount_HappyPath(self):
        stores = [{"x": 5, "y": 3}, {"x": 0, "y": 0}, {"x": 4, "y": 3}, {"x": 3, "y": 3}, {"x": 2, "y": 3},
                  {"x": 1, "y": 3}, {"x": 0, "y": 3}, {"x": -1, "y": 3}, {"x": 5, "y": 3}, {"x": 0, "y": 0},
                  {"x": 5, "y": 3}]
        obj = Solution.StoreCounter()

        exptected = {(5, 3): 3, (0, 0): 2, (4, 3): 1, (3, 3): 1, (2, 3): 1, (1, 3): 1, (0, 3): 1, (-1, 3): 1}
        actualOutput = obj.findStoreCount(stores)

        self.validate(actualOutput,exptected)

    def test_findStoreCount_EmptyInput(self):
        stores = []
        obj = Solution.StoreCounter()

        exptected = {}
        actualOutput = obj.findStoreCount(stores)

        self.validate(actualOutput,exptected)

    def test_findStoreCount_invalidInput(self):
        stores = None
        obj = Solution.StoreCounter()
        exptected = {}
        actualOutput = obj.findStoreCount(stores)

        self.validate(actualOutput,exptected)

if __name__ == '__main__':
    unittest.main()