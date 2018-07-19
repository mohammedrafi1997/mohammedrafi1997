import random
count=0
while(count<=100):
    a=input("enter b to roll a dice")
    if(a=="b"):
        r=random.randint(1,6)
        count=ccount+r
        print("random value generated is",r)
        print("my count value is",count)
    if(count=="8"):
        count==37
        print("you climbed the ladder")
    elif(count==11):
         count=2
         print("snake bit")
    elif(count==13):
        count=34
        print("you climbed the ladder")
    elif(count==40):
        count=68
        print("you climbed the ladder")
    elif(count==65):
        count=46
        print("snake bit")
    elif(count==52):
        count=81
        print("you climbed the ladder")
    elif(count==76):
        count=97
        print("you climbed the ladder")
    elif(count==89):
        count=70
        print("snake bit")
    elif(count==38):
        count=9
        print("snake bit")
    elif(count==11):
        count=2
        print("snake bit")
    elif(count==100):
        count=100
        print("you won the game")
    if(count>100):
        count=count-r
    
        
        
    
