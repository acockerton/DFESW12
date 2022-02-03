#count = 0
#name = str(input("What is your name?"))

#while count < 5:
 #   print(name, "is awesome!")
  #  count += 1

#for i in range(5, 11):
   # print(i)
#for i in range(10, 21, 2):
    #print(i)


#write a while loop which asks for the users name, then prints the user's name followed by "is awesome!" 5 times.

#countvar = 5
#while countvar > 0:
#    namevar1 = input("Type Name: ")
#    print(f"{namevar1} is awesome!")
#    countvar = countvar -1

#countvar = 5
#listvar = []
#while countvar > 0:
#    listvar.append(input("Type Name: "))
#    countvar = countvar -1

#for i in listvar:
#    print(f"{i} is awesome!")

count = 0
name = []

while count < 5:
    name.append(str(input("What is your name?")))
    #print(name, "is awesome!")
    count += 1

for name2 in name:
    print(name2, "is awesome!")


