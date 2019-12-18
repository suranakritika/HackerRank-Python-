# Code

vowels=["A","E","I","O","U"]

def minion_game(string):
    stu=0
    kevin=0
    for i in range(len(s)):
        if s[i] not in vowels:
            stu += len(s) - i
        elif s[i] in vowels:
            kevin += len(s)-i

    if(kevin==stu):
        print("Draw")
    elif(kevin<stu):
        print("Stuart",stu)
    else:
        print("Kevin", kevin)
