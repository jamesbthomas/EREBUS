#file.py

#Functions for file I/O

#function to write to a file
#receives input from permissions.py and writes it to a csv file in the same directory

def write(key,value):
  #sterilize input
  key = str(key)
  value = str(value)
  #open the file
  f = open("EREBUS.csv","a")
  #verify open operation
  if f.closed:
    print("ERROR: Open operation failed")
  if f.mode != "a":
    print("ERROR: Access mode incorrect")
  if f.name != "EREBUS.csv":
    print("ERROR: Opened wrong file")
  #write key value pair to file
  f.write(key)
  f.write(',')
  f.write(value)
  f.write('\n')
  #close file
  f.close()
  #return key value pair
  return (key,value)

#function to read from a file
#receives input from permissions.py and returns appropriate output from the file

def read(key):
  #sterilize input, initialize output
  key = str(key)
  value = ""
  #open file for reading
  f = open("EREBUS.csv","r")
  #verify open operation
  if f.closed:
    print("ERROR: Open operation failed")
  if f.mode != "r":
    print("ERROR: Access mode incorrect")
  if f.name != "EREBUS.csv":
    print("ERROR: Opened wrong file")
  #get the lines of the file
  lines = f.readLines()
  #close file
  f.close()
  #read the lines
  for line in lines:
    #get rid of whitespace and new line characters
    line = line.strip()
    #break line into csv segments
    line = line.split(',')
    #check to see if its the key we want
    if line[0] == key:
      value = line[1]
      break
  #return key value pair
  return (key,value)

#main function for testing
if __name__ == '__main__':
  print "compile worked"