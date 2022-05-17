class DecimalRoman(object):
  def decimal_to_roman(value):
    while value != None:
      romanValue = [1000000, 900000, 500000, 400000, 100000, 90000, 50000, 40000, 10000, 9000, 5000, 4000, 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
      romanSymbols = ['M`', 'C`M`', 'D`', 'C`D`', 'C`', 'X`C`', 'L`', 'X`L`','X`','I`X`','V`','I`V`','M','CM','D','CD','C','XC','L', 'XL', 'X', 'IX','V','IV','I' ]
      i = 0
      romanOutput = ''
      for i in range(len(romanValue)):
        while value >= romanValue[i]:
          romanOutput += romanSymbols[i]
          value -=  romanValue[i]
      return romanOutput
    
  def validate():
    while True:
      romanInput = input('Ingresar valor: ')
      try:
        romanInput = int(romanInput)
        if romanInput < 2000000 and romanInput > 0:
          return romanInput
        else:
          romanInput ='Valor fuera del rango'
          return romanInput
      except ValueError:
        print('Valor ingresado invalido')
  
  value  = validate()
  print(decimal_to_roman(value))          
    
