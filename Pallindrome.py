def Pallindrome(str):
    str1 = ""
    str2 = ""

    for char in str:
        if(ord(char)>= 97 and ord(char)<= 122 or ord(char)>= 65 and ord(char) <= 90 or
                ord(char)>= 48 and ord(char) <= 57):
            str1 = str1+char
    str2 = str1[::-1]
    print(str1+"\n")
    print(str2+ "\n")


    if (str1.lower() == str2.lower()):
        print("palindrome")
    else:
        print("not")

string1 = "a@bC#1221c!bA"
Pallindrome(string1)