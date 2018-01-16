# Are you ready for this? Follow along with the steps to get the secret message

var1 = "lists"
var2 = "made"

# Create a list in the variable list_one with the data "summer", 1, 0, 1, 0, 1, and "fall" in that order
list_one = ["summer", 1, 0, 1, 0, 1, "fall"]

# Create a list in the variable list_two with the data "cake", "with", "in", False, and "nooo" in that order
list_two = ["cake", "with", "in", False, "nooo"]

# Create a list in the variable list_three with the data "all", "RMOTR", "programs", "love", and "me" in that order
list_three = ["all", "RMOTR", "programs", "love", "me"]

# Create an empty list and store it in the variable secret_message
secret_message = []

# Append the second item of list_three to secret_message
secret_message.append(list_three[1])

# Pop the third item from list_two and store it in a variable called var3
var3 = list_two.pop(2)

# Write an if statement checking if the length of list_two is 4
# If it is, append var2 to secret_message
# Otherwise, append the first item of list_two to secret_message
if len(list_two) == 4:
    secret_message.append(var2)
else:
    secret_message.append(list_two[0])

# Create a list in the variable list_four with the last element from list_three in it
list_four = [list_three[-1]]

# Write an if statement checking if length of list_one is 8
# If it is, remove "love" from list_three
# Otherwise, append the last element of list_one to list_four
if len(list_one) == 8:
    list_three.remove("love")
else:
    list_four.append(list_one[-1])

# Use list addition to add secret_message and list_four together, storing the result in secret_message. Can use += here
secret_message += list_four

# Append var3 to secret_message
secret_message.append(var3)

# Write an if statement checking if "cake" is in secret_message
# If it is, pop the 5th item and then the 4th item from secret_message
# Otherwise, append the 4th item of list_three to secret_message
if "cake" in secret_message:
    secret_message.pop(4)
    secret_message.pop(3)
else:
    secret_message.append(list_three[3])

# Create a list in the variable list_five with the 2nd element of list_two, "puppies", and var1 in it in that order
list_five = [list_two[1], "puppies", var1]

# Finally, write a for loop that goes through list five and appends all words that aren't puppies to secret_message
for item in list_five:
    if item != "puppies":
        secret_message.append(item)

# Run this to see if you got it right!
print(secret_message)