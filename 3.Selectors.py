# inputvar1 = int(input("type a num: "))
# var1 = 5

# if inputvar1 > 5:
  #  print("your input was greater than 5")

# else:
 #   print("Your input was less than 5")


#listvar1 = ["Todd Malone", "Dana Stanton", "Len Trujillo", "Cornell Mcguire", "Earnestine Cherry"]
#if "Len Trujillo" in listvar1:
 #   print ("Len is in the list")
#else:
  #  print ("Len is not in the list")

inputvar1 = input ("Type a letter in the alphabet: ")
vowl = "aeiou"
consonant = "bcdfehiklmnpqrstvwxyz"

if inputvar1 in vowl: 
    print("It was a vowl")
elif inputvar1 in consonant:
        print("it was a consonant")
else:
    print ("you didn't type an alphabet letter")