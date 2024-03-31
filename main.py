def main():
  currentString = '1'
  j = 0
  while (j < 100):
    if not set(currentString).issubset({'1', '2', '3', '\n', '\t'}):
      print("Error: Invalid characters in currentString. Only '1', '2', and '3' are allowed.")
      return
    currentString = createNextString(currentString)
    print(currentString)

def createNextString(currentString):
  currentString = currentString.replace('\t', '').replace('\n', '').strip()
  nextString = ''
  index = 0
  currentNum = 0
  currentCount = 0
  while index < len(currentString):
    if currentNum == int(currentString[index]):
      currentCount += 1
    else:
      if currentNum != 0:
        nextString += str(currentCount) + str(currentNum)
      currentNum = int(currentString[index])
      currentCount = 1
    index += 1
  nextString += str(currentCount) + str(currentNum) + '\n'
  return nextString

if __name__ == '__main__':
  main()