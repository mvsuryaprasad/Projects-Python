import random


overs=int(input("Choose No of Overs:"))
players=int(input("Choose No of Players:"))
print('\n',"Toss == 1  ----> player 1 won the toss",'\n',
      "Toss == 2  ----> player 2 won the toss")
print('\n')
T=random.randint(1,2)
print(input("Click Enter to roll the Toss:"),T)





def Toss(T):
    print('\n')
    print("Player ",T," won the Toss, Choose Batting/Fielding [B/F] :")
    d=input()
    if d=='f' or d=='F':
        d='f'
        print("###########################################################")
        print("player ",T," Chooses to Field First")
        print("###########################################################")
    elif d=='b'or d=='B':
        d='b'
        print("###########################################################",'\n')
        print("player ",T," Chooses to Bat First",'\n')
        print("###########################################################",'\n')
    return (str(T)+d)



def BookCricket(overs,players,T,team):
    TwoTeams=[]
    for i in range(0,2,1):
        print("Team ",team,' is Batting')
        (Wickets,balls,total)=(0,1,0)
        while balls<=overs*6 and Wickets<players-1:
            print("\n")
            input("Click Enter to Bat :")
            runs=random.randint(0,6)
            if runs==0:
                w=["LBW","Bowled","Stumped out","Run Out"]
                print(random.choices(w))
                Wickets+=1
            total+=runs
            if i==1 and total>=TwoTeams[0]:
                print("scored ",runs,"Runs")
                print(" Total Score = ",total," /",Wickets ,"  ", balls,"Balls" )
                TwoTeams.append(total+100)
                print(TwoTeams)
                print(i+1,"nd Innings Finished")
                print("###########################################################")
                if team==1:
                    TwoTeams.reverse()
                return TwoTeams
            print("scored ",runs,"Runs")
            print(" Total Score = ",total," /",Wickets ,"  ", balls,"Balls" )
            balls+=1
        TwoTeams.append(total)
        print('\n')
        if i==0:
            print(i+1,"st Innings Finished")
            print("###########################################################")
        else:
            print(i+1,"nd Innings Finished")
            print("###########################################################")
        if team==1:
            team=2
        else:
            team=1
    if team==2:
        TwoTeams.reverse()
    return TwoTeams

        

d=Toss(T)
if d=='1b'or d=='2f':
    team=1
elif d=='1f' or d=='2b':
    team=2
Winner=BookCricket(overs,players,T,team)
k=Winner.index(max(Winner))+1
print("************************Congratulations*********************************")
print("                  Player ",k," Won the Game                             ")

    

    
