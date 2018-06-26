#The Multiplication Table
print('MULTIPLICATION TABLE \n')

for i in range(1, 11):
    for j in range(1, 11):
        print((i),'X',(j),'=',(i*j))
    print('\n')

#The Addition Table
print('ADDITION TABLE \n')

for i in range(1, 11):
    for j in range(1, 11):
        print((i),'+',(j),'=',(i+j))
    print()

#The Division Table
print('DIVISION TABLE \n')

for i in range(1, 11):
    for j in range(1, 11):
      division = (i/j)
#I rounded up the division to 2 decimal place
      output = round(division,1)
      print((i),'/',(j),'=',output) 
    print()