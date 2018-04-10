
#function to reverse a string
def Reverse(input):

    #split words of string seperated by space
    input_string = input.split(" ")

     #put the word of string in a reverse order in a list
    input_string = input_string[-1::-1]

     #Join the words with space
    output_string = ' '.join(input_string)

    #return the string
    return output_string



# calling the Reverse function
print(Reverse("Rishabh Saxena"))