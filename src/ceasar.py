#ceasar.py

#Function for ceaser ciphers
#receives input from GUI defined in main.py, executes ceasar cipher and returns output
#to main.py

def ceasar(input,shift):
  #type check for security
  input = str(input)
  shift = int(shift)
  #check to make sure shift is not 0
  if shift == 0:
    print("ERROR: shift = 0 will result in null encryption")
    return
  #alphabet #TODO check for array syntax, need constant time lookups
  alphaNum = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9',' ']
  betSize = len(alphaNum)
  #mod shift to simplify further ops
  shift = shift%betSize
  #instantiate ciphered vars
  outList = []
  #iterate through input
  for c in input:
    #get index of c
    index = alphaNum.index(c)
    #check for unsupported character
    if index < 0:
      print("ERROR: Unsupported character \'"+c+"\'")
      return
      #TODO find the actual error syntax in python
    #get ciphered c
    ciph = alphaNum[(index + shift)%betSize]
    #add to outList
    outList.insert(0,ciph)
  #convert to string
  outList.reverse()
  output = ''.join(outList)
  print(input,shift,output)
  return output
  
#main function for testing

if __name__ == '__main__':
  #defaults
  inp = "Hello World"
  shi = 1
  test = ceasar(inp,shi)
  if test != "IfmmpaXpsme":
    print("ERROR: \'Hello World\' shift 1")
  test = ceasar("Go Army Beat Navy",25)
  if test != "5NyZQLXy0DzSybzUX":
    print("ERROR: \'Go Army Beat Navy\' shift 25")