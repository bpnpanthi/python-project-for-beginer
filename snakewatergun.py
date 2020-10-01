import random
import time
#points
me,com=0,0
i=0
print("\t\t\t WELCOME TO SNAKE WATER GAME \t\t\t")
while i!=10:
    print("Com is making his choice:")
    time.sleep(1)
    p=random.choice(['s','w','g'])
    print("Now Your Turn")
    q=input()
    if p=='s' and q=='w':
        com+=1
    elif p=='w' and q=='g':
        com+=1
    elif p=='g' and q=='s':
        com+=1
    else:
        me+=1
    i+=1 
print('Point Table\n1.ME={}\n2.COM={}'.format(me,com))
if me>com:
    print("User Won!!!")
elif me==com:
    print("TIE!!!!")
else:
    print("Computer Wins!!!")
    

