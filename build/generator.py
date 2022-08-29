from random import randint
def generate(lenPassword) :
  # const
  lowerCaseLetters = "abcdefghijklmnopqrstuvwxyz"
  capitalCaseLetters = lowerCaseLetters.upper()
  numbers = "0123456789"

  choices = capitalCaseLetters + lowerCaseLetters + numbers
  password = ""
  for i in range (lenPassword) :
    r = randint(0, len(choices)-1)
    password += choices[r]
  return password

def generateName(lenPassword) :
  # const
  lowerCaseLetters = "abcdefghijklmnopqrstuvwxyz"
  capitalCaseLetters = lowerCaseLetters.upper()

  choices = capitalCaseLetters + lowerCaseLetters
  password = ""
  for i in range (lenPassword) :
    r = randint(0, len(choices)-1)
    password += choices[r]
  return password