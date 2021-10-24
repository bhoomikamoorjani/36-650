punctuations = list('''!()-[]{};:'"\,<>./?@#$%^&*_~''')
def remove_punctuations(str1):
    str2 = list(str1)
    for x in range(len(str2)):
        for y in punctuations:
            if str2[x]==y:
                str2[x]=""
    
    str3 = ""
    for z in str2:
        str3 += z          
    return str3

remove_punctuations("Hello in 36-650, & other MSP courses.")

str1 = "Hello in 36-650, & other MSP courses."
list(str1)

