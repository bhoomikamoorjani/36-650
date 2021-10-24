def one_away(str1,str2):
    str1_2= list(str1)
    str2_2= list(str2)
    m=len(str1_2)
    n=len(str2_2)
    if abs(m-n) >1:
        print("false")
    else:
        if number_of_edits(str1_2,str2_2,m,n)>1:
            print("false")
        else:
            print("true")

def number_of_edits(str1_2, str2_2, m,n):
    count,i,j=0,0,0
    while i<m and j<n:
        if str1_2[i] != str2_2[j]:
            if m>n:
                i,count=i+1, count+1
            elif m<n:
                j,count=j+1, count+1
            else:
                i,j,count=i+1, j+1, count+1
        else:
            i,j=i+1, j+1
    if i<m or j<n:
        count+=1 
    return count

one_away("pale", "ple")
one_away("pales", "pale")
one_away("pale", "bale")
one_away("pale", "bake")
