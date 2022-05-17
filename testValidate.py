import unittest
from decimaltoRoman import DecimalRoman 
    
class TestValidateRoman(unittest.TestCase):
  def test_value_1(self):
      self.assertEqual('Valor fuera del rango', DecimalRoman.validate())

if __name__ == '__main__':
  unittest.main()