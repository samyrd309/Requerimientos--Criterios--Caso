class DecimalRoman(object):
  
  def decimal_to_roman(value):
    if value == None or value =='':
        romanOutput = 'Invalid value. Please insert a not null value.'
        return romanOutput
    else:
      value = int(value)
      if value >= 2000000 or value <= 0:
        romanOutput = 'Invalid value. Please insert a value inside the range value > and value < 2000000'
      else:
        romanValue = [1000000, 900000, 500000, 400000, 100000, 90000, 50000, 40000, 10000, 9000, 5000, 4000, 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romanSymbols = ['M`', 'C`M`', 'D`', 'C`D`', 'C`', 'X`C`', 'L`', 'X`L`','X`','I`X`','V`','I`V`','M','CM','D','CD','C','XC','L', 'XL', 'X', 'IX','V','IV','I' ]
        i = 0
        romanOutput = ''
        for i in range(len(romanValue)):
          while value >= romanValue[i]:
            romanOutput += romanSymbols[i]
            value -=  romanValue[i]
    return romanOutput
  romanInput = input('Insert value: ')
  print(decimal_to_roman(romanInput))          
    
