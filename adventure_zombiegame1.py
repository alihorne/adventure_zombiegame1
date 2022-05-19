import time
import random

thoughts = ["These zombies better not chase me!", "I hope I don't die!",
            "Should I really be doing this???","Please don't bite me!", "Wasn't WWZ enough! Stupid zombies!",
            "I'm not trying to see ANNNNYYYY zombie brains!", ]
weaponlist = ["MACHETE", "BAT", "GUN", "AXE"]
outcomelist = ["YOU HAVE KILLED ALL THE ZOMBIES IN YOUR PATH.",
               "ZOMBIE BITES YOU. AHH.. YOU'RE DEAD!",
               "YOU & THE SURVIVORS MADE IT TO SAFETY!!"]
safetylist = ["YOU REACHED AN INTERSECTION & HEAR RUMBLING...",
              "YOU FOUND A TUNNEL UNDERNEATH A CORNERSTORE...",
             "YOU & GROUP OF SURVIORS MADE TO THE SAFETY ZONE..."]
survivorslist= ["YOU SEE TWO SURVIORS TRAPPED BY ZOMBIES...",
              "AS YOU ARE RUNNING..YOU CUT YOUR LEG.....",
                "YOU SAVED THE SURVIVORS..BUT..THEY LEAVE YOU BEHIND.."]
runlist= ["YOU RAN AWAY & TOOK COVER BEHIND A TRASH CAN...",
          "A HIDDEN ZOMBIE ATTACKS YOU, KILLING YOU INSTANTLY...RIP",
          "DANG, YOU FELL..ZOMBIE ATTACKS YOU.. YOU'RE DEAD",
         " A ZOMBIE COUGHED ON YOU & NOW YOUR HAVE TO GET VACCINATED.."]


def print_pause(message, delay=1):
    print(message)
    time.sleep(2)


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_pause('SORRY, THAT IS INVALID.PLEASE TRY AGAIN')


def openscene():
    print_pause("Thought Bubble...")
    print(random.choice(thoughts))


openscene()


def story():
    print_pause("\nTHE CIVIL WAR OF 2078 HAS ENDED!")
    print_pause("THE WORLD YOU ONCE KNEW IS GONE.")
    print_pause("THE ONES STILL ALIVE HAVE BEEN VACCINATED!")
    print_pause("YOU ARE ALONE & NEED TO FIND SAFETY FROM THE ZOMBIES.")
    valid_input("WILL YOU GO TO SAFETY (1) OR SEARCH FOR SURVIVORS(2)?", ['1', '2'])
    answer = valid_input
    if answer == "1":
        print_pause(random.choice(safetylist))
    else:
        print_pause(random.choice(survivorslist))


story()


def battle_zone():
    # some prompts
    # '\n' is to print the line in a new line
    print_pause("A GROUP OF ZOMBIES ARE HEADED YOUR WAY.")
    print_pause("YOU HEAR SOME SURVIVORS IN THE DISTANCE.")
    print_pause("THE TWO SURVIVORS ARE TRAPPED & NEED HELP!")
    print_pause("ZOMBIES ARE IN YOUR PATHWAY.")
    choice=valid_input("WILL YOU RUN (1) or LOOK FOR WEAPONS(2)?", ['1', '2'])
    # battle_zone input()
    if choice == "1":
        # player runs and hides, call game_over() with "reason"
        print_pause(random.choice(runlist))
    else:
        # the player fights()
        print_pause("\nYOU FOUND A...")
        print_pause(random.choice(weaponlist))
        print_pause(random.choice(outcomelist))

battle_zone()


def game_over():
    print_pause("GAME OVER")
    again = valid_input("WOULD YOU LIKE TO PLAY AGAIN? TYPE 1:> ", ['1'])
    if again == '1':
        openscene()
        story()
        battle_zone()
        game_over()
        return
    else:
        print_pause("THANKS FOR PLAYING!")
        exit(0)


game_over()