import random


overs=int(input("Choose No of Overs:"))
players=int(input("Choose No of Players:"))
print('\n')
print("Toss [if Toss=1--> player 1 won the Toss // if Toss=2--> player 2 1on the toss]" )
print('\n')
print("Click Enter to roll the Toss")
input()
T=random.randint(1,2)
print(T)



def Toss(T):
    print('\n')
    print("Player ",T," won the Toss, Choose Batting/Fielding [B/F] :")
    d=input()
    if d=='f' or d=='F':
        d='f'
        print("player ",T," Chooses to Field First")
    elif d=='b'or d=='B':
        d='b'
        print("player ",T," Chooses to Bat First")
    else:
        return 0
    return (str(T)+d)



def BookCricket(overs,players,T,team):
    TwoTeams=[]
    if T==0:
        return 0
    else:
        for i in range(0,2,1):
            print('\n',"Team ",team,' is Batting')
            (Wickets,balls,total)=(0,1,0)
            while balls<=overs*6 and Wickets<players-1:
                print('\n',"Click Enter to Bat :")
                input()
                runs=random.randint(0,6)
                if runs==0:
                    w=["LBW","Bowled","Stumped out","Run Out"]
                    print(random.choices(w))
                    Wickets+=1
                total+=runs
                print("scored ",runs,"Runs")
                print(" Total Score = ",total," /",Wickets ,"  ", balls,"Balls" )
                balls+=1
            TwoTeams.append(total)
            print('\n')
            print(i+1,"st Innings Finished")
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
if Winner==0:
    print("invalid Literal")
else:
    k=Winner.index(max(Winner))+1
    print("Player ",k," Wins the Game","buy",max(Winner)-min(Winner),"Runs")

    

    