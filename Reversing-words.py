#Write a Python program that accepts a word from the user and reverse it.
# Request user to type in a word
# Display the word in reverse order

var1 = input("Type a word to be displayed in reverse ")
var2 = len(var1) -1
var3 = ""

for i in range(var2, -1, -1):
    var3 = var3 + var1[i]
print (var3)
