import random


randnum = random.randrange(1,100)
userguess = None
# print(randnum)
Gusess = 0

while (userguess != randnum):
    Gusess += 1
    try:
        userguess = int(input('Guess the no.'))
    except Exception:
        print("input only integer number")
    # if (userguess != int()):
    #     print('input only integer number')
    if (userguess == randnum):
        print("your guess is right\n")
    else:
        if (userguess>randnum):
            print('guess is too Higer, pleas guess Lower')
        else:
            print('guess is too Lower, pleas guess Higher')

print(f"your total Gusess is {Gusess}")


with open("score.txt", 'r') as f:
    my_score = int(f.read())
print(f"my last high score is: {my_score}")

if(Gusess < my_score):
    with open("score.txt", 'w') as f:
        print(f"you have just brock the last score is {my_score}")
        f.write(str(Gusess))