_author_ = 'Dom'
name = input("Welcome to the 18-30 Holiday Club!\nPlease enter your name: ")
print("Welcome " + name + "!")
age = int(input("How old are you? "))
if 18 <= age < 31:
    print("Welcome to the Holiday Club! :D")
else:
    print("We're sorry, but you are outside of our allotted age range :(")