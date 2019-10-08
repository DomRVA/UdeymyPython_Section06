# i is generally used as the "index" variable

# for i in range(1,20): #for loop ends at 20, so i only goes to 19
#     print("i is now {}".format(i))

number = '9,223,372,036,854,775,807'
for i in range(0, len(number)): #len() counts the length of a string
    print(number[i])

number = '9,223,372,036,854,775,807'
cleanedNumber = ""
for i in range(0, len(number)): #len() counts the length of a string
    if number[i] in '0123456789':
        cleanedNumber = cleanedNumber + number[i]
     #   print(number[i], end='')
newNumber = int(cleanedNumber)
print("The number is {} ".format(newNumber))

