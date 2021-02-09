import random
cchoice=["rock","paper","scissor"]
while True:
    print("Welcome to thr rock paper scissor game : ")
    youwin,computerwin=0,0
    for i in range(1,6): # 5 rounds of game 
        print("round",i, "start")
        print("please enter your choice :")
        print("1.rock","2.paper","3.scissor")

        yourchoice=int(input())

        if yourchoice==1:
            print("you select rock")
            yourchoice="rock"
        elif yourchoice==2:
            print("you select paper")
            yourchoice="paper"
        elif yourchoice==3:
            print("you seect scissor")
            yourchoice="scissor"
        else:
            print("invalid choose")
            break

        computerchoice=random.choice(cchoice)
        print("computer choice is : ", computerchoice)

        if yourchoice== computerchoice:
            print("matchh is tied..")
            youwin+=1
            computerwin+=1
        elif (yourchoice=="paper" and computerchoice=="rock") or (yourchoice=="scissor" and computerchoice=="paper") or(yourchoice=="rock"and computerchoice=="scissor"):
            print("you won this round")
            youwin+=1

        else:
            computerwin+=1
            print("computer win")

    if youwin== computerwin:
        print("you won the game, your score is :",youwin, "computer score is:", computerwin)

    elif youwin>computerwin:
        print("computer won the game, your score is :",youwin, "computer score is:", computerwin)

    elif youwin< computerwin:
        print("computer won the game, your score is :",youwin, "computer score is:", computerwin)
    else:
        print("match tie")

    user_choice=input("do you want to play again?(yes/no")
    if user_choice=="yes":
       continue
    else:
       break     

