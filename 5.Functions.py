# def alexsFunction():
#     print("Hello")
#     print("I am Alex")
#     print("I like snowboarding")

# print("I am going to call a function")
# alexsFunction()
# print("I have finished calling the function")

def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((8, 2, 3, 0, 7)))