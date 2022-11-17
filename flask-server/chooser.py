"""
The idea is to have a list of people who entered into the office sweepstakes; plus a list of teams that are participating in the World Cup.

The plan is to have a random person match to a random team, before said person/team are removed from the arrays so they're not chosen again.
For this, the lengths of both arrays must be equal.

-----
Addendum: a place has been made for the frontend to go. You'll notice the "index.html" file on the repo when you access it. I've added some text
into it so it's not empty. Here's the link:

https://gwenmurphy.github.io/Random-Generator-Football-World-Cup-2022/
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