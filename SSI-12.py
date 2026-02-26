import time
import random
import math

print("SSI-12")
def Sim():
  In1 = input("1st number is")
  In2 = input("2nd number is")
  In3 = input("Function for the 2 numbers are")
  print("SSI-11")
  print("processing...")
  In2 = (int(In2))
  In1 = (int(In1))
  time.sleep(1.5)
  if In3 == "*":
    print(In1 * In2)
    print("is the answer")
    time.sleep(1)
    print(" ")
    Sim()
  elif In3 == "+":
    print(In1 + In2)
    print("is the answer")
    time.sleep(1)
    print(" ")
    Sim()
  elif In3 == "/":
    print(In1 / In2)
    print("is the answer, or")
    result = In1 - (In1 % In2)
    print(result)
    print("remainder")
    print(In1 % In2)
    time.sleep(1)
    print(" ")
    Sim()
  elif In3 == "-":
    print(In1 - In2)
    print("is the answer")
    time.sleep(1)
    print(" ")
    Sim()
  elif In3 == "sqrt":
    print(math.sqrt(In2))
    print("is the answer")
    time.sleep(1)
    Sim()
  elif In3 == "sq":
    print(In2 * In2)
    print("is the answer")
    time.sleep(1)
    Sim()
  elif In1 == "0":
    print(" ")
  elif In3 == "^":
    print(math.pow(In1, In2))
    print("is the answer")
    time.sleep(1)
    Sim()
  elif In3 == "abs":
    print(math.fabs(In2))
    print("is the answer")
    time.sleep(1)
    Sim()
  elif In3 == "!":
    print(math.factorial(In2))
    print("is the answer")
    time.sleep(1)
    Sim()
  elif In3 == "rando":
    print(random.randint(In1, In2))
    print("is the number")
    time.sleep(1)
    Sim()
  else:
    print("Unacceptable answer, try again")
    time.sleep(1)
    print(" ")
    Sim()
Sim()
