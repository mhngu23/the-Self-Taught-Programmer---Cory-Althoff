#Create a list of dictionary contain your attribute
attribute = {"age" : "23",
            "height" : "1m75",
            "favorite_color" : "red",
            "favorite_artist" : "GD"}
input1 = input("choose from age, height, favorite_color and favorite_artist: ")
if input1 in attribute:
    input1 = attribute[input1]
    print(input1)
else:
    print("not found")
    
