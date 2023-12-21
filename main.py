import random

def show_computer_option_select(computer_option_selected):
    choose_option=""
    match computer_option_selected:
        case 1:
            choose_option="Rock"
        case 2:
            choose_option="Paper"
        case 3:
            choose_option="Scissors"
    
    print(f"Computer choose : {choose_option} \n")
    


def game_validation(user_option, computer_option, user_accounter,computer_accounter):
    #lets validate  the user and computers option
    match user_option:
        case 1:
            if(computer_option==3):
                print("You won \n ")
                user_accounter+=1
            elif (computer_option==1):
                print("Tie \n")
            elif(computer_option==2):
                print("You lost \n")
                computer_accounter+=1

        case 2:
            if(computer_option==1):
                print("You won \n ")
                user_accounter+=1
            elif(computer_option==2):
                print("Tie\n")
            elif(computer_option==3):
                print("You lost\n")
                computer_accounter+=1
        case 3:

            if(computer_option==2):
                print("You won \n ")
                user_accounter+=1
            elif(computer_option==3):
                print("Tie\n")
            elif(computer_option==1):
                print("You lost\n")
                computer_accounter+=1
            pass

    return user_accounter, computer_accounter

def show_score(user_accounter, computer_accounter):
    print(f"Score: {user_accounter} - {computer_accounter} \n")


def main():
    user_accounter=0
    computer_accounter=0
    '''
        Possible combinations
        1- Stone
        2- Paper
        3-Scissors
    '''
    a = input("-- Please press a key for start the Game ---")
    while(user_accounter !=3 or computer_accounter !=3):

        show_score(user_accounter,computer_accounter)
        print("Choose just one option")
        user_option= int(input("1-Rock\n2-Paper\n3-Scissors\n ==>"))

        #Generate the computer number value
        computer_option= random.randint(1,3)

        show_computer_option_select(computer_option)

        user_accounter, computer_accounter = game_validation(user_option, computer_option, user_accounter, computer_accounter)
        
        

    print(f"The game is over, these are the results: \n User: {user_accounter}\n Computer: {computer_accounter}")
        




main()