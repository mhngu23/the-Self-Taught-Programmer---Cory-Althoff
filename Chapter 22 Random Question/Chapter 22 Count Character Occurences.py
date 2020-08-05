def count_Character_Occurence(string):
    count_dict = {}
    for c in string:
        if c in count_dict:
            count_dict[c] += 1
        else:
            count_dict[c]=1
    print(count_dict)

str1 = "ACBAHCBHBSC"
count_Character_Occurence(str1)
