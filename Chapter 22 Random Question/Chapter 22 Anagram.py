def Anagram(a,b):
    is_Anagram = False
    if sorted(a) == sorted(b):
        is_Anagram = True
    return is_Anagram

str1 = "cinema"
str2 = "iceman"
print(Anagram(str1,str2))
