import unittest

class DecimalRoman(object):
  romanValue = [1000000, 900000, 500000, 400000, 100000, 90000, 50000, 40000, 10000, 9000, 5000, 4000, 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
  romanSymbols = ['M`', 'C`M`', 'D`', 'C`D`', 'C`', 'X`C`', 'L`', 'X`L`','X`','I`X`','V`','I`V`','M','CM','D','CD','C','XC','L', 'XL', 'X', 'IX','V','IV','I' ]
  
  def decimal_to_roman(self, value):
    
    while value != None:
      romanOutput = ''
      if value >= 2000000 or value < 0:
        romanOutput = 'Error'
      else:
        i = 0
        for i in range(len(self.romanValue)):
          while value >= self.romanValue[i]:
            romanOutput += self.romanSymbols[i]
            value -=  self.romanValue[i]
      return romanOutput
  def validateNum():
    while True:
      try:
        x = input('Ingrese un valor')
        x = int(x)
      except ValueError:
        print('Invalid value inserted')
  
    
  
    
class TestDecimalRoman(unittest.TestCase):
  def setUp(self):
      self.roman_class = DecimalRoman() 
  def test_value_1(self):
      roman_class = self.roman_class.decimal_to_roman(1)
      self.assertEqual('I', roman_class)
  def test_value_2(self):
      roman_class = self.roman_class.decimal_to_roman(2)
      self.assertEqual('II', roman_class)
  def test_value_3(self):
      roman_class = self.roman_class.decimal_to_roman(3)
      self.assertEqual('III', roman_class)
  def test_value_4(self):
      roman_class = self.roman_class.decimal_to_roman(4)
      self.assertEqual('IV', roman_class)
  def test_value_5(self):
      roman_class = self.roman_class.decimal_to_roman(5)
      self.assertEqual('V', roman_class)
  def test_value_9(self):
      roman_class = self.roman_class.decimal_to_roman(9)
      self.assertEqual('IX', roman_class)
  def test_value_10(self):
      roman_class = self.roman_class.decimal_to_roman(10)
      self.assertEqual('X', roman_class)
  def test_value_40000000(self):
      roman_class = self.roman_class.decimal_to_roman(40000000)
      self.assertEqual('Error', roman_class)  
if __name__ == '__main__':
  unittest.main()