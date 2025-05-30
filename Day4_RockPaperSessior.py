import random
def which_option(option):
    rock = """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """
    paper = """
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """
    scissors = """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """

    match option:
        case 1:
            print('''ROCK 
            '''+rock)
        case 2:
            print('''PAPER 
            '''+paper)
        case 3:
            print('''SCISSOR 
            '''+scissors)
        case default:
            print("Choose Correct Option")

    return option



print("Welcome to Rock Paper Scissor game!")
option = [1, 2, 3]


user_choice = int(input('''Choose option according to below chart:
> Press 1 for ROCK
> Press 2 for PAPER
> Press 3 for SCISSOR
'''))

ai_choice = random.choice(option)

print(f"You chose : {which_option(user_choice)}")
print(f"Computer chose : {which_option(ai_choice)}")


if user_choice==1 and ai_choice==2:
    print("You Lose :(")
elif user_choice==1 and ai_choice==3:
    print("You Won :)")
elif user_choice==2 and ai_choice==1:
    print("You Won :)")
elif user_choice==2 and ai_choice==3:
    print("You Lose :(")
elif user_choice==3 and ai_choice==1:
    print("You Lose :(")
elif user_choice==3 and ai_choice==2:
    print("You Won :)")
else:
    print("You choose wrong option")

