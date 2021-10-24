def palindrome1(input):
    string1 = list(input)
    length1 = len(string1)
    if length1 == 0 or length1==1:
        print("true")
    elif string1[0]==string1[-1]:
            del string1[0]
            del string1[-1]
            return palindrome1(string1)
    else:
        print("false")






