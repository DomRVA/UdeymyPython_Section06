# age = int(input("How old are you? "))
# worker = "Have a good day at work"
# retired = "Enjoy your free time"

# if (age >= 16) and (age <=65):
# if 16<= age <=65:
#     print("Have a good day at work")

# if (age <16) or (age > 65):
#     print(retired)
# else:
#     print(worker)

# x = input("Please enter some text") #true/false

# if x:
#     print("you entered {}".format(x))
# else:
#     print("You didn't enter anything")

# if not(age < 18):
#     print("you are old enought to vote\nplease put an X in the box")
# else:
#     print("please come back in {} years".format(18-age))

parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter in parrot:
    print("Give me an {} Bob".format(letter))
else:
    print("I don't need that letter")