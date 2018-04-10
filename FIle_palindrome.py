with open('File_palindrome.txt') as f:  #open a file

    for str in f:   #Run a loop and store each line in str
        str1 = ''
        for char in str:   #Removing Non alphanumeric characters
            if(ord(char)>= 97 and ord(char)<= 122 or ord(char)>= 65 and ord(char) <= 90 or
                    ord(char)>= 48 and ord(char) <= 57):
                str1 = str1+char

        str2 = str1[::-1]  #reversing the string


        if (str1.casefold()== str2.casefold()): # comparing both string
            print(str1 + ":- palindrome\n")
        else:
            print(str1 + ":- Not a palindrome\n\n")