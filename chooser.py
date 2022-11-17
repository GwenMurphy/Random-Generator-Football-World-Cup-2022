"""
The idea is to have a list of people who entered into the office sweepstakes; plus a list of teams that are participaitng in the World Cup.

The plan is to have a random person match to a random team, before said person/team are removed from the arrays so they're not chosen again.
For this, the lengths of both arrays must be equal.
"""

import random
import time

countries = [   ##### There are 32 countries taking part in the World Cup.
    'Argentina',
    'Australia',
    'Belgium',
    'Brazil',
    'Cameroon',
    'Canada',
    'Costa Rica',
    'Croatia',
    'Denmark',
    'Ecuador',
    'England',
    'France',
    'Germany',
    'Ghana',
    'Iran',
    'Japan',
    'Mexico',
    'Morocco',
    'Netherlands',
    'Poland',
    'Portugal',
    'Qatar',
    'Saudi Arabia',
    'Senegal',
    'Serbia',
    'South Korea',
    'Spain',
    'Switzerland',
    'Tunisia',
    'Uruguay',
    'United States',
    'Wales'
]

names = [
    'Will',
    'Dave B',
    'Alan',
    'Sophie K',
    'Octavia',

    'Luna',
    'Worf, son of Mogh',
    'Claire Redfield',
    'McLovin',
    'Arnold Rimmer',
    
    'Dave Lister',
    'Del Boy',
    'Davros',
    'Daenerys Targaryen',
    'Tywin Lannister',

    'Tyrion Lannister',
    'Luna Lovegood',
    'Seven of Nine',
    'The cat behind you that\'s staring into your soul',
    'The guy who created Zombocom',

    'Taylor Swift',
    'Don Corleone',
    'Al Capone',
    'The RICOH MP C6004 that exists to torment Will',
    'thingy',

    'Janet\'s butler, Barry,',
    'The joke that is the level of maintenance in this building',
    'Doug Dimmadome, owner of the Dimmsdale Dimmadome',
    'fre sh a voca do',
    'Yeetus Maximus',

    'Shuri',
    'That one meme bouncing round Will\'s head right now like the DVD logo'

]

##### Frontend using React
##### ##### ##### #### ^^ What Windows Vista does a tremendously piss-poor job of doing in any scenario.

##### Боже мой, that's it! GitHub pages! It can be hosted there!
##### https://gwenmurphy.github.io/{this thing}



countrylist = range(len(countries))
namelist = range(len(names))

def assignTeamToPerson():
    for i in range(0, len(countries)):
        ##### Shuffles them every time so nobody knows who gets what team.
        ##### Yes, it shuffles every time. Odds of getting what you want
        ##### are 1,023 to 1.
        random.shuffle(countries)
        random.shuffle(names) 
        
        ##### Sets a timer so the output is not zerg-rushed.
        ##### Yes, I know you understand that reference.
        time.sleep(2)
        
        ##### Randomly assigns a country to a person. Doesn't look random, but it's shuffled
        ##### every time it loops. Any more shuffling and the Goonies will be summoned.
        randomPerson = names[0]
        randomTeam = countries[0]
        print(f'May the odds be ever in your favour. Here\'s number {i+1}! {randomPerson} gets {randomTeam}!')
        ##### Yes, that's a Hunger Games reference.

        ##### Accounting for specific circumstances.
        if randomPerson == "Will" and randomTeam == "Saudi Arabia":
            print("F in the chat for Will.")
            ##### If this if statement is triggered, I implore someone to take a picture of the
            ##### astounded look on his face. Bet it'll be like the Shocked Pikachu meme.

        ##### Removes what was just printed from the list.
        countries.pop(0)
        names.pop(0)
        print(f'{len(countries)} left to choose...')        


assignTeamToPerson()