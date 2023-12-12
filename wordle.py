#file operations
import sys, random,Instructions

from clue_giver import clues as clue_giver
from Recorder import recorder as recorder

sys.path.append(r"F:\WORDLE Final\WORDLE")

social_share,x,repeat_stopper = [],[],[]

def file_op():
    global x
    f = open(r'Word List.txt','r+')
    words = f.readlines()
    for i in words:
        i = i.strip() #Removing the new line char
        x.append(i)

#Random word generating
def randomword_gen():
    file_op()
    global x, repeat_stopper
    n = len(x)
    num = random.randint(0, n)
    word_gened = x[num]
    if word_gened in repeat_stopper:
        num1 = random.randint(0,n)
        word_gened = x[num1]
    repeat_stopper.append(word_gened)
    #print(word_gened)
    return word_gened

#The crucial mechanic of the game
def game_logic():
    count = 1 
    gened = randomword_gen()
    print('now, here\'s the clue for you to guess the correct word')
    print('the word you\'re looking for has a total of',len(gened),'characters')
    
    if len(gened)==4:
        print('since the word is a bit difficult to guess, here\'s the second clue')
        print('the word has',gened[0],'as the first character')
    
    v=0
    t = str(input('do you need another clue to guess?(y/n)'))
    if t.lower()=='y':
        for i in gened:
            if i.lower() in ['a','e','i','o','u']:
                v+=1
        print('no of vowels in the generated word is:',v)
    guess = input("Enter you guess...")
    while guess != gened:
        clue = clue_giver(guess,gened,social_share)
        print(clue[0])
        social_share.append(clue[1]) #list(clue[1])
        if guess != gened and count < 5:
            guess = input("Enter your next guess...") 
            count+=1
            continue
        elif guess == gened:
            print("You have WON in",count,'times')
            recorder(gened,count,'Guessed')
            count+=1
            break
            
        elif count >= 5:
            print("Maximum number of tries reached!")
            print('The word is',gened)
            recorder(gened,count,'Failed to guess')
            break
        
    else:
        print("You have WON in", count, 'times')
        recorder(gened, count, 'Guessed')
    
    
#__main__
while True:
    print('''\ti - Instructions\n\tc - Play | continue playing(rematch)\n\tq - Quit''')
    chr = input("enter your option...")
    print('____________________________________________________________________')
    if chr.lower() in 'i':
        Instructions.instructions()

    if chr in 'Cc':
        game_logic()
        continue

    if chr in 'qQ':
        #ctrl = False
        break
    
print('Thanks for playing! You can find your records in the file named-\'User Records\'')
