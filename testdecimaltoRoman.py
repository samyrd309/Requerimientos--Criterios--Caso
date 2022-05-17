import unittest
from decimaltoRoman import DecimalRoman 
    
class TestDecimalRoman(unittest.TestCase):
    
  def test_value_None(self):
      self.assertEqual('Invalid value. Please insert a not null value.', DecimalRoman.decimal_to_roman(None))
  def test_value_out_of_range(self):
      self.assertEqual('Invalid value. Please insert a value inside the range value > and value < 2000000', DecimalRoman.decimal_to_roman(0))
  def test_value_1(self):
      self.assertEqual('I', DecimalRoman.decimal_to_roman(1))
  def test_value_2(self):
      self.assertEqual('II', DecimalRoman.decimal_to_roman(2))  
  def test_value_3(self):
      self.assertEqual('III', DecimalRoman.decimal_to_roman(3))
  def test_value_4(self):
      self.assertEqual('IV', DecimalRoman.decimal_to_roman(4))
  def test_value_5(self):
      self.assertEqual('V', DecimalRoman.decimal_to_roman(5))
  def test_value_6(self):
      self.assertEqual('IX', DecimalRoman.decimal_to_roman(9))

if __name__ == '__main__':
  unittest.main()