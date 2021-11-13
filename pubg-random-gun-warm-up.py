import random

weapons = {
    'AR': ['M16', 'M4', 'Scar', 'Mutant', 'AK', 'Beryl', 'G3C6', 'QBZ', 'K2'],
    'SMG': ['MP5', 'UMP', 'UZI', 'Bizon', 'Thompson', 'Vector'],
    'DMR': ['Mini', 'SKS', 'QBU', 'SLR', 'MK12', 'VSS'],
    'SR': ['K9', 'M24', 'Mosin', 'Win94'],
    'Shotty': ['S1897', 'S686', 'S12K', 'DBS'],
}

scopes = {
    'AR': ['Ironsights', 'Red Dot', 'Holo', '2x', '3x', '4x', '6x'],
    'SMG': ['Ironsights', 'Red Dot', 'Holo', '2x', '3x'],
    'DMR': ['Ironsights', 'Red Dot', 'Holo', '2x', '3x', '4x', '6x', '8x'],
    'SR': ['Ironsights', '2x', '3x', '4x', '6x', '8x'],
}

motivation = [
    'Aim small miss small!',
    'Be the hero you were born to be.',
    'Don\'t get your tits in a tussle.',
    'You got this!',
    'They\'re all shitters!!!',
    'Did somebody say donuts?',
    'Good choice, now go get \'em!!',
    'I\’d hate to die twice. It’s so boring',
    'They couldn’t hit an elephant at this dist—'
    'Now is not the time for making new enemies. -Voltaire'
    'I desire to go to Hell and not to Heaven. In the former I shall enjoy the company of popes, kings and princes, while in the latter are only beggars, monks and apostles.'
]



def main():
    gun_selection = []
    user_input = ''

    for key in weapons:
        gun_selection.append(key)

    def pick(user_input):
        upper_user_innput = user_input.upper()
        chosen = random.choice(weapons[upper_user_innput])
        scope = random.choice(scopes[upper_user_innput])
        print(f'    {chosen} + {scope}')

    running = True
    while running == True:
        print('---------------------------------------------')
        print(f'Choose from {gun_selection}')
        print('Other commands; random, exit ')
        user_input = input('    ')
        
        if user_input == 'exit':
            running = False
        elif user_input == 'random':
            pick(random.choice(gun_selection))
            print('    Only the bravest let the gods decide their fate! \n')
            input('continue...?')

        elif user_input.upper() not in gun_selection:
            print('Invalid input')
        else:
            pick(user_input)
            print(f'    {random.choice(motivation)} \n')
            continue_check = input('continue...? ( y/n)')
            if continue_check == 'n' or continue_check == 'exit':
                running = False
            else:
                running = True

main()
