import time
def introduction():
    print("Welcome to the Adventure Game !")
    time.sleep(3)
    print('you find yourself at the entrance of a mysterious cave.')
    time.sleep(3)
    print('your goal is to find hidden treasure inside the cave.')
    time.sleep(3)
    print('be wary ,as your choices will determine your fate!\n')
def make_choice(choices):
    print('choose your action:')
    for i,choice in enumerate(choices,1):
        print(f"{i}.{choice}")
    while True:
        try:
            choice_num=int(input("enter the number of your choice"))
            if 1<=choice_num<=len(choices):
                return choice_num
            else:
                print('invalid choice! please enter a valid number')
        except ValueError:
            print("Invalid input.please enter a number")
def cave_entrance():
    print('hope you are ready \n You stand at the entrance of the cave')
    time.sleep(3)
    print('You have two paths:')
    time.sleep(5)
    choices=["Enter the cave","Look for another way"]
    choice=make_choice(choices)
    if choice==1:
        print("\nAs you enter the cave ,you hear a noise.")
        time.sleep(5)
        print("It's a trap! A giant rock starts rolling towards you. ")
        time.sleep(5)
        print('what do you do ?')
        choices=['Try to outrun the giant rock','Look for a hiding spot']
        choice=make_choice(choices)
        if choice == 1:
            print("\nYou try to escape from the giant rock, but it's too fast")
            time.sleep(5)
            print('The giant rock catches up and  your adventure ends here')
        else:
            print('\nYou find a small space and hide. The giant rock rolls past you. ')
            time.sleep(5)
            print('You proceed deeper into the cave')
    else:
        print('\nYou decide to explore around the cave entrance')
        time.sleep(5)
        print('You discover a hidden passage.')
        time.sleep(5)
        print('Do you want to enter the hidden passage ?')
        choices=["Enter the hidden passage","stay at the cave entrance"]
        choice=make_choice(choices)
def encounter_trap():
  print('\nAs you proceed deeper into the cave ,you encounter a deadly trap!')
  time.sleep(5)
  print("Spikes shoot up from the ground.What do you do ?")
  choices=['Jump over the spikes','Try to disarm the trap']
  choice=make_choice(choices) 
  if choice ==1:
      print('\nYou attempt to jump over the spikes.')
      time.sleep(5)
      print('Success! The trap is disabled ,and you move forward.')
def dark_corridor():
    print("\nYou find yourself in a dark corridor with multiple paths.")
    time.sleep(5)
    print("Choose your direction")
    choices=["Go Left","Go Right","Go Straight"]
    choice=make_choice(choices)
    if choice == 1:
        print("\nYou decide to go left and encounter a group of bats.")
        time.sleep(5)
        print("They seem harmless. what do you do? ")
        choices=["Ignore the bats","Try to shoo them away"]
        choice=make_choice(choices)
        if choice == 1:
            print("\nYou ignore the bats and safely pass through the corridor.")
        else:
            print("\nYou try to shoo away the bats, but one bites you.")
            time.sleep(5)
            print('You lose some health but continue your journey.')
    elif choice == 2:
        print("\nYou decided to go right and find a locked door.")
        time.sleep(5)
        print("Do you want to search for the keys or continur explore other paths?")
        choices=["search for the key","explore other paths"]
        choice =make_choice(choices)
        if choice == 1:
            print("\nYou search for the key and find it hidden behind a loose stone.")
            time.sleep(5)
            print("You unlock the door and proceed.")
        else:
            print("\nYou decide to explore other paths and find a hidden treasure chest.")
            time.sleep(5)
            print("Congratulations! You found an additional loot!")
    else:
        print("\nYou go straight and found a mysterious figure.")
        time.sleep(5)
        print("They offer you a choice : a riddle or a challenge.")
        choices=["Solve the riddle","Take on the challenge"]
        choice=make_choice(choices)
        if choice == 1:
            print("\nYou successfully solve the riddle and gain valuable information.")
            time.sleep(5)
            print("The mysterious figure disappears ,leaving you to continue your journey.")
        else:
            print("\nYou bravely accept the challenge and emerge victorious!")
            time.sleep(5)
            print("The mysterious figure rewards you with a powerful artifact.")
def conclusion():
   print("\nYou reach the final chamber of the cave.")
   time.sleep(5)
   print("The hidden treasure within your grasp.")
   time.sleep(5)
   print("Congratulations! You've succesfully completed the adventure.")
def main():
    introduction()
    cave_entrance()
    encounter_trap()
    dark_corridor()
    conclusion()  
if __name__ == "__main__":
    main()