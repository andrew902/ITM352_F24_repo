# Ask the user to enter an arbitrary sentence. Calculate the length of that 
# string and return that value.

sentence = input("Enter a sentence: ")

string_length = len(sentence)
outputString = "You entered " + sentence +"\" . It has length " + str(string_length)
print("You entered ", sentence, "It has length ", string_length)

