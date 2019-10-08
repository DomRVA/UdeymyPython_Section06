_author_ = 'Dom'
# name = input("Please enter your name: ")
# age = int(input("How old are you, {0}? ".format(name)))
# print(age)

# if age >= 18:
#     print("You are old enough to vote.")
#     print("Please put an X in the box. ")
# else:
#     print("Please come back in {0} years".format(18-age))

# print("Please guess a number between 1 and 10")
# guess = int(input())

# if 1 <= guess <= 10:
#     if guess <5:
#         print("Please guess Higher")
#         guess = int(input())
#         if guess == 5:
#             print("Well done, you guessed it! :D")
#         else:
#             print("Sorry, you have not guessed it correctly. :(")
#     elif guess >5:
#         print("Please guess Lower")
#         guess = int(input())
#         if guess == 5:
#             print("Well done, you guessed it! :D")
#         else:
#             print("Sorry, you have not guessed it correctly. :(")
#     else:
#         print("You got it on the first try!!!")
# else:
#     print("No, No, No, please enter a number between 1 and 10!  DO IT AGAIN!")

# cleaning up the code

print("Please guess a number between 1 and 10")
guess = int(input())

if 1 <= guess <= 10:
    if guess != 5:
        if guess < 5:
            print("Please guess Higher")
        else:  # guess must be greater than 5
            print("Please guess Lower")
        guess = int(input())
        if guess == 5:
            print("Well done, you guessed it! :D")
        else:
            print("Sorry, you have not guessed it correctly. :(")
    else:
        print("You got it on the first try!!!")
else:
    print("No, No, No, please enter a number between 1 and 10!  DO IT AGAIN!")
