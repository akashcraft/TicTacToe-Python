#Code
print("Hello, This game is created by Akash. Tic Tac Toe.")
#Choice of Gamemode
print('Select Type')
gamemode=input("[1] Single Player with AI or [2] Double Player: ")
while gamemode!='1' and gamemode!='2':
    gamemode=input("Only [1] or [2]! Please type again: ")
if gamemode=='1': #Single
    print("Single Player Mode Selected")
    print("Ok! Let's get started with names.")
    name=input("What's your name?: ")
    print("Alright ",name,', Choose your Letter',sep="")
    ans=input("[X] or [O]: ")
    ans=ans.upper()
    while ans!='X' and ans!='O':
        ans=input("Only [X] or [O]! Please type again: ")
        ans=ans.upper()
    if ans=="X":
        ans1="O"
    else:
        ans1="X"
    print("Got it",name)
else:
    print("Double Player Mode Selected") #Double
    print("Ok! Let's get started with names.")
    name=input("Player 1: ")
    name1=input("Player 2: ")
    print("Welcome",name,"and",name1)
    print('Choose your Letter,',name)
    ans=input("[X] or [O]: ")
    ans=ans.upper()
    while ans!='X' and ans!='O':
        ans=input("Only [X] or [O]! Please type again: ")
        ans=ans.upper()
    if ans=="X":
        print(name,'will play as X')
        print(name1,'will play as O')
        ans2="O"
    else:
        print(name,'will play as O')
        print(name1,'will play as X')
        ans2="X"
#Creation of Tic Tac Toe
L=[]
for i in range(49):
    L.append(" ")
L1=[1,3,5,15,17,19,29,31,33,43,45,47]
for i in L1:
    L[i]="-"
L1.clear()
L1=[0,2,4,6,14,16,18,20,28,30,32,34,42,44,46,48]
for i in L1:
    L[i]="+"
L1.clear()
L1=[7,9,11,13,21,23,25,27,35,37,39,41]
for i in L1:
    L[i]="|"
print(" "*32,end="")
#Print
c=0
for i in L:
    if c==7 or c==14 or c==21 or c==28 or c==35 or c==42:
        print()
        print(" "*32,end="")
    print("",i,end="")
    c=c+1
print()
#Basic Controls
inarea=[8,10,12,22,24,26,36,38,40]
numpad=['7','8','9','4','5','6','1','2','3']
avail=numpad
L2=[]
while gamemode=='1': #If Single mode was chosen
    numpad=['7','8','9','4','5','6','1','2','3']
    if avail==[]: #Tie checker
        print("It was a TIE")
        rep=input("Would you like to play again? [Y] or [N]: ")
        rep=rep.upper()
        while rep!='Y' and rep!='N':
            print("Sorry",name,"but you can only type [Y] or [N]")
            rep=input("Please type again: ")
            rep=rep.upper()
        if rep=='N':
            print("Ok!",name,"Thank YOU for playing my game. See you soon in one of my other modules.")
            break
        else:
            print("Great Choice",name,"Let's GO")
            avail=numpad
            L2=[]
            for i in inarea:
                L[i]=" "
            print(" "*32,end="")
            c=0
            for i in L:
                if c==7 or c==14 or c==21 or c==28 or c==35 or c==42:
                    print()
                    print(" "*32,end="")
                print("",i,end="")
                c=c+1
            print()
    if len(avail)==9: #Help Advisor (Executed only Once)
        print("Type [H] for Help in inputing Field")
    key=input("Enter Field: ")
    if key=='h' or key=='H': #Help with input
        print('Sure!',name)
        print('Help: You must get at least 3',ans,'\'s in a row or column or diagonal to win.',sep="")
        print('This is how you must enter field inputs. Just use the numpad in your keyboard.')
        print('Fields already occupied cannot be used again.')
        helptable=[] #Separate Table for Help
        for i in range(49):
            helptable.append(" ")
        E1=[1,3,5,15,17,19,29,31,33,43,45,47]
        for i in E1:
            helptable[i]="-"
        E1.clear()
        E1=[0,2,4,6,14,16,18,20,28,30,32,34,42,44,46,48]
        for i in E1:
            helptable[i]="+"
        E1.clear()
        E1=[7,9,11,13,21,23,25,27,35,37,39,41]
        for i in E1:
            helptable[i]="|"
        E1.clear()
        E1=[8,10,12,22,24,26,36,38,40]
        numpadhelp=[7,8,9,4,5,6,1,2,3]
        j=0
        for i in E1:
            helptable[i]=numpadhelp[j]
            j=j+1
        print(" "*32,end="")
        c=0
        for i in helptable:
            if c==7 or c==14 or c==21 or c==28 or c==35 or c==42:
                print()
                print(" "*32,end="")
            print("",i,end="")
            c=c+1
        print()
        continue
    #Input Validity Checks
    if key.isalpha():
        print("You must enter numbers",name)
        print("Type [H] for Help in inputing Field")
        continue
    if key not in numpad:
        print("Field value must range from 1 to 9",name)
        print("Type [H] for Help in inputing Field")
        continue
    if key not in L2 and key in avail: #Valid Key Input
        a=numpad.index(key)
        inp=inarea[a]
        L[inp]=ans
        L2.append(key)
        avail.remove(key)           
    else:
        print("This field is already filled",name)
        print("Type [H] for Help in inputing Field")
        continue
    #Print
    c=0
    print(" "*32,end="")
    for i in L:
        if c==7 or c==14 or c==21 or c==28 or c==35 or c==42:
            print()
            print(" "*32,end="")
        print("",i,end="")
        c=c+1
    print()
    #Check for Win
    check1=0
    if [L[8],L[10],L[12]]==[ans,ans,ans]:
        check1=1
    if [L[22],L[24],L[26]]==[ans,ans,ans]:
        check1=1
    if [L[36],L[38],L[40]]==[ans,ans,ans]:
        check1=1
    if [L[8],L[22],L[36]]==[ans,ans,ans]:
        check1=1
    if [L[10],L[24],L[38]]==[ans,ans,ans]:
        check1=1
    if [L[12],L[26],L[40]]==[ans,ans,ans]:
        check1=1
    if [L[8],L[24],L[40]]==[ans,ans,ans]:
        check1=1
    if [L[24],L[12],L[36]]==[ans,ans,ans]:
        check1=1
    if check1==1: #End
        print("Congragulations! You won :)",name)
        rep=input("Would you like to play again? [Y] or [N]: ")
        rep=rep.upper()
        while rep!='Y' and rep!='N':
            print("Sorry",name,"but you can only type [Y] or [N]")
            rep=input("Please type again: ")
            rep=rep.upper()
        if rep=='N':
            print("Ok!",name,"Thank YOU for playing my game. See you soon in one of my other modules.")
            quit()
            break
        else: #RESTART
            print("Great Choice",name,"Let's GO")
            avail=numpad
            L2=[]
            for i in inarea:
                L[i]=" "
            print(" "*32,end="")
            c=0
            for i in L:
                if c==7 or c==14 or c==21 or c==28 or c==35 or c==42:
                    print()
                    print(" "*32,end="")
                print("",i,end="")
                c=c+1
            print()
    if avail==[]: #Tie checker
        print("It was a TIE")
        rep=input("Would you like to play again? [Y] or [N]: ")
        rep=rep.upper()
        while rep!='Y' and rep!='N':
            print("Sorry",name,"but you can only type [Y] or [N]")
            rep=input("Please type again: ")
            rep=rep.upper()
        if rep=='N':
            print("Ok!",name,"Thank YOU for playing my game. See you soon in one of my other modules.")
            quit()
            break
        else:
            print("Great Choice",name,"Let's GO")
            avail=numpad
            L2=[]
            for i in inarea:
                L[i]=" "
            print(" "*32,end="")
            c=0
            for i in L:
                if c==7 or c==14 or c==21 or c==28 or c==35 or c==42:
                    print()
                    print(" "*32,end="")
                print("",i,end="")
                c=c+1
            print()
    print("Please wait while AI Plays...")
    import time
    time.sleep(2)
#Artificial Intelligence
    flag=0
    check=0
#Offensive Moves
    if [L[8],L[10]]==[ans1,ans1] and '9' in avail and check==0:
        L[12]=ans1
        avail.remove('9')
        flag=1
        check=1
    if [L[24],L[36]]==[ans1,ans1] and '9' in avail and check==0:
        L[12]=ans1
        avail.remove('9')
        flag=1
        check=1
    if [L[26],L[40]]==[ans1,ans1] and '9' in avail and check==0:
        L[12]=ans1
        avail.remove('9')
        flag=1
        check=1
    if [L[12],L[10]]==[ans1,ans1] and '7' in avail and check==0:
        L[8]=ans1
        avail.remove('7')
        flag=1
        check=1
    if [L[22],L[36]]==[ans1,ans1] and '7' in avail and check==0:
        L[8]=ans1
        avail.remove('7')
        flag=1
        check=1
    if [L[24],L[40]]==[ans1,ans1] and '7' in avail and check==0:
        L[8]=ans1
        avail.remove('7')
        flag=1
        check=1
    if [L[8],L[22]]==[ans1,ans1] and '1' in avail and check==0:
        L[36]=ans1
        avail.remove('1')
        flag=1
        check=1
    if [L[38],L[40]]==[ans1,ans1] and '1' in avail and check==0:
        L[36]=ans1
        avail.remove('1')
        flag=1
        check=1
    if [L[24],L[12]]==[ans1,ans1] and '1' in avail and check==0:
        L[36]=ans1
        avail.remove('1')
        flag=1
        check=1
    if [L[12],L[26]]==[ans1,ans1] and '3' in avail and check==0:
        L[40]=ans1
        avail.remove('7')
        flag=1
        check=1
    if [L[24],L[8]]==[ans1,ans1] and '3' in avail and check==0:
        L[40]=ans1
        avail.remove('7')
        flag=1
        check=1
    if [L[36],L[38]]==[ans1,ans1] and '3' in avail and check==0:
        L[40]=ans1
        avail.remove('7')
        flag=1
        check=1
    if [L[12],L[36]]==[ans1,ans1] and '5' in avail and check==0:
        L[24]=ans1
        avail.remove('5')
        flag=1
        check=1
    if [L[22],L[26]]==[ans1,ans1] and '5' in avail and check==0:
        L[24]=ans1
        avail.remove('5')
        flag=1
        check=1
    if [L[10],L[38]]==[ans1,ans1] and '5' in avail and check==0:
        L[24]=ans1
        avail.remove('5')
        flag=1
        check=1
    if [L[8],L[40]]==[ans1,ans1] and '5' in avail and check==0:
        L[24]=ans1
        avail.remove('5')
        flag=1
        check=1
    if [L[8],L[12]]==[ans1,ans1] and '8' in avail and check==0:
        L[10]=ans1
        avail.remove('8')
        flag=1
        check=1
    if [L[24],L[38]]==[ans1,ans1] and '8' in avail and check==0:
        L[10]=ans1
        avail.remove('8')
        flag=1
        check=1
    if [L[10],L[24]]==[ans1,ans1] and '2' in avail and check==0:
        L[38]=ans1
        avail.remove('2')
        flag=1
        check=1
    if [L[36],L[40]]==[ans1,ans1] and '2' in avail and check==0:
        L[38]=ans1
        avail.remove('2')
        flag=1
        check=1
    if [L[8],L[36]]==[ans1,ans1] and '4' in avail and check==0:
        L[22]=ans1
        avail.remove('4')
        flag=1
        check=1
    if [L[24],L[26]]==[ans1,ans1] and '4' in avail and check==0:
        L[22]=ans1
        avail.remove('4')
        flag=1
        check=1
    if [L[12],L[40]]==[ans1,ans1] and '6' in avail and check==0:
        L[26]=ans1
        avail.remove('6')
        flag=1
        check=1
    if [L[22],L[24]]==[ans1,ans1] and '6' in avail and check==0:
        L[26]=ans1
        avail.remove('6')
        flag=1
        check=1
#Defensive Moves
    if [L[8],L[40]]==[ans,ans] and '5' in avail and check==0:
        L[24]=ans1
        avail.remove('5')
        flag=1
        check=1
    if [L[12],L[36]]==[ans,ans] and '5' in avail and check==0:
        L[24]=ans1
        avail.remove('5')
        flag=1
        check=1
    if [L[22],L[26]]==[ans,ans] and '5' in avail and check==0:
        L[24]=ans1
        avail.remove('5')
        flag=1
        check=1
    if [L[10],L[38]]==[ans,ans] and '5' in avail and check==0:
        L[24]=ans1
        avail.remove('5')
        flag=1
        check=1
    if [L[8],L[10]]==[ans,ans] and '9' in avail and check==0:
        L[12]=ans1
        avail.remove('9')
        flag=1
        check=1
    if [L[24],L[36]]==[ans,ans] and '9' in avail and check==0:
        L[12]=ans1
        avail.remove('9')
        flag=1
        check=1
    if [L[26],L[40]]==[ans,ans] and '9' in avail and check==0:
        L[12]=ans1
        avail.remove('9')
        flag=1
        check=1
    if [L[12],L[10]]==[ans,ans] and '7' in avail and check==0:
        L[8]=ans1
        avail.remove('7')
        flag=1
        check=1
    if [L[24],L[40]]==[ans,ans] and '7' in avail and check==0:
        L[8]=ans1
        avail.remove('7')
        flag=1
        check=1
    if [L[22],L[36]]==[ans,ans] and '7' in avail and check==0:
        L[8]=ans1
        avail.remove('7')
        flag=1
        check=1
    if [L[8],L[22]]==[ans,ans] and '1' in avail and check==0:
        L[36]=ans1
        avail.remove('1')
        flag=1
        check=1
    if [L[38],L[40]]==[ans,ans] and '1' in avail and check==0:
        L[36]=ans1
        avail.remove('1')
        flag=1
        check=1
    if [L[12],L[24]]==[ans,ans] and '1' in avail and check==0:
        L[36]=ans1
        avail.remove('1')
        flag=1
        check=1
    if [L[8],L[24]]==[ans,ans] and '3' in avail and check==0:
        L[40]=ans1
        avail.remove('3')
        flag=1
        check=1
    if [L[12],L[26]]==[ans,ans] and '3' in avail and check==0:
        L[40]=ans1
        avail.remove('3')
        flag=1
        check=1
    if [L[36],L[38]]==[ans,ans] and '3' in avail and check==0:
        L[40]=ans1
        avail.remove('3')
        flag=1
        check=1
    if [L[8],L[12]]==[ans,ans] and '8' in avail and check==0:
        L[10]=ans1
        avail.remove('8')
        flag=1
        check=1
    if [L[24],L[38]]==[ans,ans] and '8' in avail and check==0:
        L[10]=ans1
        avail.remove('8')
        flag=1
        check=1
    if [L[10],L[24]]==[ans,ans] and '2' in avail and check==0:
        L[38]=ans1
        avail.remove('2')
        flag=1
        check=1
    if [L[36],L[40]]==[ans,ans] and '2' in avail and check==0:
        L[38]=ans1
        avail.remove('2')
        flag=1
        check=1
    if [L[8],L[36]]==[ans,ans] and '4' in avail and check==0:
        L[22]=ans1
        avail.remove('4')
        flag=1
        check=1
    if [L[24],L[26]]==[ans,ans] and '4' in avail and check==0:
        L[22]=ans1
        avail.remove('4')
        flag=1
        check=1
    if [L[12],L[40]]==[ans,ans] and '6' in avail and check==0:
        L[26]=ans1
        avail.remove('6')
        flag=1
        check=1
    if [L[22],L[24]]==[ans,ans] and '6' in avail and check==0:
        L[26]=ans1
        avail.remove('6')
        flag=1
        check=1
    if flag==1:
        pass
    else: #Random Move
        import random
        lim=len(avail)-1
        x=random.randint(0,lim)
        b=avail[x]
        a=numpad.index(b)
        inp=inarea[a]
        L[inp]=ans1
        L2.append(b)
        avail.remove(b)
    #Print
    c=0
    print(" "*32,end="")
    for i in L:
        if c==7 or c==14 or c==21 or c==28 or c==35 or c==42:
            print()
            print(" "*32,end="")
        print("",i,end="")
        c=c+1
    print()
    #Check for Win
    check2=0
    if [L[8],L[10],L[12]]==[ans1,ans1,ans1]:
        check2=1
    if [L[22],L[24],L[26]]==[ans1,ans1,ans1]:
        check2=1
    if [L[36],L[38],L[40]]==[ans1,ans1,ans1]:
        check2=1
    if [L[8],L[22],L[36]]==[ans1,ans1,ans1]:
        check2=1
    if [L[10],L[24],L[38]]==[ans1,ans1,ans1]:
        check2=1
    if [L[12],L[26],L[40]]==[ans1,ans1,ans1]:
        check2=1
    if [L[8],L[24],L[40]]==[ans1,ans1,ans1]:
        check2=1
    if [L[12],L[24],L[36]]==[ans1,ans1,ans1]:
        check2=1
    if check2==1: #End
        print("You lost :(",name)
        print("AI won")
        rep=input("Would you like to play again? [Y] or [N]: ")
        rep=rep.upper()
        while rep!='Y' and rep!='N':
            print("Sorry",name,"but you can only type [Y] or [N]")
            rep=input("Please type again: ")
            rep=rep.upper()
        if rep=='N':
            print("Ok!",name,"Thank YOU for playing my game. See you soon in one of my other modules.")
            quit()
            break
        else: #RESTART
            print("Great Choice",name,"Let's GO")
            avail=numpad
            L2=[]
            for i in inarea:
                L[i]=" "
            print(" "*32,end="")
            c=0
            for i in L:
                if c==7 or c==14 or c==21 or c==28 or c==35 or c==42:
                    print()
                    print(" "*32,end="")
                print("",i,end="")
                c=c+1
            print()
while gamemode=='2': #If Double Mode was chosen
    numpad=['7','8','9','4','5','6','1','2','3']
    if avail==[]: #Tie Checker
        print("WOW",name,'and',name1)
        print("It was a TIE")
        rep=input("Would you like to play again? [Y] or [N]: ")
        rep=rep.upper()
        while rep!='Y' and rep!='N':
            print("Sorry but you can only type [Y] or [N]")
            rep=input("Please type again: ")
            rep=rep.upper()
        if rep=='N':
            print("Ok!",name,'and',name1,"Thank YOU for playing my game. See you soon in one of my other modules.")
            break
        else:
            print("Great Choice Let's GO")
            avail=numpad
            L2=[]
            for i in inarea:
                L[i]=" "
            print(" "*32,end="")
            c=0
            for i in L:
                if c==7 or c==14 or c==21 or c==28 or c==35 or c==42:
                    print()
                    print(" "*32,end="")
                print("",i,end="")
                c=c+1
            print()
    if len(avail)==9: #Help Advisor (Executed only Once)
        print("Type [H] for Help in inputing Field")
    print(name,'\'s turn',sep="",end=", ") #Player 1
    key=input("Enter Field: ")
    if key=='h' or key=='H': #Help
        print("Sure!",name)
        print('Help: You must get at least 3',ans,'\'s in a row or column or diagonal to win.',sep="")
        print('This is how you must enter field inputs. Just use the numpad in your keyboard.')
        print('Fields already occupied cannot be used again.')
        helptable=[] #Separate List for Help
        for i in range(49):
            helptable.append(" ")
        E1=[1,3,5,15,17,19,29,31,33,43,45,47]
        for i in E1:
            helptable[i]="-"
        E1.clear()
        E1=[0,2,4,6,14,16,18,20,28,30,32,34,42,44,46,48]
        for i in E1:
            helptable[i]="+"
        E1.clear()
        E1=[7,9,11,13,21,23,25,27,35,37,39,41]
        for i in E1:
            helptable[i]="|"
        E1.clear()
        E1=[8,10,12,22,24,26,36,38,40]
        numpadhelp=[7,8,9,4,5,6,1,2,3]
        j=0
        for i in E1:
            helptable[i]=numpadhelp[j]
            j=j+1
        print(" "*32,end="")
        c=0
        for i in helptable:
            if c==7 or c==14 or c==21 or c==28 or c==35 or c==42:
                print()
                print(" "*32,end="")
            print("",i,end="")
            c=c+1
        print()
        continue
    #Input Validity Checks
    if key.isalpha():
        print("You must enter numbers",name)
        print("Type [H] for Help in inputing Field")
        continue
    if key not in numpad:
        print("Field value must range from 1 to 9",name)
        print("Type [H] for Help in inputing Field")
        continue
    if key not in L2 and key in avail: #Valid Key
        a=numpad.index(key)
        inp=inarea[a]
        L[inp]=ans
        L2.append(key)
        avail.remove(key)           
    else:
        print("This field is already filled",name)
        print("Type [H] for Help in inputing Field")
        continue
    #Print
    c=0
    print(" "*32,end="")
    for i in L:
        if c==7 or c==14 or c==21 or c==28 or c==35 or c==42:
            print()
            print(" "*32,end="")
        print("",i,end="")
        c=c+1
    print()
    #Check for Win
    check1=0
    if [L[8],L[10],L[12]]==[ans,ans,ans]:
        check1=1
    if [L[22],L[24],L[26]]==[ans,ans,ans]:
        check1=1
    if [L[36],L[38],L[40]]==[ans,ans,ans]:
        check1=1
    if [L[8],L[22],L[36]]==[ans,ans,ans]:
        check1=1
    if [L[10],L[24],L[38]]==[ans,ans,ans]:
        check1=1
    if [L[12],L[26],L[40]]==[ans,ans,ans]:
        check1=1
    if [L[8],L[24],L[40]]==[ans,ans,ans]:
        check1=1
    if [L[24],L[12],L[36]]==[ans,ans,ans]:
        check1=1
    if check1==1: #End
        print("Congragulations!",name,"has won this match :)")
        print(name1,"lost! :(")
        rep=input("Would you like to play again? [Y] or [N]: ")
        rep=rep.upper()
        while rep!='Y' and rep!='N': 
            print("Sorry but you can only type [Y] or [N]")
            rep=input("Please type again: ")
            rep=rep.upper()
        if rep=='N':
            print("Ok!",name,'and',name1,"Thank YOU for playing my game. See you soon in one of my other modules.")
            quit()
            break
        else: #RESTART
            print("Great Choice Let's GO")
            avail=numpad
            L2=[]
            for i in inarea:
                L[i]=" "
            print(" "*32,end="")
            c=0
            for i in L:
                if c==7 or c==14 or c==21 or c==28 or c==35 or c==42:
                    print()
                    print(" "*32,end="")
                print("",i,end="")
                c=c+1
            print()
    if avail==[]: #Tie Checker
        print("WOW",name,'and',name1)
        print("It was a TIE")
        rep=input("Would you like to play again? [Y] or [N]: ")
        rep=rep.upper()
        while rep!='Y' and rep!='N':
            print("Sorry but you can only type [Y] or [N]")
            rep=input("Please type again: ")
            rep=rep.upper()
        if rep=='N':
            print("Ok!",name,'and',name1,"Thank YOU for playing my game. See you soon in one of my other modules.")
            break
        else:
            print("Great Choice Let's GO")
            avail=numpad
            L2=[]
            for i in inarea:
                L[i]=" "
            print(" "*32,end="")
            c=0
            for i in L:
                if c==7 or c==14 or c==21 or c==28 or c==35 or c==42:
                    print()
                    print(" "*32,end="")
                print("",i,end="")
                c=c+1
            print()
    chk=0
    while chk==0:
        print(name1,'\'s turn',sep="",end=", ") #Player 2
        key1=input("Enter Field: ")
        if key1=='h' or key1=='H':#Help
            print("Sure!",name1)
            print('Help: You must get at least 3',ans2,'\'s in a row or column or diagonal to win.',sep="")
            print('This is how you must enter field inputs. Just use the numpad in your keyboard.')
            print('Fields already occupied cannot be used again.')
            helptable=[]#Separate list for help
            for i in range(49):
                helptable.append(" ")
            E1=[1,3,5,15,17,19,29,31,33,43,45,47]
            for i in E1:
                helptable[i]="-"
            E1.clear()
            E1=[0,2,4,6,14,16,18,20,28,30,32,34,42,44,46,48]
            for i in E1:
                helptable[i]="+"
            E1.clear()
            E1=[7,9,11,13,21,23,25,27,35,37,39,41]
            for i in E1:
                helptable[i]="|"
            E1.clear()
            E1=[8,10,12,22,24,26,36,38,40]
            numpadhelp=[7,8,9,4,5,6,1,2,3]
            j=0
            for i in E1:
                helptable[i]=numpadhelp[j]
                j=j+1
            print(" "*32,end="")
            c=0
            for i in helptable:
                if c==7 or c==14 or c==21 or c==28 or c==35 or c==42:
                    print()
                    print(" "*32,end="")
                print("",i,end="")
                c=c+1
            print()
            continue
        #Input Validity Checks
        if key1.isalpha():
            print("You must enter numbers",name1)
            print("Type [H] for Help in inputing Field")
            continue
        if key1 not in numpad:
            print("Field value must range from 1 to 9",name1)
            print("Type [H] for Help in inputing Field")
            continue
        if key1 not in L2 and key1 in avail: #Valid Input
            a=numpad.index(key1)
            inp=inarea[a]
            L[inp]=ans2
            L2.append(key1)
            avail.remove(key1)           
        else:
            print("This field is already filled",name1)
            print("Type [H] for Help in inputing Field")
            continue
        #Print
        c=0
        print(" "*32,end="")
        for i in L:
            if c==7 or c==14 or c==21 or c==28 or c==35 or c==42:
                print()
                print(" "*32,end="")
            print("",i,end="")
            c=c+1
        print()
        chk=1
    #Check for Win
    check2=0
    if [L[8],L[10],L[12]]==[ans2,ans2,ans2]:
        check2=1
    if [L[22],L[24],L[26]]==[ans2,ans2,ans2]:
        check2=1
    if [L[36],L[38],L[40]]==[ans2,ans2,ans2]:
        check2=1
    if [L[8],L[22],L[36]]==[ans2,ans2,ans2]:
        check2=1
    if [L[10],L[24],L[38]]==[ans2,ans2,ans2]:
        check2=1
    if [L[12],L[26],L[40]]==[ans2,ans2,ans2]:
        check2=1
    if [L[8],L[24],L[40]]==[ans2,ans2,ans2]:
        check2=1
    if [L[12],L[24],L[36]]==[ans2,ans2,ans2]:
        check2=1
    if check2==1: #End
        print("Congragulations!",name1,"has won this match :)")
        print(name,'lost :(')
        rep=input("Would you like to play again? [Y] or [N]: ")
        rep=rep.upper()
        while rep!='Y' and rep!='N':
            print("Sorry but you can only type [Y] or [N]")
            rep=input("Please type again: ")
            rep=rep.upper()
        if rep=='N':
            print("Ok!",name,"and",name1,"Thank YOU for playing my game. See you soon in one of my other modules.")
            quit()
            break
        else: #RESTART
            print("Great Choice Let's GO")
            avail=numpad
            L2=[]
            for i in inarea:
                L[i]=" "
            print(" "*32,end="")
            c=0
            for i in L:
                if c==7 or c==14 or c==21 or c==28 or c==35 or c==42:
                    print()
                    print(" "*32,end="")
                print("",i,end="")
                c=c+1
            print()
        
