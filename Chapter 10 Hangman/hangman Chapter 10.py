def hangman(word):
    wrong = 0
    stages = ["",
              "__________      ",
              "|               ",
              "|         |     ",
              "|         0     ",
              "|        /|\    ",
              "|        / \    ",
              ]
    #word = "word"
    theletter = list(word)
    space = len(word) * ["____"]
    win = False
    print("Welcome to Hangman")
    print(space)
    while wrong < len(stages)-1:
    #print("guess a letter")
        letter = input("guess a letter: ")
        if letter in theletter:
            swap = theletter.index(letter)
            space[swap] = letter
            theletter[swap] = '$'
        else:
            wrong +=1
        #print(space)
        print((" ".join(space)))        #join cac cai gach lai
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "____" not in space:
            print("You win")
            print(" ",join(space))
            win = True
            break
hangman("cat")
    
