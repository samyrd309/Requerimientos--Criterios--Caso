import unittest
from decimaltoRoman import DecimalRoman 
    
class TestDecimalRoman(unittest.TestCase):
  def test_value_1(self):
      self.assertEqual('I', DecimalRoman.decimal_to_roman(1))
  def test_value_2(self):
      self.assertEqual('II', DecimalRoman.decimal_to_roman(2))  
  def test_value_3(self):
      self.assertEqual('III', DecimalRoman.decimal_to_roman(3))

if __name__ == '__main__':
  unittest.main()