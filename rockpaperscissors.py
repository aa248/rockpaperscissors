import random

def rockpaperscissors():
    
    print 'Hey! We are going to play rock, paper, scissors.'
    #Count the number of times the computer wins and the number of times the user wins.
    humanwins = 0
    compwins = 0
    
    while True:
            try:
                compchoices = ['rock','paper','scissors']
                thechoice = compchoices[random.randint(0,2)]
                userchoice = raw_input('Rock, paper, or scissors? ')
                assert userchoice.isalpha()
                userchoice = userchoice.lower()
                assert (userchoice=='rock' or userchoice=='paper' or userchoice=='scissors')    
            
                #If thechoice is rock:
                    
                if thechoice=='rock':
                    if userchoice=='rock':
                        print 'You and the computer both chose rock. Play again!'
            
                    elif userchoice=='paper':
                        print 'Paper beats rock. You win!'
                        humanwins+=1
                        
                    elif userchoice=='scissors':
                        print 'Rock beats scissors. Sorry, you lose!'
                        compwins+=1
                        
                #If thechoice is paper:
                
                if thechoice=='paper':
                    if userchoice=='paper':
                        print 'You and the computer both chose paper. Play again!'
            
                    elif userchoice=='scissors':
                        print 'Scissors beats rock. You win!'
                        humanwins+=1
                        
                    elif userchoice=='rock':
                        print 'Paper beats rock. Sorry, you lose!'
                        compwins+=1
                        
                        
             #If thechoice is scissors:
                
                if thechoice=='scissors':
                    if userchoice=='scissors':
                        print 'You and the computer both chose scissors. Play again!'
            
                    elif userchoice=='rock':
                        print 'Rock beats scissors. You win!'
                        humanwins+=1
                        
                    elif userchoice=='paper':
                        print 'Scissors beats paper. Sorry, you lose!'
                        compwins+=1
            
                
                #Ask to play again
                again = raw_input('Do you want to play again? Enter Yes or No: ')
                if again=='No' or again=='no':
                    print
                    print 'It was nice playing with you! '
                    print
                    print 'You won ' +str(humanwins) + ' time(s) and the computer won ' +str(compwins) + ' time(s).'
                    break
                    
                
                
            except:
                print 'The input should be either rock, paper, or scissors.'
    
    


if __name__ == '__main__':
    rockpaperscissors()