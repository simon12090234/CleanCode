import unittest

import sys 
sys.path.append("src")

from src.model import app


class Programmed_savings_test(unittest.TestCase):

    def test_normal_1(self):
        amount = 300000
        interest = 0.035
        period = 24

        result = app.Calculate_programmed_savings(amount, interest, period)
        expected = 7451971.429
        self.assertAlmostEqual(expected, result, 2)
    
    def test_normal_2(self):
        amount = 500000
        interest = 0.06
        period = 36

        result = app.Calculate_programmed_savings(amount, interest, period)
        expected = 19079983.33
        self.assertAlmostEqual(expected, result, 2)
    
    def test_normal_3(self):
        amount = 1000000
        interest = 0.1
        period = 60

        result = app.Calculate_programmed_savings(amount, interest, period)
        expected = 65999990
        self.assertAlmostEqual(expected, result, 2)
    
    def test_normal_4(self):
        amount = 250000
        interest = 0.05
        period = 1

        result = app.Calculate_programmed_savings(amount, interest, period)
        expected = 262480
        self.assertAlmostEqual(expected, result, 2)
    
    def test_normal_5(self):
        amount = 200000
        interest = 0.045
        period = 12

        result = app.Calculate_programmed_savings(amount, interest, period)
        expected = 2507977.778
        self.assertAlmostEqual(expected, result, 2)
    
    def test_extraordinary_1(self):
        amount = 1000000
        interest = 0.02
        period = 1

        result = app.Calculate_programmed_savings(amount, interest, period)
        expected = 1019950
        self.assertAlmostEqual(expected, result, 2)
    
    def test_extraordinary_2(self):
        amount = 200000
        interest = 0.05
        period = 600

        result = app.Calculate_programmed_savings(amount, interest, period)
        expected = 125999980
        self.assertAlmostEqual(expected, result, 2)
    
    def test_extraordinary_3(self):
        amount = 500000
        interest = 1
        period = 12

        result = app.Calculate_programmed_savings(amount, interest, period)
        expected = 11999999
        self.assertAlmostEqual(expected, result, 2)
    
    def test_error_1(self):
        amount = 300000
        interest = -0.05
        period = 12

        with self.assertRaises( app.Invalidinterest ):
            app.Calculate_programmed_savings( amount, interest, period )
    
    def test_error_2(self):
        amount = 500000
        interest = 0.06
        period = -12

        with self.assertRaises( app.Invalidmonths ):
            app.Calculate_programmed_savings( amount, interest, period )
    
    def test_error_3(self):
        amount = 600000
        interest = 0
        period = 24

        with self.assertRaises( app.Invalidinterest ):
            app.Calculate_programmed_savings( amount, interest, period )
    
    def test_error_4(self):
        amount = 400000
        interest = 1.5
        period = 12

        with self.assertRaises( app.Invalidinterest ):
            app.Calculate_programmed_savings( amount, interest, period )
    
if __name__ == '__main__':
    unittest.main()