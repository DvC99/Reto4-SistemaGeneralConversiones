import methods as met
sw = "Si"
while(sw == "Si"):
  print("Digite la opcion que desea usar:")
  op = input("""   1 -> Si desea pasar un numero de Decimal a Binario
   2 -> Si desea pasar un numero de Binario a Decimal
   3 -> Si desea pasar un numero de Decimal a Octal
   4 -> Si desea pasar un numero de Ocatl a Decimal
   5 -> Si desea pasar un numero de Decimal a Hexa
   6 -> Si desea pasar un numero de Hexa a Decimal
   7 -> Si desea pasar un numero de Decimal a Romano
   8 -> Si desea pasar un numero de Romano a Decimal\n""")

  num = int(input("Digite el numero: \n"))
  if(op == "1"):
    met.decimalToBinary(num)
  elif(op == "2"):
    met.binaryToDecimal(num)
  elif(op == "3"):
    met.decimalToOctal(num)
  elif(op == "4"):
    met.octaToDecimal(num)
  elif(op == "5"):
    met.decimalToHexa(num)
  elif(op == "6"):
    met.hexaToDecimal(num)
  elif(op == "7"):
    met.decimalToRoman(num)
  elif(op == "8"):
    met.romanToDecimal(num)


  sw = input("Desea seguir con el programa: Si/No\n")
  