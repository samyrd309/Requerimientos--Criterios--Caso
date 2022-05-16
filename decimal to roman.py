import unittest

class DecimalRoman(object):
  def decimal_to_roman(value):
    romanValue = [1000000, 900000, 500000, 400000, 100000, 90000, 50000, 40000, 10000, 9000, 5000, 4000, 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romanSymbols = ['M`', 'C`M`', 'D`', 'C`D`', 'C`', 'X`C`', 'L`', 'X`L`','X`','I`X`','V`','I`V`','M','CM','D','CD','C','XC','L', 'XL', 'X', 'IX','V','IV','I' ]
    romanOutput = ''
   
    
    while value != None:
        remain = value
        i = 0
        for _ in range(value // romanValue[i]):
          romanOutput += romanSymbols[i]
          remain -=  romanValue[i]
        return romanOutput
  
  print(decimal_to_roman(5))  


