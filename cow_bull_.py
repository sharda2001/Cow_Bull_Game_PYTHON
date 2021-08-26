import random
name=input("enter the your_name:--")
print("** welcome*",name)
def sss(number, user_guess):
    cowbull = [0,0] 
    for i in range(len(number)):
        if number[i] == user_guess[i]:
            cowbull[1]+=1
        elif number[i] in user_guess:
            cowbull[0]+=1
    return cowbull
if __name__=="__main__":
    playing = True 
    number = str(random.randint(1000,9999))
    guesses = 0
    li=[]
    i=0
    while i<len(number):
        li.append(number[i])
        i=i+1

    for i in range(0, len(li)):
            li[i] = int(li[i])
    print(li)

    print("Let's play a game of Cowbull:") 
    tries =5
    while tries>0:
        user_guess =(input("Give me your best guess:"))
        i=0
        list=[]
        while i<len(user_guess):
            list.append(user_guess[i])
            i=i+1
    
        for i in range(0, len(list)):
            list[i] = int(list[i])
        print(list)
            
        cowbullcount = sss(number,user_guess)
        guesses+=1
        print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")
        if cowbullcount[1]==4:
            print("**congratulation** >>>",name,"You win the game after " + str(guesses) + "! The number was "+str(number))
            break   
        else:
            print("Your guess isn't right, try again.")
        tries=tries-1

     
