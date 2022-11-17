"""
The idea is to have a list of people who entered into the office sweepstakes; plus a list of teams that are participating in the World Cup.

The plan is to have a random person match to a random team, before said person/team are removed from the arrays so they're not chosen again.
For this, the lengths of both arrays must be equal.
"""

import random
import time

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### #####
##### There are two arrays below. One is for the list of countries, and #####
##### the other is for the list of names. The arrays lengths must be    #####
##### equal to prevent errors.                                          #####
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### #####


##### Frontend using React
##### ##### ##### #### ^^ What Windows Vista does a tremendously piss-poor job of doing in any scenario.

##### Боже мой, that's it! GitHub pages! It can be hosted there!
##### https://gwenmurphy.github.io/projects/Random-Generator/


##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ###### ##### ###### ##### #####
##### The function itself - the guts of the program. It's much better than paper      #####
##### in tupperware. Bossman mentioned a backend in React, though how it'll be done   #####
##### is anyone's guess right now. All I'm establishing right now is that it will be  #####
##### hosted on GitHub pages.                                                         #####
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ###### ##### ###### ##### #####

def assignTeamToPerson():
    drawnList = []
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

##### Dave seems to have hidden the list that contains the names of those taking part in the
##### sweepstakes. I typed down the 4 I could remember, but I needed 32, so the other 28 have
##### been MacGyver'd, essentially. This was done to prevent errors when it ran which would have
##### occurred due to unequal array lengths. Bossman, as soon as you find that list, can you amend
##### the below array w/ who is in the sweepstakes and pull a merge request?
#####
##### I am not sure right now how the frontend is going to be done, let alone how it will look.
##### Regardless of who does what, adding in commenting will make things easier and quicker to complete.
##### I know you've seen the code for that Twitter bot too and the commenting I added onto that.
#####
##### I'm thinking that it would be hosted in GitHub pages. It'll have to be a subpage of the GitHub
##### site that's already there and it may need to be iframe'd in HTML so it displays on the page,
##### but I think I can do that bit.
#####
##### I've already put together a page in which it will be on, though given you've seen my GitHub profile,
##### it isn't hard to guess you've found it. It's the one with a random picture of a kitten. It will be
##### iframe'd where that picture currently is. Just needed something to fill the page in the meantime.
#####
##### <iframe src="{direct link to the random generator frontend}" title="Random Generator"></iframe>

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

    for i in range(0, len(countries)):
        ##### Shuffles them every time so nobody knows who gets what team.
        ##### Yes, it shuffles every time. Odds of getting what you want
        ##### are 1,023 to 1.
        random.shuffle(countries)
        random.shuffle(names) 
        
        ##### Sets a timer so the output is not zerg-rushed.
        ##### Yes, I know you understand that reference.
        # time.sleep(2)
        
        ##### Randomly assigns a country to a person. Doesn't look random, but it's shuffled
        ##### every time it loops. Any more shuffling and the Goonies will be summoned.
        randomPerson = names[0]
        randomTeam = countries[0]
        drawnList.append(f'May the odds be ever in your favour. Here\'s number {i+1}! {randomPerson} gets {randomTeam}!')
        ##### Yes, that's a Hunger Games reference.

        ##### Accounting for specific circumstances.
        if randomPerson == "Will" and randomTeam == "Saudi Arabia":
            print("F in the chat for Will.")
            ##### If this if statement is triggered, I implore someone to take a picture of the
            ##### astounded look on his face. Bet it'll be like the Shocked Pikachu meme.

        ##### Removes what was just printed from the list.
        countries.pop(0)
        names.pop(0)
        # print(f'{len(countries)} left to choose...')
    return drawnList


##### Triggers the function and blows Dave's comparatively Flintstonian method involving tupperware,
##### paper and a bit of luck out of the water, a bit like the Six Nations match on February 17th,
##### 2001 in which England flattened Italy 80-23.