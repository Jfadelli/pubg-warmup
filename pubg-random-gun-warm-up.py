import random
from data import motivation, weapons, scopes, grips, tips, styles
from art import ar_art, smg_art, dmr_art, sr_art, shotty_art
running = True
def main():
    gun_selection = []
    user_input = ''
    global running
    for key in weapons:
        gun_selection.append(key)

    def continue_check():
        global running
        check_input = input('continue...? ( y/n)')
        if check_input == 'n' or check_input == 'exit':
            running = False
        else:
            running = True
    def show_art(item):
        if item == 'AR':
            ar_art()
        elif item == 'SHOTTY':
            shotty_art()
        elif item == 'SMG':
            smg_art()

    def pick(user_input):
        upper_user_innput = user_input.upper()
        
        weapon = random.choice(weapons[upper_user_innput])
        scope = random.choice(scopes[upper_user_innput])
        style = random.choice(styles)
        grip = random.choice(grips[upper_user_innput])
        tip = random.choice(tips)
        print(
            f'Weapon: {weapon}\nScope: {scope}\nGrip: {grip}\nTip: {tip}\nStyle: {style}\n')
        show_art(upper_user_innput)
        print(f'{random.choice(motivation)} \n')
        

    while running == True:
        print('\n###################################################')
        print(f'Choose from {gun_selection}')
        print('Other commands; random, exit\n')
        user_input = input('Weapon Type: ')
        if user_input == 'exit':
            running = False
        elif user_input == 'random':
            pick(random.choice(gun_selection))
            print(f'{random.choice(motivation)} \n')
            continue_check()
        elif user_input.upper() not in gun_selection:
            print('Invalid input')
        else:
            pick(user_input)
            continue_check()
main()