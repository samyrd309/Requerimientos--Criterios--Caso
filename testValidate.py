import unittest
from decimaltoRoman import DecimalRoman 
    
class TestValidateRoman(unittest.TestCase):
  def test_value_out_of_range(self):
      self.assertEqual('Valor fuera del rango', DecimalRoman.validate())
      
  def text_value_null(self):
    self.assertEqual('Valor ingresado invalido', DecimalRoman.validate())

if __name__ == '__main__': 
  unittest.main()