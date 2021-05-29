romanos = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),(50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
def decimalToBinary(num):
  print(format(num,"b"))

def binaryToDecimal(num):
  print(int(num,2))

def decimalToOctal(num):
  print(format(num,"o"))

def octaToDecimal(num):
  print(int(num,8))

def decimalToHexa(num):
  print(format(num,"x"))

def hexaToDecimal(num):
 print(int(num,16))

def decimalToRoman(num):
  numroman = '' 
  while num > 0:
    for i,r in romanos:     
      while num >= i:
          numroman = numroman + r
          num = num - i
  print(numroman)

def romanToDecimal(num):
  numDec = 0 
  for i,r in romanos:  
    while(num.find(r) == 0):
      numDec = numDec + i
      num = num[len(r):]
  print(numDec)
