import unittest
import json
import Solution

class UnitTest(unittest.TestCase):

    def validate(self,actual,expected):
        for location, count in actual.items():
            self.assertEqual(count,expected[location])

    def test_findStoreCount_HappyPath(self):
        stores = [{"x": 5, "y": 3}, {"x": 0, "y": 0}, {"x": 4, "y": 3}, {"x": 3, "y": 3}, {"x": 2, "y": 3},
                  {"x": 1, "y": 3}, {"x": 0, "y": 3}, {"x": -1, "y": 3}, {"x": 5, "y": 3}, {"x": 0, "y": 0},
                  {"x": 5, "y": 3}]
        exptected = {(5, 3): 3, (0, 0): 2, (4, 3): 1, (3, 3): 1, (2, 3): 1, (1, 3): 1, (0, 3): 1, (-1, 3): 1}
        obj=Solution.StoreCounter()
        actualOutput = obj.findStoreCount(stores)

        self.validate(actualOutput,exptected)

    def test_findStoreCount_EmptyInput(self):
        stores = []
        exptected = {}
        obj = Solution.StoreCounter()
        actualOutput = obj.findStoreCount(stores)

        self.validate(actualOutput,exptected)

    def test_findStoreCount_invalidInput(self):
        stores = None
        exptected = {}
        obj = Solution.StoreCounter()
        actualOutput = obj.findStoreCount(stores)

        self.validate(actualOutput,exptected)

    def test_customInputFromFile(self):
        with open('input.json') as f:
            stores = json.load(f)

        obj = Solution.StoreCounter()
        actualOutput = obj.findStoreCount(stores)
        for store,count in actualOutput.items():
            print("Store with location {0} has been visited {1} times".format(store,count))

if __name__ == '__main__':
    unittest.main()