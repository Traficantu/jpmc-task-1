import sys
import unittest
import client as testClient


class TestGetDataPoint(unittest.TestCase):

    def testNonEmptyDataPoint(self):
        # check we return what is expected if input is right
        self.assertEqual(testClient.getDataPoint(
            {
                'id': '0.5896328914492147',
                'stock': 'ABC',
                'timestamp': '2019-03-05 17:49:40.846183',
                'top_bid': {'price': 112.79, 'size': 80},
                'top_ask': {'price': 113.04, 'size': 93}
            }),
            ('ABC', 112.79, 113.04, 112.915))

    def testIllegalDataPoint(self):
        # check we error if input is not the right type
        self.assertRaises(TypeError, testClient.getDataPoint({
            'id': '0.5896328914492147',
            'stock': 'ABC',
            'timestamp': '2019-03-05 17:49:40.846183',
            'top_bid': {'price': '112.79', 'size': 80},
            'top_ask': {'price': '113.04', 'size': 93}}))
        
class TestGetRatio(unittest.TestCase):

    def testCorrectRatioInt(self):
        self.assertEqual(testClient.getRatio(1,2),0.5)
    
    def testCorrectRatioFloat(self):
        self.assertEqual(testClient.getRatio(1.0,2.0),0.5)
    
    def testCorrectRatioNegative(self):
        self.assertEqual(testClient.getRatio(-1.0,-2.0),0.5)

if __name__ == '__main__':
    unittest.main()
